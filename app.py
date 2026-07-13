from flask import Flask, render_template, request 
import pdfplumber

app =Flask(__name__)

def pegar_cliente(linhas):
                
    for linha in linhas:
        if "Cliente" in linha:

            #Comando para saber as posições das variáveis

            posicao = linha.find("Cliente")
            inicio = posicao + 8

            cliente = linha[inicio:]

            return cliente

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

                cliente = pegar_cliente(linhas)
                print(cliente)

                        
                        
                            

#Enquanto nada for enviado ainda será um GET, logo, enquanto isso, afim de evitar erro, o programa pula para essa linha para que a página possa ser aberta 
    return render_template(
        "index.html")

if __name__ == "__main__":
    app.run(debug=True)