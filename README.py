# Python-0
# Questções de python

# BLOCO 1 - Remove um elemento existente do conjunto
frutas = {"macã", "banana", "laranja"}
frutas.remove("banana")  # Remove "banana"
print(frutas)
print()


# BLOCO 2 - Tenta remover um elemento que não existe
frutas = {"macã", "banana", "laranja"}
frutas.discard("chiclete")  # Não gera erro se o elemento não existir
print(frutas)
print()


# BLOCO 3 - Remove todos os elementos do conjunto
frutas = {"macã", "banana", "laranja"}
frutas.clear()  # Esvazia o conjunto
print(frutas)   # Exibe: set()
print()


# BLOCO 4 - Mostra os elementos presentes nos dois conjuntos
turma_a = {"Carlos", "Mariana", "joão"}
turma_b = {"Mariana", "Pedro", "Ana"}

print(turma_a & turma_b)  # Interseção: elementos compartilhados
print()


# BLOCO 5 - Mostra as diferenças entre os conjuntos
turma_a = {"Carlos", "Mariana", "joão"}
turma_b = {"Mariana", "Pedro", "Ana"}

print(turma_a - turma_b)  # Elementos exclusivos de turma_a
print(turma_b - turma_a)  # Elementos exclusivos de turma_b
print(turma_a ^ turma_b)  # Elementos que estão em apenas um dos conjuntos
print()


# BLOCO 6 - Percorre e exibe os nomes da turma
turma = {"Carlos", "Mariana", "João", "Pedro", "Ali"}

for i in turma:
    print(i, end=", ")

print()
print()


# BLOCO 7 - Compara as matérias dos dois alunos
aluno1 = {"Python", "Java", "PHP"}
aluno2 = {"Python", "JavaScript", "C#"}

print(f"Matérias compartilhadas: {aluno1 & aluno2}.")
print(f"Matérias não compartilhadas: {aluno1 ^ aluno2}.")
print()


# BLOCO 8 - Guarda os resultados da comparação em variáveis
aluno1 = {"Python", "Java", "PHP"}
aluno2 = {"Python", "JavaScript", "C#"}

compartilhadas = aluno1 & aluno2
nao_compartilhadas = aluno1 ^ aluno2

print(f"Matérias compartilhadas: {compartilhadas}.")
print(f"Matérias não compartilhadas: {nao_compartilhadas}.")

# BLOCO 9 - Compara e reúne as matérias dos dois alunos
aluno1 = {"Python", "Java", "PHP"}
aluno2 = {"Python", "JavaScript", "C#"}

todas = aluno1 | aluno2
compartilhadas = aluno1 & aluno2
nao_compartilhadas = aluno1 ^ aluno2

print(f"Todas as matérias: {todas}.")
print(f"Matérias compartilhadas: {compartilhadas}.")
print(f"Matérias não compartilhadas: {nao_compartilhadas}.")
print()

listaproduto = []

while True:
    id = int(input("Digite o código do produto: "))
    nome = str(input("Nome do produto: "))
    qualidade = str(input("Qualidade do produto: "))
    preco = float(input("Preço do produto: "))
    cor = str(input("Cor do produto: "))
    peso = float(input("Peso do produto: "))
    qtd = int(input("Quantidade do produto: "))
    

    
    listaproduto.append({"nome": nome, "qualidade": qualidade, "preco": preco, "cor": cor, "peso": peso, "qtd": qtd})
    
    sn = str(input("Deseja sair (S/N)? ")).lower()
        if sn == "s":
        break
    
print(listaproduto)


while True:
    print("DIGITE A OPÇÃO")
    print("1 - Cadastrar.")
    print("2 - Alterar.")
    print("3 - Excluir.")
    print("4 - Listar.")
    print("5 - Consultar.")
    print("6 - Sair")

    opc = int(input("Opção: "))

    if opc  == 1:
        print()
    elif opc  == 2:
        print()
    elif opc  == 3:
        print()
    elif opc  == 4:
        print()
    elif opc  == 5:
        print()
    elif opc  == 6:
        print()
        break
    else:
        print()
        

listaproduto = []
while True:
    print("DIGITE A OPÇÃO")
    print("1 - Cadastrar Produto.")
    print("2 - Alterar.")
    print("3 - Excluir.")
    print("4 - Listar.")
    print("5 - Consultar.")
    print("6 - Sair")

    opc = int(input("Opção: "))

    if opc  == 1:

        while True:
            id = int(input("Digite o código do produto: "))
            nome = str(input("Nome do produto: "))
            qualidade = str(input("Qualidade do produto: "))
            preco = float(input("Preço do produto: "))
            cor = str(input("Cor do produto: "))
            peso = float(input("Peso do produto: "))
            qtd = int(input("Quantidade do produto: "))
            

            
            listaproduto.append({"nome": nome, "qualidade": qualidade, "preco": preco, "cor": cor, "peso": peso, "qtd": qtd})
            
            sn = str(input("Deseja sair (S/N)? ")).lower()
            if sn == "s":
                break
            
            print()
            
        print(listaproduto)

    elif opc  == 2:
        print()
    elif opc  == 3:
        print()
    elif opc  == 4:
        print()
    elif opc  == 5:
        print()
    elif opc  == 6:
        print()
        break
    else:
        print()
        


