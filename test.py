import sys

a = int(sys.stdin.read())
b = list(int(sys.stdin.read().split()))
c = 0
for i in range(a):
    c += b[i]/max(b)*100

print(c/a)