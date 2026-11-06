# Modelo de datos (Moto / Ticket)
from datetime import datetime

class RegistroMoto:
    def __init__(self, placa: str, hora_ingreso: datetime = None):
        self.placa = placa.upper().strip()
        self.hora_ingreso = hora_ingreso or datetime.now()
        self.hora_salida = None
        self.total_a_pagar = 0.0

    def to_dict(self):
        return {
            "placa": self.placa,
            "hora_ingreso": self.hora_ingreso.isoformat(),
            "hora_salida": self.hora_salida.isoformat() if self.hora_salida else None,
            "total_a_pagar": self.total_a_pagar
        }