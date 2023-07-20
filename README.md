# ChatBot en Telegram con PNL para machine learning info.

## Requerimientos

- Python >= 3.9.6

## Instalación

```commandline
python3 -m pip install --upgrade pip
python3 -m pip  install -r requirements.txt
```

Precarga de los lenguajes para NTLK

```commandline
python3 NltkInstallLanguage.py
```

## Uso

```commandline
python3 Telegram.py
```

## Nota
Actualmente se están generando las respuestas automáticas al canal público si se desea que el chabot creado genere las respuestas automáticas se debe cambiar la propiedad del archivo application.yaml **channel** por el del **chatId**.
