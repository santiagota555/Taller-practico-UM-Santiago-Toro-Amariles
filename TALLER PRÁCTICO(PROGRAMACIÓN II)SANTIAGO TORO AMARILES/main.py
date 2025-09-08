from funciones import registrar_cliente, estadisticas, ordenar_clientes, buscar_cliente

def menu():
    while True:



        print("\nTALLER PRACTICO UNIVERCIDAD DE MANIZALES POR SANTIAGO TORO AMARILES")
        print("\n")    
        print("MENU PRINCIPAL")
        print("1.Registrar cliente")
        print("2.Ver estadísticas")
        print("3.Ver clientes ordenados por valor de atencion")
        print("4.Buscar cliente por cédula")
        print("5.Salir")
      

        opcion = input("Seleccione una opciOn por favor:")

        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            estadisticas()
        elif opcion == "3":
             ordenar_clientes()
        elif opcion == "4":
            cedula = input("Ingrese la cédula de ciudadania a buscar: ")
            cliente = buscar_cliente(cedula)
            if cliente:
                print("Cliente encontrado:")
                print(f"Nombre: {cliente.nombre}")
                print(f"Teléfono: {cliente.telefono}")
                print(f"Tipo: {cliente.tipo_cliente}")
                print(f"Atención: {cliente.tipo_atencion}")
                print(f"Total a pagar: ${cliente.total_pagar}")
            else:
                print("Cliente no se encuentra en la base de datos por favor revise el numero de cedula.")
        elif opcion == "5":
            print("Saliendo del programa (gracias por su tiempo que tenga buen dia)...")
            break
        else:
            print("esa opcion es invalida revise bien el menu de opciones.")

if __name__ == "__main__":
    menu()
