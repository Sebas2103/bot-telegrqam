from typing import Final
from  telegram import Update
from telegram.ext import Aplication ,CommandHandler,MessageHandler,filters,ContextTypes

TOKEN:Final="7004412096:AAH5kltUrZmD9TCOhCr8bmbgxEfa_a-Jb9o";
BOT_USERNAME:Final="@tensasbot";
#commands
async def start_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola como estas es mi bot de telegram hecho por python Sebas")

async def start_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Soy el primer bot de telegram hecho por mi creador")
async def start_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Soy TensasBot ,bienvenido!")
#Reponses

def handle_reponse(text:str)->str:
    processed:str=text.lower();
    if "hola"or "Hola" in processed:
        return "Hola"
    if "como estas"or "Como estas?" in processed:
        return "estoy super bien"
    return "no puedo entenderte"
async def handle_message(update:Update, Context:ContextTypes.DEFAULT_TYPE):
    message_type:str= update.message.chat.type
    text: str=update.text
    print(f'User({update.message.chat.id}in {message_type})')