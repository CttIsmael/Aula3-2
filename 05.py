def alfa(letra):
    vogal = 'a e i o u'
    consoante = 'b c d f g h j k l m n p q r s t v x z y w' 
    if letra.lower() in vogal :
        return f'vogal'
    elif letra.lower() in consoante:
        return f'consoante'  
    elif letra.isdigit():
        return f'número'
    else:
        return f'símbolo' 
    
def  main():
    letra = input()

    ad = alfa(letra)

    print(ad)

if __name__== "__main__":
    main()
