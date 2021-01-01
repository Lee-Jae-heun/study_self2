#test.py

while 1:
    a = 0; b = 0; c = 0; d = 0
    try:
        insert = int(input())
        insert = insert - 220
    except ValueError or EOFError:
        break
    
    while 1:
        if insert >= 500:
            insert -= 500
            a += 1
        elif insert >= 100:
            insert -= 100
            b += 1
        elif insert >= 50:
            insert -= 50
            c += 1
        elif insert >= 10:
            insert -= 10
            d += 1
        else:
            print("500원 {}개, 100원 {}개, 50원 {}개, 10원 {}개".format(a,b,c,d))
            break