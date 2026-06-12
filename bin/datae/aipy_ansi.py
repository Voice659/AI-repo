import os, sys, datetime, random

if os.name == "nt":
    os.system("color")
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except:
        pass
C_RESET = "\033[0m"
C_RED = "\033[91m"
C_GREEN = "\033[92m"
C_YELLOW = "\033[93m"
C_BLUE = "\033[94m"
C_MAGENTA = "\033[95m"
C_CYAN = "\033[96m"
C_BOLD = "\033[1m"
C_DIM = "\033[2m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def get_time_greeting():
    h = datetime.datetime.now().hour
    if h < 6 or h >= 22:
        return "You're up late"
    if h < 12:
        return "Good morning"
    if h < 18:
        return "Good afternoon"
    return "Good evening"

def random_greeting():
    langs = [("Hello","English"),("Hola","Spanish"),("Bonjour","French"),("Ciao","Italian"),
             ("Konnichiwa","Japanese"),("Namaste","Hindi"),("Salaam","Arabic"),("Zdravo","Serbian"),
             ("Ni hao","Chinese"),("Annyeong","Korean"),("Guten Tag","German"),("Ola","Portuguese"),
             ("Privet","Russian"),("Merhaba","Turkish"),("Sawadee","Thai"),("Jambo","Swahili"),
             ("Goddag","Danish"),("Hej","Swedish"),("Hei","Norwegian"),("Hei","Finnish"),
             ("Dzien dobry","Polish"),("Ahoj","Czech"),("Buna ziua","Romanian"),("Zdraveite","Bulgarian"),
             ("Yassou","Greek"),("Shalom","Hebrew"),("Salam","Persian"),("Chao","Vietnamese"),
             ("Kumusta","Filipino"),("Apa khabar","Malay"),("Halo","Indonesian"),("Sawubona","Zulu"),
             ("Dia duit","Irish"),("Salut","Catalan"),("Hej","Icelandic"),("Sveiki","Latvian"),
             ("Labas","Lithuanian"),("Tere","Estonian"),("Szia","Hungarian"),("Cze","Polish short"),
             ("Marhaba","Lebanese"),("Ahla","Jordanian"),("Sannu","Hausa"),("Molo","Xhosa"),
             ("Nde-wo","Ewe"),("Kia ora","Maori"),("Talofa","Samoan"),("Bula","Fijian"),
             ("Hafa adai","Chamorro"),("Aloha","Hawaiian")]
    return random.choice(langs)
