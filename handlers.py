from telegram import Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    user = update.message.from_user

    update.message.reply_text(
        f'Assalomu alaykum! Botimizga xush kelibsiz {user.full_name}.\n\n'
        'bu bot testing uchun'
    )


def help(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Qanday Yordam Kerak'
    )


def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)
