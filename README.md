# markov-chains-github
A simple discord bot that uses past channel messages and markov chains to generate random messages which sometimes makes sense and sometimes funny.

#How does it work?
The bot listens for it's own mention and when it receives it, it retrieves the past 1500 messages (no bot message or link) and trains a markov chain model on the messages and generates a response using it.

# Getting Started
1. Clone the repo and navigate to the project dir.
2. Install the requirements.txt file.
3. Create an env file and put your token like this: token='your_token' where your token is the token of your bot.
4. Run the bot
5. If the bot is mentioned in a channel it can see, it'll send the response.

# Credits
Thanks to the [Markov Bot](https://top.gg/bot/903354338565570661) for this. That's written in typescript, mine's written in python :)
