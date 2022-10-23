# ChatBot en Telegram con PNL para machine learning info.

## Requerimientos

- Python = 3.10

## Instalación

```commandline
pip -m pip install --upgrade pip
pip install -r requirements.txt
```

## Uso

```commandline
python holo_detector.py -i <input_video_path> -o <output_path> -t <document_type> [flags]
```

Donde ``[flags]`` puede ser:

* ``--show``: muestra la imagen del documento con los hologramas detectados al terminar la ejecución
* ``--debug``: activa el modo de depuración para guardar los resultados intermedios en la carpeta ``<output_path>``
* ``--dataset``: genera set de datos para entrenamiento de modelos

Al ejecutar el programa, dentro de la carpeta ``<output_path>`` encontrará la imagen con los posibles hologramas, así
como un archivo JSON con información de la métrica IoU (*intersection over union*) y la ubicación de los hologramas en 
la imagen. El archivo tiene la siguiente estructura:

```json
{
    "candidates": 1,
    "values": [
        {
            "IOU": 0.8235,
            "location": {
                "xmin": 132,
                "ymin": 117,
                "width": 73,
                "height": 72
            }
        }
    ]
}
```

## Ejemplos

* Procesamiento de video de la licencia de conducción de la Florida:

```commandline
python holo_detector.py -i .\data\video.mp4 -o .\resultado -t USA-lic-FL --show
```

* Genera datos intermedios para depuración de errores:

```commandline
python holo_detector.py -i .\data\video.mp4 -o .\resultado -t USA-lic-FL --show --debug
```

* Genera datos para entrenamiento de modelos:

```commandline
python holo_detector.py -i .\data\video.mp4 -o .\resultado -t USA-lic-FL --dataset
```