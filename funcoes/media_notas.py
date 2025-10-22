def media(notas):
    quantidade = len(notas)
    total = 0
    
    for n in notas:
        total += n
    
    return total / quantidade

def maior(notas):
    return max(notas)

def menor(notas):
    return min(notas)