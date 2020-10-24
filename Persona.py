class Persona:
    rol = ''
    nombre = ''
    personaje = ''

    def toString(self):
        return '{ "rol": "' + self.rol + '", "nombre": "' + self.nombre.strip() + '" , "personaje": "' + self.personaje.replace('\n', '').strip() + '" }'