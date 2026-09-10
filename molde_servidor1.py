"""
Archivo original de práctica: Conceptos de Programación Orientada a Objetos en Python.
Demuestra: Clases, Atributos, Instancias, Herencia y Polimorfismo.
"""

import os
import platform

# 'class' define el molde o plantilla para instanciar objetos
class Servidor:
    # El constructor __init__ se ejecuta automáticamente cuando nace un objeto.
    # 'self' en Python hace referencia a la propia instancia del objeto.
    def __init__(self, ip, hostname, os_name):
        self.ip = ip
        self.hostname = hostname
        self.os_name = os_name
        self.estado = "Desconocido"

    def verificar_estado(self):
        # Adaptación multiplataforma para ping
        param = "-n 1" if platform.system().lower() == "windows" else "-c 1"
        respuesta = os.system(f"ping {param} {self.ip} > /dev/null 2>&1")

        if respuesta == 0:
            self.estado = "Activo"
        else:
            self.estado = "Caído"

    def mostrar_info(self):
        print(f"[{self.estado}] {self.hostname} ({self.ip}) - SO: {self.os_name}")


# Clase hija ServidorWeb (Hereda de Servidor)
class ServidorWeb(Servidor):
    def auditar(self):
        print(f"[{self.hostname}] Auditando vulnerabilidades en puertos 80 y 443 de la IP {self.ip}...")


# Clase hija ServidorBaseDeDatos (Hereda de Servidor)
class ServidorBaseDeDatos(Servidor):
    def auditar(self):
        print(f"[{self.hostname}] Auditando inyecciones SQL en puerto 3306 de la IP {self.ip}...")


if __name__ == "__main__":
    print("--- Demostración Básica POO ---")
    mi_web = ServidorWeb("127.0.0.1", "WEB-PROD", "Linux")
    mi_sql = ServidorBaseDeDatos("10.0.0.5", "DB-MAIN", "Windows")

    infraestructura = [mi_web, mi_sql]

    for equipo in infraestructura:
        equipo.verificar_estado()
        equipo.mostrar_info()
        equipo.auditar()
