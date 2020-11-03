class Persona:
    rol = ''
    nombre = ''
    personaje = ''

    def toString(self):
        return '{ "rol": "' + self.rol.replace('\"', '') + '", "nombre": "' + self.nombre.strip().replace('\"', '') + '" , "personaje": "' + self.personaje.replace('\n', '').strip().replace('\"', '') + '" }'