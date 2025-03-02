# Zadnanie: Zaimplementuj swoją własną wersję jakiejś funkcji która np sortuje coś w liście 

lista = [1, 2, 2, 1, 3, 1]
def sortowanie(lista):
    n = len(lista)
    for x in range(n):
        for y in range(n - 1 - x):
            if lista[y] > lista[y + 1]:
                lista[y], lista[y + 1] = lista[y + 1], lista[y]
                czy_zmieniono = True
        if not czy_zmieniono: #Jeśli nie było zamiany, lista jest już posortowana
            break
    print(lista)

sortowanie(lista) 


#Możemy zoptymalizować funkcję zmniejszając liczbę niepotrzebnych iteracji
#W obecnym kodzie wykonujemy n pełnych iteracji, nawet jeśli lista jest już posortowana
#Możemy dodać flagę cz_zmieniono, aby przerwać pętle, gdy nie było żadnej zmiany w danej iteracji 

#Optymalizacja: jeśli w jednej iteracji nie dokonano żadnej zmiany, oznacza to, że lista jest już posortowana
# i można przerwać pętle 