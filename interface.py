"""Interface gráfica (tkinter) de "O Laboratório Abandonado do Alquimista"."""

import random
import time
import tkinter as tk
from tkinter import font as tkfont

import audio
import cenarios
from dados import NIVEIS

TEMPO_POR_SALA = 300
PENALIDADE_ERRO = 20
PENALIDADE_DICA = 30

BG = "#14110f"
PAINEL = "#201a16"
OURO = "#d4a64a"
TEXTO = "#e8dcc4"
CINZA = "#8a7f6e"
VERDE = "#6fbf73"
AMARELO = "#e0b341"
VERMELHO = "#d9534f"


class Jogo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("O Laboratório Abandonado do Alquimista")
        self.geometry("920x900")
        self.minsize(920, 860)
        self.configure(bg=BG)

        self.f_titulo = tkfont.Font(family="Georgia", size=22, weight="bold")
        self.f_sub = tkfont.Font(family="Georgia", size=12, slant="italic")
        self.f_texto = tkfont.Font(family="Georgia", size=12)
        self.f_enigma = tkfont.Font(family="Georgia", size=13, weight="bold")
        self.f_mono = tkfont.Font(family="Consolas", size=11)
        self.f_botao = tkfont.Font(family="Georgia", size=11, weight="bold")

        self.indice = 0
        self.q = None
        self.fim = 0.0
        self.erros = 0
        self.dica_usada = False
        self.sala_ativa = False
        self.tick_id = None

        self.t0 = time.time()
        barra = tk.Frame(self, bg=BG)
        barra.pack(fill="x", padx=20, pady=(8, 0))
        self.btn_musica = tk.Button(barra, text="♪ Música: ligada", command=self.alternar_musica,
                                    font=self.f_mono, bg=PAINEL, fg=CINZA, relief="flat",
                                    activebackground=PAINEL, activeforeground=OURO, bd=0,
                                    padx=10, pady=3, cursor="hand2")
        self.btn_musica.pack(side="right")
        self.bind("<m>", lambda e: self.alternar_musica() if e.widget.winfo_class() != "Entry" else None)
        self.protocol("WM_DELETE_WINDOW", self.fechar)

        self.container = tk.Frame(self, bg=BG)
        self.container.pack(fill="both", expand=True, padx=20, pady=(0, 14))
        self.tela_inicial()

    def alternar_musica(self):
        mudo = audio.alternar_mudo()
        self.btn_musica.config(text="♪ Música: desligada" if mudo else "♪ Música: ligada")

    def fechar(self):
        audio.parar()
        self.destroy()

    def criar_cenario(self, pai, nivel):
        self.cena = tk.Canvas(pai, width=cenarios.W, height=cenarios.H, bg=BG,
                              highlightthickness=2, highlightbackground=OURO)
        self.cena.pack(pady=(0, 6))
        self.nivel_cena = nivel
        cenarios.desenhar(self.cena, nivel)

    # ---------- utilidades ----------
    def limpar(self):
        if self.tick_id:
            self.after_cancel(self.tick_id)
            self.tick_id = None
        self.sala_ativa = False
        for w in self.container.winfo_children():
            w.destroy()

    def botao(self, pai, texto, comando, cor=OURO):
        return tk.Button(pai, text=texto, command=comando, font=self.f_botao,
                         bg=cor, fg=BG, activebackground=TEXTO, activeforeground=BG,
                         relief="flat", padx=18, pady=8, cursor="hand2", bd=0)

    def rotulo(self, pai, texto, fonte=None, cor=TEXTO, **kw):
        kw.setdefault("justify", "left")
        return tk.Label(pai, text=texto, font=fonte or self.f_texto, fg=cor, bg=BG,
                        wraplength=840, **kw)

    # ---------- telas ----------
    def tela_inicial(self):
        self.limpar()
        self.indice = 0
        audio.tocar("menu")
        self.criar_cenario(self.container, 1)
        cenarios.animar(self.cena, 1, 3.0, 0.15)
        self.rotulo(self.container, "O LABORATÓRIO\nABANDONADO DO ALQUIMISTA",
                    self.f_titulo, OURO, justify="center").pack(pady=(30, 14))
        self.rotulo(
            self.container,
            "Você acorda no chão frio de um laboratório subterrâneo. A porta está selada "
            "e um gás esverdeado sobe pelas rachaduras. As paredes trazem a assinatura do "
            "lendário Paracelso. Resolva os enigmas de Análise Combinatória de cada sala "
            "antes que o ar acabe.",
        ).pack(pady=10)
        self.rotulo(
            self.container,
            f"Cada sala tem {TEMPO_POR_SALA}s de ar  •  Erro: -{PENALIDADE_ERRO}s  •  "
            f"Dica: -{PENALIDADE_DICA}s",
            self.f_sub, CINZA,
        ).pack(pady=20)
        self.botao(self.container, "Entrar no laboratório", self.iniciar_sala).pack(pady=20)

    def iniciar_sala(self):
        self.limpar()
        nivel = NIVEIS[self.indice]
        self.q = random.choice([q for q in nivel["questoes"] if q is not self.q])
        self.erros = 0
        self.dica_usada = False
        self.fim = time.time() + TEMPO_POR_SALA
        self.sala_ativa = True
        audio.tocar(nivel["nivel"])

        cab = tk.Frame(self.container, bg=BG)
        cab.pack(fill="x")
        self.rotulo(cab, f"SALA {nivel['nivel']} DE {len(NIVEIS)}  •  {nivel['tema']}",
                    self.f_sub, CINZA).pack(anchor="w")
        self.rotulo(cab, nivel["titulo"], self.f_titulo, OURO).pack(anchor="w", pady=(0, 4))
        self.criar_cenario(self.container, nivel["nivel"])

        topo = tk.Frame(self.container, bg=BG)
        topo.pack(fill="x")

        self.canvas = tk.Canvas(topo, height=22, bg=PAINEL, highlightthickness=1,
                                highlightbackground=CINZA)
        self.canvas.pack(fill="x")
        self.lbl_gas = self.rotulo(topo, "", self.f_mono, CINZA)
        self.lbl_gas.pack(anchor="w", pady=(2, 8))

        self.rotulo(self.container, nivel["narrativa"], self.f_sub, TEXTO).pack(anchor="w", pady=6)

        caixa = tk.Frame(self.container, bg=PAINEL, padx=14, pady=10)
        caixa.pack(fill="x", pady=8)
        tk.Label(caixa, text="ENIGMA", font=self.f_botao, fg=AMARELO, bg=PAINEL).pack(anchor="w")
        tk.Label(caixa, text=self.q["pergunta"], font=self.f_enigma, fg=TEXTO, bg=PAINEL,
                 wraplength=800, justify="left").pack(anchor="w", pady=(4, 0))

        linha = tk.Frame(self.container, bg=BG)
        linha.pack(fill="x", pady=8)
        self.entrada = tk.Entry(linha, font=self.f_enigma, width=10, bg=PAINEL, fg=TEXTO,
                                insertbackground=OURO, relief="flat", justify="center")
        self.entrada.pack(side="left", ipady=6, padx=(0, 10))
        self.entrada.bind("<Return>", lambda e: self.responder())
        self.entrada.focus_set()
        self.btn_responder = self.botao(linha, "Responder", self.responder)
        self.btn_responder.pack(side="left", padx=4)
        self.btn_dica = self.botao(linha, f"Dica (-{PENALIDADE_DICA}s)", self.pedir_dica, CINZA)
        self.btn_dica.pack(side="left", padx=4)

        self.lbl_msg = self.rotulo(self.container, "", self.f_texto, TEXTO)
        self.lbl_msg.pack(anchor="w", pady=4)

        self.area_final = tk.Frame(self.container, bg=BG)
        self.area_final.pack(fill="both", expand=True)

        self.atualizar_gas()

    # ---------- lógica da sala ----------
    def restante(self):
        return self.fim - time.time()

    def atualizar_gas(self):
        if not self.sala_ativa:
            return
        resto = self.restante()
        if resto <= 0:
            self.estourou_tempo()
            return
        frac = max(0.0, min(1.0, 1 - resto / TEMPO_POR_SALA))
        cor = VERDE if frac < 0.5 else AMARELO if frac < 0.8 else VERMELHO
        self.canvas.delete("all")
        largura = self.canvas.winfo_width()
        self.canvas.create_rectangle(0, 0, largura * frac, 22, fill=cor, width=0)
        self.lbl_gas.config(text=f"Gás alquímico: {int(frac * 100)}%   |   ar restante: {int(resto)}s")
        cenarios.animar(self.cena, self.nivel_cena, time.time() - self.t0, frac)
        self.tick_id = self.after(100, self.atualizar_gas)

    def pedir_dica(self):
        if not self.sala_ativa:
            return
        if not self.dica_usada:
            self.fim -= PENALIDADE_DICA
            self.dica_usada = True
            self.btn_dica.config(text="Dica usada")
        self.mensagem("DICA: " + self.q["dica"], AMARELO)

    def mensagem(self, texto, cor):
        self.lbl_msg.config(text=texto, fg=cor)

    @staticmethod
    def ler_numero(texto):
        limpo = texto.strip().replace(".", "").replace(" ", "")
        return int(limpo) if limpo.lstrip("-").isdigit() else None

    def responder(self):
        if not self.sala_ativa:
            return
        nivel = NIVEIS[self.indice]
        valor = self.ler_numero(self.entrada.get())
        if valor is None:
            self.mensagem("Digite apenas um número inteiro.", CINZA)
            return
        if valor == self.q["resposta_correta"]:
            self.sala_ativa = False
            audio.sucesso()
            cenarios.animar(self.cena, self.nivel_cena, time.time() - self.t0, 0, aberta=True)
            self.mensagem(nivel["mensagem_sucesso"], VERDE)
            self.mostrar_gabarito(self.q, sucesso=True)
        else:
            audio.erro()
            self.erros += 1
            self.fim -= PENALIDADE_ERRO
            self.mensagem(f"{nivel['mensagem_erro']}\n(Erros: {self.erros}  •  -{PENALIDADE_ERRO}s de ar)",
                          VERMELHO)
            self.entrada.delete(0, "end")

    def estourou_tempo(self):
        nivel = NIVEIS[self.indice]
        self.sala_ativa = False
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 0, self.canvas.winfo_width(), 22, fill=VERMELHO, width=0)
        self.lbl_gas.config(text="Gás alquímico: 100%   |   ar restante: 0s")
        self.mensagem("O gás toma o ambiente e tudo escurece... Estude o gabarito e tente de novo.",
                      VERMELHO)
        self.mostrar_gabarito(self.q, sucesso=False)

    def mostrar_gabarito(self, q, sucesso):
        self.entrada.config(state="disabled")
        self.btn_responder.config(state="disabled")
        self.btn_dica.config(state="disabled")

        txt = tk.Text(self.area_final, height=7, font=self.f_mono, bg=PAINEL, fg=TEXTO,
                      relief="flat", wrap="word", padx=10, pady=8)
        txt.insert("end", f"GABARITO — resposta: {q['resposta_correta']}\n")
        txt.insert("end", f"Fórmula: {q['formula']}\n\n{q['gabarito']}")
        txt.config(state="disabled")
        txt.pack(fill="both", expand=True, pady=(4, 8))

        ultimo = self.indice == len(NIVEIS) - 1
        if sucesso:
            rotulo = "Ver desfecho" if ultimo else "Próxima sala"
            self.botao(self.area_final, rotulo, self.avancar, VERDE).pack(anchor="e")
        else:
            self.botao(self.area_final, "Tentar a sala novamente", self.iniciar_sala, VERMELHO).pack(anchor="e")

    def avancar(self):
        self.indice += 1
        if self.indice >= len(NIVEIS):
            self.tela_final()
        else:
            self.iniciar_sala()

    def tela_final(self):
        self.limpar()
        audio.tocar("fim")
        self.criar_cenario(self.container, 5)
        cenarios.animar(self.cena, 5, 1.0, 0, aberta=True)
        self.rotulo(self.container, "VOCÊ ESCAPOU!", self.f_titulo, VERDE, justify="center").pack(pady=(40, 20))
        self.rotulo(self.container,
                    "O teto se abre sobre o céu estrelado. Você dominou o Princípio Fundamental "
                    "da Contagem, permutações, arranjos, combinações e a mesa circular. "
                    "O laboratório de Paracelso fica para trás.",
                    justify="center").pack(pady=10)
        self.botao(self.container, "Jogar novamente", self.tela_inicial).pack(pady=30)


if __name__ == "__main__":
    Jogo().mainloop()
