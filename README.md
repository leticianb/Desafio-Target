# Desafio-Target
1 - 
Observe o trecho de código abaixo:

int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);



Ao final do processamento, qual será o valor da variável SOMA?
**Resposta: 91**

2-**Arquivo do código no repositório**
def fibonacci(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def verifica(numero, sequencia):
    if numero in sequencia:
        print(f"O número {numero} pertence à sequência Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência Fibonacci.")

numero = int(input("Digite um número: "))
sequencia = fibonacci(numero)

print(verifica(numero, sequencia))

3-
a) 1, 3, 5, 7, **9**

b) 2, 4, 8, 16, 32, 64, **128**

c) 0, 1, 4, 9, 16, 25, 36, **49**

d) 4, 16, 36, 64, **100**

e) 1, 1, 2, 3, 5, 8, **13** 

f) 2,10, 12, 16, 17, 18, 19, **20**

4-
Primeiro, ligo o primeiro interruptor por alguns minutos.
Depois, desligo o primeiro interruptor e ligo o segundo interruptor.
Após esse processo, vou para a sala das lâmpadas.
A lâmpada que estiver ligada estará conectada ao segundo interruptor.
Ao tocar as lâmpadas, aquela que estiver apagada e quente estará conectada ao primeiro interruptor.
A lâmpada que estiver apagada e fria estará conectada ao terceiro interruptor

5-**Arquivo do código no repositório**
def inverte(palavra):
    invertida = palavra[::-1]
    return invertida

palavra = input('Digite uma palavra: ')
invertida = inverte(palavra)
print(invertida).
