while True:
    print(f"-- Menú de Galletas --")
    print(f"1. Registrar galleta básica")
    print(f"2. Registrar galleta con chispas")
    print(f"3. Registrar galleta rellena")
    print(f"4. Lista de galletas")
    print(f"5. Buscar galleta")
    print(f"6. Eliminar galleta")
    print(f"7. Salir")

    option_user = input(f"Ingrese la opción que desea realizar: ")

    match option_user:
        case "1":
            print(f"- Registrar galleta básica -")

        case "2":
            print(f"- Registrar galleta con chispas -")

        case "3":
            print(f"- Registrar galleta rellena -")

        case "4":
            print(f"- Lista de galletas -")

        case "5":
            print(f"- Buscar galleta por nombre -")

        case "6":
            print(f"- Eliminar galleta -")

        case "7":
            print(f"Saliendo del programa ...")
            break

        case _:
            print(f"Error: ingreso una opción inválida, intente de nuevo.")