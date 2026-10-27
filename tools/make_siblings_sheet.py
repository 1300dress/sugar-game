"""Contact sheet of the ten siblings: one main cut each, on one image.

Reads sprites/siblings/siblings.json and the sprites made by
make_siblings.py. Writes sprites/preview/siblings_sheet.png.

Every ant is drawn at the same print scale, standing on one baseline,
so size differences read as they will in the game. Under each ant: its
gait as a filmstrip (one cell per frame, with how long it is held) and
a specimen label.

Needs Pillow (preview only, not used by the game):  pip install pillow
Run from the repo root or tools/:  python3 tools/make_siblings_sheet.py
"""
import json
import os
import random

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
OUT = os.path.join(ROOT, "sprites", "preview", "siblings_sheet.png")

PAPER = (214, 206, 190)
INK = (42, 34, 27)
GHOST = (128, 104, 78)
FADED = (92, 74, 56)

COLS, ROWS = 5, 2
CELL_W, CELL_H = 300, 430      # sheet px at 1x, before the 2x enlargement
MARGIN_X, MARGIN_TOP, MARGIN_BOTTOM = 40, 70, 40
PRINT = 0.95                   # source px -> sheet px for the main cut
BASELINE = 150                 # y of the floor line inside a cell
STRIP_Y = 178
LABEL_Y = 250
ENLARGE = 2

MONO = "/usr/share/fonts/truetype/freefont/FreeMono.ttf"
MONO_BOLD = "/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf"
SERIF_KR = ("/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc", 1)

LEG_KO = {"front": "front", "middle": "mid", "hind": "hind"}


def paper(w, h, rng):
    """Faded print paper: blotches, grain, a few specks (like the game floor)."""
    small = Image.new("RGB", (w // 3 + 1, h // 3 + 1))
    px = small.load()
    # soft blotches: a coarse random grid enlarged smoothly
    coarse = Image.new("L", (small.width // 24 + 2, small.height // 24 + 2))
    coarse.putdata([rng.randrange(256) for _ in range(coarse.width * coarse.height)])
    blot = coarse.resize(small.size, Image.BICUBIC).load()
    for y in range(small.height):
        for x in range(small.width):
            b = blot[x, y] / 255
            f = 0.86 + 0.14 * b
            g = (rng.random() - 0.5) * 22
            px[x, y] = tuple(max(0, min(255, round((c + g) * f))) for c in PAPER)
    img = small.resize((small.width * 3, small.height * 3), Image.NEAREST).crop((0, 0, w, h))
    d = ImageDraw.Draw(img)
    for _ in range(w * h // 900):
        x, y = rng.randrange(w), rng.randrange(h)
        d.rectangle([x, y, x + (1 if rng.random() < 0.85 else 2), y], fill=(42, 34, 27) if rng.random() < 0.75 else (251, 248, 241))
    return img


def opaque_box(im):
    return im.getchannel("A").point(lambda a: 255 if a > 60 else 0).getbbox()


def main():
    data = json.load(open(os.path.join(ROOT, "sprites", "siblings", "siblings.json"), encoding="utf-8"))
    ants = data["ants"]
    rng = random.Random(data["seed"])

    W = MARGIN_X * 2 + CELL_W * COLS
    H = MARGIN_TOP + CELL_H * ROWS + MARGIN_BOTTOM
    sheet = paper(W, H, rng)

    # --- ants and filmstrips at 1x (pixel art stays pixel art)
    for i, ant in enumerate(ants):
        cx = MARGIN_X + (i % COLS) * CELL_W
        cy = MARGIN_TOP + (i // COLS) * CELL_H
        folder = os.path.join(ROOT, "sprites", "siblings", ant["letter"])
        frames = [Image.open(os.path.join(folder, f"walk_{n:02d}.png")).convert("RGBA") for n in range(1, 5)]

        # main cut: the first frame of its own gait, size on top of print scale
        main_im = frames[ant["sequence"][0] - 1]
        s = PRINT * ant["size"]
        big = main_im.resize((round(main_im.width * s), round(main_im.height * s)), Image.NEAREST)
        box = opaque_box(big)
        x = cx + (CELL_W - (box[2] - box[0])) // 2 - box[0]
        y = cy + BASELINE - box[3]
        sheet.paste(big, (x, y), big)

        # gait filmstrip: same frames, small, one cell per step
        n = len(ant["sequence"])
        cell = 44
        gap = 4
        sx = cx + (CELL_W - (n * cell + (n - 1) * gap)) // 2
        for k, f in enumerate(ant["sequence"]):
            im = frames[f - 1]
            t = (cell - 4) / im.width
            th = im.resize((round(im.width * t), round(im.height * t)), Image.NEAREST)
            fx = sx + k * (cell + gap)
            sheet.paste(th, (fx + 2, STRIP_Y + cy + (30 - th.height) // 2), th)

    sheet = sheet.resize((W * ENLARGE, H * ENLARGE), Image.NEAREST)
    d = ImageDraw.Draw(sheet)
    E = ENLARGE

    mono = ImageFont.truetype(MONO, 11 * E)
    mono_small = ImageFont.truetype(MONO, 9 * E)
    mono_bold = ImageFont.truetype(MONO_BOLD, 30 * E)
    head = ImageFont.truetype(MONO_BOLD, 13 * E)
    kr = ImageFont.truetype(SERIF_KR[0], 11 * E, index=SERIF_KR[1])

    def text(x, y, s, font, fill=INK):
        # ghost ink 1 px down-right, then ink (same as the title)
        d.text((x * E + E, y * E + E), s, font=font, fill=GHOST)
        d.text((x * E, y * E), s, font=font, fill=fill)

    text(MARGIN_X, 26, "SUGAR  /  SIBLINGS  A-J", head)
    text(W - MARGIN_X - 175, 28, f"draw seed {data['seed']}", mono_small, FADED)

    for i, ant in enumerate(ants):
        cx = MARGIN_X + (i % COLS) * CELL_W
        cy = MARGIN_TOP + (i // COLS) * CELL_H

        # cell rule and the shared floor line
        d.line([(cx + 14) * E, cy * E, (cx + CELL_W - 14) * E, cy * E], fill=GHOST, width=1)
        d.line([(cx + 30) * E, (cy + BASELINE + 2) * E, (cx + CELL_W - 30) * E, (cy + BASELINE + 2) * E], fill=FADED, width=1)

        text(cx + 16, cy + 8, ant["letter"], mono_bold)

        # filmstrip frames and their hold times
        n = len(ant["sequence"])
        cell, gap = 44, 4
        sx = cx + (CELL_W - (n * cell + (n - 1) * gap)) // 2
        for k, ms in enumerate(ant["intervals"]):
            fx = sx + k * (cell + gap)
            d.rectangle([fx * E, (cy + STRIP_Y - 2) * E, (fx + cell) * E, (cy + STRIP_Y + 32) * E], outline=FADED, width=1)
            label = f"{ms}"
            tw = d.textlength(label, font=mono_small) / E
            text(fx + (cell - tw) / 2, cy + STRIP_Y + 36, label, mono_small, FADED)
        text(cx + 30, cy + STRIP_Y + 52, f"{n} frames / ms held", mono_small, FADED)

        legs = ant["legs_missing"]
        lines = [
            f"SIZE      {ant['size']:.2f}",
            f"IMPAIR    {ant['impairment']:.2f}",
            f"SPEED     {ant['speed']} px/s",
            f"LEGS      {6 - len(legs)}/6" + (f"  -{', -'.join(LEG_KO[l] for l in legs)}" if legs else ""),
            f"ANTENNAE  {ant['antennae']}",
            f"RULE      {ant['rule']}",
        ]
        ly = cy + LABEL_Y
        for line in lines:
            text(cx + 30, ly, line, mono)
            ly += 17
        text(cx + 30, ly + 6, ant["rule_ko"], kr)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    sheet.save(OUT)
    print("wrote", os.path.relpath(OUT, ROOT), sheet.size)


if __name__ == "__main__":
    main()
