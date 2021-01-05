def han(n):
    count = 0
    if int(n)<100:
        print(n)
    else:
        for j in range(100,int(n)+1):
            k = str(j)
            minus = int(k[1]) - int(k[0])
            print("{}:{}".format(k,minus))
            for i in range(len(str(j)) - 1):
                print("{}::".format(int(k[i + 1]) - int(k[i]) == minus))
                if int(k[i + 1]) - int(k[i]) == minus:
                    count += 1
        print(count + 99)
n = 100
han(n)