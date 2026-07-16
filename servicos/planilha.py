from openpyxl import load_workbook
from datetime import datetime

CELULAS = {
    "data": "B3",
    "numero_pedido": "B4",
    "cliente": "B6",
    "padrao": "B7",
    "filme": "B8",
    "peso_tubete": "B10"
}

# aplicação do Excel para abrir a planilha
def preencher_planilha(dados):

# Carrega o arquivo Excel anexado no programa dentro do sistema
    planilha = load_workbook("modelos/FR.PRO.014 - RASTREABILIDADE DE PALLET (1).xlsx")

#Permite acessar a primeira página do arquivo Excel (Eu acho)
    aba = planilha.active

#Comando de repetição para que não precise toda vez acrescentar uma linha nova na função preencher_planilha toda vez que uma nova variável for acrescentada como essa, por exemplo: aba[CELULAS["cliente"]] = dados["cliente"] ,(que é a mesma coisa que) == aba[CELULAS["B6"]] = dados["FBR EMBALAGENS LTDA"]
    for chave in dados:
        aba[CELULAS[chave]] = dados[chave]

# Comando para nomear a data e hora no arquivo
    nome = datetime.now().strftime("%Y%m%d_%H%M%S")

    arquivo = f"resultado_{nome}.xlsx"
    planilha.save(arquivo)

    return arquivo