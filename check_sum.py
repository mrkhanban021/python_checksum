data = "6219861902312980"

def luhn_check(card_number: str) -> bool:
    
    reversed_digits = card_number[::-1]
    
    total = 0
    for i , digit in enumerate(reversed_digits):
        n = int(digit)
        if i % 2 == 1:
            x = n * 2
            if x > 9:
                x -= 9
            total += x
        else:
            total += n
        print(total)
    return total % 10 == 0


sheba = "IR220560213780004251511001"

def check_sheba(sheba_number: str)-> bool:
    if len(sheba_number) != 26:
        return False
    
    sheb = sheba_number[4:] + '1827' + sheba_number[2:4]
    
    if int(sheb) % 97 == 1:
        return True
    return False
    
print(check_sheba(sheba))