class Usuario:
    def __init__(self, nome, telefone, endereco, email):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.email = email

nome = input("Digite seu nome completo: ")
telefone = input("Digite seu telefone para contato: ")
endereco = input("Digite seu endereço: ")
email = input("Digite seu email: ")

pessoa1 = Usuario(nome, telefone, endereco, email)
print("----- DADOS DO USUARIO -----")
print(pessoa1.nome)
print(pessoa1.telefone)
print(pessoa1.endereco)
print(pessoa1.email)

info = [pessoa1]
def buscardados(n):

    if n == "nome":
      for i in range(len(info)):
       return info[i].nome
    if n == "telefone":
     for i in range(len(info)):
      return info[i].telefone
    if n == "endereco":
      for i in range(len(info)):
        return info[i].endereco
    if n == "email":
        for i in range(len(info)):
            return info[i].email

n =input("# Busque um dado: ")
print(buscardados(n))

print("-----------")
def excluirdados(n):
    if n == "nome":
        for i in range(len(info)):
            info[i].nome = "Nome Indisponível"

    if n == "telefone":
        for i in range(len(info)):
            info[i].telefone = "Telefone Indisponível"

    if n == "endereco":
        for i in range(len(info)):
            info[i].endereco = "Endereço Indisponível"

    if n == "email":
        for i in range(len(info)):
            info[i].email = "Email Indisponível"

n = input("# Exclua um dado: ")
print("---- DADOS ATUALIZADOS ----")
excluirdados(n)

for i in range(len(info)):
    print(info[i].nome)
    print(info[i].telefone)
    print(info[i].endereco)
    print(info[i].email)