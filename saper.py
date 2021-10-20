lista=[]
bomby=[[0, 0], [0, 1], [2, 1], [7, 3]]

def drukuj_plansze(n, m, bomby):
    bomby_umieszczone = 0
    sprawdzone_wiersze = 0
    k = 0
    b = 0

    #tworzenie pustej planszy
    for i in range(n):
        col = []
        for j in range(m):
            col.append(0)
        lista.append(col)
    
    #umieszczanie bomb
    try:
        while bomby_umieszczone < len(bomby):
            for x in bomby:
                lista[x[0]][x[1]] = "*"
                bomby_umieszczone += 1
    except IndexError:
        print("Błędna koordynata. Maksymalna wartość koordynat to", n, "i", m)
    
    #sprawdzanie planszy
    for sprawdzone_wiersze in lista:
        while k < m:
            #liczenie bomb dookola pola
            if lista[b][k] == "*":
                #prawa strona
                if k+1 < m and lista[b][k+1] != "*":
                    lista[b][k+1] +=1
                #lewa strona
                if k-1 >= 0 < m and lista[b][k-1] != "*":
                    lista[b][k-1] +=1
                #dol
                if b+1 < n and lista[b+1][k] != "*":
                    lista[b+1][k] +=1
                #gora
                if b-1 >=0 < n and lista[b-1][k] != "*":
                    lista[b-1][k] +=1
                #gora lewo
                if b-1 >=0 < n and k-1>=0<m and lista[b-1][k-1] !="*":
                    lista[b-1][k-1] +=1
                #gora prawo
                if b-1 >=0<n and k+1 < m and lista[b-1][k+1] != "*":
                    lista[b-1][k+1] +=1
                #dol lewo 
                if b+1 <n and k-1 >=0<m and lista[b+1][k-1] != "*":
                    lista[b+1][k-1] += 1
                #dol prawo
                if b+1 <n and k+1 < m and lista[b+1][k+1] != "*":
                    lista[b+1][k+1] +=1  
            k +=1
        k = 0
        b += 1

    #drukowanie planszy
    for l in lista:
        print(*l, sep="")

#wywolanie funkcji
drukuj_plansze(3, 5, bomby)
