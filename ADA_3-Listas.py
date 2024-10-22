"""
Created on Monday 21/10/24

@author: Victor Mendoza
"""
class Resposteria: # Se crea la clase "Reposteria"
    def __init__(self): # Se inicializan las listas
        self.POSTRES = []
        self.INGREDIENTES = []

    def insertar_postres(self): # Método para ingresar los postres
        while True:
            P = input("\nIngrese un postre: ")
            self.POSTRES.append(P)
            self.POSTRES.sort()

            Resp = input("\n¿Desea ingresar otro postre? (Si/No) ").lower()

            if Resp != "si":
                print("\nLa lista de postres es:\n",self.POSTRES)
                break
    
    def ingresar_ingredientes(self): # Método para ingresar los ingredientes de los postres
        for i in range(len(self.POSTRES)):
            I = input(f"\nIngrese los ingresdintes del postre '{self.POSTRES[i]}' separado por espacios: ").split()
            self.IN = [str(num) for num in I]
            self.INGREDIENTES.append(self.IN)

    def imprimir_ingredientes(self): # Método para imprimir los ingredientes de los postres
        Postre = input("\nIngrese el nombre de un postre de la lista: ")

        if Postre in self.POSTRES:
            indice = self.POSTRES.index(Postre)

            print("Los ingredientes del postre son:",self.INGREDIENTES[indice])

        Resp = input("\n¿Desea ingresar otro nombre de postre? (Si/No) ").lower()

        if Resp == "si":
            self.imprimir_ingredientes() # Llamada recursiva del método

    def ingresar_nuevo_ingrediente(self): # Método para ingresar un nuevo ingrediente a los postres
        Postre = input("\nIngrese el nombre de un postre de la lista: ")

        if Postre in self.POSTRES:
            indice = self.POSTRES.index(Postre)
            Nuevo_ingrediente = input("Ingrese un nuevo ingrediente para el postre: ")
            self.INGREDIENTES[indice].append(Nuevo_ingrediente)

            print(f"\nLa nueva lista de ingredientes para {Postre} es:\n",self.INGREDIENTES[indice])

        self.eliminar_elementos_repetidos()

        Resp = input("\n¿Desea ingresar otro ingrediente a un postre? (Si/No) ").lower()

        if Resp == "si":
            self.ingresar_nuevo_ingrediente() # Llamada recursiva del método

    def eliminar_ingrediente(self): # Método para eliminar un ingrediente de un postre
        Postre = input("\nIngrese el nombre de un postre de la lista: ")

        if Postre in self.POSTRES:
            indice = self.POSTRES.index(Postre)
            Eliminar_ingrediente = input("Ingrese el ingrediente que quiere eliminar del postre: ")
            self.INGREDIENTES[indice].remove(Eliminar_ingrediente)

            print(f"\nLa nueva lista de ingredientes para {Postre} es:\n",self.INGREDIENTES[indice])

        Resp = input("\n¿Desea eliminar otro ingrediente de un postre? (Si/No) ").lower()

        if Resp == "si":
            self.eliminar_ingrediente() # Llamada recursiva del método

    def insertar_nuevo_postre(self): # Método para ingresar nuevos postres y sus ingredientes
        P = input("\nIngrese un postre: ")
        self.POSTRES.append(P)

        I = input(f"\nIngrese los ingresdintes del postre {P} separado por espacios: ").split()
        self.IN = [str(num) for num in I]
        self.INGREDIENTES.append(self.IN)

        print("\nLa lista nueva de postres es:\n", self.POSTRES)
        print("\nLa nueva lista de ingredientes es:\n",self.INGREDIENTES)

        self.eliminar_elementos_repetidos()

        Resp = input("\n¿Desea ingresar otro postre con sus ingredientes? (Si/No) ").lower()

        if Resp == "si":
            self.insertar_nuevo_postre() # Llamada recursiva del método

    def eliminar_postre(self): # Método para eliminar un postre y sus ingredientes
        Postre = input("\nIngrese el nombre de un postre de la lista: ")

        if Postre in self.POSTRES:
            indice = self.POSTRES.index(Postre)
            self.POSTRES.pop(indice)
            self.INGREDIENTES.pop(indice)

            print("\nLa lista nueva de postres es:\n", self.POSTRES)
            print("\nLa nueva lista de ingredientes es:\n",self.INGREDIENTES)
            
        Resp = input("\n¿Desea eliminar otro postre con sus ingredientes? (Si/No) ").lower()
        
        if Resp == "si":
            self.eliminar_postre() # Llamada recursiva del método

    def eliminar_elementos_repetidos(self): # Subprograma para eliminar ingredientes repetidos
        ingredientes_vistos = set()
    
        for i in range(len(self.INGREDIENTES)):
            ingredientes_unicos = []
            for ingrediente in self.INGREDIENTES[i]:
                if ingrediente not in ingredientes_vistos:
                    ingredientes_unicos.append(ingrediente)
                    ingredientes_vistos.add(ingrediente)
            self.INGREDIENTES[i] = ingredientes_unicos

        print("\nLista de ingredientes actualizada sin repetidos:\n", self.INGREDIENTES)

R = Resposteria() # Se crea el objeto de la clase "Resposteria"

def menu(): # Función menu para usar los métodos de la clase "Respoteria"
    while True:
        print("-----------------Menú de la reposteria------------------")
        print("1. Insertar postres")
        print("2. Ingresar los ingredientes de cada postre")
        print("3. Imprimir los ingredientes de un postre en específico")
        print("4. Ingresar nuevos ingredientes a un postre")
        print("5. Eliminar ingredintes de un postre")
        print("6. Insertar nuevos postres con sus ingredientes")
        print("7. Eliminar un postre con sus ingredintes")
        print("8. Salir")
        print("--------------------------------------------------------")

        opcion = input("Ingrese la opción que desea usar: ") # Varibale para seleccionar la opción a usar

        if opcion == "1":
            R.insertar_postres()
        elif opcion == "2":
            R.ingresar_ingredientes()
        elif opcion == "3":
            R.imprimir_ingredientes()
        elif opcion == "4":
            R.ingresar_nuevo_ingrediente()
        elif opcion == "5":
            R.eliminar_ingrediente()
        elif opcion == "6":
            R.insertar_nuevo_postre()
        elif opcion == "7":
            R.eliminar_postre()
        elif opcion == "8":
            print("Saliendo del programa")
            exit()
        else:
            print("\nOpción no válida, por favor intente de nuevo") # Mensaje de error

menu() # Se llama a la función