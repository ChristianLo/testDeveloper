# Test Practico de desarrollo en Django

## Tareas 

Las tareas que se solicitaron se encuentran dentro de los siguientes archivos:

- Tarea 1: `Tarea1/migrations/0002_auto_20230517_1358.py`, dentro de este archivo se encuentra la funcion que obtiene los datos de la api y los guarda dentro de la base de datos.
- Tarea 2: `main.py`, se encuentra en la raiz del repositorio y cuenta con el script utilizado para obtener la informacion, los transforma de tal manera que se adapte al modelo utilizado y que pueda agregarse utilizando el comando de `loaddata`


## Descripcion
Para cada una de las tareas se utilizo dentro de un proyecto de Django. El cual se generaron modelos y funciones adecuadas deacuerdo a las fuentes de informacion y se generaron dentro de la pagina de administracion una vista sobre los modelos de datos.

## Requisitos Previos

Para poder ejecutarlo se debe de tener los siguientes requisitos previos:

- Se debe de tener la version de python 3.10
- Tener instalado postgres dentro de su maquina.

## Configuracion

1. Clonar o descargar el repositorio dentro de su maquina o contenerdor (Docker).
2. Abrir un terminal y abrir la carpeta del repositorio descargado.
3. Crear y activar un entorno virtual para instalar las librerias necesarias.
```bash
python3 -m venv venv   
source venv/bin/activate
```
4. Instalar las librerias que se utilizan usando el siguiente comando:
```bash
pip3 install -r requirements.txt
```
* En caso de error por la libreria psycopg2, esto se debe a que dentro del sistema faltan las librerias de postgres. Para eso se debe de ejecutarel siguiente comando en el terminal (Ubuntu):
```bash
sudo apt-get update && sudo apt-get install -y postgresql postgresql-contrib libpq-dev gcc python3-dev musl-dev
```

5. Verificar si es posible conectar la base de datos utlizando los que estan por predeterminado que son:
```yaml
postgres:
  - USER: postgres
  - PASSWORD: postgres
  - NAME: posgres
  - HOST: 127.0.0.1
  - PORT: 54320
```
* Esto se debe de cambiar de forma manual en el archivo testPractico/settings.py, desde la linea 80.

6. Realizar las migracion de la base de datos ejecutando el siguiente comando:
```bash
python3 manage.py migrate
```

* se utiliza solamente ese comando debido a que las migraciones ya estan realizadas solamente deben de ejecutarse, este puede tomar un tiempo debido que dentro de la migracion de Tarea1 este carga los datos de la api.

7. Debe de ejeuctar el archivo `main.py` para obtener un json para luego cargarlo utilizando el siguiente codigo, es necesario para la Tarea2 :
```bash
python3 main.py
python3 manage.py loaddata fixtures/data.json
``` 
* Si no se encuentra la carpeta fixtures, este le lanzara error, por lo que debe de crearla usando mkdir fixtures.

8. Crear un superusuario usando el siguiente codigo:  `python3 manage.py createsuperuser`

## Ejecucion

Ya haber realizado todos los pasos sin ningun error, se procede a ejecutar el servidor de Django:
```bash
python3 manage.py runserver # python3 manage.py runserver 0.0.0.0:8000 en caso de utilizar un contenedor.
```

## Uso

Para poder verificar las tareas se debe de ingrasar a la pagina de admin `http://127.0.0.1:8000/admin` e ingrasar los datos utilizados dentro del paso 8 de las configuraciones. Con esto entrara a una pagina de admin el cual le mostrara los modelos de las respectivas tarea. Al entrar en uno de los modelos se generara una tabla de los atributos de ese modelo, pero si hace click en ID se puede visualizar la informacion completa que esta realizana a ese ID.
