# Telegram Bot
Telegram bot using python.

## What does this bot?
* This bot get some random pics, just use these comands: **/cat  /dog**  
  To make this possibly Capy bot uses these API'S:
  [Dog's API](https://dog.ceo/)
  [Cat's API](https://thecatapi.com/)

* This bot have an instagram scraper using **igramscraper** which searchs pics by tag name, to use the command just send this **/media tagname nImages**
  You can find documentation about this library [here.](https://pypi.org/project/igramscraper/)

* Finally this bot handles some messages you send like stickers o simply text.

## How to run this bot on your machine (On linux):

* You need to install some libraries:
```bash
 $ pip install python-telegram-bot
 $ pip install igramscraper
```
* Make a config.ini file where you have to put some data like:
```
[Bot]
Token = YOUR_BOT_API_TOKEN
[Credentials]
username = YOUR_IG_USERNAME   
password = YOUR_IG_PASSWORD
```
* Then just run on your terminal:
```bash
    $ python3 bot.py
 ```
