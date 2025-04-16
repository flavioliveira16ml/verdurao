class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def aplicar_desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        return self.preco - desconto

    def __str__(self):
        return f"Produto: {self.nome}, Preço: R${self.preco:.2f}, Quantidade: {self.quantidade}"

class Verdura(Produto):
    def __init__(self, nome, preco, quantidade, tipo):
        super().__init__(nome, preco, quantidade)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + f", Tipo: {self.tipo}"

class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, produto):
        if produto.nome in self.produtos:
            self.produtos[produto.nome].quantidade += produto.quantidade
        else:
            self.produtos[produto.nome] = produto

    def listagem_produtos(self):
        return [str(produto) for produto in self.produtos.values()]

    def remover_produto(self, nome, quantidade):
        if nome in self.produtos:
            if self.produtos[nome].quantidade >= quantidade:
                self.produtos[nome].quantidade -= quantidade
                if self.produtos[nome].quantidade == 0:
                    del self.produtos[nome]

    def pesquisar_produto(self, nome):
        return self.produtos.get(nome, None)

class Loja:
    def __init__(self):
        self.estoque = Estoque()

    def aplicar_desconto_produto(self, nome, percentual):
        produto = self.estoque.pesquisar_produto(nome)
        if produto:
            return produto.aplicar_desconto(percentual)
        return None

    def simular_pagamento(self, nome, quantidade, metodo_pagamento):
        produto = self.estoque.pesquisar_produto(nome)
        if produto and produto.quantidade >= quantidade:
            total = produto.preco * quantidade
            if metodo_pagamento == "avista":
                total *= 0.9
            self.estoque.remover_produto(nome, quantidade)
            return total
        return 0

def menu():
    loja = Loja()

    while True:
        print("\nMenu:")
        print("1. Adicionar Verdura")
        print("2. Listar Verduras")
        print("3. Aplicar Desconto em Verdura")
        print("4. Simular Pagamento")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Verduras disponíveis para adicionar:")
            verduras = [
                "Abóbora",
                "Quiabo",
                "Pepino",
                "Beterraba",
                "Cebola"
            ]
            for i, verdura in enumerate(verduras, start=1):
                print(f"{i}. {verdura}")

            escolha = int(input("Escolha um número correspondente à verdura: ")) - 1
            nome = verduras[escolha]
            preco = float(input(f"Preço da {nome}: "))
            quantidade = int(input(f"Quantidade da {nome}: "))

            tipo = "Verdura"
            loja.estoque.adicionar_produto(Verdura(nome, preco, quantidade, tipo))
            print(f"{nome} adicionada com sucesso.")

        elif opcao == "2":
            produtos = loja.estoque.listagem_produtos()
            for produto in produtos:
                print(produto)

        elif opcao == "3":
            nome = input("Nome da verdura: ")
            percentual = float(input("Percentual de desconto: "))
            novo_preco = loja.aplicar_desconto_produto(nome, percentual)
            if novo_preco:
                print(f"Novo preço de {nome}: R${novo_preco:.2f}")
            else:
                print("Verdura não encontrada.")

        elif opcao == "4":
            nome = input("Nome da verdura: ")
            quantidade = int(input("Quantidade a ser comprada: "))
            metodo_pagamento = input("Método de pagamento (avista/dinheiro): ")
            total = loja.simular_pagamento(nome, quantidade, metodo_pagamento)
            if total:
                print(f"Total a pagar: R${total:.2f}")
            else:
                print("Verdura não disponível ou quantidade insuficiente.")

        elif opcao == "5":
            print("Saindo do sistema.")
            break

if __name__ == "__main__":
    menu()