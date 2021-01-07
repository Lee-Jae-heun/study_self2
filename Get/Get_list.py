# 리스트에 관한 포인터 개념
a = [1,2,3]
k = a
a = a + [4,5]
k += [6,7]
print(k)
print(a)