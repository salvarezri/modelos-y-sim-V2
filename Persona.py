import random
class Persona():
    contador_persona = 0

    @classmethod
    def contadorPersonas(cls):
        cls.contador_persona +=1
        return cls.contador_persona

    def __init__(self, dosis, idPersona):
        self.idPersona = idPersona
        self.dosis = dosis
        # estado = 0 -> sano ; estado = 1 -> infectado
        self.estado = 0
        # último día en el que se contagió
        self.diaContagio = 0
        self.tiempoRecuperación = 0

    def calcularContagio(self, probabilidad, dia, tiempoRec) -> bool:
        # si esta contagiado no se puede volver a contagiar
        if self.estado == 1:
            # restar días hasta la recuperación
            self.tiempoRecuperación -=1
            # comprobar que ya pasó el tiempo de recuperación
            if self.tiempoRecuperación == 0:
                # la persona se recuperó
                self.estado = 0
            return False
        # calcula la probabilidad de contagio según la dosis y el grupo(probabilidad)
        probabilidad = probabilidad/self.dosis
        # se escoge un numero aleatorio entre 0 y 1.
        # Si el número es menor o igual a la probabilidad de que una persona este contagiada,
        # esta persona se contagia
        num = random.random()
        if num < probabilidad:
            # actualiza el estado, el último día de contagio y el periodo para rla recuperación
            self.estado = 1
            self.diaContagio = dia
            self.tiempoRecuperación = tiempoRec
            return True
        else:
            return False

    def __str__(self):
        return f'Persona[ID: {self.idPersona}, Dosis: {self._dosis}, Posibilidad: {self._posibilidad}]'