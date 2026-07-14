from flask import Flask, render_template, request, send_file
import pdfplumber
from openpyxl import load_workbook
from openpyxl.styles import Font
from datetime import datetime

CELULA_DATA = "B3"
CELULA_NUMERO_PEDIDO = "B4"
CELULA_CLIENTE = "B6"
CELULA_PADRAO = "B7"
CELULA_FILME = "B8"
CELULA_PESO_TUBETE = "B10"

app =Flask(__name__)

def pegar_cliente(linhas):
                
    for linha in linhas:
        if "Cliente" in linha:

            # Comando para saber as posições das variáveis

            posicao = linha.find("Cliente")
            inicio = posicao + len("Cliente ")

            cliente = linha[inicio:]

            return cliente
        
def pegar_data(linhas):
                
    for linha in linhas:
        if "data de entrega" in linha:
            
            # Outro exemplo de como fazer a mesma coisa

            inicio = linha.find("data de entrega")
            inicio += inicio + len("data de entrega ")

            data = linha[inicio:]

            return data
        
def pegar_numero_pedido(linhas):
                
    for linha in linhas:
        if "Pedido de Venda" in linha:

            posicao = linha.find("Pedido de Venda")
            inicio = posicao + len("Pedido de Venda ")

            numero_pedido = linha[inicio:]

            return numero_pedido
        
def pegar_filme(linhas):
                
    for linha in linhas:
        if "FILME" in linha:

            posicao = linha.find("FILME")
            inicio = posicao + len("FILME ")

            filme = linha[inicio:inicio+3]

            return filme
        
def pegar_peso_tubete(linhas):
                
    for linha in linhas:
        if "FILME +" in linha:

            posicao = linha.find("FILME +")
            inicio = posicao + len("FILME + ")

            peso_tubete = linha[inicio:inicio+2]

            return peso_tubete
    return ""
        
def pegar_padrao(linhas):
    padrao = ""
         
    for linha in linhas:
        if "- (" in linha:
            palavras = linha.split(" ")
        
            for palavra in palavras:

                palavra1 = palavra.replace("(", "")
                palavra2 = palavra.replace(")", "")

                if palavra.isdigit():

                    padrao = palavra1 + " + " + palavra2

    return padrao

# aplicação do Excel para abrir a planilha
def preencher_planilha(data, numero_pedido, cliente, padrao, filme, peso_tubete):

    planilha = load_workbook("modelos/FR.PRO.014 - RASTREABILIDADE DE PALLET (1).xlsx")

    aba = planilha.active

    aba[CELULA_DATA] = data
    aba[CELULA_NUMERO_PEDIDO] = numero_pedido
    aba[CELULA_CLIENTE] = cliente
    aba[CELULA_PADRAO] = padrao
    aba[CELULA_FILME] = filme
    aba[CELULA_PESO_TUBETE] = peso_tubete

    # Comando para nomear a data e hora no arquivo
    nome = datetime.now().strftime("%Y%m%d_%H%M%S")

    arquivo = f"resultado_{nome}.xlsx"
    planilha.save(arquivo)

    return arquivo

@app.route("/", methods = ["GET", "POST"])
def home():

    if request.method == "POST":

        arquivo = request.files.get("pdf")

        if not arquivo:
            print("Nenhum arquivo recebido")
        
        elif not arquivo.filename.lower().endswith(".pdf"):
            print("Arquivo inválido")
        else:
            print("PDF recebido!")
#abre o arquivo PDF na variável pdf
            with pdfplumber.open(arquivo) as pdf:
                
#Testes para verificar se o conteúdo está sendo impresso da forma correta

#Abre a página que for solicitada
                pagina = pdf.pages[0]
#Imprime o conteúdo que estiver nessa página                
                texto = pagina.extract_text()

#Separação de conteúdo por linha
                linhas = texto.split("\n")

# Dados do PDF
                data = pegar_data(linhas)

                numero_pedido = pegar_numero_pedido(linhas)

                cliente = pegar_cliente(linhas)
                
                padrao = pegar_padrao(linhas)

                filme = pegar_filme(linhas) + "A"

                peso_tubete = pegar_peso_tubete(linhas) + "KG"
                print(peso_tubete)

                #Comando Excel

                arquivo_excel = preencher_planilha( data,
                                    numero_pedido,
                                    cliente,
                                    padrao,
                                    filme,
                                    peso_tubete)
                
                return send_file(arquivo_excel)
                

#Enquanto nada for enviado ainda será um GET, logo, enquanto isso, afim de evitar erro, o programa pula para as linha anteriores para que a página possa ser aberta, carregando a página através do arquivo HTML
    return render_template(
        "index.html")

if __name__ == "__main__":
    app.run(debug=True)