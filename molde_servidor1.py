import os

#class hace referencia al molde o plano que se usara para los objetos
class Servidor:
    #El consteructor __init__ Es un metodo especial que se ejecuta automaticamente cuando "Nace" un objeto
    #Una vez establecido el __init__ se crean los atributos (Variables que pertenecen a ese objeto)
    #self en Python significa "yo mismo". Se usa dentro del molde para que el objeto sepa que guarda sus propios datos
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

#Es la cosa creada a partir del molde
server_web = Servidor("192.168.1.0","WEB-PROD-01","LINUX")
server_db = Servidor("10.0.0.5","DB-MAIN","Windows Server")

server_db.verificar_estado()
server_web.verificar_estado()

server_db.mostrar_info()
server_web.mostrar_info()

#Se crea la clase hija SERVIDOR WEB.
#Para heredar los atributos 
class ServidorWeb(Servidor):
    def auditar_web(self):
        print(f"[{self.hostname}] Auditando vulnerabilidades en puertos  80 y 443 de la IP {self.ip}...")

server_web = ServidorWeb("192.168.1.10","WEB-PROD-01", "Linux")

server_web.verificar_estado()
server_web.mostrar_info()
server_web.auditar_web()
