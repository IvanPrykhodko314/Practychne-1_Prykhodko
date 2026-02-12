def isEven(num):
    isEven = ""
    delThree = "" 
    if num % 2 == 0:
        isEven = "парне"
    else:
        isEven = "непарне"
    
    if num % 3 == 0:
        delThree = "ділиться на 3"
    else:
        delThree = "не ділиться на три"
    
    print(f"Число {isEven} і {delThree}")
    return isEven, delThree

isEven(int(input()))