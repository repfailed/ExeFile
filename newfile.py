from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
Application,
CommandHandler,
MessageHandler,
filters,
CallbackContext
)

TOKEN = "7846106769:AAHqq_v2Djm9zcEc1M5qqGHmYS68tpv6zu8"

Function to handle /start

async def start(update: Update, context: CallbackContext): keyboard = [["Admin", "Exe"], ["Want to join exe 神"]] reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True) await update.message.reply_text("Yokoso, welcome to my Exe. What are you looking for?", reply_markup=reply_markup)

Function to handle "Admin" option

async def admin(update: Update, context: CallbackContext): await update.message.reply_text("The admin of the bot is Izana of Exe, known as @repfailed")

Function to handle "Exe" option

async def exe(update: Update, context: CallbackContext): keyboard = [["Want to learn banning"], ["Unban", "Banning", "New banner"], ["Back"]] reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True) await update.message.reply_text("Choose an option:", reply_markup=reply_markup)

Function to handle "Want to learn banning"

async def learn_banning(update: Update, context: CallbackContext): keyboard = [["Impersonation", "Suicide/self"], ["Hate", "Violation"], ["Selling illegal", "Spam"], ["False information", "Bullying/Harassment"], ["Nudity"], ["Back"]] reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True) await update.message.reply_text("Select a category for banning:", reply_markup=reply_markup)

Function to handle "Impersonation"

async def impersonation(update: Update, context: CallbackContext): keyboard = [["Back"]] reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True) await update.message.reply_text( "Impersonation:\n\n" "Yes, it's impersonation. If you find a profile using the same or a similar profile picture as a verified account, you can report it for impersonation. Many verified profiles are commonly used for impersonation, and you can find a list of them in the 'Banning' section of the previous menu.\n\n" "Cloning: Cloning is a form of impersonation where someone creates an account that closely mimics another user's profile. This method requires an account older than the targeted one, i.e., 2k12 or etc. This usually involves copying the same username (with slight variations), profile picture, bio, and other details to make the fake account look as authentic as possible. The purpose of cloning is often to deceive others, spread misinformation, or engage in scams while pretending to be the original user.\n\n" "Since cloning falls under impersonation bans, such accounts can be reported and removed. If you need a more detailed explanation or examples, the Exe admins can provide further insights.\n\n" "Exe admins - @repfailed || @lazyxst\n" "On Instagram\n\n" "Thank you!", reply_markup=reply_markup )

Function to handle category selections

async def banning_category(update: Update, context: CallbackContext): await update.message.reply_text(f"You selected: {update.message.text}. More details coming soon.", reply_markup=ReplyKeyboardMarkup([["Back"]], resize_keyboard=True))

Function to handle "Unban"

async def unban(update: Update, context: CallbackContext): await update.message.reply_text("soon")

Function to handle "Banning"

async def banning(update: Update, context: CallbackContext): await update.message.reply_text("soon")

Function to handle "New banner"

async def new_banner(update: Update, context: CallbackContext): await update.message.reply_text("soon")

Function to handle "Want to join exe 神"

async def join_exe(update: Update, context: CallbackContext): await update.message.reply_text( "Sure! Currently, there are three admins of Exe:\n" "Izana - @repfailed\n" "Zesty - @lazyxst\n" "Gin - @slowbans\n\n" "You can DM us on Instagram, we will reply as soon as possible." )

Function to handle "Back" button

async def back(update: Update, context: CallbackContext): await learn_banning(update, context)

Function to log errors

def error_handler(update: object, context: CallbackContext): print(f"Update {update} caused error {context.error}")

Create the bot application

app = Application.builder().token(TOKEN).build()

Command Handlers (for slash commands)

app.add_handler(CommandHandler("start", start)) app.add_handler(CommandHandler("admin", admin)) app.add_handler(CommandHandler("exe", exe))

Message Handlers (for text commands)

app.add_handler(MessageHandler(filters.Regex("^Admin$"), admin)) app.add_handler(MessageHandler(filters.Regex("^Exe$"), exe)) app.add_handler(MessageHandler(filters.Regex("^Want to join exe 神$"), join_exe)) app.add_handler(MessageHandler(filters.Regex("^Want to learn banning$"), learn_banning)) app.add_handler(MessageHandler(filters.Regex("^Impersonation$"), impersonation)) app.add_handler(MessageHandler(filters.Regex("^Back$"), back))

Error Logging

app.add_error_handler(error_handler)

Start polling

app.run_polling()

