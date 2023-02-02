# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

import utils
import requests
import random
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

API_key = "k_1h89yff5"

class ActionFilmByActor(Action):

    def name(self) -> Text:
        return "action_search_film_by_actor"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        out_list = [elem for elem in tracker.get_latest_entity_values('actor')]
        
        if(len(out_list) == 0):
            dispatcher.utter_message("Non ho riconosciuto nessun attore, puoi inserirne un altro?")
            return []

        entity = out_list[-1]

        response = requests.get(f'https://imdb-api.com/en/API/SearchName/{API_key}/{entity}').json()
        actor = response['results'][0]

        response = requests.get(f"https://imdb-api.com/en/API/Name/{API_key}/{actor['id']}").json()
        results = response['castMovies']
        i = random.randint(0, len(results)-1)
        movie_id = results[i]['id']

        while(results[i]['role'] not in ["Actor","Actress"]):
            i = random.randint(0, len(results)-1)
            movie_id = results[i]['id']

        movie = requests.get(f'https://imdb-api.com/it/API/Title/{API_key}/{movie_id}').json()

        message = f"Ecco cosa ho trovato:\nTitolo: {movie['title']}\nDurata: {movie['runtimeStr']}\nTrama: \n{movie['plotLocal']}"
        dispatcher.utter_message(text=message, image=movie['image'])

        return []

class ActionFilmByGenre(Action):

    def name(self) -> Text:
        return "action_search_film_by_genre"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        out_list = [elem for elem in tracker.get_latest_entity_values('genre')]

        if(len(out_list) == 0):
            dispatcher.utter_message("Non ho riconosciuto nessun genere, puoi inserirne un altro?")
            return []

        entity = utils.trad_genere_ita_eng(out_list[-1])
        response = requests.get(f'https://imdb-api.com/API/AdvancedSearch/{API_key}?title_type=feature&genres={entity}&sort=moviemeter,asc').json()

        results = response['results']

        i = random.randint(0, len(results)-1)
        movie_id = results[i]['id']
        movie = requests.get(f'https://imdb-api.com/it/API/Title/{API_key}/{movie_id}').json()
        message = f"Ecco cosa ho trovato:\nTitolo: {movie['title']}\nDurata: {movie['runtimeStr']}\nTrama: \n{movie['plotLocal']}"
        dispatcher.utter_message(text = message, image = movie['image'])
        return []

class ActionSerieByGenre(Action):

    def name(self) -> Text:
        return "action_search_serie_by_genre"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        out_list = [elem for elem in tracker.get_latest_entity_values('genre')]

        if(len(out_list) == 0):
            dispatcher.utter_message("Non ho riconosciuto nessun genere, puoi inserirne un altro?")
            return []

        entity = utils.trad_genere_ita_eng(out_list[-1])
        response = requests.get(f'https://imdb-api.com/API/AdvancedSearch/{API_key}?title_type=tv_series&genres={entity}&sort=moviemeter,asc').json()
        results = response['results']

        n_max = len(results)
        i = random.randint(0, n_max-1)
        serie = results[i]

        message = f"Ecco cosa ho trovato:\nTitolo: {serie['title']}\nDurata: {serie['runtimeStr']}\nTrama: \n{serie['plot']}"
        dispatcher.utter_message(text = message, image = serie['image'])
        return []

class ActionOraAlCinema(Action):
    def name(self) -> Text:
        return "action_ora_al_cinema"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        response = requests.get(f"https://imdb-api.com/en/API/InTheaters/{API_key}")

        text = "Ecco i primi 5 che ho trovato:\n"
        i, limit = 0, 5
        response = response.json()
        results = response['items']
        while (i < limit):
            movie = results[i]
            text+= f"Titolo: {movie['title']}\nDurata: {movie['runtimeStr']}\nGenere: {movie['genres']}\nRegista: {movie['directors']}"
            text +="\n________________\n"
            i += 1
        dispatcher.utter_message(text = text)

        return []

class ActionInformazioniFilm(Action):

    def name(self) -> Text:
        return "action_informazioni_film"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        out_list = [elem for elem in tracker.get_latest_entity_values('film')]
        
        if(len(out_list) == 0):
            dispatcher.utter_message("Non ho riconosciuto nessun film, puoi inserirne un altro?")
            return []

        entity = out_list[-1]
        response = requests.get(f"https://imdb-api.com/it/API/SearchTitle/{API_key}/{entity}").json()
        movie_id = response['results'][0]['id']
        movie = requests.get(f'https://imdb-api.com/it/API/Title/{API_key}/{movie_id}').json()
        text = f"Ecco cosa ho trovato:\nTitolo: {movie['title']}\nDurata: {movie['runtimeStr']}\nRegista: {movie['directors']}\nGenere: {movie['genres']}\nTrama: \n{movie['plotLocal']}\nRating di IMDB: {movie['imDbRating']}"
        dispatcher.utter_message(text = text, image=movie['image'])
        
        return []