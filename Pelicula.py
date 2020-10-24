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
    idioma = []
    subtitulada = 'no'
    duracion = ''
    year = ''
    resumen = ''
    reparto = []

    def __init__(self, id):
        self.idPelicula = id

    def toString(self):
        cad = 'db.pelicula.insert({\n'
        cad += '\t' + self.getNombre() + ',\n'
        cad += '\t' + self.getFecha() + ',\n'
        cad += '\t' + self.getClasificacion() + ',\n'
        cad += '\t' + self.getGenero() + ',\n'
        cad += '\t' + self.getCasaProductora() + ',\n'
        cad += '\t' + self.getIdioma() + ',\n'
        cad += '\t' + self.getSubitulada() + ',\n'
        cad += '\t' + self.getDuracion() + ',\n'
        cad += '\t' + self.getYear() + ',\n'
        cad += '\t' + self.getResumen() + ',\n'
        cad += '\t' + self.getActores() + '\n'
        cad += '});'
        #print(cad)
        return cad

    def getNombre(self):
        return '"nombre": "' + self.nombre.strip() + '"'

    def getFecha(self):
        return '"fecha": "' + self.fecha.strip() + '"'

    def getClasificacion(self):
        return '"clasificacion": "' + self.clasificacion.strip() + '"'

    def getGenero(self):
        cad = ''
        cont = 0
        size = len(self.generos)
        for item in self.generos:
            if cont == size-1:
                cad += '"' + item.strip() + '"'
            else:
                cad += '"' + item.strip() + '", '
            cont += 1
        return '"genero": [' + cad + ']'

    def getCasaProductora(self):
        cad = ''
        cont = 0
        size = len(self.productores)
        for item in self.productores:
            if cont == size - 1:
                cad += '"' + item.strip() + '"'
            else:
                cad += '"' + item.strip() + '", '
            cont += 1
        return '"casa_productora": [' + cad + ']'

    def getIdioma(self):
        cad = ''
        cont = 0
        size = len(self.idioma)
        for item in self.idioma:
            if cont == size - 1:
                cad += '"' + item.strip() + '"'
            else:
                cad += '"' + item.strip() + '", '
            cont += 1
        return '"idioma": [' + cad + ']'

    def getSubitulada(self):
        return '"subtitulada": "' + self.subtitulada.strip() + '"'

    def getDuracion(self):
        return '"duracion": "' + self.duracion.strip() + '"'

    def getYear(self):
        return '"anio_produccion": ' + self.year.strip()

    def getResumen(self):
        return '"resumen": "' + self.resumen.strip().replace('\n', '') + '"'

    def getActores(self):
        cad = ''
        cont = 0
        size = len(self.reparto)
        for actor in self.reparto:
            if cont == size - 1:
                cad += '\t\t' + actor.toString() + '\n'
            else:
                cad += '\t\t' + actor.toString() + ',\n'
            cont += 1
        return '"actores": [\n' + cad + '\t]'

