from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, Dispatcher
from settings import TOKEN


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text(text="Assalomu alaykum")


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text(f'{update.message.from_user.full_name}, Nima yordam kerak!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def echo_photo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text('siz photo yubordingiz')


def echo_video(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text('siz video yubordingiz')


def echo_voice(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text('siz voice yubordingiz')


def main() -> None:
    """Start the bot."""
    updater = Updater(TOKEN)

    dispatcher: Dispatcher = updater.dispatcher

    # command handler
    dispatcher.add_handler(CommandHandler("boshlash", start))
    dispatcher.add_handler(CommandHandler("yordam", help_command))

    # message handler
    dispatcher.add_handler(MessageHandler(Filters.text, echo))
    dispatcher.add_handler(MessageHandler(Filters.photo, echo_photo))
    dispatcher.add_handler(MessageHandler(Filters.video, echo_video))
    dispatcher.add_handler(MessageHandler(Filters.voice, echo_voice))

    # start
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
