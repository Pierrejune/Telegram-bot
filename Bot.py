import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import logging

# Configuration du logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Chargement du token de l'API Telegram
TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TOKEN:
    raise ValueError("❌ ERREUR : La variable d'environnement TELEGRAM_TOKEN est absente.")

bot = telebot.TeleBot(TOKEN)

# Configuration de base
test_mode = True
mise_depart = 5
stop_loss_levels = [(30, 50), (200, 100), (1000, 100)]
influencers_to_monitor = [
    "elonmusk", "VitalikButerin", "BillyM2k", "SatoshiLite", "mcuban", "SnoopDogg",
    "officialmcafee", "AkitaInu", "KishuToken", "Shibtoken", "dogecoinfoundatio"
]
detected_tokens = {}

# Commande /start
@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "🤖 Bienvenue sur ton bot de trading de memecoins !")
    show_main_menu(message.chat.id)

# Menu principal
def show_main_menu(chat_id):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("📈 Statut", callback_data="status"),
        InlineKeyboardButton("⚙️ Configurer", callback_data="config"),
        InlineKeyboardButton("🚀 Lancer", callback_data="launch"),
        InlineKeyboardButton("❌ Arrêter", callback_data="stop")
    )
    bot.send_message(chat_id, "Que veux-tu faire ?", reply_markup=markup)

# Gestion des callbacks
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global test_mode, mise_depart

    try:
        if call.data == "status":
            bot.send_message(call.message.chat.id, f"📊 Ton statut :\n- Mise: {mise_depart}€\n- Mode test: {test_mode}")
        elif call.data == "config":
            show_config_menu(call.message.chat.id)
        elif call.data == "launch":
            bot.send_message(call.message.chat.id, "🚀 Le bot a commencé à trader !")
            detect_new_tokens(call.message.chat.id)
            monitor_influencers_and_devs(call.message.chat.id)
        elif call.data == "stop":
            bot.send_message(call.message.chat.id, "⏹ Le bot a arrêté le trading.")
        elif call.data == "set_mise":
            mise_depart += 5
            bot.send_message(call.message.chat.id, f"💰 Mise augmentée à {mise_depart}€")
        elif call.data == "toggle_test":
            test_mode = not test_mode
            bot.send_message(call.message.chat.id, f"🎯 Mode Test {'activé' if test_mode else 'désactivé'}.")
    except Exception as e:
        logging.error(f"Erreur dans callback_query: {str(e)}")
        bot.send_message(call.message.chat.id, "⚠️ Une erreur est survenue.")

# Menu de configuration
def show_config_menu(chat_id):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("💰 Modifier mise", callback_data="set_mise"),
        InlineKeyboardButton("🎯 Activer/Désactiver Mode Test", callback_data="toggle_test")
    )
    bot.send_message(chat_id, "⚙️ Configuration du bot :", reply_markup=markup)

# Détection automatique des tokens (simulation)
def detect_new_tokens(chat_id):
    global detected_tokens
    new_token = "TOKEN_XYZ"
    detected_tokens[new_token] = {"status": "sain"}
    bot.send_message(chat_id, f"🆕 Nouveau token détecté : {new_token}.")
    
    if is_rug_pull(new_token):
        bot.send_message(chat_id, f"⚠️ Attention : {new_token} semble être un rug pull et a été ignoré.")
    else:
        bot.send_message(chat_id, f"✅ {new_token} ajouté pour le trading.")

# Surveillance des influenceurs et développeurs (simulation)
def monitor_influencers_and_devs(chat_id):
    for influencer in influencers_to_monitor:
        bot.send_message(chat_id, f"👀 Surveillance de {influencer} en cours.")
        check_influencer_activity(influencer)

def check_influencer_activity(influencer):
    logging.info(f"Vérification de l'activité de {influencer}")

# Vérification des rug pulls
def is_rug_pull(token):
    return token not in detected_tokens

# Lancer le bot en mode polling
if __name__ == "__main__":
    logging.info("✅ Bot lancé en mode polling...")
    bot.infinity_polling()
