#Q1

Lado = int (input("insira tamanho do lado \n"))
quadra = Lado*Lado 
print(quadra)


#Q3
#File "main.py", line 13
#Lado = float(input("insira tamanho do lado \n"))
#IndentationError: unexpected indent

#Q4
#num = int(input("insira o numero\n"))
#if num % 2 == 0:
#  print(" par")
#else:
#  print("ímpar")

#Q5

#num = int(input("insira o numero\n"))
#num2 = int(input("insira o numero\n"))
#mul = 1

#n3 = 0
#lista = []
#while len(lista) < mul: 
#  n3 += 1
#  if (n3 % num == 0 and n3 % num2 == 0):
 #     lista.append(n3)
#print (lista)
   

#Q6
#num1 = int(input("insira o numero  "))

#if num1 % 3 == 0:
#    print(num1, " divisivel por 3")
#elif num1 % 5 == 0:
#    print(num1, " divisivel por 5")
#elif num1 % 7 == 0:
#    print(num1, " divisivel por 7")
#else:
#    print(num1, "não é divisvel por nenhum")

#Q7
#salario1 = float(input(" salario atual: "))

#if salario1 <= 1000:
#    aumento = salario1 *0.2
#elif salario1 <= 2000:
#    aumento = salario1 *0.18
#elif salario1 <= 4000:
#    aumento = salario1 *0.15
#else:
#    aumento = salario1 *0.1

#aumento2 = salario1 + aumento

#print("O aumento final do salario é de   {:.2f} reais".format(aumento2))

#Q8
#L1 = int(input("lado  1 \n"))
#L2 = int(input("lado  2 \n"))
#L3 = int(input("lado  3 \n"))


#if L1 == L2 and L2 == L3:
#  print("equilatero")
#elif L1 == L2 or L1 == L3 or L2 == L3:
#  print ("isoceles")
#else:
#  print("escaleno")

#Q9

#idade = int(input("insira a idade \n"))

#if idade <= 3: print("Bebê nascimento até 3 anos")

#elif idade<=7: print("Criança 4 até 7 anos")

#elif idade <=12: print("Pré-adolescente 8 até 12 anos")
#elif idade <=20: print("Adolescente 13 até 20 anos")
#elif idade <=40: print("Jovem 21 a 40 anos")
#elif idade <=64: print("Meia-idade 41 até 64 anos")
#else: print("Idoso 65 anos em diante")


#Q10
#idade = int(input("insira a idade \n"))
#peso = float(input("insira o peso \n"))

#if peso <= 3:
#    if idade <= 2:
#        idadeconvertida = idade * 12.5
#    else:
#        idadeconvertida = 25 + (idade - 2) * 5.2
#elif peso <= 23:
#    if idade <= 2:
#        idadeconvertida = idade * 10.5
#    else:
#        idadeconvertida = 21 + (idade - 2) * 5.7
#else:
#    if idade <= 2:
#        idadeconvertida = idade * 9
#    else:
#        idadeconvertida = 18 + (idade - 2) * 7.8

#print(f"A idade do cachorro é de {idadeconvertida} anos humanos")




#1
#num =int(input("insira o numero 1\n"))
#num2 =int(input("insira o numero 2\n"))
#num3 =int(input("insira o numero 3\n"))

#if num > num2 and num > num3
#print("numero 1")
#elif num2 > num and num2 > num3
#print("numero 2")
# else:
#print("numero 3")

#2
#turno = (input("insira seu turno M-matutino ou V-Vespertino ou N- Noturno\n"))

#if turno =="M":
#       print("Bom Dia")
#elif turno =="V":
#       print("Boa Tarde")
#elif turno =="N":
#      print("Boa Noite")
#else:
#      print("Valor Inválido")



#3
#salario1 = float (input("salario atual\n"))

#salario2= salario1 *20 /100
#salario3=salario1 *15 /100
#salario4=salario1 *10 /100
#salario5=salario1 *10 /100

#if salario1 <=  280.0: print(f"20% ,até R$ 280,00{salario2}")


#elif salario1<=700.0: print(f"15% ,entre R$ 280,00 e R$ 700,00{salario3}")

#elif salario1 <=1500.0: print(f"10% ,entre R$ 700,00 e R$ 1500,00 {salario4}")
  
#elif salario1 >=1500.0: print(f"5% ,de R$ 1500,00 em diante{salario5}")

#else:
                                      
#   print("invalido")


 #4

nota1 = float (input("nota 1\n"))
nota2= float (input("nota 1\n"))

media = nota1+nota2/2


if media >=  10.0:
  print("APROVADO")


elif media>=7.5: 
  print("APROVADO")

elif media >=6.0: 
  print("APROVADO")

elif media <=6.0: 
  print("reprovado")


else:
                                      
   print("reprovado")





#5
#lado1 = int(input("lado  1 \n"))
#lado2 = int(input("lado  2 \n"))
#lado3 = int(input("lado  3 \n"))

#if lado1 == lado2 and lado2 == lado3:
#  print("o triangulo é equilatero")
#elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
#  print ("o triangulo é isoceles")
#else:
#  print("o triangulo é escaleno")





#6
#num = int(input("insira o numero\n"))
#num2 = int(input("insira o numero\n"))
#num3= int(input("insira o numero\n"))

#lista = [num ,num2,num3]

#print (lista)