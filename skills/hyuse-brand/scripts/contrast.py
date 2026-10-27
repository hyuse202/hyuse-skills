#!/usr/bin/env python3
"""WCAG 2.x contrast ratio for color pairs.

Usage:
    python3 contrast.py "#1C1A17" "#F6F1E7"
    python3 contrast.py "#1C1A17:#F6F1E7" "#B4532A:#F6F1E7"
    python3 contrast.py "oklch(23% 0.014 60):oklch(95.2% 0.012 84)"

Each pair is foreground then background. Prints the ratio and which
levels it passes: AA body text (4.5:1) and AA large text or UI (3:1).
"""

import math
import re
import sys


def parse_oklch(value):
    m = re.fullmatch(r"oklch\(\s*([\d.]+)(%?)\s+([\d.]+)\s+([\d.]+)(?:deg)?\s*\)", value.strip())
    if not m:
        raise ValueError(f"not an oklch() color: {value}")
    L = float(m.group(1)) / (100 if m.group(2) else 1)
    C, H = float(m.group(3)), math.radians(float(m.group(4)))
    a, b = C * math.cos(H), C * math.sin(H)
    l_ = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m_ = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s_ = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    lin = (4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_,
           -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_,
           -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_)
    def encode(x):
        x = max(0.0, min(1.0, x))
        return 12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055
    return tuple(round(encode(c) * 255) / 255 for c in lin)


def parse_color(value):
    if value.strip().lower().startswith("oklch("):
        return parse_oklch(value)
    return parse_hex(value)


def parse_hex(value):
    value = value.strip().lstrip("#")
    if len(value) == 3:
        value = "".join(c * 2 for c in value)
    if len(value) != 6:
        raise ValueError(f"not a 3 or 6 digit hex color: #{value}")
    return tuple(int(value[i:i + 2], 16) / 255 for i in (0, 2, 4))


def luminance(rgb):
    def channel(c):
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

    r, g, b = (channel(c) for c in rgb)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def ratio(fg, bg):
    l1, l2 = sorted((luminance(parse_color(fg)), luminance(parse_color(bg))), reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


def pairs_from_args(args):
    if all(":" in a for a in args):
        return [tuple(a.split(":", 1)) for a in args]
    if len(args) % 2:
        raise ValueError("give colors in foreground/background pairs")
    return list(zip(args[0::2], args[1::2]))


def main(argv):
    if not argv:
        print(__doc__.strip())
        return 1
    try:
        pairs = pairs_from_args(argv)
        for fg, bg in pairs:
            r = ratio(fg, bg)
            body = "pass" if r >= 4.5 else "fail"
            large = "pass" if r >= 3 else "fail"
            print(f"{fg} on {bg}: {r:.2f}:1  body {body}  large/UI {large}")
    except ValueError as err:
        print(f"error: {err}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
