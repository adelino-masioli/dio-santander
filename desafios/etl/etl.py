import pandas as pd
import os
import requests
import json
import random

directory = os.getcwd()
messages_csv = pd.read_csv(f"{directory}/santander/desafios/etl/messages.csv")
messages = messages_csv['message'].tolist()

df = pd.read_csv(f"{directory}/santander/desafios/etl/SDW2023.csv")
user_ids = df['UserID'].tolist()


sdw2023_api_url = 'https://sdw-2023-prd.up.railway.app'


def get_message():
    return random.choice(messages)


def get_user(id):
    response = requests.get(f'{sdw2023_api_url}/users/{id}')
    return response.json() if response.status_code == 200 else None


users = [user for id in user_ids if (user := get_user(id)) is not None]
print(json.dumps(users, indent=2))


def generate_ai_news(user):
    return f"{user['name']}, {get_message()}"


for user in users:
    news = generate_ai_news(user)
    print(news)
    user['news'].append({
        "icon": "https://digitalinnovationone.github.io/santander-dev-week-2023-api/icons/credit.svg",
        "description": news
    })
