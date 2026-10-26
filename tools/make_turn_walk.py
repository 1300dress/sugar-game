"""Derive front/back walk cycles from the master turn sprites.

No new drawing: every output pixel is copied from turn_01 / turn_02.
The body and antennae stay put; only the legs are bent up and down.
Bend grows with distance from the body (tips move most) and follows
an ant tripod gait: front + back legs on one side move with the
middle leg on the other side.

Run from the repo root or tools/:  python3 tools/make_turn_walk.py
"""
import math
import os

from pngio import read_rgba, write_rgba

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

# body band (x range left untouched) and the rows the legs live in,
# read off the alpha maps of each source sprite
SOURCES = {
    "front_walk": dict(src="turn/turn_01.png", band=(60, 116), legs=(60, 168)),
    "back_walk":  dict(src="turn/turn_02.png", band=(58, 118), legs=(40, 166)),
}

SHIFT = 13       # px at the leg tips, in source pixels
RAMP = 30        # px from the body band over which the bend grows
PHASES = [1, 0, -1, 0]   # 4 frames, same count as walk/run


def frame(w, h, px, band, legs, phase):
    x0, x1 = band
    y0, y1 = legs
    out = [list(row) for row in px]
    for y in range(h):
        if y < y0 or y > y1:
            continue
        t = (y - y0) / (y1 - y0)
        g = math.cos(2 * math.pi * t)   # +1 front, -1 middle, +1 back
        for x in range(w):
            if x0 <= x <= x1:
                continue
            dist = (x0 - x) if x < x0 else (x - x1)
            ramp = min(1.0, dist / RAMP)
            side = 1 if x < x0 else -1
            off = SHIFT * ramp * g * side * phase
            sy = round(y - off)
            if y0 <= sy <= y1 or (0 <= sy < h and px[sy][x][3] == 0):
                out[y][x] = px[sy][x] if 0 <= sy < h else (0, 0, 0, 0)
            else:
                out[y][x] = (0, 0, 0, 0)
    return out


def main():
    for name, cfg in SOURCES.items():
        w, h, px = read_rgba(os.path.join(ROOT, "sprites", cfg["src"]))
        folder = os.path.join(ROOT, "sprites", name)
        os.makedirs(folder, exist_ok=True)
        for i, phase in enumerate(PHASES, 1):
            path = os.path.join(folder, f"{name}_{i:02d}.png")
            write_rgba(path, w, h, frame(w, h, px, cfg["band"], cfg["legs"], phase))
            print("wrote", os.path.relpath(path, ROOT))


if __name__ == "__main__":
    main()
