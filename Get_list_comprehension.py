# 리스트 캄프리헨션 (List comprehension)
t = [x for x in input().split() if int(x)%2 == 0]
print(t)
for i in range(len(t)):
    print(t[i],end=' ')
print("\n")
print(' '.join(t))
print("\n")
print(t)