import logging

logging.basicConfig(
    filename = "logs.txt",
    level= logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def registrar_info(mensagem):
    logging.info(mensagem)

def registrar_erro(mensagem):
    logging.error(mensagem)