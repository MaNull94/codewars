#https://www.codewars.com/kata/58f5c63f1e26ecda7e000029

def wave(people:str):
    result = []
    if people:
        for i in range(0, len(people)):
            if people[i].isspace():
                continue
            result.append(people[:i] + people[i:].capitalize())
    return result
