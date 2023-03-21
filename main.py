from fastapi import FastAPI
import pandas as pd
#from coneccion import consul
from typing import Optional
import uvicorn


app=FastAPI(title="Api de consultas en Plataformas striming",
            description="Esta Api realiza cosultas en las plataformas Amazon,Hulu, Netflix y Disney",
            version="V1.0")


consul=pd.read_csv("DataPlataformas.csv",sep=";")


# introduccion
@app.get("/")
def presentacion():
    return {"PI 01 - Cristian Andres Contreras"}

@app.get("/contacto")
def contacto():
    return "Email: cristos34_9@hotmail.com / Github: cristos34"

#1) Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN.
@app.get("/get_max_duration/{year}/{plataforma}/{duration_type}")
def get_max_duration(year: Optional[int] = None, plataforma: Optional[str] = None, duration_type: Optional[str] = 'min'):
    #Lectura de la base de datos:
    

    # Verificar que la plataforma sea una de las opciones válidas
    if plataforma is not None and plataforma.lower() not in ['disney', 'amazon', 'hulu', 'netflix']:
        raise ValueError("opciones válidas: Disney, Amazon, Hulu o Netflix.")
    if duration_type is not None and duration_type not in ['min', 'season']:
        return('Los valores validos son: min, season')

   
    peliPlataforma= consul[consul['id'].str.contains(plataforma[0], case= False)]

    #Aplico filtro para el año y e tipo de duracion
    año_duracion= peliPlataforma[(peliPlataforma.release_year == year) & (peliPlataforma.duration_type == duration_type)]
    #Accedo a las columnas y tomo el indice mayor de cada columna
    idmax= año_duracion[['title','duration_int', 'duration_type']].loc[año_duracion.duration_int.idxmax()] 
    #El resultado lo paso a un formato de diccionario
    MayorDuracion= idmax.T.to_dict() 

    return MayorDuracion

#2) Cantidad de películas por plataforma con un puntaje mayor a XX en
#  determinado año (la función debe llamarse get_score_count(platform, scored, year))
@app.get("/Cantidad de películas por plataforma - get_score_count/{plataforma}/{scored}/{release_year}")
def get_score_count(plataforma : str, scored : float, release_year: int):

    # plataformas validas que se pueden elegir 
    if plataforma is not None and plataforma.lower() not in ['disney', 'amazon', 'hulu', 'netflix']:
        raise ValueError("opciones válidas: disney, amazon, hulu o netflix.")
    # seleccionamos las peliculas por año y puntaje especifico
    año_dur = consul[(consul.plataforma == plataforma) & (consul.scored > scored) & (consul.release_year == release_year) & (consul.type == 'movie')]
    # Agrupar por plataforma y contar el número de filas resultantes
    cantPeliPorPLataf = año_dur.groupby('plataforma').size()
     
    return cantPeliPorPLataf.to_dict()

#3) Cantidad de películas por plataforma con filtro de PLATAFORMA. 
# (La función debe llamarse get_count_platform(platform))

@app.get("/Cantidad de películas por plataforma - get_count_platform/{plataforma}")
def get_count_platform(plataforma: str):
   

    # plataformas validas que se pueden elegir 
    if plataforma is not None and plataforma.lower() not in ['disney', 'amazon', 'hulu', 'netflix']:
        raise ValueError("Opciones válidas: disney, amazon, hulu, netflix.")
    #Filtrar las películas para la plataforma
    peli_plat= consul[consul['id'].str.contains(plataforma[0], case= False)]
    #luego hago un conteo del tamaño del filtro que hice
    cant_pelis= len(peli_plat)

    return cant_pelis

#4) Actor que más se repite según plataforma y año. 
# (La función debe llamarse get_actor(platform, year))


@app.get("/actor que más se repite - get_actor(plataforma, year")
def get_actor(plataforma:str,año:int):
    actorMax=consul[(consul["release_year"]==año)&(consul["plataforma"]==plataforma)]["cast"]

    # contamos los el actor que mas se repite y cantidad de apariciones 
    if actorMax.value_counts().index[0]=="sin dato":
        return {actorMax.value_counts().index[0]:actorMax.value_counts()[0].tolist()}
    elif actorMax.value_counts().index[0] != "sin dato":
        return {actorMax.value_counts().index[0]:actorMax.value_counts()[0].tolist()}

#if __name__ == "__main__":
#   uvicorn.run("main:app", host="0.0.0.0", port=8080)
    
#python -m venv venv -- crear el ambiente virtual desde la terminal
#crear el main.py -- crear un archivo en el ambinete virtual
#cd
#.\venv\
#Set-ExecutionPolicy -ExecutionPolicy Remotesigned -Scope process
#.\Scripts\
#.\activate
#cd ..
#uvicorn main:app
#uvicorn main:app --reload  #---> para que quede cocorriendo mientras dse programa
#http://localhost:8000
#http://localhost:8000/docs     