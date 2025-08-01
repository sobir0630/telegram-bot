from telegram import Update
from telegram.ext import CallbackContext



def start(update: Update, context: CallbackContext):
    user = update.message.from_user

    update.message.reply_text(
        f'Assalomu alaykum! Botimizga xush kelibsiz {user.full_name}.\n\n'
        'bu bot testing uchun /help komandasini bosing.\n\n'
    )


# /help komandasini ishlovchi funksiya
def help(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Qanday Yordam Kerak\n\n'
        '/start - Botni ishga tushirish\n'
        '/help - Yordam\n'
    )

# reply text handlers
def echo(update: Update, context: CallbackContext):
    update.message.reply_text(update.message.text)
    
#  reply photo handlers   
def echo_photo(update: Update, context: CallbackContext):
    update.message.reply_photo(update.message.photo[-1].file_id, caption=update.message.caption)

#  reply video handlers
def echo_video(update: Update, context: CallbackContext):
    update.message.reply_video(update.message.video.file_id, caption=update.message.caption)

#  reply animation handlers
def echo_animation(update: Update, context: CallbackContext):
    animation = update.message.animation
    update.message.reply_animation(animation=animation.file_id, caption=update.message.caption)

# echo location
def echo_location(update: Update, context: CallbackContext):
    update.message.reply_location(
        latitude=update.message.location.latitude,
        longitude=update.message.location.longitude
    )

# reply voice handlers
def echo_voice(update: Update, context: CallbackContext):
    update.message.reply_voice(update.message.voice.file_id, caption=update.message.caption)

# reply video_note handlers
def echo_video_note(update: Update, context: CallbackContext):
    update.message.reply_video_note(update.message.video_note.file_id)

# reply video_note handlers
def echo_contact(update: Update, context: CallbackContext):
    update.message.reply_contact(
        phone_number=update.message.contact.phone_number,
        first_name=update.message.contact.first_name,
        last_name=update.message.contact.last_name
    )