import requests
import pyfiglet
from termcolor import colored
from random import choice

def title():
  answer = pyfiglet.figlet_format("Corny Dad Jokes")
  answer = colored(answer, "magenta")
  print(answer)


def jokes(topic):
  
  api = f"https://icanhazdadjoke.com/search?term={topic}&limit=5"
  res = requests.get(api, headers={"Accept": "application/json"}).json()
  rand = res["results"]
  if   res["total_jokes"] > 1:
    print("theres multiple jokes but here is one")
    print(choice(rand)["joke"])
  elif res["total_jokes"] == 1:
    print("thers is only 1 joke")
    print(rand[0]["joke"])
  else:
    print(f"sorry there are no jokes that contain {topic}")

start = 0

while start != 100:
  title()
  topic = input(" What joke topic would you like to hear?")
  jokes(topic)
  start += 1
  