## Questão 1

indice = 13
soma = 0
k = 0

while k < indice:
    k += 1
    soma += k

## print(soma)
## o valor final da soma será 91 ao final do processamento


## Questão 2
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


def verifica_numero_fibonacci(num):
    numeros_fibonacci = set()
    i = 0
    while True:
        fib_num = fibonacci(i)
        if fib_num > num:
            break
        numeros_fibonacci.add(fib_num)
        i += 1
    if num in numeros_fibonacci:
        return f"{num} pertence à sequência de Fibonacci."
    else:
        return f"{num} não pertence à sequência de Fibonacci."


## verifica_numero_fibonacci(numero)

## Questão 3
## a) 1, 3, 5, 7, 9
## b) 2, 4, 8, 16, 32, 64, 128
## c) 0, 1, 4, 9, 16, 25, 36, 49
## d) 4, 16, 36, 64, 100
## e) 1, 1, 2, 3, 5, 8, 13
## f) 2,10, 12, 16, 17, 18, 19, 20

## Questão 4
## na primeira ida, na sala dos interruptores, eu deixaria um interruptor ligado continuamente.
## ligaria o segundo interruptor, esperaria um tempo e depois desligaria.
## na outra sala, eu iria observar as lampadas. a lampada desligada e fria seria o interruptor
## que eu não toquei. a lâmpada desligada e um pouco quente seria o segundo interruptor.
## a lampada ligada seria a do primeiro interruptor.

## Questão 5

string = "Pedro Lucas"
lista = list(string)
lista_reversa = lista[::-1]

string_reversa = ""
for item in lista_reversa:
    string_reversa += item

## print(string_reversa)
