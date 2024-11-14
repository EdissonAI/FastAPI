from fastapi import FastAPI 
from fastapi.responses import HTMLResponse
app = FastAPI() #Crea una instancia de la clase FastAPI 
app.title = "My Favorite Rock Songs"
app.version = "0.0.1"

Songs_List = [
    {
        "ID": 1,
        "Title": "Love Gun",
        "Artist": "Kiss",
        "Álbum": "Track número 6 del sexto álbum de estudio de la banda estadounidense Kiss, titulado Love Gun",
        "Year": 1977,
        "Rating": 9,
    },
    {
        "ID": 2,
        "Title": "Barracuda",
        "Artist": "Heart",
        "Álbum": "Track número 1 del álbum de estudio de la banda estadounidense Heart, tituladoLittle Queen",
        "Year": 1977,
        "Rating": 9,
    },
    {
        "ID": 3,
        "Title": "Crazy Train",
        "Artist": "Ozzy Osbourne",
        "Álbum": "Track número 2 del álbum debut del músico y compositor británico Ozzy Osbourne, tituladoBlizzard of Ozz",
        "Year": 1980,
        "Rating": 10,
    },
    {
        "ID": 4,
        "Title": "Paranoid",
        "Artist": "Black Sabbath",
        "Álbum": "Track número 2 del segundo álbum de estudio de la banda británica Black Sabbath, titulado Paranoid",
        "Year": 1970,
        "Rating": 9.5,
    },
    {
        "ID": 5,
        "Title": "More than a felling",
        "Artist": "Boston",
        "Álbum": "Track número 1 del álbum debut de la banda estadounidense Boston, titulado Boston",
        "Year": 1976,
        "Rating": 9,
    },
    {
        "ID": 6,
        "Title": "Separate Ways",
        "Artist": "Journey",
        "Álbum": "Track número 1 del octavo álbum de estudio de la banda estadounidense Journey, titulado Frontiers",
        "Year": 1983,
        "Rating": 9.3,
    },
    {
        "ID": 7,
        "Title": "Dont stop believing",
        "Artist": "Journey",
        "Álbum": "Track número 1 del septimo álbum de estudio de la banda estadounidense Journey, titulado Escape",
        "Year": 1981,
        "Rating": 9,
    },
    {
        "ID": 8,
        "Title": "I was made for loving you",
        "Artist": "Kiss",
        "Álbum": "Track número 1 del septimo álbum de estudio de la banda estadounidense Kiss, titulado Dynasty",
        "Year": 1979,
        "Rating": 9.6,
    },
    {
        "ID": 9,
        "Title": "Living on a prayer",
        "Artist": "Bon Jovi",
        "Álbum": "Track número 3 del tercer álbum de estudio de la banda estadounidense Bon Jovi, titulado Slippery When Wet",
        "Year": 1986,
        "Rating": 8.9,
    },
    {
        "ID": 10,
        "Title": "Bohemian Rhapsody",
        "Artist": "Queen",
        "Álbum": "Track número 11 del cuarto álbum de estudio de la banda británica Queen, titulado A Night at the Opera",
        "Year": 1976,
        "Rating": 9.8,
    }
]
@app.get('/', tags=["Home"])#Definimos una ruta
def message(): # Definimos una función de la ruta
    return HTMLResponse ('<h1>Hola Maundo</h1>') # Devolvemos un string en la respuesta de la ruta
@app.get('/Songs', tags=["Songs List"]) #Definimos una ruta de la clase FastAPI
def Songs(): 
    return Songs_List
@app.get('/Songs/{ID}', tags=["Songs Search"])#Definimos una ruta de la clase FastAPI
def get_Song(ID: int):
    for item in Songs_List:
        if item['ID'] == ID:
            return item
    return []