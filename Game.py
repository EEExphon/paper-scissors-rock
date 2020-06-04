import random
YN = 1
while YN == 1:
    input("Start___")

    m = random.choice([1,2,3])
    n = random.choice([1,2,3])
    
    if m == 1:
        m = "Rock"
    elif m == 2:
        m = "Paper"
    elif m == 3:
        m = "Scissors"
    else:
        m = random.choice([1,2,3])
        while m != 1 and m != 2 and m != 3:
            m = random.choice([1,2,3])
            
    if n == 1:
        n = "Rock"
    elif n == 2:
        n = "Paper"
    elif n == 3:
        n = "Scissors"
    else:
        n = random.choice([1,2,3])
        while n != 1 and n != 2 and n != 3:
            n = random.choice([1,2,3])
        
    if m == n:
        print("Player one gives:",m)
        input("=================="+"="*len(m))
        print("Player two gives:",n)
        print("=================="+"="*len(n))
        result = "Draw."
    
    if m == "Rock":
        if n == "Paper":
            print("Player one gives:",m)
            input("=================="+"="*len(m))
            print("Player two gives:",n)
            print("=================="+"="*len(n))
            result = "Player two wins."
        elif n == "Scissors":
            print("Player one gives:",m)
            input("=================="+"="*len(m))
            print("Player two gives:",n)
            print("=================="+"="*len(n))
            result = "Player one wins."
    elif m == "Scissors":
        if n == "Paper":
            print("Player one gives:",m)
            input("=================="+"="*len(m))
            print("Player two gives:",n)
            print("=================="+"="*len(n))
            result = "Player one wins."
        elif n == "Rock":
            print("Player one gives:",m)
            input("=================="+"="*len(m))
            print("Player two gives:",n)
            print("=================="+"="*len(n))
            result = "Player two wins."
    print(result)
    input("="*len(result))
    input("Next round---")
