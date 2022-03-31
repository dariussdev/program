"""
1. Se citește de la tastatura o valoare numerică NR.
2. Ulterior, se fac NR citiri de la tastatură de șiruri de caractere, pe care le
 stocăm într-o listă.
3. După ce am terminat citirea tuturor datelor, vrem să parcurgem lista de
 elemente obținută și să adaug fiecare element într-o altă listă - DAR - fiecare
  element va trebui să fie scris cu litere mari.
4. Afișăm elementele celor două liste."""


"""
REZULTAT
Lista inițială: [mere, pere, ANANAS]
Lista prelucrată: [MERE, PERE, ANANAS]
"""

lista_initiala = []
lista_prelucrata = []
NR = input("Introduceti valoarea lui NR: ")
NR = int(NR)
while NR > 0:
    val = input("Introduceti cuvantul: ")
    val = str(val)
    lista_initiala.append(val)
    NR -= 1
print("Lista initiala: ", lista_initiala)


for i in range(len(lista_initiala)):
    lista_prelucrata.append(lista_initiala[i].upper())
print("Lista prelucrata: ", lista_prelucrata)
