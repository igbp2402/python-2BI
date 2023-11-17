class Monitor:
    def __init__(self, modelo):
        self.modelo = modelo
        self.conectado_computador = False

    def conectar_computador(self):
        self.conectado_computador = True
        print(f"Monitor {self.modelo} conectado a um computador.")

    def desconectar_computador(self):
        self.conectado_computador = False
        print(f"Monitor {self.modelo} desconectado do computador.")


class Computador:
    def __init__(self, marca):
        self.marca = marca
        self.monitor = None

    def conectar_monitor(self, monitor):
        if isinstance(monitor, Monitor):
            self.monitor = monitor
            monitor.conectar_computador()
            print(f"Computador {self.marca} conectado ao monitor {monitor.modelo}.")
        else:
            print("Erro: Objeto fornecido não é uma instância de Monitor.")

    def desconectar_monitor(self):
        if self.monitor:
            self.monitor.desconectar_computador()
            print(f"Computador {self.marca} desconectado do monitor {self.monitor.modelo}.")
            self.monitor = None
        else:
            print("Erro: Nenhum monitor conectado.")

monitor1 = Monitor("Samsung")
monitor2 = Monitor("LG")

computador1 = Computador("Dell")
computador2 = Computador("HP")

computador1.conectar_monitor(monitor1)
computador2.conectar_monitor(monitor2)

computador1.desconectar_monitor()
