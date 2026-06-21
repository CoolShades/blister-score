"""Generate BLISTER Score PWA icons — a white shield with an ECG blip on a
Glacier-blue gradient. Rendered at 4x and downsampled for clean anti-aliasing."""
from PIL import Image, ImageDraw

ACCENT_TOP = (42, 139, 212)   # #2A8BD4
ACCENT_BOT = (14, 34, 51)     # #0E2233 ink navy
SHIELD     = (244, 249, 252)  # near-white
ECG        = (31, 116, 196)   # #1F74C4 accent

# Shield outline as fractions of the icon box.
SHIELD_PTS = [
    (0.50, 0.07), (0.855, 0.205), (0.855, 0.50), (0.795, 0.68),
    (0.655, 0.84), (0.50, 0.935), (0.345, 0.84), (0.205, 0.68),
    (0.145, 0.50), (0.145, 0.205),
]
# ECG / QRS blip, fractions of the icon box.
ECG_PTS = [
    (0.245, 0.545), (0.405, 0.545), (0.458, 0.385),
    (0.525, 0.70), (0.578, 0.545), (0.755, 0.545),
]

def gradient(size, top, bot):
    img = Image.new("RGB", (size, size), top)
    px = img.load()
    for y in range(size):
        t = y / (size - 1)
        r = round(top[0] + (bot[0] - top[0]) * t)
        g = round(top[1] + (bot[1] - top[1]) * t)
        b = round(top[2] + (bot[2] - top[2]) * t)
        for x in range(size):
            px[x, y] = (r, g, b)
    return img

def rounded_mask(size, radius):
    m = Image.new("L", (size, size), 0)
    d = ImageDraw.Draw(m)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=radius, fill=255)
    return m

def draw_icon(size, *, shield_scale=0.64, shield_dy=0.0, rounded=True, transparent=True):
    S = size * 4  # supersample
    base = gradient(S, ACCENT_TOP, ACCENT_BOT)
    draw = ImageDraw.Draw(base)

    # Shield, scaled about its centroid and centred.
    cx, cy = 0.5, 0.5 + shield_dy
    def place(pts):
        out = []
        for (fx, fy) in pts:
            x = (cx + (fx - 0.5) * shield_scale) * S
            y = (cy + (fy - 0.5) * shield_scale) * S
            out.append((x, y))
        return out
    draw.polygon(place(SHIELD_PTS), fill=SHIELD)

    # ECG blip — rounded caps + curved joints.
    ecg = place(ECG_PTS)
    lw = max(2, int(S * 0.052 * (shield_scale / 0.64)))
    draw.line(ecg, fill=ECG, width=lw, joint="curve")
    r = lw / 2
    for (x, y) in (ecg[0], ecg[-1]):
        draw.ellipse([x - r, y - r, x + r, y + r], fill=ECG)

    img = base.convert("RGBA")
    if rounded:
        mask = rounded_mask(S, int(S * 0.225))
        if transparent:
            out = Image.new("RGBA", (S, S), (0, 0, 0, 0))
            out.paste(img, (0, 0), mask)
            img = out
        else:
            bg = Image.new("RGBA", (S, S), ACCENT_BOT + (255,))
            bg.paste(img, (0, 0), mask)
            img = bg
    return img.resize((size, size), Image.LANCZOS)

OUT = r"C:\Users\ubhal\Documents\code\blister-score"

# Standard maskable-friendly + transparent rounded icons.
draw_icon(192, rounded=True).save(OUT + r"\icon-192.png")
draw_icon(512, rounded=True).save(OUT + r"\icon-512.png")
# Maskable: full-bleed square, shield inside the 80% safe zone.
draw_icon(512, shield_scale=0.52, rounded=False, transparent=False).save(OUT + r"\icon-maskable-512.png")
# Apple touch icon: full square, no transparency (iOS masks it itself).
draw_icon(180, shield_scale=0.66, rounded=False, transparent=False).save(OUT + r"\apple-touch-icon.png")
# Favicons.
draw_icon(32, shield_scale=0.74, rounded=True).save(OUT + r"\favicon-32.png")
ico = draw_icon(64, shield_scale=0.74, rounded=True)
ico.save(OUT + r"\favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
print("icons written")
