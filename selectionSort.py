import time

# Selection Sort simples
def selection_sort_simples(lista):
    n = len(lista)
    iteracoes = 0  # contador de iterações
    print("Lista inicial:\n", lista)
    
    inicio = time.time()  # marca o início do tempo
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            iteracoes += 1
            if lista[j] < lista[min_index]:
                min_index = j
        
        if min_index != i:
            print(f"Trocando {lista[i]} com {lista[min_index]}")
            lista[i], lista[min_index] = lista[min_index], lista[i]
        
        print(f"Passada {i + 1}: {lista}")
    
    fim = time.time()  # marca o fim do tempo
    print("Lista ordenada:", lista)
    print("Total de iterações:", iteracoes)
    print(f"Tempo de execução: {fim - inicio:.6f} segundos")
