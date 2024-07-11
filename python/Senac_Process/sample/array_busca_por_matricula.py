alunos = [
    {"matricula": 123, "nome": "Ana Silva"},
    {"matricula": 456, "nome": "João Souza"},
    {"matricula": 789, "nome": "Maria Oliveira"},
    # ... outros alunos
]

# Função para buscar aluno por matrícula:
def buscar_aluno(matricula):
    for aluno in alunos:
        if aluno["matricula"] == matricula:
            return aluno["nome"]
    return None

# Solicitando a matrícula do usuário:
matricula_pesquisada = int(input("Digite a matrícula do aluno: "))
nome_encontrado = buscar_aluno(matricula_pesquisada)

if nome_encontrado:
    print(f"Aluno encontrado: {nome_encontrado}")
else:
    print(f"Aluno com matrícula {matricula_pesquisada} não encontrado.")

