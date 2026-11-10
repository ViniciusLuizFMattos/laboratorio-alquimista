"""Cenários desenhados em Canvas para cada sala (parte estática + animação)."""

import math
import random

W, H = 860, 200
OURO = "#d4a64a"
TOCHAS = [(45, 95), (815, 95)]
TAG_E, TAG_A = "cena", "anim"


def _ajusta(hexa, d):
    r, g, b = (int(hexa[i:i + 2], 16) for i in (1, 3, 5))
    return "#%02x%02x%02x" % tuple(max(0, min(255, v + d)) for v in (r, g, b))


def _tijolos(c, base, junta, seed):
    rnd = random.Random(seed)
    c.create_rectangle(0, 0, W, H, fill=junta, width=0, tags=TAG_E)
    for fila, y in enumerate(range(0, H, 20)):
        desl = 0 if fila % 2 == 0 else 30
        for x in range(-desl, W, 60):
            c.create_rectangle(x + 1, y + 1, x + 59, y + 19,
                               fill=_ajusta(base, rnd.randint(-9, 9)), width=0, tags=TAG_E)


def _piso(c, cor="#1d1612"):
    c.create_rectangle(0, H - 25, W, H, fill=cor, width=0, tags=TAG_E)
    c.create_line(0, H - 25, W, H - 25, fill="#000000", tags=TAG_E)


def _suportes_tocha(c):
    for x, y in TOCHAS:
        c.create_rectangle(x - 3, y, x + 3, y + 42, fill="#3b2a1c", width=0, tags=TAG_E)
        c.create_polygon(x - 9, y, x + 9, y, x + 5, y + 10, x - 5, y + 10,
                         fill="#5a4a3a", tags=TAG_E)


def _chamas(c, t, rnd):
    for x, y in TOCHAS:
        r = 42 + 6 * math.sin(t * 7 + x) + rnd.uniform(-3, 3)
        c.create_oval(x - r, y - r, x + r, y + r, fill="#ff9a2e", stipple="gray12",
                      width=0, tags=TAG_A)
        h = 24 + rnd.uniform(-4, 7)
        c.create_polygon(x - 7, y, x, y - h, x + 7, y, x + 3, y + 4, x - 3, y + 4,
                         fill="#ffb347", outline="#ff6a00", tags=TAG_A)
        c.create_polygon(x - 3, y, x, y - h * 0.55, x + 3, y, fill="#fff3b0",
                         width=0, tags=TAG_A)


def _nevoa(c, t, frac):
    if frac <= 0.02:
        return
    topo = H * (1 - frac * 0.85)
    pts = [0, H]
    for x in range(0, W + 1, 30):
        pts += [x, topo + 9 * math.sin(x / 60 + t * 1.5)]
    pts += [W, H]
    c.create_polygon(*pts, fill="#58c45a", stipple="gray25", width=0, tags=TAG_A)
    for k in range(5):
        bx = (k * 190 + t * 22 * (1 + k % 2)) % (W + 120) - 60
        by = topo + 14 + 10 * math.sin(t + k)
        c.create_oval(bx - 70, by - 18, bx + 70, by + 18, fill="#8be08c",
                      stipple="gray12", width=0, tags=TAG_A)


# ---------------- Sala 1: Vestíbulo ----------------
def _armario(c, x, rotulo):
    c.create_rectangle(x, 55, x + 100, H - 25, fill="#5b3d26", outline="#2b1a0e", width=2, tags=TAG_E)
    c.create_rectangle(x + 8, 68, x + 92, H - 38, outline="#3a2414", tags=TAG_E)
    c.create_oval(x + 44, 118, x + 56, 130, fill=OURO, outline="#7a5a1a", tags=TAG_E)
    c.create_text(x + 50, 82, text=rotulo, fill=OURO, font=("Georgia", 9, "bold"), tags=TAG_E)


def _cena1(c):
    _tijolos(c, "#4a3d34", "#2a211b", 1)
    _piso(c)
    c.create_arc(380, 4, 480, 64, start=0, extent=180, fill="#2e2e33", outline="#15151a",
                 width=3, style="pieslice", tags=TAG_E)
    c.create_rectangle(380, 34, 480, H - 25, fill="#2e2e33", outline="#15151a", width=3, tags=TAG_E)
    for x in (405, 430, 455):
        c.create_line(x, 14, x, H - 25, fill="#1a1a1f", width=3, tags=TAG_E)
    for y in (70, 120, 160):
        for x in (392, 418, 442, 468):
            c.create_oval(x - 2, y - 2, x + 2, y + 2, fill="#6b6b73", width=0, tags=TAG_E)
    c.create_oval(420, 110, 440, 130, fill=OURO, outline="#7a5a1a", width=2, tags=TAG_E)
    _armario(c, 100, "MANTOS")
    _armario(c, 235, "TOMOS")
    _armario(c, 620, "FRASCOS")
    _suportes_tocha(c)


# ---------------- Sala 2: Biblioteca ----------------
def _estante(c, x0, x1, rnd):
    cores = ["#7a2e2e", "#2e4a7a", "#3f6b3a", "#6b4a8a", "#8a6a2e", "#2e6b6b", "#5a3a22"]
    for y in (70, 115, 160):
        x = x0
        while x < x1 - 14:
            w = rnd.randint(8, 14)
            h = rnd.randint(26, 40)
            c.create_rectangle(x, y - h, x + w, y, fill=rnd.choice(cores), outline="#1a120c", tags=TAG_E)
            x += w + 1
        c.create_rectangle(x0 - 4, y, x1 + 4, y + 5, fill="#4a3220", outline="#2a1a10", tags=TAG_E)
    c.create_rectangle(x0 - 8, 25, x0 - 4, 175, fill="#4a3220", width=0, tags=TAG_E)
    c.create_rectangle(x1 + 4, 25, x1 + 8, 175, fill="#4a3220", width=0, tags=TAG_E)


PALAVRA = None  # letras do enigma atual (None = pedras com símbolos de runas)


def definir_palavra(palavra):
    """Faz as pedras da biblioteca mostrarem a palavra do enigma sorteado."""
    global PALAVRA
    PALAVRA = palavra


def _pedras(n):
    esp = 40 if n <= 6 else 34
    return [430 + (i - (n - 1) / 2) * esp for i in range(n)]


def _glifo(c, k, x, y, cor):
    k %= 6
    if k == 0:
        c.create_polygon(x, y - 9, x + 9, y + 8, x - 9, y + 8, fill="", outline=cor, width=2, tags=TAG_A)
    elif k == 1:
        c.create_oval(x - 8, y - 8, x + 8, y + 8, outline=cor, width=2, tags=TAG_A)
        c.create_oval(x - 2, y - 2, x + 2, y + 2, fill=cor, width=0, tags=TAG_A)
    elif k == 2:
        c.create_polygon(x, y - 10, x + 8, y, x, y + 10, x - 8, y, fill="", outline=cor, width=2, tags=TAG_A)
    elif k == 3:
        c.create_line(x - 8, y, x + 8, y, fill=cor, width=2, tags=TAG_A)
        c.create_line(x, y - 9, x, y + 9, fill=cor, width=2, tags=TAG_A)
    elif k == 4:
        c.create_line(x - 7, y - 9, x - 7, y + 9, fill=cor, width=2, tags=TAG_A)
        c.create_line(x - 7, y - 9, x + 7, y + 1, fill=cor, width=2, tags=TAG_A)
        c.create_line(x + 7, y + 1, x - 7, y + 9, fill=cor, width=2, tags=TAG_A)
    else:
        c.create_line(x - 8, y - 8, x + 8, y + 8, fill=cor, width=2, tags=TAG_A)
        c.create_line(x + 8, y - 8, x - 8, y + 8, fill=cor, width=2, tags=TAG_A)
        c.create_line(x, y - 10, x, y + 10, fill=cor, width=2, tags=TAG_A)


def _cena2(c):
    rnd = random.Random(2)
    _tijolos(c, "#3a3340", "#201b25", 2)
    _piso(c, "#15111a")
    _estante(c, 100, 300, rnd)
    _estante(c, 560, 760, rnd)
    c.create_rectangle(390, 150, 470, H - 25, fill="#5d5566", outline="#2d2833", tags=TAG_E)
    c.create_rectangle(380, 140, 480, 152, fill="#7a7184", outline="#2d2833", tags=TAG_E)
    for k in range(6):
        c.create_line(0, 0, 70 - k * 8, k * 12, fill="#6e6678", tags=TAG_E)
        c.create_line(W, 0, W - 70 + k * 8, k * 12, fill="#6e6678", tags=TAG_E)
    _suportes_tocha(c)


def _anim2(c, t, rnd):
    xs = _pedras(len(PALAVRA) if PALAVRA else 6)
    for i, x in enumerate(xs):
        p = 0.5 + 0.5 * math.sin(t * 3 + i)
        cor = "#%02x%02x%02x" % (int(120 + 100 * p), int(90 + 70 * p), int(170 + 60 * p))
        c.create_rectangle(x - 14, 98, x + 14, 134, fill="#3b3548", outline="#9d92b5", width=2, tags=TAG_A)
        if PALAVRA:
            c.create_text(x, 116, text=PALAVRA[i], fill="#f1e6c8", font=("Georgia", 15, "bold"), tags=TAG_A)
        else:
            _glifo(c, i, x, 116, "#f1e6c8")
        c.create_rectangle(x - 17, 95, x + 17, 137, outline=cor, width=2, tags=TAG_A)


# ---------------- Sala 3: Altar ----------------
FRASCOS = ["#d9534f", "#e0b341", "#4f9de0", "#6fbf73", "#b565d9", "#e07f4f", "#4fd9c9"]
FRASCO_X = [190 + i * 80 for i in range(7)]


def _cena3(c):
    _tijolos(c, "#3c3a46", "#1e1d25", 3)
    _piso(c, "#17151d")
    for i, x in enumerate((370, 430, 490)):
        c.create_oval(x - 24, 30, x + 24, 78, fill="#15131a", outline=OURO, width=3, tags=TAG_E)
        c.create_text(x, 54, text=str(i + 1), fill=OURO, font=("Georgia", 18, "bold"), tags=TAG_E)
    c.create_rectangle(150, 135, 710, H - 25, fill="#cfc9bd", outline="#8f897d", width=2, tags=TAG_E)
    c.create_rectangle(125, 118, 735, 138, fill="#e6e0d3", outline="#8f897d", width=2, tags=TAG_E)
    for k in range(5):
        c.create_line(160 + k * 110, 142, 175 + k * 110, H - 28, fill="#aaa497", tags=TAG_E)
    for cor, x in zip(FRASCOS, FRASCO_X):
        c.create_rectangle(x - 5, 66, x + 5, 86, fill="#cfd8dc", outline="#7a8588", tags=TAG_E)
        c.create_rectangle(x - 6, 62, x + 6, 68, fill="#8b5a2b", width=0, tags=TAG_E)
        c.create_oval(x - 18, 84, x + 18, 118, fill=cor, outline="#f3f3f3", tags=TAG_E)
        c.create_oval(x - 11, 90, x - 5, 98, fill="#ffffff", stipple="gray50", width=0, tags=TAG_E)
    _suportes_tocha(c)


def _anim3(c, t, rnd):
    for i, (cor, x) in enumerate(zip(FRASCOS, FRASCO_X)):
        for k in range(2):
            fase = (t * 18 + i * 13 + k * 25) % 50
            y = 62 - fase
            r = 3 - fase / 25
            if r > 0.5:
                c.create_oval(x - r + 4 * math.sin(t + i + k), y - r,
                              x + r + 4 * math.sin(t + i + k), y + r,
                              fill=cor, outline="", tags=TAG_A)


# ---------------- Sala 4: Estufa ----------------
VASOS_X = [95, 165, 235, 305, 555, 625, 695, 765]


def _planta(c, x, rnd):
    c.create_polygon(x - 14, H - 25, x + 14, H - 25, x + 11, H - 48, x - 11, H - 48,
                     fill="#8b4a2b", outline="#4a2a18", tags=TAG_E)
    alt = rnd.randint(55, 95)
    c.create_line(x, H - 48, x + rnd.randint(-8, 8), H - 48 - alt, fill="#2f7a3a", width=3, tags=TAG_E)
    for k in range(4):
        dx = rnd.choice((-1, 1)) * rnd.randint(8, 16)
        y = H - 52 - k * alt / 4
        c.create_oval(x + dx - 9, y - 5, x + dx + 9, y + 5,
                      fill=rnd.choice(("#3f9a4a", "#2f7a3a", "#58b85f")), width=0, tags=TAG_E)
    flor = rnd.choice(("#e0b341", "#d9534f", "#b565d9", "#4fd9c9"))
    c.create_oval(x - 6, H - 52 - alt - 6, x + 6, H - 52 - alt + 6, fill=flor, outline="#ffffff", tags=TAG_E)


def _cena4(c):
    rnd = random.Random(4)
    c.create_rectangle(0, 0, W, H, fill="#10261d", width=0, tags=TAG_E)
    for x in range(0, W + 1, 70):
        c.create_line(x, 0, x, H, fill="#2f6b5a", tags=TAG_E)
    for y in range(0, H, 50):
        c.create_line(0, y, W, y, fill="#2f6b5a", tags=TAG_E)
    c.create_rectangle(0, 0, W, H, outline="#1b4a3b", width=4, tags=TAG_E)
    _piso(c, "#1a1812")
    for x in VASOS_X:
        _planta(c, x, rnd)
    c.create_line(390, 170, 380, H - 25, fill="#2a2a30", width=5, tags=TAG_E)
    c.create_line(470, 170, 480, H - 25, fill="#2a2a30", width=5, tags=TAG_E)
    c.create_oval(360, 110, 500, 185, fill="#1a1a1f", outline="#0a0a0d", width=2, tags=TAG_E)
    c.create_oval(366, 104, 494, 134, fill="#2b2b33", outline="#0a0a0d", width=2, tags=TAG_E)
    _suportes_tocha(c)


def _anim4(c, t, rnd):
    c.create_oval(374, 112, 486, 130, fill="#6fd36f", outline="", tags=TAG_A)
    for k in range(6):
        fase = (t * 16 + k * 9) % 54
        x = 395 + k * 14 + 5 * math.sin(t * 2 + k)
        r = 2 + fase / 14
        if fase < 50:
            c.create_oval(x - r, 118 - fase - r, x + r, 118 - fase + r,
                          outline="#9cf59c", width=1, tags=TAG_A)


# ---------------- Sala 5: Círculo ----------------
CX, CY, RX, RY = 430, 148, 175, 48


def _estatua(c, x, y, cor):
    c.create_polygon(x - 13, y, x + 13, y, x + 9, y - 36, x - 9, y - 36,
                     fill=cor, outline="#201a28", tags=TAG_E)
    c.create_oval(x - 8, y - 52, x + 8, y - 36, fill=cor, outline="#201a28", tags=TAG_E)


def _cena5(c):
    rnd = random.Random(5)
    c.create_rectangle(0, 0, W, H, fill="#17121f", width=0, tags=TAG_E)
    for _ in range(70):
        x, y = rnd.randint(0, W), rnd.randint(0, 90)
        c.create_oval(x, y, x + 2, y + 2, fill=rnd.choice(("#ffffff", "#cdb6ff", "#ffe9a8")),
                      width=0, tags=TAG_E)
    c.create_oval(110, 85, 750, 215, fill="#241a30", outline="#3b2c4d", width=2, tags=TAG_E)
    c.create_oval(CX - 150, CY - 32, CX + 150, CY + 32, fill="#4a4358", outline=OURO, width=2, tags=TAG_E)
    c.create_oval(CX - 120, CY - 22, CX + 120, CY + 22, outline="#6a6078", tags=TAG_E)
    pos = []
    for i in range(6):
        a = math.radians(30 + 60 * i)
        pos.append((i, CX + RX * math.cos(a), CY + RY * math.sin(a)))
    # desenha primeiro as estátuas do fundo (menor y)
    pos.sort(key=lambda p: CY + RY * math.sin(math.radians(30 + 60 * p[0])))
    for i, x, _ in pos:
        y = CY + RY * math.sin(math.radians(30 + 60 * i))
        junto = i in (0, 1)
        _estatua(c, x, y, OURO if junto else "#8d8a99")
    ax = CX + RX * math.cos(math.radians(30))
    bx = CX + RX * math.cos(math.radians(90))
    ay = CY + RY * math.sin(math.radians(30))
    by = CY + RY * math.sin(math.radians(90))
    c.create_line(ax - 10, ay - 22, bx + 10, by - 22, fill="#fff3b0", width=2, tags=TAG_E)
    _suportes_tocha(c)


def _anim5(c, t, rnd):
    p = 0.5 + 0.5 * math.sin(t * 2.5)
    cor = "#%02x%02x%02x" % (int(106 + 106 * p), int(74 + 92 * p), int(168 - 94 * p))
    c.create_oval(CX - 215, CY - 62, CX + 215, CY + 62, outline=cor, width=2,
                  dash=(4, 8), dashoffset=int(t * 20) % 12, tags=TAG_A)
    c.create_oval(CX - 190, CY - 50, CX + 190, CY + 50, outline=cor, width=1,
                  dash=(2, 6), dashoffset=-int(t * 15) % 8, tags=TAG_A)


CENAS = {1: (_cena1, None), 2: (_cena2, _anim2), 3: (_cena3, _anim3),
         4: (_cena4, _anim4), 5: (_cena5, _anim5)}


def desenhar(c, nivel):
    c.delete("all")
    CENAS[nivel][0](c)


def animar(c, nivel, t, frac, aberta=False):
    c.delete(TAG_A)
    rnd = random.Random(int(t * 12))
    anim = CENAS[nivel][1]
    if anim:
        anim(c, t, rnd)
    _chamas(c, t, rnd)
    if aberta:
        r = 90 + 8 * math.sin(t * 3)
        c.create_oval(W / 2 - r * 2, H - r, W / 2 + r * 2, H + r, fill="#ffe9a8",
                      stipple="gray25", width=0, tags=TAG_A)
    else:
        _nevoa(c, t, frac)
