Este repositorio contiene todo los archivos correspondientes al examen práctico de IA sobre el modelo de Regresión Logística.

Para poder testear los archivos, primero deberás clonar el repositorio: 
```shell
git clone https://github.com/iavalle2024/examen-reglog
```

O en su defecto, en caso de tener configurada una clave SSH:
```shell
git clone git@github.com:iavalle2024/examen-reglog
```

Una vez clonado el repositorio, deberás inicializar un nuevo entorno virtual dentro del directorio del repositorio clonado: 
```shell
python -m venv .
```

Tras crear el entorno virutal, el siguiente paso será activarlo:
```shell
# MacOS / GNU+Linux
source bin/activate

# Windows
.\Scripts\activate
```

He dejado un archivo de dependencias para instalar todas las librerías necesarias a través de dicho archivo:
```shell
pip install -r requirements.txt
```

Finalmente, podrás abrir el proyecto en VSCode utilizando:
```shell
code .
```
