from flask import Flask, render_template, request, send_file
from openpyxl import load_workbook
from datetime import datetime

#importações vindas de outros arquivos
from extrator_pdf import processar_pdf

CELULA_DATA = "B3"
CELULA_NUMERO_PEDIDO = "B4"
CELULA_CLIENTE = "B6"
CELULA_PADRAO = "B7"
CELULA_FILME = "B8"
CELULA_PESO_TUBETE = "B10"

app =Flask(__name__)

# aplicação do Excel para abrir a planilha
def preencher_planilha(dados):

    planilha = load_workbook("modelos/FR.PRO.014 - RASTREABILIDADE DE PALLET (1).xlsx")

    aba = planilha.active

    aba[CELULA_DATA] = dados["data"]
    aba[CELULA_NUMERO_PEDIDO] = dados["numero-pedido"]
    aba[CELULA_CLIENTE] = cl
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

# Linha responsável por determinar que somente arquivos PDF serão importados
        arquivo = request.files.get("pdf")

        if not arquivo:
            print("Nenhum arquivo recebido")
        
        elif not arquivo.filename.lower().endswith(".pdf"):
            print("Arquivo inválido")
        else:
            print("PDF recebido!")
#abre o arquivo PDF na variável pdf
            

                #Comando Excel

            dados = processar_pdf(arquivo)
            arquivo_excel = preencher_planilha( dados)
                
            return send_file(arquivo_excel)
                

#Enquanto nada for enviado ainda será um GET, logo, enquanto isso, afim de evitar erro, o programa pula para as linha anteriores para que a página possa ser aberta, carregando a página através do arquivo HTML
    return render_template(
        "index.html")

if __name__ == "__main__":
    app.run(debug=True)