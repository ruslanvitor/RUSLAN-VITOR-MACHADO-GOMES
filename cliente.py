nome = input("Digite o nome do cliente: ")
telefone = input("Digite o telefone do cliente: ")

cliente = [nome, telefone]

print("Dados digitados:", cliente)
# cliente.py

def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ").strip()
    
    # Validação do nome
    if not nome:
        print("Erro: O nome não pode estar vazio.")
        return

    telefone = input("Digite o telefone do cliente: ").strip()
    
    # Validação do telefone (apenas números)
    if not telefone.isdigit():
        print("Erro: O telefone deve conter apenas números.")
        return

    # Armazenamento em lista
    cliente = [nome, telefone]

    # Confirmação e exibição dos dados
    print("\n✓ Cadastro confirmado com sucesso!")
    print(f"Nome: {cliente[0]}")
    print(f"Telefone: {cliente[1]}")

if __name__ == "__main__":
    cadastrar_cliente()