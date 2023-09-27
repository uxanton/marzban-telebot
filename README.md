<p align="center">
    <img src="https://github.com/mmdchnar/marzban-telebot/blob/main/screenshots/marzban-telebot2.PNG" alt="Charge screenshot" width="500" height="auto">
</p>

**<a href="https://github.com/mmdchnar/marzban-telebot/tree/main/screenshots">Screenshots</a>**

# Установка

First you need to clone [the repository](https://github.com/uxanton/marzban-telebot) to your sever. You can do it by this:

```bash
cd /opt/marzban
git clone https://github.com/uxanton/marzban-telebot
```

Then you have to map files to your docker container. Add this line to volume section of `docker-compose.yml`:

**(DO NOT REPLACE WHOLE FILE, Just the last two lines)**
```docker
services:
    marzban:
        ...
        volumes:
            ...
            - /opt/marzban/marzban-telebot/telegram:/code/app/telegram
            - /opt/marzban/marzban-telebot/config.py:/code/config.py
```
Then you have to edit your `.env` file.
edit like this:

**WARNING: `TELEGRAM_ADMIN_ID` renamed to `TELEGRAM_ADMINS_ID`**
```
TELEGRAM_API_TOKEN = 123456789:AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
TELEGRAM_ADMINS_ID = 987654321, 123456789
TELEGRAM_LOGGER_CHANNEL_ID = -1234567891234
TELEGRAM_DEFAULT_VLESS_XTLS_FLOW = "xtls-rprx-vision"
```

For logger channel you have to create a channel (its better to private), and send a message to the channel,
then forward the message to <a href="https://t.me/userinfobot">userinfobot</a> the bot send you the channel id


Now you can restart your marzban's docker:
```
marzban restart
```

# Обновить

For update just need to pull repository and restart:
```bash
cd /opt/marzban/marzban-telebot/
git pull
marzban restart
```
