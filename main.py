#PARA ESTOS 2 EJERCICIOS UTILIZAREMOS DEFINICIONES DE SUBRUTINAS
#EL PRIMER EJERCICIO SE SOLUCIONA CON LA PRIMERA SUBRUTINA
#EL SEGUNDO EJERCICIO ES LA COMBINACIÓN DE LA PRIMERA Y LA SEGUNDA SUBRUTINA

#PRIMERA SUBRUTINA
def bisiesto():     #NOMBRE BISIESTO
    a = int(input("Introduzca un año: "))       #PIDE AÑO
        #VALOR DEBE SER UN INT
    bisiesto = a % 4 == 0 or (a % 4 == 0 and a % 100 != 0)      #SI ES  BISIESTO, BISIESTO = TRUE
    if bisiesto:     #SI ES BISIESTO
        print ("El año introducido es bisiesto")        #OUTPUT
    else:       #SI NO
        print ("El año introducido no es bisiesto")     #OUTPUT

    Mes(bisiesto)       #LLAMADA A SUBRUTINA MES() (EJERCICIO SEGUNDO)

#SEGUNDA SUBRUTINA
def Mes(bisiesto):      #NOMBRE MES
    a = int (input ("Introduzca un mes (número): "))        #PIDE NÚMERO DE MES
    if a == 2:      #SI ES FEBRERO
        if bisiesto:        #SI ES BISIESTO
            print ("El mes de Febrero en el año designado tiene 29 días.")      #OUTPUT
        else:       #SI NO
            print ("El mes de Febrero en el año designado tiene 28 días.")      #OUTPUT

    else:       #NO ES FEBRERO
        if a%2==0:      #ES PAR (31 DÍAS)
            print ("El mes introducido tiene 31 días.")     #OUTPUT
        else:           #RESTO (IMPARES ==> 30 DÍAS)
            print ("El mes introducido tiene 30 días.")     #OUTPUT


bisiesto()      #LLAMADA A PRIMERA SUBRUTINA
                #LA PRIMERA SUBRUTINA ENLAZARÁ CON LA SEGUNDA AL FINAL
