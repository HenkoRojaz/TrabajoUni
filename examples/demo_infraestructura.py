"""
Ejemplo de ejecución del sistema de monitoreo y auditoría POO.
"""

import sys
import os

# Permitir importar desde el directorio src
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from src.servidor import Servidor, ServidorWeb, ServidorBaseDeDatos


def main():
    print("=== MONITOREO E INSPECCIÓN DE INFRAESTRUCTURA (POO) ===")

    # Instanciación de objetos especializados
    web_prod = ServidorWeb("127.0.0.1", "WEB-PROD-01", "Linux (Ubuntu)", puerto_web=443)
    db_main = ServidorBaseDeDatos("10.0.0.5", "DB-MAIN-01", "Windows Server", puerto_db=3306)
    gw_router = Servidor("192.168.1.1", "GW-CORE", "Cisco IOS")

    infraestructura = [web_prod, db_main, gw_router]

    print("\n[1] Verificando estado ICMP Ping...")
    for equipo in infraestructura:
        equipo.verificar_estado()
        equipo.mostrar_info()

    print("\n[2] Ejecutando Auditoría Polimórfica de Seguridad...")
    for equipo in infraestructura:
        equipo.auditar()

if __name__ == "__main__":
    main()
