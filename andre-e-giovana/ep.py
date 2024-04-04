# Importa as funções necessárias da biblioteca 'os' e do arquivo 'funcoes.py'
from funcoes import num_palavras, palavras_unicas, num_linhas, buscar_palavra, sub_palavras, imp_linha, frequencia_palavras, nuvemDePalavras
import os

# Informa ao programa o diretório em que ele deve trabalhar
endereço = "C:/Users/ndrca/OneDrive/Documents/GitHub/EP-UFABC/andre-e-giovana"
os.chdir(endereço)

print("Projeto Dirigido de André Inamura Calixto e Giovana Coutinho Nascimento \n")

def main():
    print("Insira um arquivo txt dentro da pasta 'andre-e-giovana', e escreva seu nome no terminal.\nEx: arquivo.txt\n")

    while True:
        arquivo = str(input())
        arquivo_tipo = os.path.splitext(arquivo)[1]
        # Verifica se o arquivo existe no diretório alvo
        if not os.path.exists(arquivo):
            print(f"O arquivo '{arquivo}' não existe\nTente novamente.")
        # Verifica se o arquivo é, de fato, do tipo txt
        elif arquivo_tipo != ".txt":
            print("O arquivo precisa ser do tipo txt\nTente novamente.\n")
        else:
            break

    while True:
        opcoes = int(input("\nDigite o número da opção desejada:\n\n1. Número de palavras\n2. Número de palavras distintas\n3. Número de linhas\n4. Frequência das palavras\n5. Imprimir uma linha específica\n6. Buscar uma palavra e imprimir a linha em que aparece a primeira ocorrência da palavra\n7. Substituir todas as ocorrências de uma palavra por outra\n8. Abrir outro livro\n9. Gerar nuvem de palavras\n10. Encerrar o programa\n"))

        if opcoes == 1:
            print(num_palavras(arquivo))

        elif opcoes == 2:
            print(palavras_unicas(arquivo))

        elif opcoes == 3:
            print(num_linhas(arquivo))
        
        elif opcoes == 4:
            contagem_palavras = frequencia_palavras(arquivo)
            if contagem_palavras:
                print("Frequência das palavras:\n")
                for palavra, quantidade in contagem_palavras.items():
                    if quantidade == 1:
                        print(f"A palavra {palavra} ocorre 1 vez;")
                    else:
                        print(f"A palavra {palavra} ocorre {quantidade} vezes;")
            else:
                print("O documento está vazio.")
        
        elif opcoes == 5:
            indice_linha = int(input("Escreva o número da linha que você deseja imprimir: \n"))
            print(imp_linha(arquivo, indice_linha))
        
        elif opcoes == 6:
            busca = str(input("Escreva a palavra que você quer procurar.\n"))
            maiuscula = busca.upper()
            resultado = buscar_palavra(maiuscula, arquivo)
            if resultado == False:
                print(f"A palavra '{busca}' não foi achada no documento.")
            else:
                print(f"\n{resultado}")
        
        elif opcoes == 7:
            nova = str(input("Escreva a palavra que você deseja adicionar ao documento:\n"))
            antiga = str(input("Escreva a palavra que você deseja substituir no documento:\n"))
            nome_arquivo = str(input("Escreva o nome do novo documento, sem extensão, em que você deseja salvar esse texto:\n"))
            sub_palavras(nova, antiga, nome_arquivo, arquivo)
            print(f"Todas as palavras '{antiga}', foram substituídas por '{nova}' no novo arquivo: {nome_arquivo}.txt")
        
        elif opcoes == 8:
            main()
            break

        elif opcoes == 9:
            # Define todas as opções de plano de fundo e de paleta de cores que o usuário pode escolher para a wordcloud
            opcoes_bg_color = ["white", "black", "lightgray", "lightblue"]
            opcoes_colormap = ["magma", "Spectral", "plasma", "copper", "viridis", "twilight", "gist_rainbow", "Wistia", "spring", "turbo"]
            max_palavras = int(input("Escreva qual o número máximo de palavras que deseja ver na nuvem: \n"))
            # Verifica se o usuário digitou uma opção válida para a cor de plano de fundo
            while True:
                bg_color = str(input("Escolha dentre as seguintes opções de cores para plano de fundo:\n\n- white\n- black\n- lightgray\n- lightblue\n"))
                if not bg_color in opcoes_bg_color:
                    print("Escreva uma opção válida.")
                else:
                    break
            # Verifica se o usuário digitou uma opção válida para a paleta de cores
            while True:
                colormap = str(input("Escolha dentre as seguintes opções de paleta de cor:\n\n- magma\n- Spectral\n- plasma\n- copper\n- viridis\n- twilight\n- gist_rainbow\n- Wistia\n- spring\n- turbo\n"))
                if not colormap in opcoes_colormap:
                    print("Escreva uma opção válida.")
                else:
                    break
            nuvemDePalavras(arquivo, bg_color, colormap, max_palavras)
                
        elif opcoes == 10:
            print("Programa encerrado")
            break

        else:
            print("Insira uma opção válida")
        
main()
