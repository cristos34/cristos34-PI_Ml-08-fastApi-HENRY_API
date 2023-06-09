<p align=center><img src=https://assets.soyhenry.com/logos/LOGO-HENRY-04.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Data Engineering`**</h1>
*Cristian Andres Contreras*

*Negociante internacional*

*Data Sciencie(In progress)*
<p align="center">
<img src="https://cosasdedevs.com/media/sections/images/fastapi.png"height=180>
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1k9eb0ZrfvW_VQoiim4y4NBPnvQXmCGQbMw&usqp=CAU"  height=100>
</p>

<hr>  


# <h2 align=center>**`Extarcion Transformacion y Carga (ETL)`**</h2>



<p align="center">
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXVWET0vYFMDJn92VOuXpkONKjS4F-KamSBQ&usqp=CAU"height=120>
<img src=""  height=180>
</p>


<hr>

Este trabajo esta basado en realizar un proceso de extracción transformación y carga (ETL) con diversos dataset, con la fin de entregar datos estandarizados y de buena calidad (limpios) que puedan ser procesados por nuestra Application Programming Interface (API), la cual va estar trabajando desde un modo de producción desde un servidor llamado Render.

API, Una API o interfaz de programación de aplicaciones, con un protocolo que se usa para diseñar e integrar el software de las aplicaciones.
Es una herramienta muy versátil y fundamental para la creación de app web, sitios estáticos entre otras formas de uso, esta permite realizar una sinnúmero de operaciones para vincular con una plataforma Web.

Hoy en día contamos con **FastAPI** y **Flask** entre muchas otras, son framework modernos y de alto rendimiento para construir APIs con Python.
<p align=center>
<img src = "https://tekla.io/wp-content/uploads/2022/06/QueEsAPIRest-Recurso-01.jpg" height=250><p>

<hr>

## **Tecnologías**

Para la elboración de este proyecto se utilizaron las siguiente tecnologías:

* Fastapi
* Visual studio code
* Jupyter
* Python
* Pandas
* Uvicorn
* Render
<hr>

## **Pasos para la elaboración del proyecto**


<p align=center>
<img src = 'https://images.jifo.co/53775302_1581003928973.jpg' height=250><p>

**1.** **EDA** 

Se realiza un analisis exploratorio con el objetivo de verificar el estado los datos de entrada, para lograr detallar que están cargados correctamente, lo cual permite poder tomar decisiones en la limpieza de estos; los archivos orginales fueron suministrados en formato *csv*, estos se cargaron de la siguiente manera:

Para visualizar la limpieza completa se pueden remitir a [Limpieza y extacion](https://github.com/cristos34/cristos34-PI_Ml-fastApi-HENRY_API/blob/cafca497c31cff8e8e1d2db426e657899d49f769/Proyecto_PI_ETL_Uno.ipynb).


## **2.** **Creación de la API**

Para crear la API se utilizó el framework [FasAPI](https://fastapi.tiangolo.com/), que está catalogado en el momento como el frameworkde más alto procesamiento y de mayor facilidad de uso.
            
La API llamanda **platafomas-streaming** permite conocer diferentes datos de las platafromas Amazon, Hulu, Diney, Netflix, está se trabajó en un archivo llamado **main.py** y se inició de la siguiente manera:

Para ver el código completo donde están todas las funciones que de la API se pueden remitir a [main.py](https://github.com/cristos34/cristos34-PI_Ml-fastApi-HENRY_API/blob/37c7c0c8b08fd7c52ff687ea97fd46c417a0991f/main.py).
            
Tambien se una API con el framework [Flask]([https://fastapi.tiangolo.com/](https://flask.palletsprojects.com/en/2.2.x/)), que está catalogado tambien como un framework con mucha facilidad para trabajar pandas y muchas otras bases de datos, ademas que resta mauchos de los servicios que presta FastApi.
            
La API, llamada  **mainFlask** permite conocer diferentes datos de las plataformas  Amazon, Hulu, Disney, Netflix, esta se trabajó en un archivo llamado **mainFlask.py** y pero no se le pudo hacer el deploying debido a que no se encontró información que sirviera de guía y que funcionaran sus pasos.

Para ver el código completo donde están todas las funciones de esta API se pueden remitir a [mainFlask.py](https://github.com/cristos34/PI-Flask-app-Plataforrmas/blob/01070124cf76e0849ccfaffbafd719161ddadd27/mainFlask.py).



app=FastAPI(title="Api de consultas en Plataformas striming",
            description="Esta Api realiza cosultas en las plataformas Amazon,Hulu, Netflix y Disney",
            version="V1.0")

* Datos para requiremensts.txt :
```Python
     * pip
     * fastapi
     * pandas
     * typing
     * uvicorn
```
## **2.1** **Pasos para crear el ambiente virtual**

* Crear el ambiente virtual desde la terminal con la siguiente línea de código nombre de la carpeta venvv, pero antes nos ubicamos en la carpeta raíz.
            
            **python -m venv venvv** 
           
* Creamos un archivo principal, normalmente llamado Main.py o App.py
           
             ** main.py** 
            
* Nos dirijimos a la carpeta \venvv\ con el comando cd y tab
            
            **cd + tab**
            **.\venvv\**
            
* Copiamos la siguiente línea de código y la pegamos en la ruta de \ven
            
            **Set-ExecutionPolicy -ExecutionPolicy Remotesigned -Scope process**
            
* Nos dirijimos a la carpeta \Scripts\ con el comando cd y tab
            
            **cd + tab**
                        
* Copiamos la siguiente línea de código y la pegamos en la ruta de \Scrip
            
            **\activate**
            
* Nos dirijimos a la carpeta raíz, ósea que salimos de \venvv\ y \Scripts\  con el comando cd espacio 2 puntos cd ..
            
            **cd ..**
            **cd ..**
            
* Creamos un archivo llamado .gitignore, con el fin que ignorar el ambiente virtual cuando se suba al GitHub, dentro debe tener el nombre del ambiente virtual más el  /            
           ``` Venvv/```
            
* Creamos un archivo llamado requirements.txt, para especificar las librerías que vamos a usar con su versión, ingresando el siguiente comando y la podemos actualizar que el mismo comando
            
           **pip frezze>requirements.txt**
## <h2>**`Instalado nuestro entorno virtual podemos continuar con nuestra Api`**</h2>         
            
## **2.2** **Ejecutar la api creada en FastApi localmente**
* El siguiente comando es para correr nuestra Api
              **uvicorn main:app**
* El siguiente comando es para mantener corriendo nuestra Api, mientras esta en desarrollo
              **uvicorn main:app --reload**
* Rutas para colocar en el navegador después de ejecutar nuestra api de FastApi y poder observar el funcionamiento de la misma.
             #http://localhost:8000 
             #http://localhost:8000/docs
             #127.0.0.1:8000/docs
             #0.0.0.0:8000/docs
             
## **2.3** **Pasos crear un repositorio en GitHub**     
* Debe estar **Registrado en GitHub**
* Entrar a su **Cuenta de GitHub**
* Dar clic en **Repositories**
* Dar clic en **NEW**
* Colocar el **nombre al Repositorio** 
* Dar una **breve Descripcion** del repo
* Dar clic en **Create Repository**
* Seguir los pasos del punto **2.4** del presente **README.md**
    
## **2.4** **Pasos para cargar el archivo a gitHub**     
* Ir a la carpeta donde se encuentra el archivo 
* Dar click derecho 
* Escoger Git Bash Here - 
**Aparece una consola donde deben ingresar los siguientes comandos:**
* git init
* git status
* git add . ``` todos los archivos ```
* git add README.md  ```opcional```
* git add nombre del archivo ```opcional```
* git commit -m ``` "nombre de la carga del repositorio" ejemplo  “first commit”```
* git branch -M main
* git remote add origin ```https://ruta del repositorio donde se alojara el proyecto ```
* git push -u origin main

## **2.5** **Pasos realizar el deploying a la API con FastAPI**
*  Ingresamos a Render.com
*  Dar clic en **GET STARTED FOR FREE**
*  Nos registramos en Render.com o entramos a través de **Github**
*  Dar clic en **NEW+**
*  Dar Clic en **Web service**
*  Dar clic en **Connect**
       -Colocar el nombre que deseemos
*  Ir a **Stard Command**
       colocar esta sentencia verificar el host y el port
       **-uvicorn main:app --host 0.0.0.0 --port 10000**
*  Dar clic en **Create Web Service**
       **-Environment Variables**
          **-Add Environment Variables**
             **-Key: PIP_VERSION**
             **-Value:22.3.1** -->Esta es la vercion del pip se debe consultar puede ser con **pip list**
*  Dar clic en Save changes
*  Ir **Logs**
*  Dar clic en **Manual Deploy**
      -Dar clic en **Deploy Latest Commit**
*  Esperar un rato a que cargue (Demora un poquito)
*  Copiamos la direccion **URL** y le agragamos **/docs**
*  **Ejemplo https://fastapi-platafomas-streaming.onrender.com/docs**
 
## **2.6** **Paso a paso para ejecutar la API de forma remota con el deploy en Render**

Paso a paso para ejecutar la API, se tiene que ingresar al siguiente link que se coneceta con el servidor (https://fastapi-platafomas-streaming.onrender.com/docs)

```
Una vez encendido ingresados al link ya podemos utilizar nuestras consultas en la API, como son:

* Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type))

* Se realiza la verificación los valores mínimos y máximos del dataframe

* Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year))

* Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))

```

**video de presentación**.
 ([https://drive.google.com/file/d/1QDk4qe1-GVL1jOaTSR7OPoSB2ERB6usp/view?usp=share_link](https://drive.google.com/file/d/1vZMK-M0V41zpkx1y0-gEn2aKHFe0mqE3/view?usp=sharing))

**Gracias por su visita**.
