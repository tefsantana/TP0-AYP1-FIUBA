"""Se pide crear un programa donde el usuario ingrese el día y mes de su cumpleaños y el programa le imprimir por pantalla a qué signo del zodíaco corresponde.

Aries: 21 de marzo al 20 de abril.
Tauro: 21 de abril al 20 de mayo.
Geminis: 21 de mayo al 21 de junio.
Cancer: 22 de junio al 23 de julio.
Leo: 24 de julio al 23 de agosto.
Virgo: 24 de agosto al 23 de septiembre.
Libra: 24 de septiembre al 22 de octubre.
Escorpio: 23 de octubre al 22 de noviembre.
Sagitario: 23 de noviembre al 21 de diciembre.
Capricornio: 22 de diciembre al 20 de enero.
Acuario: 21 de enero al 19 de febrero.
Piscis: 20 de febrero al 20 de marzo.
Ejemplo:

>>>Ingrese el dia: 20
>>>Ingrese el mes: 2
Piscis
>>>Ingrese el dia: 31
>>>Ingrese el mes: 12
Capricornio
>>>Ingrese el dia: 10
>>>Ingrese el mes: 6
Geminis"""

def signo_zodiaco(dia, mes):
    '''
    DOCUMENTACION
    '''

    if ((mes==3) and (dia >= 21)) or ((mes==4) and (dia <= 20)):
        print("Aries")
    
    elif ((mes==4) and (dia >= 21)) or ((mes==5) and (dia <= 20)):
        print("Tauro")
    
    elif ((mes==5) and (dia >= 21)) or ((mes==6) and (dia <= 21)):
        print("Geminis")
    
    elif ((mes==6) and (dia >= 22)) or ((mes==7) and (dia <= 23)):
        print("Cancer") 
    
    elif ((mes==7) and (dia >= 24)) or ((mes==8) and (dia <= 23)):
        print("Leo") 

    elif ((mes==8) and (dia >= 24)) or ((mes==9) and (dia <= 23)):
        print("Virgo") 
    
    elif ((mes==9) and (dia >= 24)) or ((mes==10) and (dia <= 22)):
        print("Libra") 
    
    elif ((mes==10) and (dia >= 23)) or ((mes==11) and (dia <= 22)):
        print("Escorpio") 
    
    elif ((mes==11) and (dia >= 23)) or ((mes==12) and (dia <= 21)):
        print("Sagitario") 

    elif ((mes==12) and (dia >= 22)) or ((mes==1) and (dia <= 20)):
        print("Capricornio") 

    elif ((mes==1) and (dia >= 21)) or ((mes==2) and (dia <= 19)):
        print("Acuario")

    elif ((mes==2) and (dia >= 20)) or ((mes==3) and (dia <= 20)):
        print("Piscis")



def main():
    '''
    El programa pide al usuario su dia y mes de nacimiento e imprime por pantalla su signo zodiacal
    '''
    dia: int = int(input("Ingrese el dia: "))
    mes: int = int(input("Ingrese el mes: "))

    while (mes > 12) or (mes < 1) or (dia > 31) or ((dia > 30) and ((mes == 2) or (mes == 4) or (mes == 6) or (mes == 9) or (mes == 11))) or not dia.isnumeric() or not mes.isnumeric():
        dia = int(input("Ingrese el dia: "))
        mes = int(input("Ingrese el mes: "))
    
    signo_zodiaco(dia, mes)
    

main()