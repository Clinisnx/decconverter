### Criador: Nairam dos Santos / https://github.com/Clinisnx ###

inteiro = int(input("Insira um número inteiro para a conversão de bases"))
binario = ""
hexadec = [ ]
octal = ""
ops = int(input('''Selecione a operação de acordo com o número indicado:
                [1] Binário
                [2] Hexadecimal
                [3] Octal
                '''))

if ops == 1:
    while inteiro!=0:
        r = inteiro%2
        binario = str(r) + binario 
        inteiro = inteiro//2
print(binario)

if ops == 2:
    while inteiro!=0:
        if inteiro%16==1:
            inteiro=(inteiro-1)/16
            hexadec.insert(0, 1)
        elif inteiro%16==2:
            inteiro=(inteiro-2)/16
            hexadec.insert(0, 2)
        elif inteiro%16==3:
            inteiro=(inteiro-3)/16
            hexadec.insert(0, 3)
        elif inteiro%16==4:
            inteiro=(inteiro-4)/16
            hexadec.insert(0, 4)
        elif inteiro%16==5:
            inteiro=(inteiro-5)/16
            hexadec.insert(0, 5)
        elif inteiro%16==6:
            inteiro=(inteiro-6)/16
            hexadec.insert(0, 6)
        elif inteiro%16==7:
            inteiro=(inteiro-7/16)
            hexadec.insert(0, 7)
        elif inteiro%16==8:
            inteiro=(inteiro-8)/16
            hexadec.insert(0, 8)
        elif inteiro%16==9:
            inteiro=(inteiro-9)/16
            hexadec.insert(0, 9)
        elif inteiro%16==10:
            inteiro=(inteiro-10)/16
            hexadec.insert(0, 'A')
        elif inteiro%16==11:
            inteiro=(inteiro-11)/16
            hexadec.insert(0, 'B')
        elif inteiro%16==12:
            inteiro=(inteiro-12)/16
            hexadec.insert(0, 'C')
        elif inteiro%16==13:
            inteiro=(inteiro-13)/16
            hexadec.insert(0, 'D')
        elif inteiro%16==14:
            inteiro=(inteiro-14)/16
            hexadec.insert(0, 'E')
        elif inteiro%16==15:
            inteiro=(inteiro-15)/16
            hexadec.insert(0, 'F')
        elif inteiro%16==0:
            inteiro=(inteiro)/16
            hexadec.insert(0, 0)
print("O valor da conversão é de: ", hexadec  )

if ops == 3:
    while inteiro!=0:
        r = inteiro%8
        octal = str(r) + octal
        inteiro = inteiro//8
    print(octal)