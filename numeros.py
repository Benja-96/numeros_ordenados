def ordenar_numeros():
    numeros= []
    print("Por favor, ingrese 10 numeros: ")
    for i in range(10):
        while True:
            try:
                num = float(input(f"Ingesa el numero ¨{i + 1}: "))
                numeros.append(num)
                break
            except ValueError:
                print("ERROS: Ingrese un numero valido. ")

    print("\n--- MENU CHIKITITO---")
    print("1. Ordenar de menor a mayor")
    print("2. Ordenar de mayor a menor")

    opcion = input("Elige una opcion (1 0 2): ")

    if opcion == "1":
        numeros.sort()
        print("\nLista ordenada de menor a mayor: ")
        print(numeros)

    elif opcion == "2":
        numeros.sort(reverse=True)
        print("\nLista ordenada de mayor a menor: ")
        print(numeros)

    else:
        print("\nOpcion no valida. Por favor, ejecuta el programa nuevamente.")
ordenar_numeros()