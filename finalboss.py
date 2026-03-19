alunosfpb = {}

alunosfpb["Aluno01"] = {
    "nome": "Anderson",
    "idade": 22,
    "notas": [3.5, 4, 7.5]
}

alunosfpb["Aluno02"] = {
    "nome": "Marceline",
    "idade": 20,
    "notas": [7, 8, 3]
}

alunosfpb["Aluno03"] = {
    "nome": "Felipe",
    "idade": 19,
    "notas": [8.5, 4.5, 8]
}

print("Relatório dos alunos cadastrados\n")
for aluno in alunosfpb:
    nome = alunosfpb[aluno]["nome"]
    idade = alunosfpb[aluno]["idade"]
    notas = alunosfpb[aluno]["notas"]
    media = sum(notas) / len(notas)
    print("Aluno: " + nome + ", idade:" + str(idade) + ", média: " +str(media) + "\n")
