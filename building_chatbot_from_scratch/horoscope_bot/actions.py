import requests
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class GetTodaysHoroscope(Action):
    def name(self):
        return "get_todays_horoscope"
    
    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        user_horoscope_sign = tracker.get_slot('horoscope_sign')
        # open-source horoscope api: code can be @https://github.com/tapasweni-pathak/Horoscope-API
        # download the codebase and host it on heroku.
        base_url = http://horoscope-api.herokuapp.com/horoscope/{day}/{sign}
        url = base_url.format(**{'day': 'today', 'sign': user_horoscope_sign})

        # http://horoscope-api.herokuapp.com/horoscope/today/capricorn

        res = requests.get(url)
        todays_horoscope = res.json()['horoscope']
        response = "Your today's horoscope: \n{}".format(todays_horoscope)

        dispatcher.utter_message(response)

        return [SlotSet("horoscope_sign", user_horoscope_sign)]


class SubscribeUser(Action):
    def name(self):
        return "subscribe_user"
    
    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        subscribe = tracker.get_slot('subscribe')

        if subscribe == "True":
            response = "You're successfully sbuscribed"
        if subscribe == "False":
            response = "You're successfully unsubscribed"
        
        dispatcher.utter_message(response)

        return [SlotSet('subscribe', subscribe)]


class CustomActionTemplate(Action):
    def name(self):
        return "action_name"
    
    def run(self, dispatcher, tracker, domain):
        # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        action = tracker.get_slot('action')

        #logic for the reponse goes here
        reponse = ''
        
        dispatcher.utter_message(response)

        return [SlotSet('action', action)]