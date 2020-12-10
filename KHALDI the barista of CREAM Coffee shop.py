#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Chatbot "Kaldi" for CREAM Coffee shop chatbot 
#Special thanks to DATACAMP NLP tutorials :) 

# Define the states
INIT=0 
CHOOSE_COFFEE=1
ORDERED=2
DONE=3

# Define the ChatBot reply dictionary
ChatBot_Reply = {
    (INIT, 'none'):(INIT, "Can not understand what are you saying sir!"),
    (INIT, 'snacks'): (INIT, "Can not understand what are you saying sir!"),
    (INIT, 'specify_coffee'): (INIT, "Can not understand what are you saying sir!"),
    (INIT, 'order'): (INIT, "Can not understand what are you saying sir!"),
    (INIT, 'ask_explanation'): (INIT, "Can not understand what are you saying sir!"),
    (INIT, "ask_explanation"): (INIT, "My name is Kaldi. I am here to assist you to order your coffee"),
    (INIT, "order"): (CHOOSE_COFFEE, "ok, We have 4 types of beans. Arabica, Robusta, Liberica, Excelsa. Which one do you want sir?"),
    (CHOOSE_COFFEE, "ask_explanation"): (CHOOSE_COFFEE, "The Arabica is sweeter.The Robusta have hints of chocolate and rum.Liberica have a woody taste.Excelsa has a fruitier flavor"),      
    (CHOOSE_COFFEE, "specify_coffee"): (ORDERED, "Nice choice sir. Your coffee is on the way! Do you like to have some snack with it?"),
    (ORDERED, 'snacks'): (DONE, "ok sir you snacks and coffee in on the way. Mean while have a look at some facts about coffee......") 
}

#The interpret function returns a proper key by finding some word token from the user's responce
def interpret(message):
    msg = message.lower()
    if 'order' in msg or 'want' in msg or 'have' in msg :
        return 'order'
    if 'arabica' in msg or 'robusta' in msg or 'liberica' in msg or 'excelsa' in msg :
        return 'specify_coffee'
    if 'yes' in msg:
        return 'snacks'
    if 'what' in msg or 'difference' in msg:
        return 'ask_explanation'
    
    return 'none'

#The respond function takes the previous state and generates next state as well as a key using the interpret function
def respond(state, message):
    (new_state, response) = ChatBot_Reply[(state, interpret(message))]
    return new_state, response

#send_message function prints a responce from bot using the respond function 
def send_message(state, message):
    new_state, response = respond(state, message)
    print("Kaldi : {}".format(response))
    return new_state


#Sample question for user
print("""
Try these following  questions:

Hi, I want to have some coffee
what is the difference?
Liberica
yes
bye
""")


countinue=True
state = INIT
print("Hello sir, thank you for choosing our CREAM coffee shop. What would you like to have sir?")
while countinue==True:  
    user = input()
    if user=='bye':
        print("We are extremly sorry for the delay. Use code 5692coffee for discount in your next order")
        break
    state = send_message(state,user)
    if state==DONE:
        print("""
        
        
        
        
A brief story of the origin of coffee according to a Ethiopian Legend

Coffee grown worldwide can trace its heritage back centuries to the ancient coffee forests on the Ethiopian plateau. There, legend says the goat herder Kaldi first discovered the potential of these beloved beans. 

The story goes that that Kaldi discovered coffee after he noticed that after eating the berries from a certain tree, his goats became so energetic that they did not want to sleep at night. 

Kaldi reported his findings to the abbot of the local monastery, who made a drink with the berries and found that it kept him alert through the long hours of evening prayer. The abbot shared his discovery with the other monks at the monastery, and knowledge of the energizing berries began to spread.

As word moved east and coffee reached the Arabian peninsula, it began a journey which would bring these beans across the globe.


Source: National Coffee Association of U.S.A
""")
        break
  


# In[ ]:





# In[ ]:




