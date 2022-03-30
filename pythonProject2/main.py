"""
velocidade_internet = 10
print(velocidade_internet)

final_trabalho = False
if final_trabalho == True:
    print('Bah! vamos la guri!')
else:
    print('nao vai rolar, estou cheio de coisas pra fazer!')
******
numero_de_atrasos = 0
if numero_de_atrasos >=3:
    print('voce esta suspenso:')
elif numero_de_atrasos == 1:
    print('pode entrar, caso falte mais 2 vezes sera suspenso!')
elif numero_de_atrasos == 2:
    print('pode entarr mas se faltar mais uma vez sera suspenso!')
else:
    print('pode entrar !')
****
condicionais if, elif, e else
primeiro_valor = input('Digite o primeiro valor')
segundo_valor = input('Digite o segundo valor')
if int(primeiro_valor) > int(segundo_valor):
print('o primeiro valor e maior:')
else:
print('o segundo valor e maior:')
****

lacos de repeticao
for palavra in range(1,4):
print('carregando')
***

for item in range(1,20,2):
print(item)


nomes = ['Maicon', 'Douglas', 'Soledade']
for nome in nomes:
print(nome

****

valor_maximo = int(input('digite o valor maximo'))
valor_inicial = 1
for numero in range(valor_inicial, valor_maximo + 1):
print(numero)

***

listas colecao

precos = [20,50,200]
#          0  1  2
print(precos[0])
print(precos.index(200)) aqui vai mostrar qual seria o numero da sequencia a baixo do 200.
# listas
diversidades = [15,'Maicon',True]
print(diversidades[0])
print(diversidades[1])
print(diversidades[2])
***
lacos entre variaveis
for preco in precos:
print(preco)

*****
idades = [15,46,10,100,25]
total =0
for  idade in idades:
total = total + idade
print(total)
****


numero = int(input('digite um  numero'))
if numero > 0:
fatorial = 1
for item in range(1,numero + 1):
fatorial = fatorial + item
print(fatorial)

****
import random

valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
chute = int(input('chute um valor de 1 a 10:')
if chute > valor_aleatorio:
print('chuve foi maior que o gerado')
elif chute < valor_aleatorio:
print('chute foi menor que o gerado')
elif chute == valor_aleatorio:
acertou = True
print('voce acertou')
*****

velocidade = int(input('Digite a velocidade'))
velocidade_maxima = 80
if velocidade <= velocidade)maxima:
print('nao levou multa')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
print('levou uma multa de leve')
elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
print('levou uma baita multa tche')
elif velocidade > velocidade_maxima + 20:
print('levou uma multa muito grave')

"""
