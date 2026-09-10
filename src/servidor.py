"""
Módulo de Monitoreo e Inspección de Servidores utilizando Programación Orientada a Objetos (POO).
Demuestra conceptos de Herencia, Encapsulamiento y Polimorfismo aplicados a SysAdmin y Ciberseguridad.
"""

import os
import platform


class Servidor:
    """Clase base (molde) que representa un servidor genérico dentro de la infraestructura."""

    def __init__(self, ip: str, hostname: str, os_name: str):
        self.ip = ip
        self.hostname = hostname
        self.os_name = os_name
        self.estado = "Desconocido"

    def verificar_estado(self) -> str:
        """Verifica la conectividad mediante ICMP Ping adaptado al Sistema Operativo host."""
        param = "-n 1" if platform.system().lower() == "windows" else "-c 1"
        # Redirigir stdout/stderr para mantener la consola limpia
        cmd = f"ping {param} {self.ip} > /dev/null 2>&1"
        if platform.system().lower() == "windows":
            cmd = f"ping {param} {self.ip} > nul 2>&1"

        respuesta = os.system(cmd)
        if respuesta == 0:
            self.estado = "Activo"
        else:
            self.estado = "Caído"
        return self.estado

    def mostrar_info(self):
        """Muestra en pantalla el estado actual y especificaciones del equipo."""
        print(f"[{self.estado}] {self.hostname} ({self.ip}) - SO: {self.os_name}")

    def auditar(self):
        """Método base para auditoría de seguridad (a ser sobreescrito por clases hijas)."""
        print(f"[{self.hostname}] Realizando inspección base en IP {self.ip}...")


class ServidorWeb(Servidor):
    """Clase especializada para servidores Web (Hereda de Servidor)."""

    def __init__(self, ip: str, hostname: str, os_name: str, puerto_web: int = 443):
        super().__init__(ip, hostname, os_name)
        self.puerto_web = puerto_web

    def auditar(self):
        """Polimorfismo: Inspección específica para servicios web (HTTP/HTTPS)."""
        print(
            f"[{self.hostname}] Auditando vulnerabilidades web en puertos 80 y {self.puerto_web} (IP: {self.ip})..."
        )


class ServidorBaseDeDatos(Servidor):
    """Clase especializada para servidores de Base de Datos (Hereda de Servidor)."""

    def __init__(self, ip: str, hostname: str, os_name: str, puerto_db: int = 3306):
        super().__init__(ip, hostname, os_name)
        self.puerto_db = puerto_db

    def auditar(self):
        """Polimorfismo: Inspección específica para motores de base de datos (SQL Injection, puertos)."""
        print(
            f"[{self.hostname}] Auditando seguridad en motor de BD en puerto {self.puerto_db} (IP: {self.ip})..."
        )
