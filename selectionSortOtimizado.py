import time



def selection_sort_otimizado(lista):
    n = len(lista)
    iteracoes = 0  # contador de iterações
    print("Lista inicial:", lista)
    
    inicio = time.time()
    
    for i in range(n - 1):
        min_index = i
        trocou = False  # flag para detectar se houve troca 
        for j in range(i + 1, n):
            iteracoes += 1
            if lista[j] < lista[min_index]:
                min_index = j
                trocou = True  # só marca troca se realmente encontramos um menor
        if min_index != i:
            print(f"Trocando {lista[i]} com {lista[min_index]}")
            lista[i], lista[min_index] = lista[min_index], lista[i] 
        print(f"Passada {i + 1}: {lista}")
        if not trocou:
            print("Lista já ordenada. Encerrando...")
            break
    
    fim = time.time()
    print("Lista ordenada:", lista)
    print("Total de iterações:", iteracoes)
    print(f"Tempo de execução: {fim - inicio:.6f} segundos")