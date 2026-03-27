import os

class Servidor:
    def __init__(self, ip, hostname, os):
        self.ip = ip
        self.hostname = hostname
        self.os = os
        self.estado = "Desconocido"
    
    def verificar_estado(self):
        respuesta = os.system(f"ping -n 1 {self.ip}")

        if respuesta == 0:
            self.estado = "Activo"
        
        else:
            self.estado = "Caido"
            
    def mostrar_info(self):
        print(f"[{self.estado}] {self.hostname} ({self.ip}) - SO: {self.os}")

server_web = Servidor("192.168.1.0","WEB-PROD-01","LINUX")
server_db = Servidor("10.0.0.5","DB-MAIN","Windows Server")

server_db.verificar_estado()
server_web.verificar_estado()

server_db.mostrar_info()
server_web.mostrar_info()

