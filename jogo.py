"""O Laboratório Abandonado do Alquimista: escape room de Análise Combinatória."""

import os
import random
import sys
import time

from dados import NIVEIS

TEMPO_POR_SALA = 300      # segundos de ar respirável por sala
PENALIDADE_ERRO = 20      # segundos perdidos a cada resposta errada
PENALIDADE_DICA = 30      # segundos perdidos ao pedir a dica

COR = {
    "reset": "\033[0m", "negrito": "\033[1m", "verde": "\033[92m",
    "vermelho": "\033[91m", "amarelo": "\033[93m", "ciano": "\033[96m",
    "cinza": "\033[90m",
}


def cor(texto, nome):
    return f"{COR[nome]}{texto}{COR['reset']}"


def preparar_terminal():
    os.system("")  # habilita sequências ANSI no console do Windows
    for fluxo in (sys.stdout, sys.stdin):
        try:
            fluxo.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass


def digitar(texto, atraso=0.012):
    for letra in texto:
        sys.stdout.write(letra)
        sys.stdout.flush()
        time.sleep(atraso)
    print()


def linha(titulo=""):
    print(cor("=" * 64, "cinza"))
    if titulo:
        print(cor(titulo.center(64), "negrito"))
        print(cor("=" * 64, "cinza"))


def barra_gas(restante):
    consumido = max(0, min(1, 1 - restante / TEMPO_POR_SALA))
    cheio = int(consumido * 20)
    cor_barra = "verde" if consumido < 0.5 else "amarelo" if consumido < 0.8 else "vermelho"
    barra = "#" * cheio + "." * (20 - cheio)
    return (f"Gás alquímico [{cor(barra, cor_barra)}] {int(consumido * 100)}%"
            f"  |  ar restante: {max(0, int(restante))}s")


def ler_numero(texto):
    limpo = texto.strip().replace(".", "").replace(" ", "")
    return int(limpo) if limpo.lstrip("-").isdigit() else None


def mostrar_gabarito(q):
    print()
    print(cor("Gabarito", "ciano"))
    print(f"Resposta: {cor(str(q['resposta_correta']), 'verde')}")
    print(f"Fórmula:  {q['formula']}")
    print(q["gabarito"])
    print()


def sortear(nivel, anterior=None):
    """Sorteia um enigma da sala, evitando repetir o da tentativa anterior."""
    opcoes = [q for q in nivel["questoes"] if q is not anterior]
    return random.choice(opcoes)


def jogar_sala(nivel, q):
    linha(f"NÍVEL {nivel['nivel']} - {nivel['titulo'].upper()}")
    print(cor(f"Tópico: {nivel['tema']}", "cinza"))
    print()
    digitar(nivel["narrativa"])
    print()
    print(cor("ENIGMA", "amarelo"))
    print(q["pergunta"])
    print()
    print(cor("Comandos: número = responder | d = dica | s = sair", "cinza"))

    fim = time.time() + TEMPO_POR_SALA
    erros = 0
    dica_usada = False

    while True:
        restante = fim - time.time()
        if restante <= 0:
            print(cor("\nO gás toma o ambiente. Tudo escurece...", "vermelho"))
            mostrar_gabarito(q)
            return False
        print(barra_gas(restante))
        entrada = input("> ").strip().lower()

        if entrada == "s":
            return None
        if entrada == "d":
            if not dica_usada:
                fim -= PENALIDADE_DICA
                dica_usada = True
                print(cor(f"(a dica custa {PENALIDADE_DICA}s de ar)", "cinza"))
            print(cor("DICA: ", "amarelo") + q["dica"])
            continue

        valor = ler_numero(entrada)
        if valor is None:
            print(cor("Digite apenas um número inteiro, 'd' ou 's'.", "cinza"))
            continue

        if valor == q["resposta_correta"]:
            print()
            digitar(cor(nivel["mensagem_sucesso"], "verde"))
            mostrar_gabarito(q)
            input(cor("[Enter para continuar]", "cinza"))
            return True

        erros += 1
        fim -= PENALIDADE_ERRO
        print()
        digitar(cor(nivel["mensagem_erro"], "vermelho"))
        print(cor(f"Tentativas erradas: {erros} (-{PENALIDADE_ERRO}s de ar)", "cinza"))


def abertura():
    linha("O LABORATÓRIO ABANDONADO DO ALQUIMISTA")
    digitar(
        "Você acorda no chão frio de um laboratório subterrâneo. A porta está selada "
        "e um gás esverdeado começa a subir pelas rachaduras. As paredes trazem a "
        "assinatura do lendário Paracelso. Para sobreviver, resolva os enigmas de "
        "combinação e organização de cada sala antes que o ar acabe."
    )
    print()
    print(f"Cada sala tem {TEMPO_POR_SALA}s de ar. Erro: -{PENALIDADE_ERRO}s. "
          f"Dica: -{PENALIDADE_DICA}s.")
    input(cor("\n[Enter para começar]", "cinza"))
    print()


def main():
    preparar_terminal()
    abertura()
    for nivel in NIVEIS:
        q = None
        while True:
            q = sortear(nivel, q)
            resultado = jogar_sala(nivel, q)
            if resultado is True:
                break
            if resultado is None:
                print("Você abandona o laboratório. Até a próxima.")
                return
            if input("Tentar a sala novamente? (s/n) ").strip().lower() != "s":
                print("O laboratório guarda mais uma alma.")
                return
            print()
    linha("FIM")
    print(cor("Você escapou do laboratório de Paracelso. Parabéns!", "verde"))


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nSaindo.")
