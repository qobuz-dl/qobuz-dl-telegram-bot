# qobuz-dl-telegram-bot


[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://dashboard.heroku.com/new?button-url=https%3A%2F%2Fgithub.com%2F&template=https://github.com/qobuz-dl/qobuz-dl-telegram-bot)

## Premium account is required for the bot to work.

## Commands Bot( @BotFather )

```
start - start bot
download - dl one link and multi link
status - bot status
log - log
reset - restart bot

```
1. **Installing requirements**

 - Clone repo:

        git clone https://github.com/qobuz-dl/qobuz-dl-telegram-bot

2. **Set up config file**

- Fill up variables config.py:

   - Mandatory variables:
   
        - `API_ID`: get this from https://my.telegram.org. Don't put this in quotes
        - `API_HASH`: get this from https://my.telegram.org
        - `BOT_TOKEN`: The Telegram Bot Token (get from @BotFather)
        - `OWNER_ID`: your Telegram User ID (not username) of the owner of the bot
        - `AUTH_IDS`: Group Id -100xxxx
        - `QOBUZ_MAIL`: qobuz email
        - `QOBUZ_PASS`: qobuz pass
        - `QOBUZ_QUAL`: Quality
        - `BOT_USERNAME`: Bot username not @
        - `LOG_CHANNEL`: Channel Id -100xxxx
        
        Heroku Restart Bot
        
        - `HEROKU_API_KEY`: Heroku Api Key
        - `HEROKU_APP_NAME`: Heroku Name
    


## Quality
```
  5:  MP3-320 Kbps
  6:  CD-16-bit/44,1 kHz
  7:  24-Bit Hi-Res/Upto 96 kHz
  27: 24-Bit Hi-Res/Upto 192 kHz
```

## Support Link
```
Artist: https://open.qobuz.com/artist/43821
Albüm:  https://open.qobuz.com/album/doldeure0459b
Track:  https://open.qobuz.com/track/138731318

```
3. **Deploying on VPS Using Docker**

- Start Docker daemon (skip if already running), if installed by snap then use 2nd command:
    
        sudo dockerd
        sudo snap start docker

     Note: If not started or not starting, run the command below then try to start.

        sudo apt install docker.io

- Build Docker image:

        sudo docker build . -t qobuz-dl-bot 

- Run the image:

        sudo docker run qobuz-dl-bot

- To stop the image:

        sudo docker ps
        sudo docker stop id

- To clear the container:

        sudo docker container prune

- To delete the images:

        sudo docker image prune -a

4. **Deploying on VPS Using docker-compose**

**NOTE**: If you want to use port other than 80, change it in docker-compose.yml

```
sudo apt install docker-compose
```
- Build and run Docker image:
```
sudo docker-compose up
```
- After editing files with nano for example (nano start.sh):
```
sudo docker-compose up --build
```
- To stop the image:
```
sudo docker-compose stop
```
- To run the image:
```
sudo docker-compose start

```
