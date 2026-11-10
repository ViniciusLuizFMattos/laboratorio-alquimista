# O Laboratório Abandonado do Alquimista

Escape room com interface gráfica para praticar Análise Combinatória: PFC, permutação com repetição, arranjo, combinação e permutação circular.

## Como jogar

Requer Python 3.8 ou superior com tkinter (já incluso no instalador oficial). Sem dependências externas.

```bash
python interface.py
```

Versão só de terminal:

```bash
python jogo.py
```

Cada sala tem 300 s de "ar". Erro custa 20 s e a dica custa 30 s. A música começa desligada; use o botão no topo ou a tecla `M` para ligar.

## Versão online

Jogue no navegador: https://viniciusluizfmattos.github.io/laboratorio-alquimista/

A página é gerada com `python build_web.py` (a partir de `web/template.html` e `dados.py`) e fica em `docs/index.html`.

## Enigmas

Cada sala tem 22 enigmas diferentes e um deles é sorteado a cada partida (na versão web, o jogo dá preferência aos que ainda não apareceram). Respostas e gabaritos são calculados por fórmula em `questoes.py`, e `test_niveis.py` confere todos por força bruta.

## Estrutura

- `questoes.py`: bancos de enigmas de cada sala
- `build_web.py` e `web/`: geração da versão web

- `interface.py`: janela do jogo (tkinter)
- `cenarios.py`: cenário animado de cada sala, desenhado em código
- `audio.py`: trilha ambiente gerada por código na primeira execução (pasta `audio/`) e efeitos sonoros (Windows)
- `dados.py`: os 5 níveis (narrativa, pergunta, resposta, dica, mensagens, gabarito)
- `jogo.py`: versão de terminal
- `test_niveis.py`: confere os gabaritos (`python -m unittest`)
