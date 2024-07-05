import funciones as f
lista = []
while True:
    print("""
        1. Registrar puntajes torneo
        2. Listar todos los puntajes
        3. Imprimir por Tipo
        4. Salir del programa  
    """)
    op = input('-->')
    if op == '1':
        lista = f.registrarPuntajes(lista)
    elif op == '2':
        f.listarTodo(lista)
    elif op == '3':
        f.listarTipo(lista)
    elif op == '4':
        print('Saliendo....')
        break
    else:
        print('Opción NO existe!!')