def bin2dec(binario):
    dec = 0
    binario = binario[::-1]
    for cont in range(len(binario)):        
        if (binario[cont] == '1'):
            dec += 2 ** cont
    return dec

binario = input("numero binario: ")
print(bin2dec(binario), binario)