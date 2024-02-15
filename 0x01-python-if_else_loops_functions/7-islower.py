#!/usr/bin/python3
def islower(c):
    try:
        return 'a' <= c <= 'z'
    except TypeError:
        print("Error: Input is not a character.")
        return False
    
result = islower('a')
print(result)

result = islower('A')
print(result)
