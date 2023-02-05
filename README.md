# ADMTbot

ADMTbot è un chatbot sviluppato con il framework Rasa.<br>
Esso è in grado di:
- consigliare film specificando un attore o un genere;
- consigliare serie tv specificando un genere;
- fornire informazioni su un film specificando il titolo;
- fornire informazioni sui primi cinque film presenti al cinema.

# Configurazione

Requisiti:
- Python 3.8;
- Rasa;
- ngrok.

Per installare Rasa è necessario eseguire da terminale:<br>
``pip install rasa``

Dopodichè, per avviare il chatbot è necessario eseguire da terminale nella cartella di progetto:<br>
``rasa train | rasa run``

Per configurare un bot su Telegram, è necessario avere un account e interagire con il bot ufficiale, <a href="https://telegram.me/botfather">BotFather</a>.<br>

Per collegare il chatbot Rasa con il bot Telegram è necessario modificare il file *credentials.yml*, inserendo i propri *access_token* e *verify*.<br>

Per avviare ngrok, è necessario eseguire da terminale nella cartella di progetto:<br>
`ngrok http 5005`
<br><img src="images/ngrok.png" width=50% height=20%><br>

Copiare il *webhook_url* (parte evidenziata nell'immagine), come prefisso nella corrispettiva voce del file *credentials.yml*.
<br><img src="images/credentials.png" width=50% height=20%><br>

Per rendere disponibili le *actions*, è necessario eseguire in una nuova finestra del terminale:<br>
``cd actions``
``rasa run actions``

Dopodichè, cercando il proprio bot su Telegram è possibile iniziare a chattare.

# Casi d'uso
Messaggio di benvenuto.
<br><img src ="images/benvenuto.png" width=50% height=20%><br>

Messaggio di arrivederci.
<br><img src ="images/arrivederci.png" width=50% height=20%><br>

L'utente chiede al chatbot di consigliare una serie tv specificando un genere, in mancanza, viene chiesto di riprovare;
<br><img src ="images/serie_genere.png" width=50% height=20%><br>

L'utente chiede al chatbot di consigliare un film di specificando un genere, in mancanza, viene chiesto di riprovare;
<br><img src ="images/film_genere.png" width=50% height=20%><br>

L'utente chiede al chatbot di consigliare un film specificando un attore, in mancanza viene chiesto di riprovare;
<br><img src ="images/film_attore.png" width=50% height=20%><br>

L'utente chiede al chatbot cosa c'è al cinema, il chatbot restituisce i primi cinque film proiettati nelle sale nel periodo corrente;
<br><img src ="images/ora_cinema.png" width=50% height=20%><br>

L'utente chiede al chatbot informazioni aggiuntive di un film specificando il titolo, in mancanza viene chiesto di riprovare;
<br><img src ="images/info_film.png" width=50% height=20%><br>
