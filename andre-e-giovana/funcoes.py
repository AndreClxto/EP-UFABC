# Referente a opção 1
def num_palavras (arquivo):
    quantidade_palavras = 0
    f = open(arquivo, "r", encoding='utf-8-sig')
    for linha in f:
        palavras = linha.split() #separa a linha em palavras
        quantidade_palavras += len(palavras)
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
    for linha in conjunto_linhas:
        for palavra in linha.split():
            palavra_limpa = palavra.strip(".,!?")
            conjunto_palavras.append(palavra_limpa)
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
    conjunto_linhas = f.readlines()
    if conjunto_linhas > 1:
        return f"Há {len(conjunto_linhas)} linhas neste documento."
    elif conjunto_linhas == 0:
        return "O documento está vazio."
    
# Referente a opção 4
def frequencia_palavras(arquivo):
    contagem_palavras = {}
    f = open(arquivo, "r", encoding='utf-8-sig')
    conjunto_linhas = f.readlines()
    for linha in conjunto_linhas:
        conjunto_palavras = linha.split()
        for palavra in conjunto_palavras:
            palavra_limpa = palavra.strip(".,!?")
            if palavra_limpa:
                contagem_palavras[palavra_limpa] = contagem_palavras.get(palavra_limpa, 0) + 1
    return contagem_palavras

# Referente a opção 5
def imp_linha(arquivo, indice_linha):
    f = open(arquivo, "r", encoding='utf-8-sig')
    conjunto_linhas = f.readlines()
    return conjunto_linhas[indice_linha-1]

# Referente a opção 6
def buscar_palavra(maiuscula: str, arquivo):
    f = open(arquivo, "r", encoding='utf-8-sig')    
    conjunto_linhas = f.readlines()
    conjunto_palavras = list()
    for linha in conjunto_linhas:
        for palavra in linha.split():
            conjunto_palavras.append(palavra.upper())
            if palavra.upper() == maiuscula:
                return linha
    return False

# Referente a opção 7
def sub_palavras(nova, antiga, nome_arquivo, arquivo):
    f = open(arquivo, "r+", encoding='utf-8-sig')
    caminho_arquivo = f"{nome_arquivo}.txt"
    novo_arquivo = open(caminho_arquivo, 'w', encoding='utf-8-sig')
    texto = f.read()
    novo_texto = texto.replace(antiga, nova)
    novo_arquivo.write(novo_texto)
