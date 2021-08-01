import turtle

A = range(1, 6)
print(*A)
for x in A: # A интерируемый объект
    print(x)

A = [1, 2, 3]
type(A)
for x in A:
    print(x)

A = [(1, 10), (2, 20), (3, 30)]
for T in A:

    angle, length = T
    turtle.forward(length)

for angle, length in A:
    turtle.forward(length)

D = dict(Dolgoprudny=6283, Moscow=78621, Piter=82851)
# D = {'Moscow': 78621,
#      'Dolgoprudny': 6283,            Это тотже словарь что и сверху в другой интерпритации
#      'Piter': 82851
# }
D['Rostov'] = 762
print(D)

for key in D:
    print(key,
          D[key])