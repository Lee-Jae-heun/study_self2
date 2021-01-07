count = 0
for i in range (int(input())):
    a = list(input())
    print("a value : ",a)
    print("len == set?: ",len(a) == set(a))
    if len(a) == set(a):
        count = count + 1
        print("count value : ",count)
    else:
        t = []
        recent = 'None'
        count = count + 1
        end = True
        print("t value : ",t)
        print("recent value : ",recent)
        print("count value : ",count)
        while end:
            for j in a:
                print("j value : ",j)
                print("j not in t? : ",j not in t)
                if j not in t:
                    t.append(j)
                    recent = j
                    print("t value : ",t)
                    print("recent value : ",recent)
                else:
                    print("recent != j? : ",recent != j)
                    if recent != j:
                        count = count - 1
                        end = False
                        break
                        print("count value : ",count)
                    else:
                        recent = recent
                        print("recent value : ",recent)
                end = False

print(count)