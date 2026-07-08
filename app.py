from flask import Flask, render_template, request 

app =Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def home():

    empresa = "luari"
    produto = "filme stretch"
    quantidade = 250

    if request.method == "POST":

        arquivo = request.files.get("pdf")
        
        if arquivo:
            print("arquivo recebido!")

        else:
            print("arquivo não recebido.")
        

    return render_template(
        "index.html",
        empresa = empresa,
        produto = produto,
        quantidade = quantidade)

if __name__ == "__main__":
    app.run(debug=True)