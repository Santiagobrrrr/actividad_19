class Cookie:
    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size

    def display_info(self):
        print(f"Nombre de la galleta: {self.name} - Precio de galleta:Q{self.price} - Tamaño de galleta: {self.size}(cm)\n")

class RegisterCookie:
    def __init__(self):
        self.cookies = []

    def add_cookie(self):
        while True:
            try:
                while True: # Validar nombre y duplicados
                    name_cookie = input("Nombre de la galleta: ").strip().lower()
                    if name_cookie == "":
                        print("No puede ingresar un nombre vacío, intente nuevamente.\n")
                        continue

                    for cookie in self.cookies:
                        if cookie.name == name_cookie:
                            print("La galleta ya existe, intente nuevamente.\n")
                            break
                    else:
                        break # Solo entra aquí si NO se ejecutó el break => no hay duplicado

                while True: # Validar precio
                    try:
                        price_cookie = float(input("Precio de la galleta: Q"))
                        if price_cookie <= 0:
                            print("El precio de la galleta debe ser mayor que Q0, intente nuevamente.\n")
                            continue
                        break
                    except ValueError:
                        print("Error: ingreso mal un valor, intente de nuevo.")
                    except Exception as e:
                        print(f"Ocurrió un error inesperado: {e}")

                while True: # Validar tamaño
                    try:
                        size_cookie = float(input("Tamaño de la galleta (cm): "))
                        if size_cookie <= 0:
                            print("El tamaño de la galleta debe ser mayor a 0 cm, intente nuevamente.\n")
                            continue
                        break
                    except ValueError:
                        print("Error: ingreso mal un valor, intente de nuevo.")
                    except Exception as e:
                        print(f"Ocurrió un error inesperado: {e}")

                cookie = Cookie(name_cookie, price_cookie, size_cookie) # Crear y agregar galleta
                self.cookies.append(cookie)
                print("Galleta registrada correctamente.\n")
                cookie.display_info()
                break

            except Exception as e:
                print(f"Error: {e}")

        cookie.display_info()

    def display_cookies(self):
        if not self.cookies:
            print("No hay galletas registradas.\n")
            return

        print("\nLista de galletas registradas:")
        for i, cookie in enumerate(self.cookies, start=1):
            print(f"{i}. ", end="")
            cookie.display_info()
        print()

register = RegisterCookie()

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
            register.add_cookie()

        case "2":
            print(f"- Registrar galleta con chispas -")

        case "3":
            print(f"- Registrar galleta rellena -")

        case "4":
            print(f"- Lista de galletas -")
            register.display_cookies()

        case "5":
            print(f"- Buscar galleta por nombre -")

        case "6":
            print(f"- Eliminar galleta -")

        case "7":
            print(f"Saliendo del programa ...")
            break

        case _:
            print(f"Error: ingreso una opción inválida, intente de nuevo.")