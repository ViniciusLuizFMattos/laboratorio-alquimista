"""Dados dos níveis de "O Laboratório Abandonado do Alquimista"."""

NIVEIS = [
    {
        "nivel": 1,
        "titulo": "O Vestíbulo",
        "tema": "Princípio Fundamental da Contagem (PFC)",
        "narrativa": (
            "A porta de ferro se fecha atrás de você com um estrondo. No vestíbulo, "
            "três armários trazem inscrições gastas: MANTOS, TOMOS e FRASCOS. "
            "Uma placa de latão diz: 'Só passa quem vestir o traje completo do aprendiz'."
        ),
        "pergunta": (
            "O traje completo exige 1 manto, 1 tomo e 1 frasco.\n"
            "Há 4 mantos diferentes, 3 tomos diferentes e 5 frascos diferentes.\n"
            "Quantos trajes completos distintos podem ser montados?"
        ),
        "resposta_correta": 60,
        "formula": "PFC: n1 · n2 · n3 · ...",
        "gabarito": (
            "Cada escolha é independente das outras e acontece em etapas.\n"
            "  Etapa 1 (manto):  4 opções\n"
            "  Etapa 2 (tomo):   3 opções\n"
            "  Etapa 3 (frasco): 5 opções\n"
            "Pelo PFC, multiplicamos: 4 · 3 · 5 = 60 trajes."
        ),
        "dica": (
            "Quando uma tarefa acontece em etapas independentes, o total é o "
            "produto do número de opções de cada etapa."
        ),
        "mensagem_sucesso": (
            "As três inscrições brilham em âmbar. Engrenagens ocultas giram dentro "
            "da parede e a porta de ferro desliza para o lado, soltando poeira de séculos."
        ),
        "mensagem_erro": (
            "O cadeado emite um estalo seco e uma névoa esverdeada escapa pelas "
            "frestas. Respire fundo: releia as etapas e tente de novo."
        ),
    },
    {
        "nivel": 2,
        "titulo": "A Biblioteca das Sombras",
        "tema": "Permutação com Repetição (anagramas)",
        "narrativa": (
            "Estantes altas se perdem na escuridão. No centro, um pedestal exibe seis "
            "pedras com letras gravadas: A, R, C, A, N, A. O alquimista deixou um recado: "
            "'A palavra certa abre o caminho, mas há muitas formas de embaralhá-la'."
        ),
        "pergunta": (
            "Para destrancar a porta, é preciso testar todas as ordens possíveis das "
            "seis pedras A, R, C, A, N, A (a palavra ARCANA e seus anagramas).\n"
            "Quantos anagramas distintos existem?"
        ),
        "resposta_correta": 120,
        "formula": "P(n; a, b, ...) = n! / (a! · b! · ...)",
        "gabarito": (
            "São 6 letras no total, mas a letra A aparece 3 vezes.\n"
            "Se todas fossem diferentes teríamos 6! = 720 ordens.\n"
            "Trocar os três A's entre si não gera palavra nova: dividimos por 3! = 6.\n"
            "  6! / 3! = 720 / 6 = 120 anagramas."
        ),
        "dica": (
            "Permutação de n itens com repetição: n! dividido pelo fatorial de cada "
            "quantidade repetida. Quantas vezes a letra A aparece?"
        ),
        "mensagem_sucesso": (
            "As estantes tremem e uma delas desliza, revelando uma passagem estreita. "
            "As letras se apagam das pedras, uma a uma, como se tivessem cumprido seu dever."
        ),
        "mensagem_erro": (
            "Um sussurro percorre os corredores e as velas se apagam por um instante. "
            "O gás fica mais denso. Lembre-se: letras repetidas não geram palavras novas."
        ),
    },
    {
        "nivel": 3,
        "titulo": "O Altar dos Elixires",
        "tema": "Arranjo Simples",
        "narrativa": (
            "Sobre um altar de mármore rachado repousam 7 frascos de cores distintas. "
            "Diante deles, três encaixes numerados: 1º, 2º e 3º. A inscrição avisa: "
            "'A reação só ocorre na ordem correta. Misture primeiro o que vem primeiro'."
        ),
        "pergunta": (
            "Você deve escolher 3 dos 7 frascos e colocá-los nos encaixes 1º, 2º e 3º, "
            "sem repetir frasco. A ordem altera a reação.\n"
            "Quantas sequências de reação diferentes são possíveis?"
        ),
        "resposta_correta": 210,
        "formula": "A(n, p) = n! / (n - p)!",
        "gabarito": (
            "Escolhemos 3 frascos entre 7 e a ordem importa: é um arranjo.\n"
            "  A(7, 3) = 7! / (7 - 3)! = 7! / 4! = 7 · 6 · 5 = 210.\n"
            "Pelo PFC: 7 opções para o 1º encaixe, 6 para o 2º, 5 para o 3º."
        ),
        "dica": (
            "A ordem importa e nenhum frasco se repete. Use A(n, p) = n!/(n-p)! "
            "ou multiplique as opções que restam a cada encaixe."
        ),
        "mensagem_sucesso": (
            "Os frascos fervem em sequência, cada cor acendendo a seguinte. O altar "
            "afunda no chão com um rangido e abre um corredor iluminado por brasas azuis."
        ),
        "mensagem_erro": (
            "Os frascos tremem e um deles estala, soltando vapor amargo. A ordem "
            "importa aqui, e cada frasco só pode ser usado uma vez. Tente novamente."
        ),
    },
    {
        "nivel": 4,
        "titulo": "A Estufa dos Reagentes",
        "tema": "Combinação Simples",
        "narrativa": (
            "O ar é úmido e perfumado. Em canteiros de vidro crescem 8 plantas raras. "
            "Um caldeirão enferrujado espera os ingredientes do antídoto. Uma tábua "
            "de madeira diz: 'Importa quais plantas entram, não a ordem em que caem'."
        ),
        "pergunta": (
            "O antídoto exige exatamente 3 plantas diferentes, escolhidas entre as 8 "
            "disponíveis. A ordem em que são colocadas no caldeirão não muda nada.\n"
            "Quantos grupos de plantas distintos podem ser formados?"
        ),
        "resposta_correta": 56,
        "formula": "C(n, p) = n! / (p! · (n - p)!)",
        "gabarito": (
            "A ordem não importa: é uma combinação.\n"
            "  C(8, 3) = 8! / (3! · 5!) = (8 · 7 · 6) / (3 · 2 · 1) = 336 / 6 = 56.\n"
            "Raciocínio alternativo: o arranjo A(8,3) = 336 conta cada grupo 3! = 6 vezes, "
            "então 336 / 6 = 56."
        ),
        "dica": (
            "Como a ordem NÃO importa, comece pelo arranjo e divida por p!, "
            "ou use C(n, p) = n!/(p!(n-p)!)."
        ),
        "mensagem_sucesso": (
            "O caldeirão borbulha e libera um vapor dourado que dissolve as vinhas "
            "da parede. Uma grade de vidro se ergue lentamente, revelando a escada para o último salão."
        ),
        "mensagem_erro": (
            "As folhas murcham, o líquido ganha um tom escuro e um cheiro azedo "
            "invade o ar. Pergunte-se: trocar a ordem das plantas gera um antídoto novo?"
        ),
    },
    {
        "nivel": 5,
        "titulo": "O Círculo Interno",
        "tema": "Permutação Circular com restrição (itens juntos)",
        "narrativa": (
            "No coração do laboratório, uma mesa redonda de pedra aguarda 6 estátuas "
            "de alquimistas. Duas delas, Paracelso e sua discípula Isolda, foram "
            "esculpidas de mãos dadas e não podem ser separadas. O gás já arde nos olhos: "
            "esta é a última porta."
        ),
        "pergunta": (
            "Seis estátuas devem ser posicionadas ao redor da mesa redonda. Paracelso e "
            "Isolda precisam ficar sempre lado a lado. Rotações da mesa inteira não "
            "contam como arranjos diferentes.\n"
            "De quantas maneiras distintas as estátuas podem ser dispostas?"
        ),
        "resposta_correta": 48,
        "formula": "PC(n) = (n - 1)!   e   bloco de k itens juntos: k! permutações internas",
        "gabarito": (
            "Trate Paracelso e Isolda como um único bloco.\n"
            "  Elementos na mesa: 4 estátuas soltas + 1 bloco = 5 elementos.\n"
            "  Permutação circular de 5: (5 - 1)! = 4! = 24.\n"
            "  Dentro do bloco, os dois podem trocar de lugar: 2! = 2.\n"
            "  Total: 24 · 2 = 48 maneiras."
        ),
        "dica": (
            "Junte as duas estátuas em um bloco, faça a permutação circular dos "
            "elementos restantes (n-1)! e multiplique pelas formas de ordenar dentro do bloco."
        ),
        "mensagem_sucesso": (
            "As estátuas giram até encontrar seus lugares e o círculo se acende em "
            "runas douradas. O teto se abre num rangido: ar frio e estrelas. Você escapou "
            "do laboratório de Paracelso."
        ),
        "mensagem_erro": (
            "Uma runa se apaga com um estalo e o gás queima sua garganta. Lembre-se: "
            "na mesa redonda, girar todo o grupo não cria uma disposição nova."
        ),
    },
]
