def vogal(letra):
    if letra.lower() in 'a e i o u b c d f g h j k l m n p q r s t v x z y w':
        return True
    else:
        if letra in ('0 1 2 3 4 5 6 7 8 9'):
            return False
    
def main():
    letra = str(input())
    print((vogal(letra)))

if __name__ == "__main__":
    main()

