"""Dados dos níveis de "O Laboratório Abandonado do Alquimista".

Cada nível tem uma lista de `questoes`; uma delas é sorteada a cada partida.
"""

from questoes import QUESTOES_1, QUESTOES_2, QUESTOES_3, QUESTOES_4, QUESTOES_5

NIVEIS = [
    {
        "nivel": 1,
        "titulo": "O Vestíbulo",
        "tema": "Princípio Fundamental da Contagem (PFC)",
        "narrativa": (
            "A porta de ferro se fecha atrás de você com um estrondo. No vestíbulo, três armários trazem "
            "inscrições gastas: MANTOS, TOMOS e FRASCOS. Uma placa de latão exibe o enigma que guarda a saída."
        ),
        "mensagem_sucesso": (
            "As inscrições brilham em âmbar. Engrenagens ocultas giram dentro da parede e a porta de ferro "
            "desliza para o lado, soltando poeira de séculos."
        ),
        "mensagem_erro": (
            "O cadeado emite um estalo seco e uma névoa esverdeada escapa pelas frestas. Respire fundo: "
            "releia as etapas e tente de novo."
        ),
        "questoes": QUESTOES_1,
    },
    {
        "nivel": 2,
        "titulo": "A Biblioteca das Sombras",
        "tema": "Permutação Simples e com Repetição (anagramas)",
        "narrativa": (
            "Estantes altas se perdem na escuridão. No centro, um pedestal exibe pedras com símbolos gravados. "
            "O alquimista deixou um recado: 'A ordem certa abre o caminho, mas há muitas formas de embaralhar'."
        ),
        "mensagem_sucesso": (
            "As estantes tremem e uma delas desliza, revelando uma passagem estreita. As letras se apagam "
            "das pedras, uma a uma, como se tivessem cumprido seu dever."
        ),
        "mensagem_erro": (
            "Um sussurro percorre os corredores e as velas se apagam por um instante. O gás fica mais denso. "
            "Lembre-se: itens repetidos não geram ordens novas."
        ),
        "questoes": QUESTOES_2,
    },
    {
        "nivel": 3,
        "titulo": "O Altar dos Elixires",
        "tema": "Arranjo Simples",
        "narrativa": (
            "Sobre um altar de mármore rachado repousam frascos de cores distintas. Diante deles, encaixes "
            "numerados. A inscrição avisa: 'A reação só ocorre na ordem correta. Misture primeiro o que vem primeiro'."
        ),
        "mensagem_sucesso": (
            "Os frascos fervem em sequência, cada cor acendendo a seguinte. O altar afunda no chão com um "
            "rangido e abre um corredor iluminado por brasas azuis."
        ),
        "mensagem_erro": (
            "Os frascos tremem e um deles estala, soltando vapor amargo. A ordem importa aqui, e cada item "
            "só pode ser usado uma vez. Tente novamente."
        ),
        "questoes": QUESTOES_3,
    },
    {
        "nivel": 4,
        "titulo": "A Estufa dos Reagentes",
        "tema": "Combinação Simples",
        "narrativa": (
            "O ar é úmido e perfumado. Em canteiros de vidro crescem plantas raras. Um caldeirão enferrujado "
            "espera os ingredientes do antídoto. Uma tábua de madeira diz: 'Importa quais entram, não a ordem em que caem'."
        ),
        "mensagem_sucesso": (
            "O caldeirão borbulha e libera um vapor dourado que dissolve as vinhas da parede. Uma grade de "
            "vidro se ergue lentamente, revelando a escada para o último salão."
        ),
        "mensagem_erro": (
            "As folhas murcham, o líquido ganha um tom escuro e um cheiro azedo invade o ar. Pergunte-se: "
            "trocar a ordem dos itens gera um grupo novo?"
        ),
        "questoes": QUESTOES_4,
    },
    {
        "nivel": 5,
        "titulo": "O Círculo Interno",
        "tema": "Permutação Circular e Restrições (juntos ou separados)",
        "narrativa": (
            "No coração do laboratório, uma mesa redonda de pedra aguarda as estátuas dos alquimistas. "
            "Algumas foram esculpidas de mãos dadas; outras jamais podem ficar lado a lado. O gás já arde "
            "nos olhos: esta é a última porta."
        ),
        "mensagem_sucesso": (
            "As estátuas giram até encontrar seus lugares e o círculo se acende em runas douradas. O teto "
            "se abre num rangido: ar frio e estrelas. Você escapou do laboratório de Paracelso."
        ),
        "mensagem_erro": (
            "Uma runa se apaga com um estalo e o gás queima sua garganta. Lembre-se: na mesa redonda, "
            "girar todo o grupo não cria uma disposição nova."
        ),
        "questoes": QUESTOES_5,
    },
]
