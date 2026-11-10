"""Bancos de enigmas de cada sala.

Cada enigma guarda os parâmetros em `meta`; a resposta e o gabarito são calculados
a partir deles, o que evita divergência entre o texto e a conta.
"""

from collections import Counter
from math import comb, factorial, perm, prod


def _lista(itens, sep=" · "):
    return sep.join(str(i) for i in itens)


# ------------------------------------------------------------------ nível 1: PFC
def pfc(pergunta, etapas):
    ops = [n for _, n in etapas]
    resp = prod(ops)
    linhas = "\n".join(f"  Etapa {i} ({rot}): {n} opções" for i, (rot, n) in enumerate(etapas, 1))
    return {
        "pergunta": pergunta,
        "resposta_correta": resp,
        "formula": "PFC: n1 · n2 · n3 · ...",
        "gabarito": ("A tarefa acontece em etapas e cada etapa tem seu número de opções.\n"
                     f"{linhas}\nPelo PFC, multiplicamos: {_lista(ops)} = {resp}."),
        "dica": ("Quando uma tarefa acontece em etapas independentes, o total é o produto do número "
                 "de opções de cada etapa. Se algo não pode se repetir, as opções diminuem a cada etapa."),
        "meta": {"tipo": "pfc", "opcoes": ops},
    }


QUESTOES_1 = [
    pfc("O traje completo exige 1 manto, 1 tomo e 1 frasco.\nHá 4 mantos diferentes, 3 tomos diferentes "
        "e 5 frascos diferentes.\nQuantos trajes completos distintos podem ser montados?",
        [("manto", 4), ("tomo", 3), ("frasco", 5)]),
    pfc("Um cadeado alquímico tem 3 discos. Cada disco mostra um de 5 símbolos e os símbolos podem se "
        "repetir entre os discos.\nQuantas combinações diferentes o cadeado possui?",
        [("disco 1", 5), ("disco 2", 5), ("disco 3", 5)]),
    pfc("O cofre de Paracelso abre com uma senha de 3 dígitos (de 0 a 9). Os dígitos podem se repetir.\n"
        "Quantas senhas são possíveis?",
        [("1º dígito", 10), ("2º dígito", 10), ("3º dígito", 10)]),
    pfc("Duas runas distintas devem ser gravadas lado a lado na porta, escolhidas entre 6 runas disponíveis, "
        "sem repetir runa.\nDe quantas maneiras isso pode ser feito?",
        [("1ª runa", 6), ("2ª runa", 5)]),
    pfc("Uma poção exige 1 base (3 líquidos possíveis), 1 erva (4 possíveis) e 1 pó (2 possíveis).\n"
        "Quantas poções diferentes podem ser preparadas?",
        [("base", 3), ("erva", 4), ("pó", 2)]),
    pfc("Do vestíbulo ao laboratório há 3 corredores. Do laboratório ao altar há 4 escadas.\n"
        "Quantos caminhos diferentes levam do vestíbulo ao altar passando pelo laboratório?",
        [("corredor", 3), ("escada", 4)]),
    pfc("Um ritual exige 1 vela (5 tipos), 1 incenso (3 tipos), 1 amuleto (4 tipos) e 1 cristal (2 tipos).\n"
        "Quantos rituais diferentes podem ser montados?",
        [("vela", 5), ("incenso", 3), ("amuleto", 4), ("cristal", 2)]),
    pfc("Cada selo do laboratório é formado por 1 letra (A, B, C ou D) seguida de 2 algarismos (0 a 9, "
        "podendo repetir).\nQuantos selos diferentes existem?",
        [("letra", 4), ("1º algarismo", 10), ("2º algarismo", 10)]),
    pfc("Para a cerimônia, o aprendiz escolhe 1 capuz entre 3, 1 par de luvas entre 2 e 1 par de botas entre 4.\n"
        "Quantas combinações de vestimenta existem?",
        [("capuz", 3), ("luvas", 2), ("botas", 4)]),
    pfc("Quantos números de 3 algarismos distintos podem ser formados com os algarismos 1, 2, 3, 4, 5 e 6?",
        [("centena", 6), ("dezena", 5), ("unidade", 4)]),
    pfc("Quantos números naturais de 2 algarismos existem? (O primeiro algarismo não pode ser zero.)",
        [("dezena", 9), ("unidade", 10)]),
    pfc("Uma bandeira ritual tem 3 listras horizontais e cada listra deve ter uma cor diferente das outras. "
        "Há 5 cores disponíveis.\nQuantas bandeiras diferentes podem ser feitas?",
        [("1ª listra", 5), ("2ª listra", 4), ("3ª listra", 3)]),
    pfc("Quatro alavancas diferentes precisam ser acionadas, uma de cada vez, em alguma ordem.\n"
        "De quantas ordens diferentes elas podem ser acionadas?",
        [("1ª alavanca", 4), ("2ª alavanca", 3), ("3ª alavanca", 2), ("4ª alavanca", 1)]),
    pfc("A porta tem 3 entradas. Para sair, é preciso usar uma entrada diferente da que foi usada para entrar.\n"
        "De quantas maneiras é possível entrar e sair?",
        [("entrada", 3), ("saída", 2)]),
    pfc("Uma parede será pintada: há 6 cores para o fundo e 5 cores para as bordas.\n"
        "Quantas combinações de pintura existem?",
        [("fundo", 6), ("borda", 5)]),
    pfc("Na festa de formatura dos alquimistas, cada convidado usa 1 de 3 chapéus, 1 de 4 túnicas, "
        "1 de 2 cajados e 1 de 3 anéis.\nQuantas fantasias diferentes são possíveis?",
        [("chapéu", 3), ("túnica", 4), ("cajado", 2), ("anel", 3)]),
    pfc("Um painel tem 5 lâmpadas e cada uma pode estar acesa ou apagada.\n"
        "Quantas configurações diferentes o painel pode mostrar?",
        [("lâmpada 1", 2), ("lâmpada 2", 2), ("lâmpada 3", 2), ("lâmpada 4", 2), ("lâmpada 5", 2)]),
    pfc("Uma senha é formada por 2 letras do alfabeto (26 letras), podendo repetir.\n"
        "Quantas senhas existem?",
        [("1ª letra", 26), ("2ª letra", 26)]),
    pfc("Uma pedra pode ser colocada em qualquer uma das 6 linhas e em qualquer uma das 5 colunas de um tabuleiro.\n"
        "Em quantas posições diferentes ela pode ficar?",
        [("linha", 6), ("coluna", 5)]),
    pfc("O conselho tem 7 alquimistas e precisa escolher 1 chefe e 1 subchefe, que devem ser pessoas diferentes.\n"
        "De quantas maneiras a escolha pode ser feita?",
        [("chefe", 7), ("subchefe", 6)]),
    pfc("Um ramal de 3 dígitos não pode começar com zero. Os outros dois dígitos podem ser qualquer algarismo.\n"
        "Quantos ramais existem?",
        [("1º dígito", 9), ("2º dígito", 10), ("3º dígito", 10)]),
    pfc("Uma placa de pedra tem 4 posições e cada posição recebe um de 3 símbolos (podendo repetir).\n"
        "Quantas placas diferentes podem ser gravadas?",
        [("posição 1", 3), ("posição 2", 3), ("posição 3", 3), ("posição 4", 3)]),
]


# ------------------------------------------------------------------ nível 2: permutações
def permutacao(pergunta, contagens):
    n = sum(contagens)
    reps = [c for c in contagens if c > 1]
    resp = factorial(n) // prod(factorial(c) for c in reps)
    if reps:
        den = prod(factorial(c) for c in reps)
        fat = _lista(f"{c}!" for c in reps)
        gab = (f"São {n} itens no total, mas alguns se repetem ({', '.join(f'{c} iguais' for c in reps)}).\n"
               f"Se todos fossem diferentes teríamos {n}! = {factorial(n)} ordens.\n"
               f"Trocar os itens iguais entre si não gera ordem nova: dividimos por {fat} = {den}.\n"
               f"  {n}! / ({fat.replace(' · ', ' · ')}) = {factorial(n)} / {den} = {resp}.")
        formula = "P(n; a, b, ...) = n! / (a! · b! · ...)"
        dica = ("Permutação com repetição: n! dividido pelo fatorial de cada quantidade repetida. "
                "Quantos itens iguais existem de cada tipo?")
    else:
        gab = (f"São {n} itens, todos diferentes, e a ordem importa.\n"
               f"  P({n}) = {n}! = {_lista(range(n, 0, -1))} = {resp}.")
        formula = "P(n) = n!"
        dica = "Todos os itens são diferentes: o total de ordenações é n! (n · (n-1) · ... · 1)."
    return {"pergunta": pergunta, "resposta_correta": resp, "formula": formula, "gabarito": gab,
            "dica": dica, "meta": {"tipo": "permutacao", "contagens": contagens}}


def anagrama(palavra, abertura="Quantos anagramas distintos tem a palavra"):
    q = permutacao(f"{abertura} {palavra}?\n(Anagrama é qualquer ordenação das letras, "
                   "com ou sem sentido.)", list(Counter(palavra).values()))
    q["palavra"] = palavra  # o cenário mostra estas letras nas pedras
    return q


QUESTOES_2 = [
    {**permutacao("Para destrancar a porta, é preciso testar todas as ordens possíveis das seis pedras "
                  "A, R, C, A, N, A (a palavra ARCANA e seus anagramas).\nQuantos anagramas distintos existem?",
                  [3, 1, 1, 1]), "palavra": "ARCANA"},
    anagrama("MAGIA"),
    anagrama("RUNAS", "O feitiço só funciona se as letras forem pronunciadas na ordem certa. Quantas ordens "
                      "diferentes existem para as letras da palavra"),
    anagrama("TOMO"),
    anagrama("FOGO"),
    anagrama("OSSOS"),
    anagrama("ARARA"),
    anagrama("ELIXIR"),
    anagrama("ENIGMA"),
    anagrama("ARANHA"),
    anagrama("CRISTAL"),
    permutacao("Cinco tomos diferentes devem ser enfileirados em uma prateleira.\n"
               "De quantas maneiras podem ser organizados?", [1] * 5),
    permutacao("Quatro frascos de cores diferentes serão alinhados em uma bancada.\n"
               "Quantas ordens diferentes existem?", [1] * 4),
    permutacao("Em uma prateleira devem ficar 5 tomos: 3 vermelhos idênticos e 2 azuis idênticos.\n"
               "De quantas maneiras distintas eles podem ser enfileirados?", [3, 2]),
    permutacao("Sete velas serão enfileiradas no altar: 4 vermelhas idênticas e 3 brancas idênticas.\n"
               "Quantas disposições diferentes existem?", [4, 3]),
    permutacao("Seis bandeirolas serão alinhadas: 2 de ouro, 2 de prata e 2 de bronze (as da mesma cor são idênticas).\n"
               "Quantas ordens diferentes existem?", [2, 2, 2]),
    permutacao("Oito pedras serão dispostas em linha: 5 azuis idênticas e 3 verdes idênticas.\n"
               "De quantas maneiras podem ser dispostas?", [5, 3]),
    permutacao("Quatro amuletos serão pendurados em fila: 2 deles são idênticos e os outros 2 são diferentes entre si "
               "e diferentes dos primeiros.\nQuantas ordens distintas existem?", [2, 1, 1]),
    permutacao("Cinco aprendizes, todos diferentes, vão se enfileirar para entrar na sala.\n"
               "De quantas maneiras a fila pode ser formada?", [1] * 5),
    permutacao("Três alavancas diferentes devem ser acionadas, uma de cada vez.\n"
               "Quantas sequências de acionamento existem?", [1] * 3),
    permutacao("Seis cristais serão enfileirados: 3 azuis idênticos, 2 verdes idênticos e 1 vermelho.\n"
               "Quantas disposições distintas existem?", [3, 2, 1]),
    permutacao("Seis poções diferentes serão colocadas em uma estante.\n"
               "De quantas formas podem ser organizadas?", [1] * 6),
]


# ------------------------------------------------------------------ nível 3: arranjo
def arranjo(pergunta, n, p):
    resp = perm(n, p)
    fatores = list(range(n, n - p, -1))
    posicoes = ", ".join(f"{f} para a {i}ª posição" for i, f in enumerate(fatores, 1))
    return {
        "pergunta": pergunta,
        "resposta_correta": resp,
        "formula": "A(n, p) = n! / (n - p)!",
        "gabarito": (f"Escolhemos {p} entre {n} e a ordem importa (sem repetição): é um arranjo.\n"
                     f"  A({n}, {p}) = {n}! / ({n} - {p})! = {n}! / {n - p}! = {_lista(fatores)} = {resp}.\n"
                     f"Pelo PFC: {posicoes}."),
        "dica": ("A ordem importa e nenhum item se repete. Use A(n, p) = n!/(n-p)! ou multiplique as opções "
                 "que restam a cada posição."),
        "meta": {"tipo": "arranjo", "n": n, "p": p},
    }


QUESTOES_3 = [
    arranjo("Você deve escolher 3 dos 7 frascos e colocá-los nos encaixes 1º, 2º e 3º, sem repetir frasco. "
            "A ordem altera a reação.\nQuantas sequências de reação diferentes são possíveis?", 7, 3),
    arranjo("Oito alquimistas disputam um torneio. O 1º, o 2º e o 3º lugares recebem prêmios diferentes.\n"
            "De quantas maneiras o pódio pode ser formado?", 8, 3),
    arranjo("Há 5 chaves diferentes e 3 fechaduras numeradas. Cada fechadura recebe uma chave diferente.\n"
            "De quantas maneiras as chaves podem ser colocadas?", 5, 3),
    arranjo("O cofre tem senha de 4 dígitos distintos, usando os algarismos de 0 a 9.\n"
            "Quantas senhas são possíveis?", 10, 4),
    arranjo("Entre 6 tomos diferentes, escolhem-se 3 para formar uma pilha na mesa (a ordem na pilha importa).\n"
            "Quantas pilhas diferentes existem?", 6, 3),
    arranjo("Nove candidatos disputam os cargos de mestre, vice-mestre e escriba, todos diferentes.\n"
            "De quantas formas os cargos podem ser preenchidos?", 9, 3),
    arranjo("Entre 9 runas, 2 serão gravadas em sequência na entrada (a ordem muda o significado).\n"
            "Quantas sequências existem?", 9, 2),
    arranjo("Seis estátuas diferentes estão disponíveis e 4 delas serão colocadas em fila no corredor.\n"
            "Quantas filas diferentes podem ser montadas?", 6, 4),
    arranjo("Existem 8 salas no laboratório e é preciso visitar 3 delas, em sequência, sem repetir sala.\n"
            "Quantos roteiros distintos existem?", 8, 3),
    arranjo("Quantos números de 3 algarismos distintos podem ser formados com os algarismos 1, 2, 3, 4, 5 e 6?", 6, 3),
    arranjo("Um código de 3 letras distintas é formado com as letras A, B, C, D, E, F e G.\n"
            "Quantos códigos existem?", 7, 3),
    arranjo("Entre 6 aprendizes, 4 vão se sentar em 4 bancos numerados.\n"
            "De quantas maneiras isso pode ser feito?", 6, 4),
    arranjo("Entre 10 candidatos, escolhem-se um mestre e um assistente (funções diferentes).\n"
            "De quantas formas?", 10, 2),
    arranjo("Seis poções diferentes: escolhem-se 4 para beber em sequência (a ordem importa).\n"
            "Quantas sequências existem?", 6, 4),
    arranjo("Entre 5 elementos (fogo, água, terra, ar e éter), 2 são ativados em sequência.\n"
            "Quantas sequências existem?", 5, 2),
    arranjo("Uma coroa terá 4 gemas diferentes em fila, escolhidas entre 7 gemas.\n"
            "Quantas coroas distintas podem ser feitas?", 7, 4),
    arranjo("Dez alquimistas disputam um concurso com premiação de 1º, 2º e 3º lugares.\n"
            "De quantas maneiras os prêmios podem ser distribuídos?", 10, 3),
    arranjo("Entre 5 notas musicais diferentes, forma-se uma melodia de 3 notas distintas (a ordem importa).\n"
            "Quantas melodias existem?", 5, 3),
    arranjo("Uma bandeira tem 3 faixas verticais de cores diferentes, escolhidas entre 6 cores.\n"
            "Quantas bandeiras diferentes existem?", 6, 3),
    arranjo("Palavras mágicas de 3 letras distintas são formadas com as vogais A, E, I, O e U.\n"
            "Quantas palavras existem?", 5, 3),
    arranjo("Entre 12 aprendizes, escolhem-se um capitão e um imediato (funções diferentes).\n"
            "De quantas formas?", 12, 2),
    arranjo("Entre 8 selos diferentes, 4 são colocados em sequência no pergaminho.\n"
            "Quantas sequências distintas existem?", 8, 4),
]


# ------------------------------------------------------------------ nível 4: combinação
def _txt_comb(n, p):
    if p == 1:
        return f"C({n}, 1) = {n}"
    num = _lista(range(n, n - p, -1))
    den = _lista(range(p, 0, -1))
    return f"C({n}, {p}) = ({num}) / ({den}) = {comb(n, p)}"


def combinacao(pergunta, grupos):
    resp = prod(comb(n, p) for n, p in grupos)
    if len(grupos) == 1:
        n, p = grupos[0]
        gab = (f"A ordem não importa: é uma combinação.\n  {_txt_comb(n, p)}.\n"
               f"Raciocínio alternativo: o arranjo A({n},{p}) = {perm(n, p)} conta cada grupo {factorial(p)} vezes "
               f"({p}!), então {perm(n, p)} / {factorial(p)} = {resp}.")
    else:
        linhas = "\n".join(f"  Grupo {i}: {_txt_comb(n, p)}" for i, (n, p) in enumerate(grupos, 1))
        gab = ("Cada grupo é escolhido sem importar a ordem (combinação) e as escolhas são independentes.\n"
               f"{linhas}\nPelo PFC, multiplicamos: {_lista(comb(n, p) for n, p in grupos)} = {resp}.")
    return {
        "pergunta": pergunta,
        "resposta_correta": resp,
        "formula": "C(n, p) = n! / (p! · (n - p)!)",
        "gabarito": gab,
        "dica": ("Como a ordem NÃO importa, use C(n, p) = n!/(p!(n-p)!), ou comece pelo arranjo e divida por p!. "
                 "Se há mais de um grupo, calcule cada combinação e multiplique."),
        "meta": {"tipo": "combinacao", "grupos": grupos},
    }


QUESTOES_4 = [
    combinacao("O antídoto exige exatamente 3 plantas diferentes, escolhidas entre as 8 disponíveis. "
               "A ordem em que são colocadas no caldeirão não muda nada.\n"
               "Quantos grupos de plantas distintos podem ser formados?", [(8, 3)]),
    combinacao("Um comitê de 4 pessoas será escolhido entre 9 alquimistas.\nQuantos comitês diferentes existem?", [(9, 4)]),
    combinacao("Um feitiço usa 5 pedras escolhidas entre 7 pedras diferentes (a ordem é irrelevante).\n"
               "Quantas escolhas existem?", [(7, 5)]),
    combinacao("Seis alquimistas se encontram e cada um cumprimenta todos os outros uma única vez.\n"
               "Quantos cumprimentos acontecem?", [(6, 2)]),
    combinacao("Oito pontos de energia estão marcados no chão, sem três deles alinhados. Cada par de pontos é ligado "
               "por um fio.\nQuantos fios são necessários?", [(8, 2)]),
    combinacao("Entre 10 ingredientes, escolhem-se 2 para a mistura base.\nDe quantas formas?", [(10, 2)]),
    combinacao("Entre 12 frascos diferentes, escolhem-se 3 para levar na bolsa.\nQuantas escolhas existem?", [(12, 3)]),
    combinacao("Uma equipe de 3 aprendizes será escolhida entre 10 para limpar a estufa.\nQuantas equipes existem?", [(10, 3)]),
    combinacao("A receita pede 2 ervas, escolhidas entre 5, e 1 mineral, escolhido entre 4.\n"
               "Quantas receitas diferentes existem?", [(5, 2), (4, 1)]),
    combinacao("Uma banca terá 2 mestres escolhidos entre 4 e 3 aprendizes escolhidos entre 5.\n"
               "Quantas bancas diferentes podem ser formadas?", [(4, 2), (5, 3)]),
    combinacao("Entre 8 chaves, escolhem-se 4 para formar um molho.\nQuantos molhos diferentes existem?", [(8, 4)]),
    combinacao("De um baralho de 6 cartas mágicas, retiram-se 2 cartas.\nDe quantas maneiras?", [(6, 2)]),
    combinacao("Quantos subconjuntos de 3 elementos possui o conjunto {1, 2, 3, 4, 5, 6, 7}?", [(7, 3)]),
    combinacao("Uma mistura leva 1 líquido, escolhido entre 3, e 2 ervas, escolhidas entre 6.\n"
               "Quantas misturas diferentes existem?", [(3, 1), (6, 2)]),
    combinacao("Entre 6 relíquias, escolhem-se 5 para expor na vitrine.\nQuantas escolhas existem?", [(6, 5)]),
    combinacao("Entre 9 livros, escolhem-se 3 para levar à viagem.\nQuantas escolhas existem?", [(9, 3)]),
    combinacao("Um júri de 2 pessoas será escolhido entre 11 alquimistas.\nQuantos júris diferentes existem?", [(11, 2)]),
    combinacao("Entre 5 mestres, uma comissão de 3 será formada.\nQuantas comissões existem?", [(5, 3)]),
    combinacao("Uma equipe terá 2 alquimistas escolhidos entre 6 e 2 aprendizes escolhidos entre 4.\n"
               "Quantas equipes diferentes existem?", [(6, 2), (4, 2)]),
    combinacao("Entre 10 relíquias, escolhem-se 4 para o ritual.\nDe quantas formas?", [(10, 4)]),
    combinacao("Escolhem-se 3 reagentes entre 8 e, depois, 1 catalisador entre 2.\n"
               "Quantas preparações diferentes existem?", [(8, 3), (2, 1)]),
    combinacao("Entre 7 pergaminhos, escolhem-se 6 para queimar.\nQuantas escolhas existem?", [(7, 6)]),
]


# ------------------------------------------------------------------ nível 5: circular e restrições
def circular(pergunta, n):
    resp = factorial(n - 1)
    return {
        "pergunta": pergunta, "resposta_correta": resp,
        "formula": "PC(n) = (n - 1)!",
        "gabarito": ("Em uma mesa redonda, girar todo o grupo não gera disposição nova. Fixamos um elemento "
                     "e permutamos os demais.\n"
                     f"  PC({n}) = ({n} - 1)! = {n - 1}! = {resp}."),
        "dica": "Na mesa redonda, rotações iguais contam como uma só: use PC(n) = (n-1)!.",
        "meta": {"tipo": "circular", "n": n},
    }


def circular_juntos(pergunta, n, k):
    a, b = factorial(n - k), factorial(k)
    return {
        "pergunta": pergunta, "resposta_correta": a * b,
        "formula": "PC(n) = (n - 1)!   e   bloco de k itens juntos: k! permutações internas",
        "gabarito": (f"Trate os {k} que ficam juntos como um único bloco.\n"
                     f"  Elementos na mesa: {n - k} soltos + 1 bloco = {n - k + 1} elementos.\n"
                     f"  Permutação circular de {n - k + 1}: ({n - k + 1} - 1)! = {n - k}! = {a}.\n"
                     f"  Dentro do bloco, os {k} podem se reorganizar: {k}! = {b}.\n"
                     f"  Total: {a} · {b} = {a * b} maneiras."),
        "dica": ("Junte os que devem ficar lado a lado em um bloco, faça a permutação circular dos elementos "
                 "restantes e multiplique pelas formas de ordenar dentro do bloco."),
        "meta": {"tipo": "circular_juntos", "n": n, "k": k},
    }


def circular_separados(pergunta, n):
    total, juntos = factorial(n - 1), factorial(n - 2) * 2
    return {
        "pergunta": pergunta, "resposta_correta": total - juntos,
        "formula": "separados = total - juntos",
        "gabarito": (f"Total na mesa redonda: ({n} - 1)! = {total}.\n"
                     f"Com os dois juntos (bloco): PC({n - 1}) = {n - 2}! = {factorial(n - 2)}, e eles podem trocar "
                     f"de lugar: 2! = 2, logo {juntos}.\n"
                     f"Separados: {total} - {juntos} = {total - juntos} maneiras."),
        "dica": "Conte o total, depois conte os casos em que os dois ficam juntos (bloco) e subtraia.",
        "meta": {"tipo": "circular_separados", "n": n},
    }


def fila_juntos(pergunta, n, k):
    a, b = factorial(n - k + 1), factorial(k)
    return {
        "pergunta": pergunta, "resposta_correta": a * b,
        "formula": "(n - k + 1)! · k!",
        "gabarito": (f"Trate os {k} que ficam juntos como um único bloco.\n"
                     f"  Elementos na fila: {n - k} soltos + 1 bloco = {n - k + 1}, que se ordenam de "
                     f"{n - k + 1}! = {a} maneiras.\n"
                     f"  Dentro do bloco: {k}! = {b}.\n"
                     f"  Total: {a} · {b} = {a * b}."),
        "dica": "Una os que devem ficar juntos em um bloco, permute os elementos e multiplique pela ordem interna do bloco.",
        "meta": {"tipo": "fila_juntos", "n": n, "k": k},
    }


def fila_separados(pergunta, n):
    total, juntos = factorial(n), factorial(n - 1) * 2
    return {
        "pergunta": pergunta, "resposta_correta": total - juntos,
        "formula": "separados = total - juntos",
        "gabarito": (f"Total de filas: {n}! = {total}.\n"
                     f"Com os dois juntos (bloco): {n - 1}! = {factorial(n - 1)}, vezes 2! = 2, logo {juntos}.\n"
                     f"Separados: {total} - {juntos} = {total - juntos}."),
        "dica": "Conte o total, depois conte os casos em que os dois ficam juntos (bloco) e subtraia.",
        "meta": {"tipo": "fila_separados", "n": n},
    }


QUESTOES_5 = [
    circular_juntos("Seis estátuas devem ser posicionadas ao redor da mesa redonda. Paracelso e Isolda precisam "
                    "ficar sempre lado a lado. Rotações da mesa inteira não contam como arranjos diferentes.\n"
                    "De quantas maneiras distintas as estátuas podem ser dispostas?", 6, 2),
    circular("Cinco alquimistas vão se sentar ao redor de uma mesa redonda. Rotações não contam como disposições "
             "diferentes.\nDe quantas maneiras podem se sentar?", 5),
    circular("Sete velas diferentes serão acesas em círculo ao redor do caldeirão.\n"
             "Quantas disposições distintas existem (rotações são iguais)?", 7),
    circular("Quatro estátuas diferentes ficarão ao redor de uma mesa redonda.\n"
             "Quantas disposições distintas existem?", 4),
    circular("Seis aprendizes de mãos dadas formam uma roda. Rotações da roda não contam como diferentes.\n"
             "Quantas rodas distintas existem?", 6),
    circular_juntos("Cinco amigos sentam-se em uma mesa redonda e dois deles fazem questão de ficar lado a lado.\n"
                    "De quantas maneiras podem se sentar?", 5, 2),
    circular_juntos("Sete estátuas serão dispostas em uma mesa redonda e duas delas, gêmeas, ficam sempre lado a lado.\n"
                    "Quantas disposições existem?", 7, 2),
    circular_juntos("Seis alquimistas sentam-se em uma mesa redonda e 3 deles (mestre, aprendiz e escriba) precisam "
                    "ficar juntos.\nQuantas disposições distintas existem?", 6, 3),
    circular_juntos("Quatro cristais diferentes são colocados em um círculo e dois deles são complementares e devem "
                    "ficar lado a lado.\nDe quantas maneiras?", 4, 2),
    circular_juntos("Sete amuletos são dispostos em círculo e 3 deles, da mesma coleção, devem ficar juntos.\n"
                    "Quantas disposições existem?", 7, 3),
    circular_separados("Cinco alquimistas sentam-se em uma mesa redonda. Dois deles são rivais e não podem ficar "
                       "lado a lado.\nDe quantas maneiras podem se sentar?", 5),
    circular_separados("Seis estátuas ficam em uma mesa redonda; duas delas se repelem e não podem ficar vizinhas.\n"
                       "Quantas disposições existem?", 6),
    circular_separados("Quatro cristais ficam em círculo e dois deles reagem mal se ficarem lado a lado.\n"
                       "De quantas formas podem ser dispostos?", 4),
    fila_juntos("Cinco aprendizes entram em fila, e dois deles, irmãos, precisam ficar lado a lado.\n"
                "De quantas maneiras a fila pode ser formada?", 5, 2),
    fila_juntos("Seis livros diferentes são colocados em uma prateleira e dois deles (volumes 1 e 2) devem ficar juntos.\n"
                "Quantas ordens existem?", 6, 2),
    fila_juntos("Quatro frascos são alinhados na bancada e dois deles devem ficar juntos.\n"
                "Quantas ordens existem?", 4, 2),
    fila_juntos("Seis alquimistas se enfileiram e 3 deles precisam ficar juntos.\nDe quantas maneiras?", 6, 3),
    fila_separados("Cinco aprendizes entram em fila, mas dois deles, rivais, não podem ficar lado a lado.\n"
                   "De quantas maneiras a fila pode ser formada?", 5),
    fila_separados("Quatro frascos são alinhados na bancada e dois deles reagem se ficarem juntos.\n"
                   "Quantas ordens evitam esse contato?", 4),
    fila_separados("Seis tomos são colocados em uma prateleira, e dois deles não podem ficar lado a lado.\n"
                   "Quantas ordens existem?", 6),
    circular("Oito pedras diferentes serão posicionadas em círculo ritual (rotações são iguais).\n"
             "Quantas disposições distintas existem?", 8),
    circular_juntos("Oito estudantes sentam-se em uma mesa redonda; 2 deles precisam ficar lado a lado.\n"
                    "De quantas maneiras?", 8, 2),
]
