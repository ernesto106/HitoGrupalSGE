class Padre():
    def llevarEscuela(self):
        print("Padre lleva a su hijo a la escuela")


class Madre():
    def hacerComida(self):
        print("Madre hace la comida para su hijo")


# Herencia múltiple: Aquí la clase hijo hereda de dos clases, de la clase Padre y la clase Madre
class Hijo(Padre, Madre):
    def irEscuela(self):
        print("Soy el hijo y quiero mucho a mis padres")


# Esto significa que la clase hijo hereda tanto los metodos del padre como los de la madre, ademas de poder utlizar los suyos propios.
hijo = Hijo()
hijo.llevarEscuela()
hijo.hacerComida()
hijo.irEscuela()
