import logging
import os

print(os.getcwd())

print("logger carregando")

logging.basicConfig(
    filename = "logs.txt",
    level= logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def registrar_info(mensagem):
    print(f"INFO: {mensagem}")
    logging.info(mensagem)

def registrar_erro(mensagem):
    print(f"ERRO: {mensagem}")
    logging.error(mensagem)