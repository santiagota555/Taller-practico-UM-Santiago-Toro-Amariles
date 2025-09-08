class Cliente:
    def __init__(self, cedula, nombre, telefono, tipo_cliente, tipo_atencion, cantidad, prioridad, fecha, valor_cita, valor_atencion, total_pagar):
        self.cedula = cedula
        self.nombre = nombre
        self.telefono = telefono
        self.tipo_cliente = tipo_cliente
        self.tipo_atencion = tipo_atencion
        self.cantidad = cantidad
        self.prioridad = prioridad
        self.fecha = fecha
        self.valor_cita = valor_cita
        self.valor_atencion = valor_atencion
        self.total_pagar = total_pagar

    def __str__(self):
        return f"{self.nombre} - {self.tipo_atencion} - ${self.total_pagar}"

