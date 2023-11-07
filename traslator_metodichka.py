print(f"Траслятор в методичевский")
magic_number1 = 29
magic_number2 = 982

def translate_char(c:str) -> str:
    try:
        return chr(ord(c) - magic_number2)
    except:
        return chr(ord(c) - magic_number1)

def translate(s:str) -> str:
    return ''.join([translate_char(c) for c in s])

run = True
print("Для выхода: exit")

while run:
    s = input("Введите строку на человечьем ")
    
    if(s.lower() == "exit"):
        run = False
        
        break
    
    print(translate(s))

        
    
