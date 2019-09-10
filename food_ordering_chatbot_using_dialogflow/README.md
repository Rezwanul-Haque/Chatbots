# Scope of this chatbot —
### what it can do and to what extent.
* It should be able to greet the user dynamically.
* It should be able to understand the menu items and their quantity requested.
* Chatbot should be able to place an order on the user’s behalf.
* Give the user the status of the order when asked.

# Listing Intents
* Default welcome intent: when the user messages the chatbot
* Place order intent: when the user asks the bot to order food
* Item description intent: when the user tells what item and quantity they want
* Order status: when the user wants to know his order status
* Order_ID: the bot needs to understand the user’s order ID for tracking.
* User thanks: when the user thanks the bot

# Listing Entities
* food_items: what food does the user want to order?
* quantities: what is the quantity of the food item the user is willing to order?
* order_id: order_id of the place order for user

# Chatbot and User Conversation Script:
* User: Hello
* OnlineEatsBot: Hello and Welcome! How may I help you?
* User: I am looking to order Chinese food.
* OnlineEatsBot: Sure, what would you like to order today?
* User: One chicken dumpling and two spring rolls.
* OnlineEatsBot: Done. Your final amount is XYZ, and your order is placed for 1 Chicken dumpling and 2 spring rolls.
* User: I haven’t received my order yet. Where is my food?
* OnlineEatsBot: Can you please help me with your order ID?
* User: 123456
* OnlineEatsBot: Order Status for Order ID: 123456. Th delivery guy is in your locality, your food will arrive in about 5 minutes.
* User: Thanks.
* OnlineEatsBot: Thanks a lot for your cooperation.

# Dialogflow 
### Step 1: Create account @ https://dialogflow.com/
### Step 2: Login to account
### Step 3: Create agent
### Step 4: Create intents
* Their will be two default intents
    1. Default fallback intent - Fallback intents are triggered if a user’s input is not matched by any of the regular intents or enabled built-in small talk. 
    2. Default welcome intent - This welcome intent for our own chatbots. You should add some of our own user expressions and default responses.
### Step 5: Add some custom intent in Default welcome intent
### Step 6: Save
### Step 7: Test Dialogflow's agent response using right sidebar
### Step 8: Creating Intents and Adding Utterances
* create the order intent
    1. place_order_intent
        1. I want food
        2. I want to order food asap
        3. Can you please take my order for food?
        4. Take my order please
        5. I want to place an order for Chinese food
        6. I want to place an order
        7. Would you please help me to order food?
        8. Can you please order food for me?
        9. I want to order food
        10. I am looking to order Thi food
        11. I am looking to order Chinese food
### Step 9: Adding Default Response to the Intent
  1. place_order_intent
    1. Sure, What would you like to order today?
    2. Defiitely, What would you like to have today?
    3. Certainly, I’ll try to help you with that. What are you feeling like eating today?
### Step 10: Creating Intents and Adding Utterances for items_description
### Step 11: Creating Intents and Adding Utterances for user_order_id, order_status, user_thanks
    In Utterances variable names can be used in default responses using $variable_name
### Step 12: Go to Intregation page and Turn on web demo app for dialogflow there we can test the chatbot we just created.
