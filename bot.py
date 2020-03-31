import random

joke_list = ["I ate a clock yesterday, it was very time-consuming.",
"Did you hear about the crook who stole a calendar? He got twelve months.",
"I own the world’s worst thesaurus. Not only is it awful, it’s awful.",
"I’ve just written a song about tortillas; actually, it’s more of a rap."]

while True:
  user_response = input("User input: ")

  if "goodbye" in user_response.lower().split(' '):
    print("Goodbye fellow human!")
    break

  elif user_response.lower() == "how are you":
    print("I am doing good")

  elif user_response.lower() ==  "tell me a joke":
    print(random.choice(joke_list))
    
  else:
    print("Why is " + user_response +"?")
