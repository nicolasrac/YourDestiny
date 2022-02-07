#Usamos el atributo supervevencia. Según las decisiones, este puede aumentar o disminuir, de ahí la lógica del juego
class Personaje:
    def __init__(self):
        self.supervivencia = 0

    def obtenerEstado(self):
        return 'Supervivencia: ' + str(self.supervivencia)

