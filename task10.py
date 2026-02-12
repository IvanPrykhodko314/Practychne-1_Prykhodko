userInput = input('Введіть дані: ')

partInput = userInput.split(", ")

name = partInput[0].split(": ")[1].strip('"')
age = partInput[1].split(": ")[1].strip('"')
city = partInput[2].split(": ")[1].strip('"')

print(f"{name}, якому {age} рік проживає у місті {city}")