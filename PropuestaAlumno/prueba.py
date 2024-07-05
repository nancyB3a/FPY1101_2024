jugadores=[]
principiante=[]
avanzado=[]
experto=[]

def registrar_puntajes(jugadores):
    print('\n***Registrar usuario***\n')
    id = input('Ingrese ID Jugador: ')
    nombre = input('Ingrese Nombre del Jugador: ')
    tipo = input('Ingrese Tipo de Jugador [Principiante - Avanzado - Experto] : ').capitalize()

    try:
        print('\n***Ingresar puntaje del Jugador (Sólo números)***\n')
        valorant = int(input('Ingrese puntaje VALORANT: '))
        fortnite = int(input('Ingrese puntaje FORTNITE: '))
        fifa = int(input('Ingrese puntaje FIFA: '))

        if valorant<0 or fortnite<0 or fifa<0:
            print('\nIngrese números positivos!!!\n')

    except ValueError:
        print('\nSólo NÚMEROS!!!\n')

    jugadores.append({
        'ID JUGADOR' : id,
        'NOMBRE' : nombre,
        'VALORANT' : valorant,
        'FORTNITE' : fortnite,
        'FIFA' : fifa,
        'TIPO' : tipo
    })

    if tipo == 'Principiante':
        principiante.append({
        'ID JUGADOR' : id,
        'NOMBRE' : nombre,
        'VALORANT' : valorant,
        'FORTNITE' : fortnite,
        'FIFA' : fifa,
        'TIPO' : tipo
        })

    elif tipo == 'Avanzado':
        avanzado.append({
        'ID JUGADOR' : id,
        'NOMBRE' : nombre,
        'VALORANT' : valorant,
        'FORTNITE' : fortnite,
        'FIFA' : fifa,
        'TIPO' : tipo
        })

    elif tipo == 'Experto':
        experto.append({
        'ID JUGADOR' : id,
        'NOMBRE' : nombre,
        'VALORANT' : valorant,
        'FORTNITE' : fortnite,
        'FIFA' : fifa,
        'TIPO' : tipo
        })

    print('\nJugador registrado con éxito.')

def listar_puntajes(jugadores):
    if (len(jugadores)) <= 0:
        print('\nNO HAY JUGADORES REGISTRADOS!!!')
    else:
        print('\nLista de Jugadores\n')
        print(f'| {('ID JUGADOR'):<16} | {('Nombre'):<16} | {('VALORANT'):<16} | {('FORTNITE'):<16} | {('FIFA'):<16} | {('TIPO'):<16} |')
        print('='*120)
        for i in jugadores:
            print(f'| {i['ID JUGADOR']:<16} | {i['NOMBRE']:<16} | {i['VALORANT']:<16} | {i['FORTNITE']:<16} | {i['FIFA']:<16} | {i['TIPO']:<16} |')

def imprimir_por_tipo(principiante,avanzado,experto):

    tipo_jugadores=('Principiante','Avanzado','Experto')

    with open('planilla.txt','w') as file:
        try:
            print('\n***Imprimir Jugadores por Tipo***\n')
            tipo_jugador=input('Ingrese tipo de jugador [Principiante - Avanzado - Experto]: ').capitalize()
            if tipo_jugador not in tipo_jugadores:
                print('\nError!!! Ingrese un tipo de jugador válido!!!')

            elif tipo_jugador == 'Principiante':
                file.write('planilla principiante\n')
                file.write('\nLista de Jugadores\n')
                file.write(f'| {('ID JUGADOR'):<16} | {('Nombre'):<16} | {('VALORANT'):<16} | {('FORTNITE'):<16} | {('FIFA'):<16} | {('TIPO'):<16} |\n')
                for i in principiante:
                    file.write(f'| {i['ID JUGADOR']:<16} | {i['NOMBRE']:<16} | {i['VALORANT']:<16} | {i['FORTNITE']:<16} | {i['FIFA']:<16} | {i['TIPO']:<16} |\n')            

            elif tipo_jugador == 'Avanzado':
                file.write('planilla avanzado\n')
                file.write('\nLista de Jugadores\n')
                file.write(f'| {('ID JUGADOR'):<16} | {('Nombre'):<16} | {('VALORANT'):<16} | {('FORTNITE'):<16} | {('FIFA'):<16} | {('TIPO'):<16} |\n')
                for i in avanzado:
                    file.write(f'| {i['ID JUGADOR']:<16} | {i['NOMBRE']:<16} | {i['VALORANT']:<16} | {i['FORTNITE']:<16} | {i['FIFA']:<16} | {i['TIPO']:<16} |\n')

            elif tipo_jugador == 'Experto':
                file.write('planilla experto\n')
                file.write('\nLista de Jugadores\n')
                file.write(f'| {('ID JUGADOR'):<16} | {('Nombre'):<16} | {('VALORANT'):<16} | {('FORTNITE'):<16} | {('FIFA'):<16} | {('TIPO'):<16} |\n')
                for i in experto:
                    file.write(f'| {i['ID JUGADOR']:<16} | {i['NOMBRE']:<16} | {i['VALORANT']:<16} | {i['FORTNITE']:<16} | {i['FIFA']:<16} | {i['TIPO']:<16} |\n')
        
        except Exception:
            print('Error!!!')
    

def menu():

    opc = 0

    while opc != 4:

        print('''
            eShirlitos

        Opciones disponibles:

        1.- Registrar puntajes torneo
        2.- Listar los todos puntajes
        3.- Imprimir por Tipo
        4.- Salir del programa''')

        try:
            opc=int(input('\nIngrese un número: '))
            if opc<=0 or opc >4:
                print('\nIngrese una opción correcta!!!')
        except ValueError:
            print('\nSOLO NÚMEROS!!!')

        if opc == 1:
            registrar_puntajes(jugadores)
        elif opc == 2:
            listar_puntajes(jugadores)
        elif opc== 3:
            imprimir_por_tipo(principiante,avanzado,experto)
            print('\nPlanilla registrada con éxito.')
        elif opc == 4:
            print('\nSaliendo...\n')


    






    