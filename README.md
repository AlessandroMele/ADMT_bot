# ADMTbot

ADMTbot è un chatbot sviluppato con il framework Rasa.<br>
Esso è in grado di:
- consigliare film in base ad attore o un gener;
- consigliare serie tv in base al genere;
- darti informazioni su uno specifico film;
- dirti cosa c'è in questo momento al cinema.

# Configurazione

Requisiti:
- Python 3.8;
- Rasa;
- ngrok.

Per installare Rasa è necessario eseguire da terminale:<br>
`` pip install rasa``

Dopodichè, per avviare il chatbot è necessario eseguire da terminale nella cartella di progetto:<br>
``rasa run``

Per avviare ngrok, è necessario eseguire da terminale nella cartella di progetto:<br>
`ngrok http 5005`
<br><img src="images/ngrok.png" width=80% height=20%><br>

Copiare e incollare la parte evidenziata nell'immagine come prefisso nel *webhook_url*, presente nel file *credentials.yml*, di seguito un esempio:*https://4001-95-249-163-9.eu.ngrok.io/webhooks/telegram/webhook*<br>

Per rendere disponibili le *actions*, è necessario eseguire in una nuova finestra del terminale:<br>
``rasa run actions``

Dopodichè, cercando ADMTbot su Telegram è possibile iniziare a chattare con il bot.<br>

# Casi d'uso
Messaggio di benvenuto.
<br><img src ="images/benvenuto.png" width=50% height=20%><br>

Messaggio di arrivederci.
<br><img src ="images/arrivederci.png" width=50% height=20%><br>

L'utente chiede al chatbot di consigliare una serie tv di un certo genere, in mancanza del genere viene chiesto di riprovare;
<br><img src ="images/serie_genere.png" width=50% height=20%><br>

L'utente chiede al chatbot di consigliare un film di un certo genere, in mancanza del genere viene chiesto di riprovare;
<br><img src ="images/film_genere.png" width=50% height=20%><br>

L'utente chiede al chatbot di consigliare un film di un certo attoreed il chatbot restituisce la prima corrispondenza con quell'attore:
<br><img src ="images/film_attore.png" width=50% height=20%><br>

L'utente chiede al chatbot cosa può trovare al momento al cinema ed il chatbot restituisce i primi 5 risultati della lista di film proiettati nelle sale nel periodo corrente.
<br><img src ="images/ora_cinema.png" width=50% height=20%><br>

L'utente chiede al chatbot le informazioni relative ad uno specifico film ed il chatbot restituisce alcuni dettagli.
<br><img src ="images/info_film.png" width=50% height=20%><br>
