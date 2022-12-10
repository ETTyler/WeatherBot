# WeatherBot

Scrapes the Met Office website using Beautiful Soup and gets the current weather forecast for a selected location.
The data scraped is then sent as message through Telegram using the bot API. 
 
To run this you need to:
- Get the location ID from the Met Office website
- Create a Telegram bot and get the bot token
- Find the chat ID for the channel/user you want to send the weather data to

I use this personally as a Lambda cron job that sends me the forecast every morning.
