# Estacionamiento

API REST en **Flask** para gestionar el ingreso y salida de motos de un parqueadero, calculando el tiempo y el costo a pagar.

## Estructura

- `main.py` — punto de entrada, arranca el servidor Flask.
- `app/routes/parqueadero_routes.py` — endpoints HTTP.
- `app/services/parqueadero_service.py` — lógica de negocio (registrar ingreso, calcular cobro al salir, listar motos activas). El estado se guarda en memoria.
- `app/models/registro.py` — modelo `RegistroMoto` (placa, hora de ingreso/salida, total a pagar).
- `app/config.py` — tarifas configurables (`TARIFA_POR_MINUTO`, `TARIFA_MINIMA`).

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| `POST` | `/ingreso` | Registra el ingreso de una moto (`{"placa": "ABC123"}`). |
| `POST` | `/salida` | Procesa la salida y devuelve la factura con minutos cobrados y total. |
| `GET` | `/motos` | Lista las motos actualmente dentro del parqueadero. |

## Ejecución

```bash
python -m venv .venv
source .venv/bin/activate  # en Windows: .venv\Scripts\activate
pip install -r requerimients.txt
python main.py
```

El servidor queda disponible en `http://localhost:5000`.
