salario=float(input("Qual o seu salario?"))
if salario>=3500 and salario<=4500:
    print("Programador Júnior")
elif salario>=5500 and salario<=8500:
    print("Programador Pleno")

elif salario>=8501 and salario<=18000:
    print ("Programador Senior")

elif salario>=1500 and salario<=3499:
    print ("Estagiário de Programador")

else:
    print("Gerenciador de Projetos")
