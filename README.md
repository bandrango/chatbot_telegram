# ChatBot en Telegram con PNL para machine learning info.

## Requerimientos

- Python = 3.10

## Configuración

Se debe reemplazar los siguientes valores como se indica en el anexo del TFM (Chatbot de Telegram para la difusión y divulgación científica de machine learning con PLN) del aplicativo de Telegram:

```commandline
telegram:
    url: https://api.telegram.org/bot
    chatId: PONER_AQUI_EL_CHAT_ID
    channel: PONER_AQUI_EL_CHANNEL_ID
    token: PONER_AQUI_EL_TOKEN_ID
    sessionId: PONER_AQUI_EL_SESSION_ID
    hash: PONER_AQUI_EL_HASH_ID
```

## Instalación

```commandline
pip -m pip install --upgrade pip
pip install -r requirements.txt
```
Precargar los packages de nltk 

```commandline
python NltkInstallLanguage.py
```

## Uso

```commandline
python Telegram.py
```

## Nota
Actualmente se están generando las respuestas automáticas al canal público si se desea que el chabot creado genere las respuestas automáticas se debe cambiar la propiedad del archivo application.yaml **channel** por el del **chatId**.
