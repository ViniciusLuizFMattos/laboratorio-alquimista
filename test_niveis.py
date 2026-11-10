import math
import unittest
from itertools import permutations

from dados import NIVEIS

CAMPOS = {"nivel", "titulo", "narrativa", "pergunta", "resposta_correta", "dica",
          "mensagem_sucesso", "mensagem_erro", "gabarito", "formula"}


class TestNiveis(unittest.TestCase):
    def test_campos(self):
        self.assertEqual(len(NIVEIS), 5)
        for n in NIVEIS:
            self.assertTrue(CAMPOS <= n.keys())

    def test_respostas(self):
        esperado = [
            4 * 3 * 5,
            math.factorial(6) // math.factorial(3),
            math.perm(7, 3),
            math.comb(8, 3),
            math.factorial(4) * 2,
        ]
        self.assertEqual([n["resposta_correta"] for n in NIVEIS], esperado)

    def test_anagramas_por_forca_bruta(self):
        self.assertEqual(len(set(permutations("ARCANA"))), NIVEIS[1]["resposta_correta"])

    def test_circular_por_forca_bruta(self):
        disposicoes = set()
        for p in permutations(range(6)):
            i = p.index(0)
            rot = p[i:] + p[:i]  # normaliza rotações
            if rot.index(1) in (1, 5):  # 0 e 1 vizinhos
                disposicoes.add(rot)
        self.assertEqual(len(disposicoes), NIVEIS[4]["resposta_correta"])


if __name__ == "__main__":
    unittest.main()
