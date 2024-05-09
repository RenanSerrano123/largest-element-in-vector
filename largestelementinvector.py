def ler_vetor(n):
    vetor = []
    for i in range(n):
        elemento = int(input())
        vetor.append(elemento)
    return vetor
def encontrar_maior_elemento(vetor):
    if not vetor:
        return None
    maior = vetor[0]
    for elemento in vetor:
        if elemento > maior:
            maior = elemento
    return maior
def main():
    n = int(input())
    if n <= 0:
        print("Erro: Insira um valor inteiro positivo.")
        return
    vetor = ler_vetor(n)
    maior_elemento = encontrar_maior_elemento(vetor)
    print(f"{maior_elemento}")
main()