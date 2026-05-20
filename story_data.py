import random

def generate_story():
    templates = [
        "Once upon a time, there was a {adj1} {noun1} who lived in a {adj2} {noun2}. Every day, they would {verb1} to the {noun3} and {verb2} with the {adj3} {noun4}. One day, a {adj4} {noun5} appeared and said: '{quote}' This changed everything. From that day on, the {noun1} was never {adj5} again.",
        "In the land of {place}, a {adj1} {noun1} discovered a {adj2} {noun2} hidden beneath a {noun3}. It had the power to {verb1} anything it touched. The {noun1} knew they had to {verb2} it from the {adj3} {noun4}. With the help of a {adj4} {noun5}, they embarked on a {adj5} journey.",
        "The year was {year}. The world had changed. {adj1} {noun1} now ruled the {noun2}, and {adj2} {noun3} were a thing of the past. But one {noun4} held the key to {verb1} everything. They just needed to find the {adj3} {noun5} before it was too {adj4}.",
        "It was a {adj1} day when {name} found the {noun1}. It was {adj2} and {adj3}, unlike anything they had ever seen. {name} knew it belonged to a {noun2} who lived in the {adj4} {noun3}. The journey there was {adj5}, but the reward was {noun4} itself.",
        "Deep in the {adj1} {noun1}, there lived a {adj2} {noun2} who dreamed of {verb1} the {noun3}. Every {noun4}, they would {verb2} a little closer to their goal. One {adj3} {noun5} helped them realize that the real treasure was the {noun6} they made along the way.",
        "The {adj1} {noun1} had been sleeping for {number} years. When it finally woke, the {noun2} began to {verb1} in strange ways. The {adj2} {noun3} knew they had to {verb2} the {adj3} {noun4} before the {noun5} was lost forever. It was a race against {noun6}.",
    ]
    place = random.choice(["Avalon","El Dorado","Shangri-La","Atlantis","Narnia","Middle-earth","Westeros","Hyrule","Zelda","Moria","Gondor","Rivendell","Hogwarts","Neverland","Oz","Wonderland","Camelot","Asgard","Nibelheim","Xanadu"])
    name = random.choice(["Luna","Orion","Cassandra","Merlin","Aria","Fenrir","Thalia","Eldric","Sylvan","Nova","Zephyr","Iris","Apollo","Ember","Frost"])
    adj1 = random.choice(["brave","fierce","curious","lonely","ancient","mighty","gentle","wise","foolish","kind","proud","hungry","sleepy","magical","dark","bright","silent","swift","clever","bold"])
    adj2 = random.choice(["deep","enchanted","hidden","golden","silent","crystal","misty","shimmering","crimson","emerald","shadowy","frozen","burning","twisted","sacred"])
    adj3 = random.choice(["mysterious","faithful","courageous","powerful","graceful","ancient","noble","tricky","wild","royal","blessed","cursed","forgotten","distant"])
    adj4 = random.choice(["sudden","terrible","wonderful","strange","fearsome","brilliant","unexpected","glorious","dark","radiant"])
    adj5 = random.choice(["afraid","alone","lost","broken","content","humble","restless","forlorn","hopeful","changed"])
    noun1 = random.choice(["knight","wizard","dragon","princess","warrior","elf","dwarf","mage","rogue","ranger","bard","paladin","sorcerer","druid","hunter"])
    noun2 = random.choice(["forest","castle","mountain","temple","kingdom","village","cave","river","valley","tower","gate","bridge","island","desert","city"])
    noun3 = random.choice(["treasure","portal","artifact","garden","library","sanctuary","well","mine","market","hall","shrine","pass","keep","grave","throne"])
    noun4 = random.choice(["friend","enemy","spirit","guardian","shadow","voice","heart","soul","mirror","crown","stone","blade","staff","ring","book","key","star","flame","crystal","coin"])
    noun5 = random.choice(["prophet","creature","entity","phantom","giant","serpent","eagle","wolf","bear","fox","owl","raven","stag","lion","tiger","panther"])
    noun6 = random.choice(["time","space","love","fate","hope","glory","honor","peace","power","knowledge","wisdom","truth","destiny","magic","life","death"])
    verb1 = random.choice(["seek","find","protect","destroy","create","explore","defend","conquer","heal","unlock","awaken","cross","enter","escape","reach","open","uncover","break"])
    verb2 = random.choice(["dance","sing","fight","fly","dream","laugh","speak","whisper","shout","pray","journey","climb","dive","ride","run","walk"])
    quote = random.choice([
        "The journey is the destination.", "Not all those who wander are lost.",
        "Even the smallest person can change the course of the future.", "To the well-organized mind, death is but the next great adventure.",
        "It does not do to dwell on dreams and forget to live.", "Happiness can be found even in the darkest of times.",
        "All we have to decide is what to do with the time that is given us.", "The world is not in your books and maps, it is out there.",
        "There is some good in this world, and it is worth fighting for.", "Courage is not the absence of fear, but the triumph over it.",
        "The only way to have a friend is to be one.", "Believe you can and you are halfway there.",
        "It is not the strongest who survive, but those most adaptable to change.", "In the middle of difficulty lies opportunity.",
        "The greatest glory in living lies not in never falling, but in rising every time we fall.",
        "The future belongs to those who believe in the beauty of their dreams.",
    ])
    year = random.choice(["2024","2050","1984","3000","1066","1776","1945","1969","1492","2020","2525","1888","9999","0123"])
    number = str(random.randint(100, 10000))
    template = random.choice(templates)
    return template.format(**locals())

def random_joke_theme(theme):
    theme_jokes = {
        "programming": [
            "Why do programmers hate nature? Too many bugs.", "A SQL query walks into a bar and asks for two tables.",
            "Why was the JavaScript developer sad? He didn't know how to 'null' his feelings.",
            "I would tell you a UDP joke but you might not get it.", "There are 10 types of people in the world.",
            "Why do Java devs wear glasses? They can't C#.", "How many programmers to change a light bulb? None, that's hardware.",
            "A programmer's wife says: 'Go to the store and get milk. If they have eggs, get 12.' He comes back with 12 milks.",
            "Why did the developer go broke? He used up all his cache.", "Debugging: removing the bugs you just added.",
        ],
        "animal": [
            "What do you call a bear with no teeth? A gummy bear.", "Why don't elephants use computers? They're afraid of the mouse.",
            "What do you call a fish with no eyes? A fsh.", "Why did the chicken cross the road? To get to the other side.",
            "What do you call a cow with no legs? Ground beef.", "Why do cats make great programmers? They're excellent at debugging.",
            "What do you get when you cross a snowman and a vampire? Frostbite.", "What's a cat's favorite button? Paws.",
        ],
        "food": [
            "Why did the tomato turn red? It saw the salad dressing.", "What do you call a fake noodle? An impasta.",
            "Why did the cookie go to the doctor? It felt crummy.", "What's orange and sounds like a parrot? A carrot.",
            "Why did the banana go to the hospital? It wasn't peeling well.", "What do you call cheese that isn't yours? Nacho cheese.",
            "Why did the egg hide? It was a chicken.", "What's a potato's favorite movie? The Mask-ed potato.",
        ],
        "science": [
            "Why don't scientists trust atoms? They make up everything.", "What did the proton say to the electron? 'You're so negative.'",
            "Why did the biology teacher resign? There were too many tests.", "What is a physicist's favorite food? Fission chips.",
            "Why did the chemist break up with the physicist? There was no reaction.", "What do you call a tooth in a glass of water? A one molar solution.",
            "Why are chemists great at solving problems? They have all the solutions.",
        ],
        "sports": [
            "Why did the golfer wear two pairs of pants? In case he got a hole in one.", "What is a tennis player's favorite type of music? Racket.",
            "Why can't basketball players hide? They always dribble.", "What's a hockey player's favorite dance? The puck.",
            "Why do soccer players do well in school? They know how to use their heads.",
        ],
        "music": [
            "Why did the musician get arrested? He got into treble.", "What do you call a sad guitar? A blues guitar.",
            "Why did the piano get locked out? It had the wrong key.", "What's a musician's favorite insect? A drum beatle.",
            "Why did the singer climb a ladder? To hit the high notes.",
        ],
        "math": [
            "Why was the math book sad? It had too many problems.", "What do you call a number that can't stand still? A roamin' numeral.",
            "Why was the equal sign so humble? It knew it wasn't less than or greater than anyone else.",
            "Why did the student eat his homework? The teacher said it was a piece of cake.",
            "What do you call a dead parrot? A polygon.",
        ],
        "history": [
            "Why did the archaeologist go bankrupt? His career was in ruins.", "What did the Roman say when he walked into a bar? 'I'd like a martius, please.'",
            "Why was the pharaoh so confident? He believed in pyramid schemes.", "What did the history book say to the math book? 'I've got more stories than you.'",
            "Why were the Dark Ages called the Dark Ages? Because there were so many knights.",
        ],
    }
    if theme in theme_jokes:
        return random.choice(theme_jokes[theme])
    return "No jokes for that theme."

def random_conversation_starter():
    starters = [
        "If you could have dinner with any historical figure, who would it be?",
        "What is the most interesting fact you know?",
        "If you could travel anywhere right now, where would you go?",
        "What book changed your perspective on something?",
        "If you could instantly master any skill, what would it be?",
        "What's the best piece of advice you ever received?",
        "What mystery do you wish was solved?",
        "If you could witness any historical event, what would it be?",
        "What's a movie that you think everyone should watch?",
        "If you could have any superpower, what would it be?",
        "What's the most beautiful place you've ever been?",
        "What song always gets stuck in your head?",
        "If you could meet any fictional character, who would it be?",
        "What's a small thing that makes you happy?",
        "What's the best invention of the last 100 years?",
        "If you could time travel, would you go to the past or future?",
        "What's your favorite way to spend a free day?",
        "What's something you've learned recently that surprised you?",
        "If you could solve one global problem, what would it be?",
        "What's a tradition you love?",
        "What's the most adventurous thing you've ever done?",
        "If you had to eat only one food for the rest of your life, what would it be?",
        "What's your favorite memory from childhood?",
        "What's something you're looking forward to?",
        "What's a skill you think everyone should learn?",
        "What's the most beautiful piece of art you've seen?",
        "If you could swap lives with someone for a day, who would it be?",
        "What's the most important lesson life has taught you?",
        "What's a dream you've given up on?",
        "What's something you want to learn but haven't yet?",
        "What movie made you cry?",
        "If you could write a book, what would it be about?",
        "What's your favorite season and why?",
        "What's something that always makes you laugh?",
        "What do you think happens after we die?",
        "What's the most courageous thing you've ever done?",
        "What does your ideal day look like?",
        "What's something you'd tell your younger self?",
        "What's a rule you live by?",
        "What's the best gift you ever received?",
        "If you could rename yourself, what would you pick?",
        "What's a place that feels like home?",
        "What's your favorite time of day?",
        "What's a habit you're proud of?",
        "If you could delete one thing from the world, what would it be?",
        "What's the hardest thing you've ever done?",
        "What's something you're grateful for today?",
        "What's a question you wish people would ask you?",
        "If you could have any animal as a pet (real or mythical), what would it be?",
        "What's the best decision you ever made?",
    ]
    return random.choice(starters)

def random_philosophical_question():
    questions = [
        "What is the meaning of life?",
        "Do we have free will?",
        "What is consciousness?",
        "Is reality objective or subjective?",
        "What is the nature of time?",
        "Is there a difference between the mind and the brain?",
        "What makes something moral?",
        "Do animals have rights?",
        "What is justice?",
        "Can artificial intelligence be conscious?",
        "What is the self?",
        "Does God exist?",
        "What is the nature of truth?",
        "Is it ever okay to lie?",
        "What is beauty?",
        "Is the universe deterministic?",
        "What is knowledge?",
        "Can we ever truly know anything?",
        "What is the difference between right and wrong?",
        "What is the purpose of art?",
        "Do we have a soul?",
        "What makes a life worth living?",
        "Is happiness the ultimate goal?",
        "What is the value of suffering?",
        "Should we fear death?",
        "What is the relationship between mind and body?",
        "Is there such a thing as objective morality?",
        "What is the nature of language?",
        "Can there be thought without language?",
        "What is the role of emotion in decision making?",
        "Is it possible to be completely impartial?",
        "What makes an action ethical?",
        "Is punishment justified?",
        "What is the nature of power?",
        "Is equality achievable?",
        "What is the meaning of freedom?",
        "What is the best form of government?",
        "Is democracy truly rule by the people?",
        "What are human rights?",
        "Should there be limits to freedom of speech?",
        "What is the nature of prejudice?",
        "Can we ever eliminate bias?",
        "What is the relationship between science and religion?",
        "Is there a purpose to the universe?",
        "What is the nature of quantum reality?",
        "What is the origin of the universe?",
        "Will technology save or destroy us?",
        "What is the ethical limit of scientific research?",
        "What is the nature of mathematical truth?",
        "Is logic inherent in the universe or a human construct?",
    ]
    return random.choice(questions)

def random_dad_joke():
    jokes = [
        "I'm reading a book on anti-gravity. It's impossible to put down.",
        "What do you call a fake noodle? An impasta.",
        "I told my wife she should embrace her mistakes. She gave me a hug.",
        "What do you call a factory that sells okay products? A satis-factory.",
        "Why did the scarecrow win an award? He was outstanding in his field.",
        "What's brown and sticky? A stick.",
        "I used to play piano by ear but now I use my hands.",
        "How does a penguin build a house? Igloos it together.",
        "What do you call a snowman with a six-pack? An abdominal snowman.",
        "Why don't eggs tell jokes? They'd crack each other up.",
        "What do you call a belt made of watches? A waist of time.",
        "Why did the bicycle fall over? It was two-tired.",
        "How do you organize a space party? You planet.",
        "What do you call a can opener that doesn't work? A can't opener.",
        "Why did the coffee go to the police? It got mugged.",
        "What's the best thing about Switzerland? I don't know, but the flag is a big plus.",
        "What do you call a fish wearing a bowtie? Sofishticated.",
        "What do you call a bear with no teeth? A gummy bear.",
        "What do you call a fish with no eyes? A fsh.",
        "What's orange and sounds like a parrot? A carrot.",
        "Why did the golfer wear two pairs of pants? In case he got a hole in one.",
        "Why don't scientists trust atoms? They make up everything.",
        "What do you call a programmer from Finland? Nerdic.",
        "Why was the math book sad? It had too many problems.",
        "How does a computer greet you? Hello, World!",
        "What do you call a computer that sings? A Dell.",
        "Why did the keyboard run away? It couldn't face the space bar.",
        "What do you call a mouse that can't stop eating? A track-ball.",
        "Why did the monitor go to the hospital? It had screen cancer.",
        "What do you call a printer that sings? A laser jet.",
        "Why did the hard drive go to therapy? It had a bad sector.",
        "What do you call a USB drive that tells jokes? A pun drive.",
        "Why did the database break up? It had too many foreign keys.",
        "Why did the developer go broke? He used up all his cache.",
        "What's a developer's favorite breakfast? A full-stack pancake.",
        "Why was the robot so happy? He had a motherboard.",
        "What did the computer do at lunchtime? Had a byte.",
        "Why did the computer keep freezing? It left its Windows open.",
        "What did the computer say when it won? I'm processing!",
        "Why do programmers hate nature? Too many bugs.",
        "What's a computer's favorite snack? Microchips.",
        "Why was the computer cold? It left its Windows open.",
        "A SQL query walks into a bar and asks for two tables.",
        "There are 10 types of people: those who understand binary and those who don't.",
        "How many programmers to change a light bulb? None, that's hardware.",
        "Why do Java devs wear glasses? They can't C#.",
        "I would tell you a UDP joke but you might not get it.",
        "99 little bugs in the code, 99 little bugs. Take one down, patch it around, 117 little bugs in the code.",
        "Programming is 10% writing code and 90% understanding why it's not working.",
        "A programmer's wife says: 'Go to the store and get milk. If they have eggs, get 12.' He comes back with 12 milks.",
    ]
    return random.choice(jokes)
