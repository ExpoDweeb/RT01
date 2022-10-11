# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
# from dotenv import load_dotenv
from pymongo import MongoClient

MONGODB_URI = 'mongodb+srv://appAdmin:cB45KLzyPdV8NdG3@realto-stage.xg5kl.mongodb.net/'
# MONGODB_URI = os.environ['mongodb+srv://appAdmin:cB45KLzyPdV8NdG3@realto-stage.xg5kl.mongodb.net/redev?retryWrites=true&w=majority&authMechanism=DEFAULT']

db = MongoClient(MONGODB_URI)

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World! from custom action")

        return []



class ActionGetWallet(Action):
    
    def name(self) -> Text:
        return "action_get_wallet_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # function to collect user id credntials
        # user_id = tracker.slot['user_id'] 
        query = {'userId':"617fc06495c1d37b3135e397"} # to be conneced to listener 
        # define mongoDB collection
        wallet = db.redev.crypto_wallets
        # intent = tracker.latest_message.intent['name']
        answer = wallet.find_one(query)

        response = """Your wallet currently holds {}$ in your wallet as of today:""".format(answer['balance'])

        dispatcher.utter_message(response)

class ActionGetAssets(Action):
    
    def name(self) -> Text:
        return "action_get_asset"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="asset [assList] meant to be this")

        return []


class ActionGetPortfolio(Action):
    
    def name(self) -> Text:
        return "action_get_portfolio"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # function to collect user id credntials

        query = {'userId':"617fc06495c1d37b3135e397"} # to be conneced to 
        # define mongoDB collection

        wallet = db.redev.crypto_wallets
        # intent = tracker.latest_message.intent['name']
        answer = wallet.find_one(query)


        dispatcher.utter_message("utter_wallet_balance",tracker, answer=link)

        return []



class ActionGetUserId(Action):
    
    def name(self) -> Text:
        return "action_get_userid"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # function to collect user id credntials
        return [SlotSet]