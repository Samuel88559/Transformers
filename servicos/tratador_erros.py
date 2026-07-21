from servicos.exceptions import (
    DataNaoEncontradoError,
    NumeroPedidoNaoEncontrado,
    ClienteNaoEncontradoError,
    PadraoNaoEncontradoerror,
    FilmeNaoEncontradoerror
)

MENSAGENS = {
    DataNaoEncontradoError:
    "O campo data de entrega não foi encontrado",

    NumeroPedidoNaoEncontrado:
    "O campo número do pedido não foi encontrado",

    ClienteNaoEncontradoError:
    "O campo cliente não foi encontrado",

    PadraoNaoEncontradoerror:
    "O campo padrão não foi encontrado",

    FilmeNaoEncontradoerror:    
    "O campo filme não foi encontrado"
}

def tratar_erro(erro):

# .get pergunta se tem uma chave em MENSAGENS que se relacione com esse erro
    return MENSAGENS.get(

# Se não tiver chave para esse erro, coloque essa mensagem
        type(erro),
        "⚠ Ocorreu um erro inesperado"
    )

# Sequencia lógica de como segue um erro

#extrator_pdf│
#       ▼
# raise ClienteNaoEncontradoError
#       │
#       ▼
# conversor
#       │
#       ▼
# logger
#       │
#       ▼
# tratador_erros
#       │
#       ▼
# app.py
#       │
#       ▼
# HTML
#       │
#       ▼
# Usuário