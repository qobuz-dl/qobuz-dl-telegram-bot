# qobuz-dl-telegram-bot

## Commands for bot(set through @BotFather)

```
start - start bot
download - dl one link and multi link
status - bot status
log - log

```
1. **Installing requirements**

 - Clone repo:

        git clone https://github.com/qobuz-dl/qobuz-dl-telegram-bot

2. **Set up config file**

- config.py

- Fill up variables:

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


🌿 Quality
```
  5:  MP3-320 Kbps
  6:  CD-16-bit/44,1 kHz
  7:  24-Bit Hi-Res/Upto 96 kHz
  27: 24-Bit Hi-Res/Upto 192 kHz
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
