import requests
import base64
from os     import getenv
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

githubToken = getenv('GITHUB_TOKEN')
freshdeskToken = getenv('FRESHDESK_TOKEN')

username = input("Please enter a user: ")
print(username)

tokenbase64 = base64.b64encode(bytes(freshdeskToken, 'utf-8'))
print(tokenbase64)

url = f"https://api.github.com/users/{username}"

user_data = requests.get(url).json()

name = user_data["name"]
email = user_data["email"]

pprint(user_data)

headers = {
    'Content-Type': 'application/json'
}

json_data = {
    'name': name,
    'email': email,
}

choice = input("Please choose: \n1 - creating a contact \n2 - updating a contact\n")

if choice == 1:
    response = requests.post('https://none6104.freshdesk.com/api/v2/contacts', 
    headers=headers, json=json_data, auth=(freshdeskToken, 'X'))

    print(response)

elif choice == 2:
    userID = input("Please enter userID: ")
    response = requests.post(f'https://none6104.freshdesk.com/api/v2/contacts/{userID}', 
    headers=headers, json=json_data, auth=(freshdeskToken, 'X'))
    
    print(response)
