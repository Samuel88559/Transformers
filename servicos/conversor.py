#importações vindas de outros arquivos
from servicos.validar import validar_arquivo
from servicos.extrator_pdf import processar_pdf
from servicos.planilha import preencher_planilha

def converter_pdf(arquivo):
 
# Comandos para executar as análises dos dados do PDF e o preenchimento do Excel
            validar_arquivo(arquivo)
            dados = processar_pdf(arquivo)
            arquivo_excel = preencher_planilha(dados)

            return arquivo_excel