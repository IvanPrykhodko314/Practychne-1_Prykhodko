def search(listSearch):
    searchfor = input("Введіть елемент для пошуку: ")
    isfound = False
    
    for item in listSearch:
        if str(searchfor) == str(item):
            isfound = True
            break
    
    if isfound:
        print(f"Елемент '{searchfor}' знайдено")
    else:
        print(f"Елемент '{searchfor}' не знайдено")

myList = ["apple", "banana", "cherry", 1, 2, 3, 4]
search(myList)
