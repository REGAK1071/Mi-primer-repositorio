
#Algoritmo de Euclides:  https://es.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm

def mcd(a, b):

    a = abs(a)
    b = abs(b)
    
    lista_N = []
    lista_N.append(a)
    lista_N.append(b)

    a = max(lista_N)
    b = min(lista_N)

    if (a == 0) and (b == 0):
        return 'Indefinido (No se puede dividir por cero)'

    while b != 0:
        residuo = a % b
        a = b
        b = residuo

    return a

a = int(input('Ingrese algun entero: '))
b = int(input('Ingrese algun entero: '))

print(mcd(a, b))