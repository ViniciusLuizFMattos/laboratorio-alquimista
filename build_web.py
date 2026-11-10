"""Gera docs/index.html (versão web, arquivo único) a partir de web/template.html + dados.py."""

import json
import os

from dados import NIVEIS

AQUI = os.path.dirname(os.path.abspath(__file__))


def main():
    with open(os.path.join(AQUI, "web", "template.html"), encoding="utf-8") as f:
        html = f.read()
    dados = "const NIVEIS = " + json.dumps(NIVEIS, ensure_ascii=False, indent=1) + ";"
    html = html.replace("/*DADOS*/", dados)
    saida = os.path.join(AQUI, "docs")
    os.makedirs(saida, exist_ok=True)
    with open(os.path.join(saida, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("docs/index.html gerado")


if __name__ == "__main__":
    main()
