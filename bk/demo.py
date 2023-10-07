
solonnhat = 0

for i in range(0, 11):
    print('gia tri cua i la', i)
    if i > solonnhat:
        solonnhat = i

print('so lon nhat', solonnhat)

sonhonhat = 0
for i in range (0,11):
    print ('gia tri cua i la', i)
    if i < sonhonhat:
        sonhonhat = i

print('sonhonhat', sonhonhat)

for i in range (1,20):
    s = '#' * i
    print (s)

for i in range (20,1,-1):
    s = '#' * i
    print (s)