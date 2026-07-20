#importações vindas de outros arquivos
from servicos.validar import validar_arquivo
from servicos.extrator_pdf import processar_pdf
from servicos.planilha import preencher_planilha
from servicos.logger import registrar_info, registrar_erro

def converter_pdf(arquivo):
            try:
 
# Comandos para executar as análises dos dados do PDF e o preenchimento do Excel
                validar_arquivo(arquivo)
                dados = processar_pdf(arquivo)
                arquivo_excel = preencher_planilha(dados)

                print("vou registrar o log")

                print("1 - validar")

                validar_arquivo(arquivo)

                print("2 - extrair")

                dados = processar_pdf(arquivo)

                print("3 - preencher")

                arquivo_excel = preencher_planilha(dados)

                print("4 - registrar")

                registrar_info(
                    f"Conversão do {arquivo.filename} realizada com sucesso!"
                )

                print("5 - retornar")

                return arquivo_excel
            
            except Exception as erro:

                print("Erro encontrado:", erro)

                registrar_erro(str(erro))
                raise