from selectionSort import selection_sort_simples
from selectionSortOtimizado import selection_sort_otimizado

if __name__ == "__main__":
   
    print("Selection Sort Simples\n")
    vetor = [25, 17, 31, 13, 2, 29, 8, 19, 7, 11, 6]
    selection_sort_simples(vetor)
    print("\n")
    print("Selection Sort Otimizado\n")
    vetor = [25, 17, 31, 13, 2, 29, 8, 19, 7, 11, 6]
    selection_sort_otimizado(vetor)
    
    
    print("\n\n")
    print("Selection Sort Simples\n")
    teste2 = [1,2,3,4,5]
    selection_sort_simples(teste2)
    print("\n")
    print("Selection Sort Otimizado\n")
    teste2 = [1,2,3,4,5]
    selection_sort_otimizado(teste2)

    


