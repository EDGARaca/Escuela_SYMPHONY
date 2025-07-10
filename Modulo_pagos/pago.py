class Pago:
    TIPOS_VALIDOS = ["obligacion_escuela", "nomina", "mensualidad", "inscripcion"]

    def __init__(self, pago_id, tipo, monto, fecha, metodo, pagador_id, nombre_pagador):
        if tipo not in self.TIPOS_VALIDOS:
            raise ValueError(f"Tipo de pago inválido: {tipo}. Debe ser uno de {self.TIPOS_VALIDOS}")

        self.pago_id = pago_id
        self.tipo = tipo
        self.monto = monto
        self.fecha = fecha
        self.metodo = metodo
        self.pagador_id = pagador_id
        self.nombre_pagador = nombre_pagador

    def generar_recibo(self):
        return (
            f"[RECIBO #{self.pago_id}] {self.tipo.upper()} de ${self.monto} COP\n"
            f"Pagado por: {self.nombre_pagador} (ID: {self.pagador_id})\n"
            f"Fecha: {self.fecha}\n"
            f"Método: {self.metodo}"
        )