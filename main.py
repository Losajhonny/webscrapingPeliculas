from bs4 import BeautifulSoup
from Pelicula import *
from Persona import *
from Singleton import *
import requests

pageMain = 'http://www.sensacine.com'
pageMovie = ''
pageReparto = ''

def webScraping():
    noPages = 1

    while noPages < 500:
        if noPages == 1:
            url = 'http://www.sensacine.com/peliculas/mejores/nota-espectadores/'
        else:
            url = 'http://www.sensacine.com/peliculas/mejores/nota-espectadores/?page=' + str(noPages)
        print(url)
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        getMovies(soup)

        if Pelicula.noPelicula > 500:
            break
        noPages += 1

    cadena = Singleton.getInstance().getCadena()
    cadena = "db.pelicula.insertMany([\n" + cadena + "]);"
    with open("peliculas.js", 'w', encoding='utf-8') as f:
        #f = open("peliculas.txt", 'w')
        f.write(cadena)
        f.close()

def getMovies(soup_):
    values = soup_.find_all('div', class_='data_box')

    for value in values:
        pelicula = Pelicula(Pelicula.noPelicula)
        pelicula.url = pageMain + value.find('a').get('href')
        page = requests.get(pelicula.url)
        soup = BeautifulSoup(page.content, 'html.parser')
        getMovie(soup, pelicula)

        pppp = pelicula.toString()
        print(pppp)
        Singleton.getInstance().addCadena(pppp)

        print(Pelicula.noPelicula)

        if Pelicula.noPelicula > 500:
            break

def getMovie(soup_, pelicula):
    meta = soup_.find('div', class_='meta-body')
    pelicula.nombre = soup_.find('div', class_='titlebar-title titlebar-title-lg').text

    item = meta.find('div', class_='meta-body-item meta-body-info')
    info = list(filter(lambda x: x != '' and x != '/', item.text.replace('\n', ' ').split(' ')))
    pelicula.fecha = info[0] + '/' + info[2] + '/' + info[4]
    pelicula.duracion = info[5] + ' ' + info[6]
    pelicula.generos = []

    pos = 7
    while pos < len(info):
        pelicula.generos.append(info[pos])
        pos += 1

    meta = soup_.find('section', class_='section ovw ovw-synopsis')
    info = meta.find('span', class_='certificate-text')

    if info != None:
        pelicula.clasificacion = info.text
    else:
        pelicula.clasificacion = ''

    pelicula.resumen = meta.find('div', class_='content-txt').text

    items = meta.find('div', class_='ovw-synopsis-info').find('div', class_='more-hidden').find_all('div', class_='item')

    for item in items:
        values = item.find_all('span')
        if values[0].text == 'Año de producción':
            pelicula.year = values[1].text
        elif values[0].text == 'Idiomas':
            pelicula.idioma = values[1].text.split(',')
            if len(pelicula.idioma) > 1:
                pelicula.subtitulada = 'si'
            else:
                pelicula.subtitulada = 'no'

    if Pelicula.noPelicula < 250:
        pelicula.year = '2019'
    else:
        pelicula.year = '2020'

    pelicula.urlReparto = pelicula.url + 'reparto/'
    page = requests.get(pelicula.urlReparto)
    soup = BeautifulSoup(page.content, 'html.parser')
    getReparto(soup, pelicula)

def getReparto(soup_, pelicula):
    #section section-wrap gd-2-cols gd-gap-30 row-col-sticky
    #gd gd-gap-15 gd-xs-2 gd-s-4
    #card person-card person-card-col
    try:
        info = soup_.find('section', class_='section section-wrap gd-2-cols gd-gap-30 row-col-sticky')
        values = info.find_all('div', class_='gd gd-gap-15 gd-xs-2 gd-s-4')

        directores = values[0].find_all('div', class_='card person-card person-card-col')
        actores = values[1].find_all('div', class_='card person-card person-card-col')

        values = info.find_all('div', class_='section casting-list')
        values = values[len(values) - 1].find_all('div', class_='gd gd-xs-1 gd-s-2 md-table-row')

        pelicula.productores = []
        pelicula.reparto = []

        for value in values:
            pelicula.productores.append(value.find_all('span')[1].text)

        for director in directores:
            persona = Persona()
            persona.nombre = director.find('a', class_='meta-title-link').text
            persona.rol = 'director'
            pelicula.reparto.append(persona)

        for actor in actores:
            value = actor.find('a', class_='meta-title-link')
            correcto1 = False
            correcto2 = False

            if value != None:
                nombre = value.text
                correcto1 = True

            value = actor.find('div', class_='meta-sub light')
            if value != None:
                personaje = value.text.split(':')[1]
                correcto2 = True

            if correcto1 and correcto2:
                persona = Persona()
                persona.nombre = nombre
                persona.rol = 'actor'
                persona.personaje = personaje
                pelicula.reparto.append(persona)

        Pelicula.noPelicula += 1

    except:
        print('error en una pelicula')

if __name__ == '__main__':
    webScraping()
