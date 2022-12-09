import requests
from bs4 import BeautifulSoup
import datetime

# Set the location for the weather forecast and token and chat id for the telegram bot
location = ""
bot_token = ""
chat_id = ""

# Get the current date
today = datetime.date.today()
url = "https://www.metoffice.gov.uk/weather/forecast/{}#?date={}".format(location, today)

# Send a request to the website and parse the HTML response
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract the forecast from the page
highTemp = soup.find("span", class_="tab-temp-high").text
lowTemp = soup.find("span", class_="tab-temp-low").text
summary = soup.find("span", id="tabSummaryText{}".format(today)).text
message = "The forecasted weather for today is {} With a high of {} and a low of {}.".format(summary.lower(), highTemp, lowTemp)

telegram_api_url = "https://api.telegram.org/bot{}/sendMessage".format(bot_token)
payload = {"chat_id": chat_id, "text": message}

# Send the request to the Telegram API
response = requests.post(telegram_api_url, json=payload)
print(response)