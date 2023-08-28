import requests
import json
import random
import fontstyle

response = requests.get("https://api.quotable.io/quotes")

parsed_data = json.loads(response.text)

choice = random.randint(1,len(parsed_data))

quote = parsed_data["results"][choice]["content"] +"-"+parsed_data["results"][choice]["author"].upper()

text = fontstyle.apply(quote,'bold/Italic/red')

print(text)



