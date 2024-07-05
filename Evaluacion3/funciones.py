from os import system
#utilizo un diccionario, para luego acceder por su key al tipo
tipo = { 1:'Principiante',
         2:'Avanzado',
         3:'Experto'}
#función para validar tipos numéricos, sirve para rango y para mayor qué (por eso el vMax podría ser nulo)
def validaNro(txtIn, txtEr, txtEx, vMin, vMax=None):
    while True:
        try:
            nro=int(input(txtIn))
            if (vMin <= nro and vMax == None) or (vMin <= nro <= vMax):
                break
            else:
                print(txtEr)
        except:
            print(txtEx)
    return nro
#función que se llama por cada uno de los juegos (Fortnite, Valorant, Fifa), esto es porque hice una lista para los 3 puntajes de cada usuario
def ptosJuego(juego,listPje):
    if input(f'Juega {juego}? (s/n): ').lower() == 's':
        listPje.append(validaNro(f'Ingrese Puntaje {juego}: ','Puntaje debe ser Mayor a Cero','Es un N°',1))
    else:
        listPje.append(0)
    return listPje
#función para registrar jugadores y sus puntajes
def registrarPuntajes(listJugadores):
    unJugador = {} #por cada jugador creo un diccionario
    puntajes = [] #en cada diccionario en la key 'juegos' habrá una lista de puntajes (de 3 elementos)
    unJugador['id'] = input('Ingrese ID usuario: ')
    unJugador['nombre'] = input('Ingrese Nombre Completo: ')
    puntajes = ptosJuego('Fortnite',puntajes)
    puntajes = ptosJuego('Valorant',puntajes)
    puntajes = ptosJuego('Fifa',puntajes)
    unJugador['juegos'] = puntajes
    tp = validaNro('1: Principiante - 2: Avanzado - 3: Experto: ','Tipo NO existe', 'Tipo es un N°',1,3)
    unJugador['tipo'] = tp          
    listJugadores.append(unJugador) #agrego diccionario de un jugador a la lista
    print('Jugador Registrado')
    print('\nPresione para Continuar....')
    input()
    system("cls")
    return listJugadores
#función que recorrerá la lista por elementos e imprimira la información de cada diccionario
def listarTodo(listJugadores):
    #primero imprimo el encabezado 
    print('Id Jugador'.ljust(15) +'Nombre'.ljust(30)+'Valorant'.ljust(15)+'Fortnite'.ljust(15)+'Fifa'.ljust(15)+'Tipo')
    for d in listJugadores: #por cada elemento de la lista obtengo un diccionario de jugador
        print(str(d['id']).ljust(15) + str(d['nombre']).ljust(30)+str(d['juegos'][0]).ljust(15)+str(d['juegos'][1]).ljust(15)+str(d['juegos'][2]).ljust(15)+tipo[d['tipo']])
    print('\nPresione para Continuar....')
    input()
    system("cls")
#función que crea archivo de texto y graba en él la información filtrada por tipo
def listarTipo(listJugadores):
    #primero creo el encabezado
    encabezado = 'Id Jugador'.ljust(15) +'Nombre'.ljust(30)+'Valorant'.ljust(15)+'Fortnite'.ljust(15)+'Fifa'.ljust(15)+'Tipo'
    try:
        with open('jugadores.txt', 'w') as archivo:
            archivo.write(encabezado+'\n') #agrego el encabezado al archivo
            tp = validaNro('1: Principiante - 2: Avanzado - 3: Experto: ','Tipo NO existe', 'Tipo es un N°',1,3)
            for d in listJugadores:
                for clave,valor in d.items():
                    #busco en el diccionario el tipo y verifico que corresponda al solicitado por el usuario 
                    if clave =='tipo' and valor == tp:
                        #al encontrar un jugador que coincida con el filtro,lo asigno a una variable de tipo string
                        registro = str(d['id']).ljust(15) + str(d['nombre']).ljust(30)+str(d['juegos'][0]).ljust(15)+str(d['juegos'][1]).ljust(15)+str(d['juegos'][2]).ljust(15)+tipo[d['tipo']]
                        #agrego la variable con su información al archivo
                        archivo.write(registro+'\n')
        print('Archivo Generado!!!\nPresione para Continuar....')
        input()
        system("cls")
    except Exception as e:
        print('Error:', e)