import unittest
from itertools import combinations, permutations, product

from dados import NIVEIS

CAMPOS_NIVEL = {"nivel", "titulo", "tema", "narrativa", "mensagem_sucesso", "mensagem_erro", "questoes"}
CAMPOS_QUESTAO = {"pergunta", "resposta_correta", "formula", "gabarito", "dica", "meta"}


def forca_bruta(meta):
    t = meta["tipo"]
    if t == "pfc":
        return len(list(product(*[range(n) for n in meta["opcoes"]]))) if prod_pequeno(meta) else None
    if t == "permutacao":
        itens = [i for i, c in enumerate(meta["contagens"]) for _ in range(c)]
        return len(set(permutations(itens)))
    if t == "arranjo":
        return len(list(permutations(range(meta["n"]), meta["p"])))
    if t == "combinacao":
        total = 1
        for n, p in meta["grupos"]:
            total *= len(list(combinations(range(n), p)))
        return total
    if t in ("circular", "circular_juntos", "circular_separados"):
        n = meta["n"]
        total = 0
        for resto in permutations(range(1, n)):  # elemento 0 fixo na posição 0
            mesa = (0,) + resto
            if t == "circular":
                total += 1
            elif t == "circular_juntos":
                pos = sorted(mesa.index(x) for x in range(meta["k"]))
                if any(all((p0 + d) % n in pos for d in range(meta["k"])) for p0 in pos):
                    total += 1
            else:
                a, b = mesa.index(0), mesa.index(1)
                if (a - b) % n not in (1, n - 1):
                    total += 1
        return total
    if t in ("fila_juntos", "fila_separados"):
        n, total = meta["n"], 0
        for fila in permutations(range(n)):
            if t == "fila_juntos":
                pos = sorted(fila.index(x) for x in range(meta["k"]))
                ok = pos[-1] - pos[0] == meta["k"] - 1
            else:
                ok = abs(fila.index(0) - fila.index(1)) != 1
            total += ok
        return total
    raise AssertionError(t)


def prod_pequeno(meta):
    total = 1
    for n in meta["opcoes"]:
        total *= n
    return total <= 200000


class TestNiveis(unittest.TestCase):
    def test_estrutura(self):
        self.assertEqual(len(NIVEIS), 5)
        for n in NIVEIS:
            self.assertTrue(CAMPOS_NIVEL <= n.keys())
            self.assertGreaterEqual(len(n["questoes"]), 20, f"nível {n['nivel']}")
            for q in n["questoes"]:
                self.assertTrue(CAMPOS_QUESTAO <= q.keys())

    def test_sem_perguntas_repetidas(self):
        for n in NIVEIS:
            perguntas = [q["pergunta"] for q in n["questoes"]]
            self.assertEqual(len(perguntas), len(set(perguntas)), f"nível {n['nivel']}")

    def test_respostas_por_forca_bruta(self):
        for n in NIVEIS:
            for q in n["questoes"]:
                esperado = forca_bruta(q["meta"])
                if esperado is None:
                    continue
                self.assertEqual(q["resposta_correta"], esperado,
                                 f"nível {n['nivel']}: {q['pergunta'][:60]}")

    def test_respostas_pequenas(self):
        for n in NIVEIS:
            for q in n["questoes"]:
                self.assertLessEqual(q["resposta_correta"], 25000)
                self.assertGreater(q["resposta_correta"], 0)


if __name__ == "__main__":
    unittest.main()
