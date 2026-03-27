class Servidor:
    def __init__(self, ip, hostname, os):
        self.ip = ip
        self.hostname = hostname
        self.os = os
        self.estado = "Desconocido"
    
    def mostrar_info(self):
        print(f"[{self.estado}] {self.hostname} ({self.ip}) - SO: {self.os}")

server_web = Servidor("192.168.1.0","WEB-PROD-01","LINUX")
server_db = Servidor("10.0.0.5","DB-MAIN","Windows Server")

server_db.mostrar_info()
server_web.mostrar_info()