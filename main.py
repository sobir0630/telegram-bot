from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config import TOKEN

from handlers import(
    start, 
    help,
    echo, 
    echo_photo, 
    echo_video, 
    echo_location,
    echo_animation,
    echo_voice,
    echo_video_note,
    echo_contact
)


updater = Updater(TOKEN)
dispatcher = updater.dispatcher

# command handler
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))


# message handler
dispatcher.add_handler(MessageHandler(Filters.text, echo))
dispatcher.add_handler(MessageHandler(Filters.photo, echo_photo))
dispatcher.add_handler(MessageHandler(Filters.video, echo_video))
dispatcher.add_handler(MessageHandler(Filters.location, echo_location))
dispatcher.add_handler(MessageHandler(Filters.animation, echo_animation))
dispatcher.add_handler(MessageHandler(Filters.voice, echo_voice))
dispatcher.add_handler(MessageHandler(Filters.video_note, echo_video_note))
dispatcher.add_handler(MessageHandler(Filters.contact, echo_contact))

print("Bot is running...")  # Optional: Print a message to indicate the bot is running
updater.start_polling()
updater.idle()
