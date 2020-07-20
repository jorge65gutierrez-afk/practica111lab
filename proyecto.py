# JORGE LUIS MAMANI GUTIERREZ
# CI. 10916316LP





#ingresado por primera vez
Nombredecliente= []
Apellidodelcliente =[]
CIdelcliente = []
numerodetelefono = []
D = []
DE = []
dinero=[]
totaldecuenta=[]
su1=[]
su2=[]
agd=[]
ndir=[]
def mostrarMenu() :
    print("gracias por usar el servicio de banco")
    print("----------------------------------------------------------------------------------------------------------------------")
    print("Elige una de nuestras opciones")
    print("1.- Registar a un nuevo cliente")
    print("2.- Editar informacion del cliente")
    print("3.- Desabilitar y habilitar a un cliente")
    print("4.- Mostrar a los clientes habilitados y Mostrar a los clientes deshabilitados")
    print("5.- Depositar / Retirar un monto X de la cuenta del cliente Y")
    print("6.- Calcular las Millas del cliente X en caso de que su cuenta este en dólares")
    print("7.- Probabilidad de que el cliente X gane el sorteo")
    print("8.- Plantear una consulta con los datos expuestos e implementarla")
    print("0.- salir")
def Registaraunnuevocliente():
    nuevoNombre = input("Ingrese el nombre del cliente nuevo: ")
    Nombredecliente.append(nuevoNombre)
    Apellidodelcliente.append(input("ingrese el apellido del clinete nuevo: "))
    CIdelcliente.append(input("Ingrese el CI del cliente: "))
    numerodetelefono.append(input("ingrese el numero de telefono: "))
    print("-----------------------------registro completado ------------------------- ")
def Editarinformaciondelcliente():
    numerodetelefono[0]= nuevo = input("ingrese el nuevo nuemero: ")
    print("nombre del cliente: ")
    print(Nombredecliente)
    print("apellido del cliente: ")
    print(Apellidodelcliente)
    print("CI del cliente: ")
    print(CIdelcliente)
    print("nuevo numero del cliente: ")
    print(numerodetelefono)
    print("actualizacion completada  ")

def Desabilitaryhabilitarcliente():
    def menu():
        print("elige una opcion:   ")
        print("1.- habilitar ")
        print("2.- deshabilitar")
        print("0.- salir")
    def habi():
        d = input("ingrese el name a habilitar. ")
        D.append(d)
        print("operacion exitosa  ")
    def des():
        de =input("ingrese el name a dehabilitar. ")
        DE.append(de)
        print("operacion exitosa")

    while True:
        menu()
        opcion = input()
        if opcion =="1":
            print("habilitar ")
            habi()
        elif opcion =="2":
            print("deshabilitar")
            des()
        else:
            print("exit ")
            break
        print("exit-----")
def MostraralosclienteshabilitadosyMostraralosclientesdeshabilitados():
    print("clientes habilitados ")
    print(D)
    print("clientes deshabilitados")
    print(DE)
    print("-------------")
def DepositaryoRetirarunmontoXdelacuentadelclienteY():
    def MMenu():
        print("------------elija las siguientes opciones: ---------")
        print("1.- Depositar: ")
        print("2.- retirar: ")
        print("0.- presiona cualquier tecla para salir ") 
    def DEP():
        print("estos son los nombres de los clientes")
        print(Nombredecliente)
        for x in range(1):
            nom=input("Ingrese el nombre del clientes:")
            Nombredecliente.append(nom)
            su1=int(input("Ingrese el dinero a ingresar:"))
            dinero.append([su1])
        for x in range(1):
            total=dinero[x][0]
            totaldecuenta.append(total)

        for x in range(1):
            print(Nombredecliente[x], totaldecuenta[x])

        posmayor=0
        mayor=totaldecuenta[0]
        for x in range(1,1):
            if totaldecuenta[x]>mayor:
                mayor=totaldecuenta[x]
                posmayor=x
        print("es el total de efectivo ingresado es de :")
        print(su1) 
        print("BS")
    def RET():
        print("estos son los nombres de los clientes")
        print(Nombredecliente)
        for x in range(1):
            nom=input("Ingrese el nombre del clientes:")
            Nombredecliente.append(nom)
            su2=int(input("Ingrese el dinero a retirar: "))
            dinero.append([su2])

        for x in range(1):
            total=dinero[x][0]
            totaldecuenta.append(total)

        for x in range(1):
            print(Nombredecliente[x], totaldecuenta[x])

        posmayor=0
        mayor=totaldecuenta[0]
        for x in range(1,1):
            if totaldecuenta[x]>mayor:
                mayor=totaldecuenta[x]
                posmayor=x
        print("es el total de efectivo  es de :")
        print(su2) 
        print("BS")
    while True:
        MMenu()
        opcion = input()
        if opcion =="1":

            print("Depositar")
            DEP()
        elif opcion =="2":
            print("Retirar")
            RET()
        else:
            print("          operacion exitosa----------")
            break
        print("---exit-----")
def CalcularlasMillasdelclienteXencasodequesuesteendólares():
    pDolar=float(input("ingres el precio actual minimo en el rango de 0.1 a 1: "))
    dolares=float(input("ingrese la cantidad a convetir: peso: "))
    cpeso=dolares+pDolar
    print(dolares," dolares equivalen a ", cpeso," pesos")
    print("gracias por usar el servicio de convercion: ")
    print("--------------------------------")
def  ProbabilidaddequeelclienteXganeelsorteo():
    print("estos son los clientes que estan registrados en la base de datos ")
    print(Nombredecliente)
    print("con su ahorrado total de: ")
    print(totaldecuenta)
    print("ingrese a 3 clinetes para realizar el sorteo: ")
    for x in range(3):
        nom=input("Ingrese el nombre del cliente:")
        Nombredecliente.append(nom)
        su1=int(input("Ingrese el primer ahorro:"))
        su2=int(input("Ingrese el segundo ahorro:"))
        su3=int(input("Ingrese el tercer ahorro:"))
        dinero.append([su1, su2, su3])

    for x in range(3):
        total=dinero[x][0]+dinero[x][1]+dinero[x][2]
        totaldecuenta.append(total)

    for x in range(3):
        print(Nombredecliente[x], totaldecuenta[x])

    posmayor=0
    mayor=totaldecuenta[0]
    for x in range(1,3):
        if totaldecuenta[x]>mayor:
            mayor=totaldecuenta[x]
            posmayor=x
    print("cliente con mayores ingresos---")
    print(Nombredecliente[posmayor])
    print("con un ingreso de",mayor, " es acreedeor de un tiket para un sorteo")
def Plantearconsultalosexpuestoseimplementarla():
    def menuu():
        print("print elija que consulta desea hacer: ")
        print("1.- se puede agregar mas datos? ")
        print("2.- mostar clientes registardos")
        print("3.- horarios de apertura de banco ")
        print("0.- salir")
    def agregarmasdatos():
        print("ingre el nombre al que desea agregar mas datos ")
        print(Nombredecliente)
        print("que datos desea agregar")
        print(agd)
        print("ingrese",agd, "porfabor")
        print(ndir)
        print("se a guardado correctamentela a ", Nombredecliente, "con la",agd)
        print("--------------------------------")
    def moscleintesregis():
        print("los clinetes registrados son",Nombredecliente, "con el numero de telefono ",numerodetelefono,"fin")
    def hrdeabierto():
        print("fecha y hora actual")
        import time
        print(time.ctime())
        print("los horarios de apertura son: ")
        print("lunes de 8 am a 16 pm")
        print("lunes de 8 am a 16 pm")
        print("lunes de 8 am a 16 pm")
        print("lunes de 8 am a 16 pm")
        print("lunes de 8 am a 16 pm")
        print("lunes de 8 am a 16 pm")


    while True:
        menuu()
        opcion = input()
        if opcion == "1":
            print("se puede agregar mas datos? ")
            agregarmasdatos()
        elif opcion == "2":
            print("mostar clientes registardos")
            moscleintesregis()
        elif opcion == "3":
            print("horarios de apertura de banco")
            hrdeabierto()
        else:
            print("GRACIAS POR SU CONSULTA")
            break
        print("estamos a su servicio")
while True:
    mostrarMenu()
    opcion = input()
    if opcion == "1":
        print("registro de nuevo cliente")
        Registaraunnuevocliente()
    elif opcion == "2":
        print("editar informacion del cliente")
        Editarinformaciondelcliente()
    elif opcion == "3":
        print("deshabilitar y habilitar al cliente")
        Desabilitaryhabilitarcliente()
    elif opcion == "4":
        print("Mostar cliente habilitado y deshabilitado")
        MostraralosclienteshabilitadosyMostraralosclientesdeshabilitados()
    elif opcion == "5":
        print("despositar y retirar de la cuenta")
        DepositaryoRetirarunmontoXdelacuentadelclienteY()
    elif opcion == "6":
        print("calcular las millas")
        CalcularlasMillasdelclienteXencasodequesuesteendólares()
    elif opcion == "7":
        print("probabilidades de ganar ")
        ProbabilidaddequeelclienteXganeelsorteo()
    elif opcion == "8":
        print("consultas")
        Plantearconsultalosexpuestoseimplementarla()
    else:
        print("gracias por su preferencia")
        break
    print("estamos a su servicio")
        
