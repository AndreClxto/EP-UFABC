# Importa as funções necessárias das bibliotecas 'matplotlib.pyplot' e 'wordcloud'
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Referente a opção 1
def num_palavras (arquivo):
    quantidade_palavras = 0
    f = open(arquivo, "r", encoding='utf-8-sig')
   # Separa as linhas em palavras
    for linha in f:
        palavras = linha.split()
        quantidade_palavras += len(palavras)
  # Conta as palavras do arquivo
    if quantidade_palavras == 1:
        return "O arquivo possui 1 palavra."
    elif quantidade_palavras > 1:
        return f"O arquivo possui {quantidade_palavras} palavras."
    elif quantidade_palavras == 0:
        return "O documento está vazio."

# Referente a opção 2
def palavras_unicas(arquivo):
    conjunto_palavras = list()
    f = open(arquivo, "r", encoding='utf-8-sig')
    conjunto_linhas = f.readlines()
    #Separa o arquivo em palavras
    for linha in conjunto_linhas:
        for palavra in linha.split():
            palavra_limpa = palavra.strip(".,!?")
            conjunto_palavras.append(palavra_limpa)
    # Conta as palavras somente uma vez
    unicas = set(list(map(str.upper, conjunto_palavras)))
    if len(unicas) > 1: 
        return f"Há {len(unicas)} palavras distintas neste documento."
    elif len(unicas) == 1:
        return "Há 1 palavra distintas neste documento."
    elif len(unicas) == 0:
        return "O documento está vazio."

# Referente a opção 3
def num_linhas(arquivo):
    f = open(arquivo, "r", encoding='utf-8-sig')
    #Separa o arquivo em linhas
    conjunto_linhas = f.readlines()
    #Conta a quantidade de linhas
    if conjunto_linhas > 1:
        return f"Há {len(conjunto_linhas)} linhas neste documento."
    elif conjunto_linhas == 0:
        return "O documento está vazio."
    
# Referente a opção 4
def frequencia_palavras(arquivo):
    contagem_palavras = {}
    f = open(arquivo, "r", encoding='utf-8-sig')
    # separa o arquivo em linhas
    conjunto_linhas = f.readlines()
    # separa a linha em palavras
    for linha in conjunto_linhas:
        conjunto_palavras = linha.split()
        for palavra in conjunto_palavras:
            # remove a pontuação
            palavra_limpa = palavra.strip(".,!?")
            # conta a frequência de cada palavra
            if palavra_limpa:
                contagem_palavras[palavra_limpa] = contagem_palavras.get(palavra_limpa, 0) + 1
    return contagem_palavras

# Referente a opção 5
def imp_linha(arquivo, indice_linha):
    f = open(arquivo, "r", encoding='utf-8-sig')
    # Separa o arquivo em linhas
    conjunto_linhas = f.readlines()
    # retorna a linha específica
    return conjunto_linhas[indice_linha-1]

# Referente a opção 6
def buscar_palavra(maiuscula: str, arquivo):
    f = open(arquivo, "r", encoding='utf-8-sig')    
    conjunto_linhas = f.readlines()
    # armazena as palavras limpas do arquivo
    conjunto_palavras = list()
    for linha in conjunto_linhas:
        for palavra in linha.split():
            # excluir pontuação
            palavra_limpa = palavra.strip(".,!?")
            # adiciona a palavra limpa à lista conjunto_palavras
            conjunto_palavras.append(palavra_limpa.upper())
            # verifica se a palavra limpa é igual a palavra especificada
            if palavra_limpa.upper() == maiuscula:
                return linha
    return False

# Referente a opção 7
def sub_palavras(nova, antiga, nome_arquivo, arquivo):
    f = open(arquivo, "r+", encoding='utf-8-sig')
    # cria o caminho onde as mudanças serão salvas
    caminho_arquivo = f"{nome_arquivo}.txt"
    # abre o arquivo onde as mudanças serão salvas no modo de edição
    novo_arquivo = open(caminho_arquivo, 'w', encoding='utf-8-sig')
    texto = f.read()
    # Substitui a ocorrência da palavra antiga pela nova
    novo_texto = texto.replace(antiga, nova)
    # escreve o texto modificado no novo arquivo
    novo_arquivo.write(novo_texto)


# Referente a opção 9
def nuvemDePalavras(arquivo, bg_color, colormap, max_palavras):
    # Lê todo o texto do arquivo
    f = open(arquivo, "r", encoding='utf-8-sig')
    texto = f.read()
    # Cria a nuvem com alguns parametros oferecidos pelo usuário
    wordcloud = WordCloud(max_words=max_palavras, max_font_size=60, background_color=bg_color, colormap=colormap).generate(texto)
    # Exibi a imagem
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()
