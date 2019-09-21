# Scope of the chatbot
* The Horoscope Bot should be able to understand greetings and reply with a greeting.
* The bot should be able to understand if the user is asking for a horoscope.
* The bot should be able to ask the horoscope sign of the user if the user doesn't provide it.
* If the user doesn’t know his/her horoscope sign, the bot should ask the user’s date of birth (DOB) and find it for them.
* The bot should subscribe/unsubscribe the user to get the daily horoscope.
* The bot should learn from existing responses to formulate a new response.
* The bot should be able to handle spelling mistakes by the user.

# Possible intents
* Greeting Intent: User starting with a greeting
* Get Horoscope Intent: User asking for horoscope
* User’s Horoscope Intent: User telling the horoscope sign
* User’s DOB Intent: User telling his/her DOB
* Subscription Intent: User asking for subscription

# Conversation Script Between the Horoscope Bot and the User
```
User: Hello
```
```
Horoscope Bot: Hello! Hope you are doing well.
```
```
User: I want to know my horoscope.
```
```
Horoscope Bot: Sure, may I know your horoscope sign?
```
```
User: Capricorm
```
```
Horoscope Bot: Sorry, did you mean Capricorn?
```
```
User: Yes.
```
```
Horoscope Bot: Alright, Here is your horoscope for today.
Chances are that you’ll feel upbeat and positive today. Share this energy with others who feel less than content. Your attitude can have a profound effct on friends, partners, spouse, and children. Neighbors and extended family can pick up on your spirit without you even realizing it. If someone is hurt or angry, be encouraging. Everything will eventually work out.

Horoscope Bot: Would you like to subscribe for the daily updates? If yes, just say subscribe.
```
```
User: Yes, please subscribe.
```
```
Horoscope Bot: Great, you are subscribed now. Have a good day.
```

# JSON format of the data that Rasa NLU expects 
```
{
 "rasa_nlu_data": {
    "common_examples": [],
    "regex_features" : [],
    "entity_synonyms": []
 }
}
```
### For creating the Rasa NLU data JSON file I'm going to use node module named rasa-nlu-trainer
##### install rasa-nlu-trainer
```
npm i -g rasa-nlu-trainer
```
## To Run rasa-nlu-trainer on data.json file. go to data.json folder and run the below command
```
rasa-nlu-trainer 
```
or
```
rasa-nlu-trainer --source file/path/of/data.json
```
