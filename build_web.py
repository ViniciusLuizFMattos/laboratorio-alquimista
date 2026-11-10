"""Gera docs/index.html (versão web, arquivo único) a partir de web/template.html + dados.py."""

import json
import os

from dados import NIVEIS

AQUI = os.path.dirname(os.path.abspath(__file__))


def main():
    with open(os.path.join(AQUI, "web", "template.html"), encoding="utf-8") as f:
        html = f.read()
    publico = [{**n, "questoes": [{k: v for k, v in q.items() if k != "meta"} for q in n["questoes"]]}
               for n in NIVEIS]
    dados = "const NIVEIS = " + json.dumps(publico, ensure_ascii=False, separators=(",", ":")) + ";"
    html = html.replace("/*DADOS*/", dados)
    saida = os.path.join(AQUI, "docs")
    os.makedirs(saida, exist_ok=True)
    with open(os.path.join(saida, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("docs/index.html gerado")


if __name__ == "__main__":
    main()
