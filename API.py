# To create the database, first run make_database.py file.

import requests
import json
import sqlite3
from pathlib import Path
from win10toast import ToastNotifier



username = input("UserName: ")
cocktail = input("Select Cocktail(margarita, negroni, etc.): ")
path = Path(f'./{cocktail}.json')

url = f'https://www.thecocktaildb.com/api/json/v1/1/search.php?s={cocktail}'
r = requests.get(url)


if r.status_code == 200:
    print("SUCCESS!!!\n")
        
    date = r.headers['Date']
        
    if not path.is_file():
        result_json = r.text
        res = json.loads(result_json)
        res_structured = json.dumps(res,indent = 4)
            
        with open(f'{cocktail}.json', 'w') as f:
            f.write(res_structured)


else:
    print("There Is a Problem.\n")
    

filename = f'{cocktail}.json'
with open(filename, 'r') as f:
    data = json.load(f)

print(f'{data["drinks"][0]["strInstructions"]}\n')

import sqlite3
conn = sqlite3.connect("History.sqlite")
cursor = conn.cursor()
cursor.execute("INSERT INTO History (cocktail, user, date) VALUES (?,?,?)", (cocktail, username,date))
conn.commit()
notifier = ToastNotifier()
notifier.show_toast(cocktail,'Your session has been added to the database.\n', duration=3)
conn.close()


