def validarMedia(aluno):
    media=(aluno['nota1']+aluno['nota2']+aluno['nota3'])/3
    if media>=7:
        aluno['situacao']="APROVADO PAI"
    else:
        aluno['situacao']="REPROVADO PAI"
    return aluno
