# Reglas de negocio y cálculos
import math
from datetime import datetime
from app.models.registro import RegistroMoto
from app.config import Config

class ParqueaderoService:
    def __init__(self):
        # Almacenamiento en memoria (se puede reemplazar fácilmente por DB)
        self._motos_activas = {}

    def ingresar_moto(self, placa: str) -> dict:
        placa_clean = placa.upper().strip()
        if placa_clean in self._motos_activas:
            raise ValueError(f"La moto con placa {placa_clean} ya está dentro del parqueadero.")
        
        nuevo_registro = RegistroMoto(placa_clean)
        self._motos_activas[placa_clean] = nuevo_registro
        return nuevo_registro.to_dict()

    def procesar_salida(self, placa: str) -> dict:
        placa_clean = placa.upper().strip()
        if placa_clean not in self._motos_activas:
            raise KeyError(f"La moto {placa_clean} no se encuentra registrada.")

        registro = self._motos_activas.pop(placa_clean)
        registro.hora_salida = datetime.now()

        # Cálculo de tiempo transcurrido
        diferencia = registro.hora_salida - registro.hora_ingreso
        minutos_totales = math.ceil(diferencia.total_seconds() / 60)

        # Cálculo del costo
        subtotal = minutos_totales * Config.TARIFA_POR_MINUTO
        registro.total_a_pagar = max(subtotal, Config.TARIFA_MINIMA)

        resultado = registro.to_dict()
        resultado["minutos_cobrados"] = minutos_totales
        return resultado

    def listar_motos(self) -> list:
        return [moto.to_dict() for moto in self._motos_activas.values()]

# Instancia singleton para compartir estado durante la ejecución del servidor
parqueadero_service = ParqueaderoService()