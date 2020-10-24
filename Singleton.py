class Singleton:
    instance = None

    cadena = ''

    @staticmethod
    def getInstance():
        if Singleton.instance is None:
            Singleton.instance = Singleton()
        return Singleton.instance

    def getCadena(self):
        return self.cadena

    def addCadena(self, cadena):
        self.cadena += cadena + '\n\n'
