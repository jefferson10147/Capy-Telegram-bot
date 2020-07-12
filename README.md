# Telegram Bot
Telegram bot using python.

## What does this bot?
*This bot get some random pics, just use these comands: **/cat  /dog**  
  To make this possibly Capy bot uses these API'S:
  [Dog's API](https://dog.ceo/api/breeds/image/random)
  [Cat's API](https://api.thecatapi.com/v1/images/search)

*This bot have an instagram scraper using **igramscraper** which searchs pics by tag name, to use the command **/media tagname nImages**
  You can find documentation about this library [here.](https://pypi.org/project/igramscraper/)

*Finally this bot handles some messages you send like stickers o simply text.

## How to run this bot on your machine:
**On linux**
*You need to install some libraries.


```bash
 $ pip install python-telegram-bot
 $ pip install igramscraper
```
*Make a config.ini file where you have to put some data like:
```
[Bot]
Token = YOUR_BOT_API_TOKEN
[Credentials]
username = YOUR_IG_USERNAME   
password = YOUR_IG_PASSWORD

```

*Then just run:

```bash
    $ python3 bot.py
 ```
