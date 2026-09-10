# 🖥️ TrabajoUni: Estructura de Datos y POO Aplicada a Ciberseguridad & SysAdmin

Este repositorio contiene proyectos y prácticas universitarias de la materia **Estructura de Datos (AED-1026)** e **Ingeniería en Sistemas Computacionales**, enfocados en la aplicación práctica de la **Programación Orientada a Objetos (POO)** para la administración de servidores, monitoreo de redes y auditoría de ciberseguridad.

---

## 📌 Estructura del Repositorio

```text
TrabajoUni/
├── src/
│   └── servidor.py                # Módulo principal con clases POO (Servidor, ServidorWeb, ServidorBaseDeDatos)
├── examples/
│   └── demo_infraestructura.py     # Script demostrativo de monitoreo y auditoría polimórfica
├── molde_servidor1.py              # Script inicial de práctica y conceptos clave
├── .gitignore                      # Exclusiones estándar para Python/IDE
└── README.md                       # Documentación del proyecto
```

---

## 🚀 Conceptos de POO Implementados

1. **Clases y Objetos (Instanciación)**: Uso del método constructor `__init__` y `self` para definir atributos específicos de cada servidor (`ip`, `hostname`, `os_name`, `estado`).
2. **Encapsulamiento y Métodos**: Métodos como `verificar_estado()` que ejecutan comprobaciones ICMP Ping adaptadas multiplataforma (Linux/Windows).
3. **Herencia**: Creación de clases especializadas (`ServidorWeb`, `ServidorBaseDeDatos`) a partir de la clase base `Servidor`.
4. **Polimorfismo**: Sobreescritura del método `auditar()` para ejecutar tareas de seguridad específicas según el rol del equipo (escaneo web vs. auditoría de motor SQL).

---

## 🛠️ Instrucciones de Ejecución

Para ejecutar la demostración de infraestructura:

```bash
# Clonar el repositorio
git clone git@github.com:HenkoRojaz/TrabajoUni.git
cd TrabajoUni

# Ejecutar el demo estructurado
python3 examples/demo_infraestructura.py

# O ejecutar el script práctico original
python3 molde_servidor1.py
```

---

## 👨💻 Autor

- **Mario Eduardo Rojas Nájera** (Estudiante de Ingeniería en Sistemas Computacionales - TecNM SLP)
- GitHub: [@HenkoRojaz](https://github.com/HenkoRojaz)
