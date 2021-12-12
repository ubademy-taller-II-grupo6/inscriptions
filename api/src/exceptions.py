class InvalidOperationException(Exception):
    def __init__(self, message: str):
        self.message = "Operación Inválida: " + message

    def __str__(self):
        return self.message