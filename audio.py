"""Trilha sonora ambiente (gerada por código, sem arquivos externos) e efeitos."""

import array
import math
import os
import random
import threading
import wave

try:
    import winsound
except ImportError:  # fora do Windows o jogo funciona sem som
    winsound = None

TAXA = 16000
DURACAO = 24  # segundos por volta do loop
PASTA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "audio")

# chave: (frequências do drone em múltiplos de 0.25 Hz para o loop fechar sem estalo,
#         notas dos sinos, semente)
FAIXAS = {
    "menu": ([55, 82.5, 110, 130.5], [440, 523.25, 659.25], 1),
    1: ([49, 73.5, 98, 116.5], [392, 466.16, 587.33], 2),
    2: ([55, 82.5, 110, 131], [440, 523.25, 622.25], 3),
    3: ([58.25, 87.25, 116.5, 138.5], [466.16, 554.37, 698.46], 4),
    4: ([51.75, 77.5, 103.75, 123], [415.3, 493.88, 622.25], 5),
    5: ([46.25, 69.25, 92.5, 110], [370, 440, 554.37, 740], 6),
    "fim": ([65.5, 98, 131, 196], [523.25, 659.25, 783.99, 1046.5], 7),
}

_atual = None
_mudo = False
_trava = threading.Lock()


def _gerar(chave, caminho):
    drone, escala, semente = FAIXAS[chave]
    rnd = random.Random(semente)
    sinos = [(rnd.uniform(1, DURACAO - 5), rnd.choice(escala)) for _ in range(7)]
    dois_pi = 2 * math.pi
    bruto = []
    for i in range(TAXA * DURACAO):
        t = i / TAXA
        lfo = 0.65 + 0.35 * math.sin(dois_pi * t * 2 / DURACAO)
        mod = 0.8 * math.sin(dois_pi * 0.25 * t)
        v = 0.0
        for k, f in enumerate(drone):
            v += math.sin(dois_pi * f * t + mod) * (0.55 / (k + 1) + 0.1)
        v *= lfo
        for inicio, f in sinos:
            dt = t - inicio
            if 0 <= dt < 4:
                env = math.exp(-dt * 1.3) * min(1.0, dt * 40)
                v += env * 0.5 * (math.sin(dois_pi * f * dt)
                                  + 0.4 * math.sin(dois_pi * f * 2.76 * dt))
        bruto.append(v)
    pico = max(abs(x) for x in bruto) or 1.0
    escala_pcm = 0.55 * 32767 / pico
    dados = array.array("h", (int(x * escala_pcm) for x in bruto))
    os.makedirs(PASTA, exist_ok=True)
    temp = caminho + ".tmp"
    with wave.open(temp, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(TAXA)
        w.writeframes(dados.tobytes())
    os.replace(temp, caminho)


def _tocar(chave):
    caminho = os.path.join(PASTA, f"{chave}.wav")
    with _trava:
        if not os.path.exists(caminho):
            _gerar(chave, caminho)
    if chave == _atual and not _mudo:
        winsound.PlaySound(caminho, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)


def tocar(chave):
    """Troca a trilha de fundo (gera o arquivo na primeira vez)."""
    global _atual
    _atual = chave
    if _mudo or winsound is None:
        return
    threading.Thread(target=_tocar, args=(chave,), daemon=True).start()


def alternar_mudo():
    """Liga/desliga a música. Retorna True se ficou mudo."""
    global _mudo
    _mudo = not _mudo
    if winsound is not None:
        if _mudo:
            winsound.PlaySound(None, winsound.SND_PURGE)
        elif _atual is not None:
            tocar(_atual)
    return _mudo


def parar():
    if winsound is not None:
        winsound.PlaySound(None, winsound.SND_PURGE)


def _notas(sequencia):
    if _mudo or winsound is None:
        return

    def rodar():
        for freq, ms in sequencia:
            try:
                winsound.Beep(freq, ms)
            except RuntimeError:
                pass

    threading.Thread(target=rodar, daemon=True).start()


def sucesso():
    _notas([(523, 90), (659, 90), (784, 90), (1047, 240)])


def erro():
    _notas([(196, 180), (147, 320)])
