
N1 = float(input())
N2 = float(input())
N3 = float(input())
N4 = float(input())


nota = float(input())

MEDIA = ((N1*2)+(N2*3)+(N3*4)+(N4*1))/10

print('Media: %.1f' %MEDIA)

if(MEDIA >= 7.0):
    print("Aluno aprovado.")

if(MEDIA < 5.0):
    print("Aluno reprovado.")

if(MEDIA >= 5.0 and MEDIA <= 6.9):
    print("Aluno em exame.")
    print("Nota do exame: %.1f" %nota)
    MEDIA = (MEDIA + nota)/2
    
    if(MEDIA >= 5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print('Media final: %.1f' %MEDIA)