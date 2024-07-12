# Triangulação. Complexidade: O(N^2)

def triangulate():  
    
    # Adjacência no polígono
    
    global prev, prox
    prev, prox = [], []
    for i in range(0, N):
        prev.append((i-1)%N)
        prox.append((i+1)%N)
    
    # Inicialmente, quem é orelha?
    
    ear = []
    
    for j in range(0, N):
        ear.append(eartest(j))
    
    triangulation = []
    remaining = N
    
    # Loop principal
    
    while remaining >= 3:
    
        # Encontrar uma orelha
        i = -1
        for j in range(0, N):
            if ear[j]:
                i = j
                break
        
        # Adicionar o triangulo encontrado
        triangulation.append((prev[i], i, prox[i]))
        ear[i] = False
        
        # Remover i do polígono
        prox[prev[i]] = prox[i]
        prev[prox[i]] = prev[i]
        remaining -= 1
        
        # Atualizar "status de orelha" dos vizinhos
        ear[prev[i]] = eartest(prev[i])
        ear[prox[i]] = eartest(prox[i])
        
    return triangulation