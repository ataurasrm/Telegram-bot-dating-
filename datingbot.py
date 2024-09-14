import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

API_TOKEN = '7432199919:AAGwPFRrSd2kP_1UTsU0kJ0BADOF13M_1NE'  # Replace with your actual token

# Function to log conversation to a text file
def log_conversation(user_id, message, response):
    log_dir = "conversations"
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    with open(f"{log_dir}/{user_id}_conversation.txt", "a") as file:
        file.write(f"User: {message}\n")
        file.write(f"Bot: {response}\n\n")

# Initial introduction
def start(update: Update, context: CallbackContext):
    user = update.message.from_user
    response = f"Hey, I'm Milla Zadow from Los Angeles, USA. What about you, {user.first_name}?"
    update.message.reply_text(response)
    
    # Log the conversation
    log_conversation(user.id, update.message.text, response)

# Conversation flow
def handle_message(update: Update, context: CallbackContext):
    message_text = update.message.text.lower()
    user = update.message.from_user

    # Step 1: Traffic activity question after introduction
    if "how are you" in message_text:
        response = "I'm doing great! So, what are you up to today? Busy with work, or just chilling?"
    
    # Step 2: Engage user with their traffic or interests
    elif "nothing much" in message_text or "chilling" in message_text:
        response = "That's cool! Just curious, do you use any dating apps?"
    
    # Step 3: Ask about dating preferences
    elif "yes" in message_text or "sometimes" in message_text:
        response = "Awesome! I think I have something you'll like. Do you prefer serious relationships or just casual dating?"
    
    # Step 4: If interested, share the CPA link
    elif "casual" in message_text or "serious" in message_text:
        cpa_link = "https://sites.google.com/view/sextingnow/home"
        response = f"Great! Here's a dating offer you might like: {cpa_link}"
    
    # If not interested in dating, continue conversation
    else:
        response = "No worries! But dating can be fun. Want me to suggest something exciting?"

    # Send the response back to the user
    update.message.reply_text(response)
    
    # Log the conversation
    log_conversation(user.id, message_text, response)

# Main function to start the bot
def main():
    updater = Updater(API_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
