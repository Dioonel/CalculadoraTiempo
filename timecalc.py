# Calculadora de tiempo entre 2 fechas

from sys import exit

class Fecha():                                                                                          # Definicion de la clase Fecha y sus metodos
    def __init__(self, año, meses, dias):
        self.año = año
        self.mes = meses
        self.dia = dias
    

    def validar(self, mes_dict):
        print("\nValidando datos de la fecha...\n")
        if self.mes not in mes_dict:
            print("Mes invalido.")
            exit(1)
        if not 0 < self.dia <= mes_dict[self.mes]["maxDia"]:
            print("Dia invalido.")
            exit(1)
        print("Fecha validada correctamente.")


    def mostrar(self, mes_dict):
        print(f"• AÑO: {self.año}")
        print("• MES: " + mes_dict[self.mes]["mesN"])
        print(f"• DIA: {self.dia}")


mes_data = {1 : {"mesN":"Enero", "maxDia":31},                                                          # Dict dentro de otro dict...
           2 : {"mesN":"Febrero", "maxDia":28},                                                         # contiene los nombres de cada mes y...
           3 : {"mesN":"Marzo", "maxDia":31},                                                           # la cantidad maxima de dias de cada mes
           4 : {"mesN":"Abril", "maxDia":30},
           5 : {"mesN":"Mayo", "maxDia":31},
           6 : {"mesN":"Junio", "maxDia":30},
           7 : {"mesN":"Julio", "maxDia":31},
           8 : {"mesN":"Agosto", "maxDia":31},
           9 : {"mesN":"Septiembre", "maxDia":30},
           10 : {"mesN":"Octubre", "maxDia":31},
           11 : {"mesN":"Noviembre", "maxDia":30},
           12 : {"mesN":"Diciembre", "maxDia":31}}

    
# ----------------------------------------------------------------------------------------------------------------------------------------- #

def main():                                                                                             # main
    print("\n- CALCULADORA DE TIEMPO ENTRE DOS FECHAS.")
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")                                              # Introduccion, se pide la primera fecha
    print("• Escriba los datos de la PRIMERA fecha.\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    fecha1 = Fecha(pedirAño(), pedirMes(), pedirDia())
    fecha1.validar(mes_data)


    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")                                              # Se pide la segunda fecha
    print("• Escriba los datos de la SEGUNDA fecha.\n")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
    fecha2 = Fecha(pedirAño(), pedirMes(), pedirDia())
    fecha2.validar(mes_data)

    print("\n\n\n\n#############################")                                                      # Se muestran los datos de las fechas cargadas
    print("-----------------------------\n")
    print("- DATOS DE LA PRIMERA FECHA: \n")
    fecha1.mostrar(mes_data)
    print("\n=============================\n")
    print("- DATOS DE LA SEGUNDA FECHA: \n")
    fecha2.mostrar(mes_data)
    print("\n-----------------------------")
    print("#############################")

    print("\n\n")
    calcularTiempo(fecha1, fecha2, mes_data)                                                            # Se calcula la diferencia de tiempo




# ----------------------------------------------------------------------------------------------------------------------------------------- #
def calcularTiempo(fechaA, fechaB, mesInfo):

    if fechaB.dia > fechaA.dia:                                                                         # Se calculan la dif de dias segun 3 posibles situaciones
        resultado_dias = fechaB.dia - fechaA.dia
        carry_dias = False
    elif fechaA.dia > fechaB.dia:
        resultado_dias = (mesInfo[fechaB.mes - 1]["maxDia"] - fechaA.dia) + fechaB.dia
        carry_dias = True
    elif fechaA.dia == fechaB.dia:
        resultado_dias = 0
        carry_dias = False
    else:
        print("WTF DIAS")
        exit(1)

    
    if fechaB.mes > fechaA.mes:                                                                         # Se calculan la dif de meses segun 3 posibles situaciones
        resultado_meses = fechaB.mes - fechaA.mes                                                       
        carry_meses = False
        if carry_dias:
            resultado_meses = resultado_meses - 1                                                       # Si hubo carry en los dias, resultado_meses - 1
    elif fechaA.mes > fechaB.mes:
        resultado_meses = (12 - fechaA.mes) + fechaB.mes
        carry_meses = True
        if carry_dias:
            resultado_meses = resultado_meses - 1
    elif fechaA.mes == fechaB.mes:
        resultado_meses = 0
        carry_meses = False
    else:
        print("WTF MESES")
        exit(1)
    

    resultado_años = abs(fechaB.año - fechaA.año)                                                       # Se calcula la dif de años, con abs el resultado siempre sera positivo
    if carry_meses:
        resultado_años = resultado_años - 1                                                             # Si hubo carry en los meses, resultado_años - 1
    

    print("-----------------------------------------------------\n")                                    # Se muestra el resultado final
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ RESULTADO ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~\n")
    print("Entre las 2 fechas ingresadas hay una diferencia de...")
    print(f"# # # # #   {resultado_años} años, {resultado_meses} meses y {resultado_dias} dias.   # # # # #\n")
    print("-----------------------------------------------------")    




def pedirAño():
    try:
        return int(input("• Año: "))
    except ValueError:
        valueError()

def pedirMes():
    try:
        return int(input("• Mes (EN FORMATO NUMERICO): "))
    except ValueError:
        valueError()

def pedirDia():
    try:
        return int(input("• Dia (EN FORMATO NUMERICO): "))
    except ValueError:
        valueError()

def valueError():
    print("Error en la sintaxis de la fecha.")
    exit(1)


main()