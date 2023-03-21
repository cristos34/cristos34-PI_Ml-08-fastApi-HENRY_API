<p align=center><img src=https://assets.soyhenry.com/logos/LOGO-HENRY-04.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Data Engineering`**</h1>
*Cristian Andres Contreas*

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

Este trabajo esta basado en realizar un proceso de extarcion transformacion y carga (ETL) con diversos dataset, con la fin de entregar datos estandarizados y de buena calidad (limpios) que puedan ser procesados por nuestra Application Programming Interface (API), la cual va estar trabajando desde un modo de producion desde desde un servidor llamado render.

API, Una API o interfaz de programación de aplicaciones, con un protocolo que se usa para diseñar e integrar el software de las aplicaciones.
Es una herramienta muy versátil y fundamental para la creación de app web,sitios estaticos entre otras formas de uso, esta permite realizar una sin numero de operaciones y vincular con una plataforma web.

Hoy en día contamos con **FastAPI** y **Flask** entre muchas otras, son framework modernos y de alto rendimiento para construir APIs con Python.
<p align=center>
<img src = "https://tekla.io/wp-content/uploads/2022/06/QueEsAPIRest-Recurso-01.jpg" height=250><p>

<hr>

## **Tecnologías**

Para la elboración de este proyecto se utilizaron las siguiente tecnologias:

* Fastapi
* Visual studio code
* Jupyter
* Python
* Pandas
* Uvicorn
* Render
<hr>

## **Pasos para la elaboracion del proyecto**


<p align=center>
<img src = 'https://images.jifo.co/53775302_1581003928973.jpg' height=250><p>

**1.** **EDA** 

Se realiza un analisis exploratorio con el objetivo de verificar el estado los datos de entrada logardo detallar que esten cargados correctamente, lo cual permite poder tomar decisiones en la limpieza de estos, los archivos orginales fueron provistos como *csv*, estos se cargaron de la siguiente manera:

Para visualizar la limpieza completa se pueden remitir a [Limpieza y extacion](https://github.com/cristos34/cristos34-PI_Ml-fastApi-HENRY_API/blob/37c7c0c8b08fd7c52ff687ea97fd46c417a0991f/Proyecto_PI_Uno.ipynb).



**2.** **Creación de la API**

Para crear la API se utilizo el framework [FasAPI](https://fastapi.tiangolo.com/), que esta catalogado en el momento como el frameworkde mas alto procesamineto y de mayor facilidad de uso para trabajar API.

La API llamanda **platafomas-streaming** permite conocer diferentes datos de las platafromas Amazon, Hulu, Diney, Netflix, esta se trabajo en un archivo llamado **main.py** y se inicializó de la siguiente manera:

Para ver el codigo completo donde estan todas las funciones que de la API se pueden remitir a [main.py](https://github.com/cristos34/cristos34-PI_Ml-fastApi-HENRY_API/blob/37c7c0c8b08fd7c52ff687ea97fd46c417a0991f/main.py).


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

**2.1** **Ejecutar la API**

Para ejecutar la API se tienen que ingresar alsiguente link que se coneceta conel servidor (https://github.com/cristos34/cristos34-PI_Ml-fastApi-HENRY_API/blob/37c7c0c8b08fd7c52ff687ea97fd46c417a0991f/main.py)





```
Una vez encendido ingresados al link ya podemos utilizar nuestra consultas en la API, como son:

* Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type))

* Se realiza la verificacion los valores minimos y maximos del dataframe

* Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year))

* Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))



**video de presentacion**.
 (https://drive.google.com/file/d/1QDk4qe1-GVL1jOaTSR7OPoSB2ERB6usp/view?usp=share_link)

**Gracias por su visita**.
