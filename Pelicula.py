from Persona import *

class Pelicula:

    noPelicula = 0
    idPelicula = 0

    url = ''
    urlReparto = ''

    nombre = ''
    fecha = ''
    clasificacion = ''
    generos = []
    productores = []
    idioma = ''
    subtitulada = 'no'
    duracion = ''
    year = ''
    resumen = ''
    reparto = []

    def __init__(self, id):
        self.idPelicula = id

    def listPersona(self):
        for person in self.reparto:
            print(person.nombre)
