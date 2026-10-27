"""Draw the ten ant siblings (GAME_BIBLE §11, §32) and make their sprites.

Every sibling is the master ant (sprites/walk/walk_01..04) changed by
numbers only. No new drawing: pixels are cut away, worn or toned.

1. A seeded random draw gives each ant a SIZE and an IMPAIRMENT (0..1).
2. Speed, gait (frame count and timing), visible traits and one movement
   rule each are derived from those two numbers. No two ants share a rule.
3. Sprites go to sprites/siblings/<letter>/walk_01..04.png and every
   number to sprites/siblings/siblings.json for the game to read.

Same SEED = same ten ants. Change SEED to redraw them all.

Run from the repo root or tools/:  python3 tools/make_siblings.py
"""
import json
import math
import os
import random

from pngio import read_rgba, write_rgba

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
SEED = 2833   # picked for an even spread of sizes and impairments
LETTERS = "ABCDEFGHIJ"

# --- master numbers the siblings are measured against (index.html)
MASTER_WALK_SPEED = 155      # world px/s
MASTER_WALK_INTERVAL = 130   # ms per walk frame
MASTER_SCALE = 0.477         # walk SPRITE_SCALE

# --- where things are on the master walk frames (source px)
LEG_ROOTS = {"front": 77, "middle": 92, "hind": 123}   # x where each leg leaves the body
LEG_CUT_Y = 100              # legs are separate strands below this row
ANTENNA_ROOT = (62, 50)      # where both antennae leave the head
ANTENNA_REGION = (80, 54)    # antenna pixels live left of x and above y

# --- movement rules: one per ant, never repeated
# affinity(size, impairment, traits) says how well a rule suits an ant
RULES = {
    "straight": dict(ko="곧게 간다. 멈추지 않는다.",
                     fit=lambda s, d, t: s - d),
    "stop_go":  dict(ko="몇 걸음 가다 멈추고 다시 간다.",
                     fit=lambda s, d, t: d),
    "zigzag":   dict(ko="좌우로 갈지자를 그리며 간다.",
                     fit=lambda s, d, t: 1 - s + (0.3 - abs(d - 0.3))),
    "circle":   dict(ko="한 자리를 크게 맴돈다.",
                     fit=lambda s, d, t: 0.5 - abs(d - 0.5)),
    "follow":   dict(ko="주인공을 거리를 두고 따라온다.",
                     fit=lambda s, d, t: 1 - d),
    "retreat":  dict(ko="주인공이 다가오면 뒷걸음친다.",
                     fit=lambda s, d, t: 1.2 - s),
    "freeze":   dict(ko="주인공이 다가오면 그 자리에 굳는다.",
                     fit=lambda s, d, t: (1.2 - s) + d * 0.5),
    "wander":   dict(ko="정한 곳 없이 천천히 헤맨다.",
                     fit=lambda s, d, t: d * 0.8 + 0.2),
    "veer":     dict(ko="똑바로 가려 하지만 한쪽으로 휜다.",
                     fit=lambda s, d, t: len(t["legs_missing"]) * 0.6 + d * 0.3),
    "pace":     dict(ko="같은 구간을 왔다 갔다 한다.",
                     fit=lambda s, d, t: 0.6 - abs(s - 1)),
}

# gait by impairment: walk frame sequence (indices into walk_01..04)
# and how much longer each step is held (1 = even)
GAITS = [
    (0.15, [1, 2, 3, 4],       [1, 1, 1, 1]),            # even
    (0.35, [1, 2, 4],          [1, 1, 1.3]),             # skips a step
    (0.55, [1, 2, 3, 3, 4],    [1, 1, 1, 1.6, 1]),       # one hitch
    (0.75, [1, 1, 2, 3, 3, 4], [1, 1.4, 1, 1, 1.8, 1]),  # limp
    (1.01, [1, 3],             [1.6, 2.2]),              # drags
]


def draw(rng):
    """Size and impairment for each ant, plus the traits they lead to."""
    ants = []
    for letter in LETTERS:
        size = round(rng.uniform(0.62, 1.28), 2)
        d = round(rng.random(), 2)

        if d < 0.3:
            legs = []
        elif d < 0.65:
            legs = [rng.choice(list(LEG_ROOTS))]
        else:
            legs = rng.sample(list(LEG_ROOTS), 2)

        a = d + rng.uniform(-0.25, 0.25)
        antennae = "stubs" if a > 0.85 else "worn" if a > 0.5 else "intact"

        for top, seq, holds in GAITS:
            if d < top:
                break
        jitter = rng.uniform(0.9, 1.1)
        base = MASTER_WALK_INTERVAL * math.sqrt(size) * (1 + 0.5 * d) * jitter
        intervals = [round(base * h) for h in holds]

        speed = MASTER_WALK_SPEED * size ** 0.6 * (1 - 0.55 * d) * rng.uniform(0.9, 1.1)

        ants.append(dict(
            letter=letter,
            size=size,
            impairment=d,
            speed=round(speed),
            frames=len(seq),
            sequence=seq,
            intervals=intervals,
            legs_missing=legs,
            antennae=antennae,
            wear=round(rng.uniform(0.04, 0.3), 2),     # how worn the print is
            tone=round(rng.uniform(-0.12, 0.12), 2),   # lighter (-) or darker (+) ink
        ))

    # one rule each: the ants that are hardest to place pick first
    free = list(RULES)
    order = ants[:]
    rng.shuffle(order)
    for ant in order:
        t = ant
        best = max(free, key=lambda r: RULES[r]["fit"](t["size"], t["impairment"], t)
                   + rng.uniform(0, 0.35))
        ant["rule"] = best
        ant["rule_ko"] = RULES[best]["ko"]
        free.remove(best)
    return ants


# ---------------------------------------------------------------- pixels

def components(px, w, h, y_from, y_to):
    """8-connected opaque strands between two rows."""
    seen = set()
    out = []
    for y in range(y_from, y_to):
        for x in range(w):
            if px[y][x][3] <= 60 or (x, y) in seen:
                continue
            stack, pts = [(x, y)], []
            seen.add((x, y))
            while stack:
                cx, cy = stack.pop()
                pts.append((cx, cy))
                for dx in (-1, 0, 1):
                    for dy in (-1, 0, 1):
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < w and y_from <= ny < y_to and (nx, ny) not in seen \
                                and px[ny][nx][3] > 60:
                            seen.add((nx, ny))
                            stack.append((nx, ny))
            out.append(pts)
    return out


def cut_leg(px, w, h, which):
    """Remove one leg below its knee, leaving a short stub."""
    target = LEG_ROOTS[which]
    for y_cut in range(LEG_CUT_Y, LEG_CUT_Y + 18, 2):
        best = None
        for pts in components(px, w, h, y_cut, h):
            if len(pts) > 500:          # the abdomen, not a leg
                continue
            root = [x for x, y in pts if y == y_cut]
            if not root:
                continue
            mid = (min(root) + max(root)) / 2
            if max(root) - min(root) < 16 and abs(mid - target) < 10:
                if best is None or abs(mid - target) < best[0]:
                    best = (abs(mid - target), pts)
        if best:
            gone = set(best[1])
            for x, y in best[1]:
                px[y][x] = (0, 0, 0, 0)
            # the strand's soft edge (faint pixels) is not part of it; clear it too
            for x, y in gone:
                for dx in range(-3, 4):
                    for dy in range(-3, 4):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < w and y_cut <= ny < h and 0 < px[ny][nx][3] <= 110:
                            px[ny][nx] = (0, 0, 0, 0)
            return True
    return False


def wear_antennae(px, kind):
    if kind == "intact":
        return
    reach = 38 if kind == "worn" else 18
    rx, ry = ANTENNA_ROOT
    xr, yr = ANTENNA_REGION
    for y in range(yr):
        for x in range(xr):
            if px[y][x][3] and math.hypot(x - rx, y - ry) > reach:
                px[y][x] = (0, 0, 0, 0)


PAPER_INK = (214, 206, 190)   # worn ink fades toward the paper colour


def wear_print(px, w, h, amount, tone, rng):
    """Fade the ink in a few round soft blots (worn print), then shift
    the ink density. More wear = more blots."""
    blots = []
    for _ in range(round(amount * 60)):
        blots.append((rng.uniform(0, w), rng.uniform(0, h), rng.uniform(2.5, 6.5), rng.uniform(0.25, 0.55)))

    for y in range(h):
        for x in range(w):
            r, g, b, a = px[y][x]
            if not a:
                continue
            fade = 0.0
            for bx, by, br, bs in blots:
                dist = math.hypot(x - bx, y - by)
                if dist < br:
                    t = 1 - dist / br
                    fade = max(fade, bs * t * t * (3 - 2 * t))
            if fade:
                r, g, b = (round(v + (p - v) * fade) for v, p in zip((r, g, b), PAPER_INK))
            # tone > 0 darkens toward ink, < 0 lifts toward paper
            if tone > 0:
                r, g, b = (round(v * (1 - tone)) for v in (r, g, b))
            else:
                r, g, b = (round(v + (238 - v) * -tone) for v in (r, g, b))
            px[y][x] = (r, g, b, a)


def make_sprites(ant):
    folder = os.path.join(ROOT, "sprites", "siblings", ant["letter"])
    os.makedirs(folder, exist_ok=True)
    for i in range(1, 5):
        w, h, src = read_rgba(os.path.join(ROOT, "sprites", "walk", f"walk_{i:02d}.png"))
        px = [list(row) for row in src]
        for leg in ant["legs_missing"]:
            if not cut_leg(px, w, h, leg):
                print(f"  {ant['letter']}: could not find {leg} leg in frame {i}")
        wear_antennae(px, ant["antennae"])
        # same wear pattern on every frame so the damage does not flicker
        wear_print(px, w, h, ant["wear"], ant["tone"], random.Random(f"{SEED}-{ant['letter']}-wear"))
        write_rgba(os.path.join(folder, f"walk_{i:02d}.png"), w, h, px)


def main():
    ants = draw(random.Random(SEED))
    for ant in ants:
        make_sprites(ant)
        ant["scale"] = round(MASTER_SCALE * ant["size"], 3)   # SPRITE_SCALE for its walk
        print(f"{ant['letter']}  size {ant['size']:.2f}  impairment {ant['impairment']:.2f}  "
              f"speed {ant['speed']:3d}  frames {ant['frames']}  "
              f"legs-{len(ant['legs_missing'])}  antennae {ant['antennae']:6s}  {ant['rule']}")
    out = dict(
        seed=SEED,
        note="Generated by tools/make_siblings.py. Edit SEED there and rerun; do not hand-edit.",
        anchor=dict(x=136, y=84),
        ants=ants,
    )
    path = os.path.join(ROOT, "sprites", "siblings", "siblings.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("wrote", os.path.relpath(path, ROOT))


if __name__ == "__main__":
    main()
