from tarifas import tarifas
from cliente import Cliente
from datetime import datetime

clientes = []
tipos_cliente = ["Particular", "EPS", "Prepagada"]
tipos_atencion = ["Limpieza", "Calzas", "Extracción", "Diagnóstico"]
prioridades = ["Normal", "Urgente"]

def seleccionar_opcion(lista, mensaje):
    print(mensaje)
    for i, opcion in enumerate(lista, start=1):
        print(f"{i}. {opcion}")
    while True:
        try:
            eleccion = int(input("Seleccione una opción: "))
            if 1 <= eleccion <= len(lista):
                return lista[eleccion - 1]
            else:
                print("Número inválido. Intente de nuevo.")
        except ValueError:
            print("Debe ingresar un número válido.")
def pedir_cedula():
    while True:
        cedula = input("Cédula: ")
        if cedula.isdigit() and len(cedula) >= 6:
            return cedula
        else:
            print("La cedula debe contener solo números y tener al menos 6 dígitos.")
def pedir_telefono():
    while True:
        telefono = input("Teléfono: ")
        if telefono.isdigit() and len(telefono) == 10:
            return telefono
        else:
            print("El teléfono debe contener solo números y tener exactamente 10 dígitos.")
def pedir_fecha():
    while True:
        fecha = input("Fecha de la cita (dd/mm/aaaa): ")
        try:
            datetime.strptime(fecha, "%d/%m/%Y")
            return fecha
        except ValueError:
            print("Fecha inválida. Debe ser en formato dd/mm/aaaa.")
def registrar_cliente():
    cedula = pedir_cedula()
    nombre = input("Nombre: ")
    telefono = pedir_telefono()

    tipo_cliente = seleccionar_opcion(tipos_cliente, "\nTipos de Cliente:")
    tipo_atencion = seleccionar_opcion(tipos_atencion, "\nTipos de Atención:")

    if tipo_atencion in ["Limpieza", "Diagnóstico"]:
        cantidad = 1
    else:
        while True:
            try:
                cantidad = int(input("Cantidad (para calzas o extracciones): "))
                if cantidad > 0:
                    break
                else:
                    print("Debe ser mayor a 0.")
            except ValueError:
                print("Debe ingresar un número válido.")

    prioridad = seleccionar_opcion(prioridades, "\nPrioridad de atención:")
    fecha = pedir_fecha()

    valor_cita = tarifas[tipo_cliente]["valor_cita"]
    valor_atencion = tarifas[tipo_cliente]["atenciones"][tipo_atencion] * cantidad
    total_pagar = valor_cita + valor_atencion

    cliente = Cliente(cedula, nombre, telefono, tipo_cliente, tipo_atencion, cantidad, prioridad, fecha, valor_cita, valor_atencion, total_pagar)
    clientes.append(cliente)

    print(f"\n Cliente {nombre} registrado con exito. Total a pagar: ${total_pagar}\n")
def estadisticas():
    total_clientes = len(clientes)
    ingresos_totales = sum(c.total_pagar for c in clientes)

    conteo_atenciones = {
        "Limpieza": 0,
        "Calzas": 0,
        "Extracción": 0,
        "Diagnóstico": 0
    }

    for c in clientes:
        if c.tipo_atencion in conteo_atenciones:
            conteo_atenciones[c.tipo_atencion] += 1

    print("\nESTADISTICAS")
    print(f"Total de clientes: {total_clientes}")
    print(f"Ingresos totales: ${ingresos_totales}")

    print("\nClientes por tipo de atencion:")
    for tipo, cantidad in conteo_atenciones.items():
        print(f"- {tipo}: {cantidad}")
def ordenar_clientes():
    lista_ordenada = sorted(clientes, key=lambda x: x.valor_atencion, reverse=True)

    print("\n***** CLIENTES ORDENADOS POR VALOR DE ATENCIÓN *****")
    for c in lista_ordenada:
        print(f"Cédula: {c.cedula}, Nombre: {c.nombre}, Tipo de Cliente: {c.tipo_cliente}, "
              f"Atención: {c.tipo_atencion}, Cantidad: {c.cantidad}, Total: ${c.total_pagar}\n")

    return lista_ordenada
def buscar_cliente(cedula):
    lista_ordenada = ordenar_clientes()
    for cliente in lista_ordenada:
        if cliente.cedula == cedula:
            return cliente
    return None
