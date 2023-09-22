from datetime import datetime
from app.db import GetDB, crud
from app.models.user import UserResponse
from app.telegram import bot
from pytz import UTC
from telebot.custom_filters import ChatFilter
from telebot.util import extract_arguments

from app.utils.system import readable_size

bot.add_custom_filter(ChatFilter())



@bot.message_handler(commands=['usage'])
def usage_command(message):
    username = extract_arguments(message.text)
    if not username:
        return bot.reply_to(message, 'Usage: `/usage <username>`', parse_mode='MarkdownV2')

    with GetDB() as db:
        dbuser = crud.get_user(db, username)

        if not dbuser:
            return bot.reply_to(message, "Такого пользователя нет")
        user = UserResponse.from_orm(dbuser)

        statuses = {
            'активный': '✅',
            'истекает': '🕰',
            'ограничен': '📵',
            'отключен': '❌'}

        text = f'''\
<b>Имя: </b> <code>{user.username}</code> 
{statuses[user.status]} <b>Статус:</b> <code>{user.status.title()}</code>
<b>Трафик: </b> <code>{readable_size(user.data_limit) if user.data_limit else 'безлимит'}</code>
<code>{f'<b>Использовано: </b> {readable_size(user.used_traffic)}' if user.used_traffic else ''}</code>
<b>Срок:</b> <code>{datetime.fromtimestamp(user.expire).date() if user.expire else 'бессрочно'}</code>
<code>{f'<b>Дней осталось: </b>'(datetime.fromtimestamp(user.expire or 0) - datetime.now()).days if user.expire else ''}</code>'''

    return bot.reply_to(message, text, parse_mode='HTML')
