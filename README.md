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

Cada sala tem 300 s de "ar". Erro custa 20 s e a dica custa 30 s. A música pode ser ligada/desligada pelo botão no topo ou com a tecla `M`.

## Estrutura

- `interface.py`: janela do jogo (tkinter)
- `cenarios.py`: cenário animado de cada sala, desenhado em código
- `audio.py`: trilha ambiente gerada por código na primeira execução (pasta `audio/`) e efeitos sonoros (Windows)
- `dados.py`: os 5 níveis (narrativa, pergunta, resposta, dica, mensagens, gabarito)
- `jogo.py`: versão de terminal
- `test_niveis.py`: confere os gabaritos (`python -m unittest`)
