# Sigma Bot - My very first large-scale Python Project

Sigma bot was my first venture into Discord bots and Python in general. It all started with boredom and curiosity. I developed this bot during the COVID lockdown, for my friends' discord server. 
I added moderation commands, utility commands and some fun quote commands for my friends which made conversations fun and entertaining. 

I learnt the fundamentals of asynchronous programming, interacting with APIs, git, the basics of cloud architecture and most importantly, it boosted my python skills to a great extent. 
Here was the intial tech stack I used

**Phase 1:** I used discord.py and ran my bot locally. It only had commands like kick and ban. It sent responses through pure text messages

**Phase 2:** Collected entertaining quotes from my friends and added fun quotes as well as made utility commands. Learnt how to use embeds

**Phase 3:** Deployed my bot initially through heroku until they discontinued their free tier. 

**Phase 4:** Discord.py got depricated so I shifted to nextcord and also started experimenting with slash commands. Due to the reopening of my school after the COVID lockdown and the exams following that, the project was archived for 4 yeras uptil now

**Now:** Completely migrated to slash commands and deployed my bot through Microsoft Azure

## Technical Highlights 

-**Cloud Infrastructure**: Currently deployed on Microsoft Azure using a B2ats VM. Formerly deployed on heroku

-**Library Used**: Currently nextcord.py, Formerly used discord.py

## Features
-**Moderation Suite** With classic commands like kick, ban, timeout, channel_lock

-**Utility Commands** Like a timer to remind users about incoming tasks and a timed poll feature that implements similar technology

-**Fun/Entertaintment commands** Quote commands and other features which add flavour to group chats. 

To run this project locally or to personalize for your server: 

1. **Clone the Repository**
   ```bash
    git clone https://github.com/Boomie1233/Sigma-bot.git
    cd Sigma-bot
   ```

2. **Set up Environment Variables**:Create a .env file to store your discord bot token
   ```
   TOKEN = "INSERT YOUR TOKEN HERE"
   ```
3. **Download Requirements**
   ```bash
    pip install -r requirements.txt
    ```
4. **Run the bot**
   ```
   python main.py
   ```
And you are ready to go!

PS: This project is currently archived due to my omy exhausted Azure credits.  Here's a video of me testing out the bot's features and deploying it through Azure to make up for the inconvinience:

