def dig(letra):
    vog = True
    if letra == "a":
        return vog
    if letra == "e":
        return vog
    if letra == "i":
        return vog
    if letra == "o":
        return vog
    if letra == "u":
        return vog
    if letra == "A":
        return vog
    if letra == "E":
        return vog
    if letra == "I":
        return vog
    if letra == "O":
        return vog
    if letra == "U":
        return vog
    else:
        return not vog
 
def main():
    letra = str(input())
    print (f'{dig(letra)}')

if __name__ == "__main__":
    main()
