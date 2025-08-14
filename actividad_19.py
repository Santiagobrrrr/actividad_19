class Cookie: # CLASE PADRE
    def __init__(self, name, price, weight): # Inicialización de variables
        self.name = name
        self.price = price
        self.weight = weight

    def display_info(self): # Metodo para mostrar las galletas guardadas
        return f"Nombre de la galleta: {self.name} - Precio: Q{self.price} - Peso: {self.weight}g" # Devuelve la información principal de la galleta

class Filling: # SEGUNDA CLASE PADRE
    def __init__(self, filling_flavor): # Se inicializa el sabor del relleno
        self.filling_flavor = filling_flavor

    def filling_description(self):
        return f"El sabor del relleno es {self.filling_flavor}\n" # Metodo que describe el sabor del relleno

class ChipCookie(Cookie): # CLASE DE HERENCIA SIMPLE
    def __init__(self, name, price, weight, chip_amount):
        super().__init__(name, price, weight) # Llama al constructor de Cookie e inicializa los atributos sin tener que repetir código
        self.chip_amount = chip_amount # Atributo diferente (chispas)

    def display_info(self):
        return f"{super().display_info()} - Chispas: {self.chip_amount}\n" # Combina la info base con la cantidad de chispas

class FilledCookie(Cookie, Filling): # CLASE DE MULTIHERENCIA (hereda la galleta y al relleno)
    def __init__(self, name, price, weight, filling_flavor):
        Cookie.__init__(self, name, price, weight) # Se inicializa ambas herencias padre
        Filling.__init__(self, filling_flavor)

    def display_info(self):
        return f"{super().display_info()} - {self.filling_description()}\n" # # Combina la info base de Cookie con la descripción del relleno

class RegisterCookie:
    def __init__(self):
        self.cookies = []

    def add_cookie(self): # Galleta básica
        try:
            name_cookie = input("Nombre de la galleta: ").strip()
            if not name_cookie:
                print("No puede ingresar un nombre vacío.\n") # No acepta nombres repetidos
                return
            for c in self.cookies: # Recorre la lista y evita nombres duplicados
                if c.name.lower() == name_cookie.lower():
                    print("La galleta ya existe.\n")
                    return

            price_cookie = float(input("Precio de la galleta: Q"))
            if price_cookie <= 0: # Verifica si el precio es mayor a Q0
                print("El precio debe ser mayor que Q0.\n")
                return

            weight_cookie = float(input("Peso de la galleta (g): "))
            if weight_cookie <= 0: # Verifica si el peso es mayor a 0 g
                print("El peso debe ser mayor a 0g.\n")
                return
            cookie = Cookie(name_cookie, price_cookie, weight_cookie) # Crea la galleta básica y la guarda
            self.cookies.append(cookie)
            print("Galleta registrada correctamente.\n")

        except ValueError:
            print("Error: ingreso mal un valor numérico.\n")
        except Exception as e:
            print(f"Ocurrió un error: {e}\n")

    def add_chip_cookie(self):
        try:
            name_cookie = input("Nombre de la galleta: ").strip()
            if not name_cookie:
                print("No puede ingresar un nombre vacío.\n")
                return
            for c in self.cookies: # Recorre la lista y evita nombres duplicados
                if c.name.lower() == name_cookie.lower():
                    print("La galleta ya existe.\n")
                    return

            price_cookie = float(input("Precio de la galleta: Q"))
            if price_cookie <= 0: # Verifica si el precio es mayor a Q0
                print("El precio debe ser mayor que Q0.\n")
                return

            weight_cookie = float(input("Peso de la galleta (g): "))
            if weight_cookie <= 0: # Verifica si el peso es mayor a 0 g
                print("El peso debe ser mayor a 0g.\n")
                return

            chip_amount = float(input("Ingrese cuantas chipas quiere en la galleta: "))
            if chip_amount < 0: # Verifica si la cantidad de chispas es válido
                print("Las chispas deben de ser 0 o mayores de 0\n")

            cookie = ChipCookie(name_cookie, price_cookie, weight_cookie, chip_amount) # Crea la galleta con chispas y la guarda
            self.cookies.append(cookie)
            print("Galleta registrada correctamente.\n")

        except ValueError:
            print("Error: ingreso mal un valor numérico.\n")
        except Exception as e:
            print(f"Ocurrió un error: {e}\n")

    def add_filling_cookie(self):
        try:
            name_cookie = input("Nombre de la galleta: ").strip()
            if not name_cookie:
                print("No puede ingresar un nombre vacío.\n")
                return
            for c in self.cookies:
                if c.name.lower() == name_cookie.lower():
                    print("La galleta ya existe.\n")
                    return

            price_cookie = float(input("Precio de la galleta: Q"))
            if price_cookie <= 0: # Verifica si el precio es mayor a Q0
                print("El precio debe ser mayor que Q0.\n")
                return

            weight_cookie = float(input("Peso de la galleta (g): "))
            if weight_cookie <= 0: # Verifica si el peso es mayor a 0 g
                print("El peso debe ser mayor a 0g.\n")
                return

            filling_flavor = input("Ingrese el sabor del relleno: ")

            cookie = FilledCookie(name_cookie, price_cookie, weight_cookie, filling_flavor)
            self.cookies.append(cookie)
            print("Galleta registrada correctamente.\n")

        except ValueError:
            print("Error: ingreso mal un valor numérico.\n")
        except Exception as e:
            print(f"Ocurrió un error: {e}\n")

    def display_cookies(self):
        if not self.cookies: # Verificación si esta vacía la lista
            print("No hay galletas registradas.\n")
            return

        print("\nLista de galletas registradas:") # Impresión de galletas registradas
        for i, cookie in enumerate(self.cookies, start=1):
            print(f"{i}. {cookie.display_info()}")
        print()

    def search_cookie(self):
        name_search = input("Ingrese el nombre de la galleta a buscar: ").strip().lower() # Verifica si el campo esta vacio
        for cookie in self.cookies:
            if cookie.name.lower() == name_search: # Recorre lista para buscar la galleta ingresada
                print(f"Galleta encontrada: {cookie.display_info()}\n") # Impresión de información de la galleta registrada
                return
        print("No se encontró ninguna galleta con ese nombre.\n")

    def delete_cookie(self):
        name_delete = input("Ingrese el nombre de la galleta a eliminar: ").strip().lower() # Verifica si el campo esta vacío
        for cookie in self.cookies: # Recorre la lista para buscar el nombre ingresado
            if cookie.name.lower() == name_delete:
                self.cookies.remove(cookie) # Si es encontrado el nombre se remueve o elimina el nombre de la galleta
                print("Galleta eliminada correctamente.\n")
                return
        print("No se encontró ninguna galleta con ese nombre.\n")

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
            register.add_chip_cookie()

        case "3":
            print(f"- Registrar galleta rellena -")
            register.add_filling_cookie()

        case "4":
            print(f"- Lista de galletas -")
            register.display_cookies()

        case "5":
            print(f"- Buscar galleta por nombre -")
            register.search_cookie()

        case "6":
            print(f"- Eliminar galleta -")
            register.delete_cookie()

        case "7":
            print(f"Saliendo del programa ...")
            break

        case _:
            print(f"Error: ingreso una opción inválida, intente de nuevo.")