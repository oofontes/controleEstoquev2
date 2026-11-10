"""
Sistema de Controle de Estoque
Versão 2 - cadastro, listagem, consulta e movimentação de estoque.
"""

produtos = []


# ---------------------------------------------------------------
# Funções de leitura com validação
# ---------------------------------------------------------------
def ler_texto(mensagem):
    """Lê um texto que não pode ficar vazio."""
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("Erro: este campo não pode ficar vazio.")


def ler_inteiro(mensagem, minimo=0):
    """Lê um número inteiro maior ou igual ao mínimo."""
    while True:
        try:
            valor = int(input(mensagem))
        except ValueError:
            print("Erro: digite um número inteiro.")
            continue
        if valor < minimo:
            print(f"Erro: o valor deve ser maior ou igual a {minimo}.")
            continue
        return valor


def ler_decimal(mensagem, minimo=0.0):
    """Lê um número decimal (aceita vírgula ou ponto)."""
    while True:
        try:
            valor = float(input(mensagem).replace(",", "."))
        except ValueError:
            print("Erro: digite um número válido. Ex.: 12,50")
            continue
        if valor < minimo:
            print(f"Erro: o valor deve ser maior ou igual a {minimo:.2f}.")
            continue
        return valor


# ---------------------------------------------------------------
# Regras do sistema
# ---------------------------------------------------------------
def buscar_por_codigo(codigo):
    """Retorna o produto com o código informado ou None."""
    for produto in produtos:
        if produto["codigo"] == codigo:
            return produto
    return None


def consultar_produto():
    """Busca produtos pelo código exato ou por parte do nome."""
    print("\n--- Consulta de produto ---")
    termo = ler_texto("Digite o código ou parte do nome: ")
    encontrados = [
        p for p in produtos
        if p["codigo"] == termo.upper() or termo.lower() in p["nome"].lower()
    ]
    if not encontrados:
        print("Nenhum produto encontrado.")
        return
    for p in encontrados:
        print(f"[{p['codigo']}] {p['nome']} - {p['quantidade']} un. - R$ {p['preco']:.2f}")


def cadastrar_produto():
    print("\n--- Cadastro de produto ---")
    codigo = ler_texto("Código: ").upper()
    if not codigo.isalnum() or len(codigo) > 10:
        print("Erro: o código deve ter apenas letras/números e no máximo 10 caracteres.")
        return
    if buscar_por_codigo(codigo):
        print("Erro: já existe um produto com esse código.")
        return
    nome = ler_texto("Nome: ")[:25]
    quantidade = ler_inteiro("Quantidade inicial: ", 0)
    preco = ler_decimal("Preço unitário (R$): ", 0.01)

    produtos.append({
        "codigo": codigo,
        "nome": nome,
        "quantidade": quantidade,
        "preco": preco,
    })
    print(f"Produto '{nome}' cadastrado com sucesso!")


def listar_produtos():
    print("\n--- Produtos em estoque ---")
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    print(f"{'CÓDIGO':<10}{'NOME':<25}{'QTD':>6}{'PREÇO (R$)':>14}")
    for p in sorted(produtos, key=lambda item: item["nome"].lower()):
        print(f"{p['codigo']:<10}{p['nome']:<25}{p['quantidade']:>6}{p['preco']:>14.2f}")


def registrar_entrada():
    """Soma uma quantidade ao estoque de um produto existente."""
    print("\n--- Entrada de estoque ---")
    produto = buscar_por_codigo(ler_texto("Código do produto: ").upper())
    if produto is None:
        print("Erro: produto não encontrado.")
        return
    quantidade = ler_inteiro("Quantidade recebida: ", 1)
    produto["quantidade"] += quantidade
    print(f"Entrada registrada. Novo estoque de '{produto['nome']}': {produto['quantidade']}")


def registrar_saida():
    """Retira uma quantidade do estoque, sem deixar ficar negativo."""
    print("\n--- Saída de estoque ---")
    produto = buscar_por_codigo(ler_texto("Código do produto: ").upper())
    if produto is None:
        print("Erro: produto não encontrado.")
        return
    quantidade = ler_inteiro("Quantidade retirada: ", 1)
    if quantidade > produto["quantidade"]:
        print(f"Erro: estoque insuficiente (disponível: {produto['quantidade']}).")
        return
    produto["quantidade"] -= quantidade
    print(f"Saída registrada. Novo estoque de '{produto['nome']}': {produto['quantidade']}")


# ---------------------------------------------------------------
# Menu principal
# ---------------------------------------------------------------
def mostrar_menu():
    print("\n===== CONTROLE DE ESTOQUE =====")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Consultar produto")
    print("4 - Registrar entrada")
    print("5 - Registrar saída")
    print("0 - Sair")


def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            listar_produtos()
        elif opcao == "3":
            consultar_produto()
        elif opcao == "4":
            registrar_entrada()
        elif opcao == "5":
            registrar_saida()
        elif opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
