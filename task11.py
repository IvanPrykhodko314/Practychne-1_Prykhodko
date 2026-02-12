def search(listSearch):
    searchfor = input("Введіть елемент для пошуку: ")
    isfound = False
    
    for i in listSearch:
        for j in i:
            if str(searchfor) == str(j):
                isfound = True
                break
        if isfound:
            break
    
    if isfound:
        print(f"Елемент '{searchfor}' знайдено")
    else:
        print(f"Елемент '{searchfor}' не знайдено")

myList = [[1, 2, 3], ["Львів", "Київ", "Одеса"], [4, 5, 6]]
search(myList)
