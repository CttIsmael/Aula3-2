def vogal(letra):
    if letra.lower() in ('a','e','i','o','u','b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'):
        return True
    else:
        return False
    
def main():
    letra = str(input())
    print((vogal(letra)))

if __name__ == "__main__":
    main()
