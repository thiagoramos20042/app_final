import streamlit as st
import sqlite3

# Função para criar a tabela de respostas no banco de dados
def criar_tabela():
    conn = sqlite3.connect('respostas.db')
    cursor = conn.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS respostas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER,
            funcao TEXT,
            acertos INTEGER
        )
        '''
    )
    conn.commit()
    conn.close()

# Função para inserir uma nova resposta no banco de dados
def inserir_resposta(nome, idade, funcao, acertos):
    conn = sqlite3.connect('respostas.db')
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO respostas (nome, idade, funcao, acertos)
        VALUES (?, ?, ?, ?)
        ''', (nome, idade, funcao, acertos)
    )
    conn.commit()
    conn.close()

# Criar a tabela se não existir
criar_tabela()

# Inicializar variáveis no estado da sessão
if "iniciar_teste" not in st.session_state:
    st.session_state.iniciar_teste = False
if "respostas" not in st.session_state:
    st.session_state.respostas = [""] * 11  # Ajuste o número conforme a quantidade de perguntas

# Formulário para capturar as informações do usuário
if not st.session_state.iniciar_teste:
    st.title("Teste Básico de Estatística")
    st.header("Teste de Estatística")

    with st.form("dados_usuario"):
        nome = st.text_input("Nome Completo:")
        idade = st.number_input("Idade:", min_value=0, max_value=150)
        funcao = st.text_input("Função:")
        iniciar = st.form_submit_button("Começar teste")

    if iniciar and nome and idade and funcao:
        # Armazena os dados e inicia o teste
        st.session_state.nome = nome
        st.session_state.idade = idade
        st.session_state.funcao = funcao
        st.session_state.iniciar_teste = True

# Exibir as perguntas se o teste foi iniciado
if st.session_state.iniciar_teste:
    perguntas = {
        "1. Qual das alternativas descreve melhor o que representa a média de um conjunto de dados?": [
            "A) O valor mais alto do conjunto de dados.",
            "B) O valor central exato entre o menor e o maior valor.",
            "C) A soma de todos os valores dividida pelo número de valores.",
            "D) O valor que ocorre com mais frequência no conjunto de dados."
        ],
        "2. Em uma amostra de dados com um número ímpar de observações, como é determinada a mediana?": [
            "A) A mediana é a média de todos os valores.",
            "B) A mediana é a média dos valores mínimo e máximo.",
            "C) A mediana é o valor central após ordenar todos os dados.",
            "D) A mediana é a soma dos valores centrais após ordenar todos os dados."
        ],
        "3. Qual das opções abaixo descreve corretamente o conceito de moda?": [
            "A) A moda é o valor que representa a média de todas as observações no conjunto de dados.",
            "B) A moda é o valor que aparece com maior frequência num conjunto de dados.",
            "C) A moda é o ponto médio entre o menor e o maior valor do conjunto de dados.",
            "D) A moda é a diferença entre o valor máximo e o valor mínimo no conjunto de dados."
        ],
        "4. Qual das alternativas a seguir descreve corretamente a correlação entre duas variáveis?": [
            "A) A correlação é uma medida que indica se uma variável é sempre maior que a outra.",
            "B) A correlação mede a relação entre duas variáveis, variando de -1 a 1, onde valores próximos a 1 indicam uma relação linear positiva.",
            "C) A correlação só pode ser positiva, indicando que ambas as variáveis sempre aumentam juntas.",
            "D) A correlação determina a causa de uma variável em relação à outra, mostrando uma relação de causa e efeito."
        ],
        "5. Em uma distribuição de dados, qual seria o impacto de uma variância alta?": [
            "A) Os dados estariam concentrados em torno da média.",
            "B) Os dados estariam mais dispersos em relação à média.",
            "C) Os dados estariam uniformemente distribuídos.",
            "D) Todos os dados teriam o mesmo valor."
        ],
        "6. Sabemos que a Loja A apresenta um desvio padrão maior do que a Loja B. Com base nessa informação, o que se pode inferir sobre as vendas desses produtos?": [
            "A) As vendas na Loja A são mais uniformes, com a maioria dos produtos vendendo quantidades muito próximas da média.",
            "B) A Loja A tem uma média de vendas mais alta do que a Loja B, e por isso apresenta um desvio padrão maior.",
            "C) As vendas na Loja A têm maior variabilidade, o que indica que as quantidades vendidas dos produtos variam mais em torno da média do que na Loja B.",
            "D) A Loja B tem uma maior dispersão de vendas entre os produtos, pois possui o menor desvio padrão."
        ],
        "7. O que a curtose mede em uma distribuição de dados?": [
            "A) A tendência central de um conjunto de dados.",
            "B) A dispersão em relação à média.",
            "C) A simetria da distribuição dos dados.",
            "D) A presença de picos e caudas em uma distribuição."
        ],
        "8. O que podemos dizer de um gráfico de vendas que apresenta assimetria positiva?": [
            "A) A maior parte das vendas está concentrada em valores mais altos, com uma cauda que se estende para valores menores.",
            "B) O gráfico apresenta vendas igualmente distribuídas entre valores altos e baixos.",
            "C) A assimetria positiva indica que os valores das vendas estão todos muito próximos da média.",
            "D) A maioria das vendas está concentrada em valores mais baixos, enquanto a cauda do gráfico se estende para valores mais altos."
        ],
        "9. Quando a covariância entre duas variáveis é positiva, o que isso geralmente indica sobre a relação entre elas?": [
            "A) Que as duas variáveis não têm nenhuma relação.",
            "B) Que uma variável tende a aumentar quando a outra diminui.",
            "C) Que as duas variáveis tendem a aumentar ou diminuir juntas.",
            "D) Que as duas variáveis possuem o mesmo valor."
        ],
        "10. Qual é a principal razão para utilizar a distribuição t-Student ao invés da distribuição normal quando se trabalha com amostras pequenas?": [
            "A) A distribuição t-Student possui uma média maior que a distribuição normal.",
            "B) A distribuição t-Student tem variância fixa, enquanto a normal não.",
            "C) A distribuição t-Student possui caudas mais longas, refletindo maior incerteza nas estimativas de média quando o tamanho da amostra é pequeno.",
            "D) A distribuição t-Student é mais fácil de calcular do que a normal."
        ],
        "11. Em uma distribuição normal do peso das laranjas colhidas em uma fazenda, qual das afirmações abaixo é verdadeira?": [
            "A) A média, a mediana e a moda são aproximadamente iguais e localizam-se no centro da distribuição.",
            "B) A curva da distribuição normal é assimétrica, com uma cauda maior para valores altos do peso das laranjas.",
            "C) A distribuição normal possui dois picos distintos, indicando duas modas.",
            "D) A maior parte dos pesos concentra-se nos extremos, afastados da média."
        ]
    }

    respostas_corretas = [
        "C) A soma de todos os valores dividida pelo número de valores.",
        "C) A mediana é o valor central após ordenar todos os dados.",
        "B) A moda é o valor que aparece com maior frequência num conjunto de dados.",
        "B) A correlação mede a relação entre duas variáveis, variando de -1 a 1, onde valores próximos a 1 indicam uma relação linear positiva.",
        "B) Os dados estariam mais dispersos em relação à média.",
        "C) As vendas na Loja A têm maior variabilidade, o que indica que as quantidades vendidas dos produtos variam mais em torno da média do que na Loja B.",
        "D) A presença de picos e caudas em uma distribuição.",
        "D) A maioria das vendas está concentrada em valores mais baixos, enquanto a cauda do gráfico se estende para valores mais altos.",
        "C) Que as duas variáveis tendem a aumentar ou diminuir juntas.",
        "C) A distribuição t-Student possui caudas mais longas, refletindo maior incerteza nas estimativas de média quando o tamanho da amostra é pequeno.",
        "A) A média, a mediana e a moda são aproximadamente iguais e localizam-se no centro da distribuição."
    ]

    # Exibir as perguntas
    for i, (pergunta, alternativas) in enumerate(perguntas.items()):
        st.write(pergunta)
        st.session_state.respostas[i] = st.radio(
            label="", options=alternativas, index=alternativas.index(st.session_state.respostas[i]) if st.session_state.respostas[i] in alternativas else 0, key=f"pergunta_{i}"
        )
        st.write("")

    # Botão para finalizar o teste
    if st.button("Finalizar Teste"):
        # Contar acertos
        acertos = sum([1 for i, resposta in enumerate(st.session_state.respostas) if resposta == respostas_corretas[i]])

        # Salvar respostas no banco de dados
        inserir_resposta(st.session_state.nome, st.session_state.idade, st.session_state.funcao, acertos)

        # Agradecimento ao usuário
        st.write("Obrigado por participar do teste!")
        st.write(f"Você acertou {acertos} de {len(perguntas)} perguntas.")
