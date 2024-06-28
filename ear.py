
# Leitura da entrada

L = list(input().split())
N = int(L[0])
L = L[1:]

points = []
for i in range(0, N):
    s, t = L[2*i], L[2*i+1]
    a, b = map(int, s.split('/'))
    c, d = map(int, t.split('/'))
    points.append((a/b, c/d))


# Primitiva de sentido horário/anti-horário

eps = 1e-6

def ccw(i, j, k):
    (ix, iy) = points[i]
    (jx, jy) = points[j]
    (kx, ky) = points[k]
    
    (vx, vy) = (jx - ix, jy - iy)
    (wx, wy) = (kx - jx, ky - jy)
    
    return vx*wy - vy*wx > eps


# Primitiva de estar dentro de um triângulo

def inside(i, j, k, l):
    return ccw(i, j, l) and ccw(j, k, l) and ccw(k, i, l)


# Sou ponta de orelha? Complexidade O(N)

def eartest(j):
    i, k = prev[j], prox[j]
    
    if not ccw(i, j, k):
        print(j, "is not an ear because", i, j, k, "are not counterclockwise")
        return False
    
    for l in range(0, N):
        if inside(i, j, k, l):
            print(j, "is not an ear because", l, "is in triangle", i, j, k)
            return False
    
    return True


# Adjacência no polígono

prev = []
prox = []

for i in range(0, N):
    prev.append((i-1)%N)
    prox.append((i+1)%N)
  
    
# Inicialmente, quem é orelha? Complexidade: O(N^2)

ear = []

for j in range(0, N):
    ear.append(eartest(j))

print("ear:", ear)


# Triangulação. Complexidade: O(N^2)

triangulation = []
remaining = N

while remaining >= 3:

    # Encontrar uma orelha
    i = 0
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
    


print("triangulation:", triangulation)





