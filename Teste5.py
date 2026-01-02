salario=float(input("Qual o seu salario?"))
if salario>=3500 and salario<=4500:
    print("Programador Júnior")
elif salario>=5500 and salario<=8500:
    print("Programador Pleno")

elif salario>=10000 and salario<=18000:
    print ("Programador Senior")
else:
    print("Gerenciador de Projetos")
