from math import sqrt
def pi(end):
    pi = 0.0

    # Summatory
    for i in range(1, end):
        pi += 6/(i**2)

    return sqrt(pi)

i_value = int(input("Escreve o valor para i: "))
print("Resultado: ", pi(i_value))