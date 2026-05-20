import random, string

def random_sentence():
    subjects = ["The cat", "A dog", "The programmer", "My neighbor", "The teacher", "A bird", "The robot", "Every child", "The artist", "No one"]
    verbs = ["runs", "jumps", "codes", "sings", "dances", "sleeps", "eats", "thinks", "creates", "explores"]
    objects = ["in the park", "at midnight", "with passion", "under the stars", "every morning", "near the river", "on the roof", "in the code", "without fear", "for hours"]
    return "{} {} {}.".format(random.choice(subjects), random.choice(verbs), random.choice(objects))

def random_poem():
    templates = [
        "Roses are {adj1},\nViolets are {adj2},\nYou are {adj3},\nAnd I {verb} you.",
        "The {noun1} {verb1} in the {noun2},\nWhile the {noun3} {verb2} above,\n{adj1} is the {noun4} of {noun5},\nAnd {noun6} is the {noun7} of love.",
        "I saw a {adj1} {noun1} today,\nIt made me {verb1} and {verb2},\n{adv1} I {verb3} away,\nTo a {adj2} {noun2}.",
    ]
    adj1 = random.choice(["red", "blue", "bright", "dark", "soft", "wild", "calm", "brave"])
    adj2 = random.choice(["blue", "green", "clear", "deep", "warm", "free", "kind", "proud"])
    adj3 = random.choice(["wonderful", "beautiful", "special", "amazing", "lovely", "perfect"])
    noun1 = random.choice(["moon", "sun", "star", "cloud", "tree", "flower", "river", "mountain"])
    noun2 = random.choice(["sky", "sea", "field", "forest", "valley", "garden", "ocean", "dream"])
    noun3 = random.choice(["bird", "wind", "heart", "soul", "mind", "spirit", "light", "shadow"])
    noun4 = random.choice(["life", "time", "hope", "joy", "peace", "truth", "love", "grace"])
    noun5 = random.choice(["being", "living", "dreaming", "knowing", "feeling", "giving"])
    noun6 = random.choice(["patience", "wisdom", "beauty", "passion", "freedom", "silence"])
    noun7 = random.choice(["wisdom", "courage", "beauty", "knowledge", "harmony", "balance"])
    verb1 = random.choice(["shines", "dances", "weeps", "laughs", "glows", "dreams", "sings", "flies"])
    verb2 = random.choice(["sparkles", "whispers", "glitters", "shimmers", "blooms", "floats"])
    verb3 = random.choice(["ran", "flew", "walked", "drifted", "wandered", "floated"])
    adv1 = random.choice(["softly", "quickly", "slowly", "gently", "quietly", "bravely"])
    return random.choice(templates).format(**locals())

def random_haiku():
    lines = [
        ("An old silent pond", "A frog jumps into the pond", "Splash! Silence again"),
        ("The light of a candle", "Is transferred to another candle", "Spring twilight"),
        ("Autumn moonlight", "A worm digs silently", "Into the chestnut"),
        ("Lightning flash", "What I thought were faces", "Are flowers"),
        ("A world of dew", "And within every dewdrop", "A world of struggle"),
        ("The west wind whispered", "And touched the eyelids of spring", "The earth awakened"),
        ("Clouds come from time to time", "In my little garden", "Peace returns"),
        ("Over the wintry", "Forest, winds howl in rage", "With no leaves to blow"),
        ("A summer river", "Being crossed, how pleasing", "With sandals in my hands"),
        ("In the twilight rain", "These brilliant-hued hibiscus", "A lovely sunset"),
    ]
    return "\n".join(random.choice(lines))

def random_tongue_twister():
    twisters = [
        "She sells seashells by the seashore.",
        "Peter Piper picked a peck of pickled peppers.",
        "How much wood would a woodchuck chuck if a woodchuck could chuck wood?",
        "Betty Botter bought some butter but she said the butter's bitter.",
        "I saw Susie sitting in a shoeshine shop.",
        "Fuzzy Wuzzy was a bear. Fuzzy Wuzzy had no hair.",
        "Six slippery snails slid slowly seaward.",
        "Unique New York, unique New York, unique New York.",
        "Red lorry, yellow lorry, red lorry, yellow lorry.",
        "Four fine fresh fish for you.",
        "I slit a sheet, a sheet I slit, upon a slitted sheet I sit.",
        "Three free throws from the free throw line.",
        "Tom threw Tim three thumbtacks.",
        "Which wristwatches are Swiss wristwatches?",
        "Black bug's blood, blue bug's blood.",
        "I'm not a pheasant plucker, I'm a pheasant plucker's son.",
        "Pad kid poured curd pulled cod.",
        "We surely shall see the sunshine soon.",
        "Lesser leather never weathered wetter weather better.",
        "A proper cup of coffee from a proper copper coffee pot.",
    ]
    return random.choice(twisters)

def random_proverb():
    proverbs = [
        "A journey of a thousand miles begins with a single step.",
        "Actions speak louder than words.",
        "All good things come to those who wait.",
        "A picture is worth a thousand words.",
        "Birds of a feather flock together.",
        "Cleanliness is next to godliness.",
        "Don't bite the hand that feeds you.",
        "Don't count your chickens before they hatch.",
        "Don't put all your eggs in one basket.",
        "Every cloud has a silver lining.",
        "Fortune favors the bold.",
        "Give a man a fish and you feed him for a day; teach a man to fish and you feed him for a lifetime.",
        "Haste makes waste.",
        "Honesty is the best policy.",
        "If it ain't broke, don't fix it.",
        "If you can't beat them, join them.",
        "Ignorance is bliss.",
        "It takes two to tango.",
        "Knowledge is power.",
        "Laughter is the best medicine.",
        "Look before you leap.",
        "Necessity is the mother of invention.",
        "No pain, no gain.",
        "Practice makes perfect.",
        "Practice what you preach.",
        "Rome wasn't built in a day.",
        "The early bird catches the worm.",
        "The grass is always greener on the other side.",
        "The pen is mightier than the sword.",
        "There's no place like home.",
        "Time heals all wounds.",
        "Too many cooks spoil the broth.",
        "When in Rome, do as the Romans do.",
        "Where there's a will, there's a way.",
        "You can't judge a book by its cover.",
        "You reap what you sow.",
    ]
    return random.choice(proverbs)

def random_idiom():
    idioms = [
        "Break the ice", "Hit the nail on the head", "Piece of cake", "Spill the beans",
        "Cost an arm and a leg", "Under the weather", "Once in a blue moon", "Bite the bullet",
        "Let the cat out of the bag", "Best of both worlds", "Cut corners", "Make a long story short",
        "Miss the boat", "Hit the sack", "Go back to the drawing board", "Call it a day",
        "Barking up the wrong tree", "When pigs fly", "The ball is in your court",
        "Kill two birds with one stone", "Add insult to injury", "Steal someone's thunder",
        "Face the music", "Beat around the bush", "Burn the midnight oil",
        "Go the extra mile", "Let sleeping dogs lie", "Read between the lines",
        "The best thing since sliced bread", "Your guess is as good as mine",
    ]
    return random.choice(idioms)

def random_simile():
    similes = [
        "As busy as a bee", "As blind as a bat", "As clean as a whistle",
        "As cold as ice", "As dry as a bone", "As easy as pie",
        "As free as a bird", "As gentle as a lamb", "As hard as nails",
        "As light as a feather", "As old as the hills", "As proud as a peacock",
        "As quick as lightning", "As quiet as a mouse", "As strong as an ox",
        "As sweet as honey", "As tall as a giraffe", "As thin as a rake",
        "As tough as leather", "As warm as toast", "As white as snow",
        "As wise as an owl", "As brave as a lion", "As clumsy as a bear",
        "As cunning as a fox", "As fierce as a tiger", "As graceful as a swan",
        "As happy as a clam", "As hungry as a wolf", "As lazy as a sloth",
    ]
    return random.choice(similes)

def random_metaphor():
    metaphors = [
        "Time is a thief.", "Life is a highway.", "Love is a battlefield.",
        "The world is a stage.", "Her voice was music to his ears.",
        "His heart is a cold iron.", "The classroom was a zoo.",
        "The city is a concrete jungle.", "Fear is a shadow.",
        "Hope is a beacon.", "Memory is a library.",
        "The mind is a computer.", "Dreams are seeds.",
        "Anger is a fire.", "Laughter is medicine.",
        "Friendship is a shelter.", "Wisdom is a tree.",
        "The night is a blanket.", "The sun is a golden coin.",
        "Courage is a muscle.", "Kindness is a gift.",
        "The road is a ribbon.", "The storm is a wild beast.",
        "Silence is a canvas.", "Knowledge is a light.",
        "The future is a mystery.", "The past is a ghost.",
        "Truth is a mirror.", "The heart is a compass.",
    ]
    return random.choice(metaphors)

def random_oxymoron():
    oxymorons = [
        "Jumbo shrimp", "Deafening silence", "Living dead",
        "Original copy", "Open secret", "Awfully good",
        "Bittersweet", "Controlled chaos", "Clearly confused",
        "Dark light", "Deceptively honest", "Definite maybe",
        "Divided unity", "Dull roar", "Exact estimate",
        "Found missing", "Free love", "Friendly fire",
        "Good grief", "Growing smaller", "Hell's angels",
        "Honest liar", "Icy hot", "Ignorant wisdom",
        "Inner peace", "Instant classic", "Intense apathy",
        "Jumbo shrimp", "Loud whisper", "Love-hate",
        "Married bachelor", "Microsoft Works", "Military intelligence",
        "Minor crisis", "Moving still life", "Negative growth",
        "Old news", "Only choice", "Original copy",
        "Painful joy", "Passive aggressive", "Permanent temporary",
        "Pretty ugly", "Random order", "Sad smile",
        "Same difference", "Serious fun", "Silent scream",
        "Small crowd", "Soft rock", "Sweet sorrow",
        "Terrible beauty", "True lies", "Unbiased opinion",
        "Virtual reality", "Working vacation", "Controlled freedom",
        "Deliberate mistake", "Falsely true", "Happily miserable",
        "Known secret", "Loving hate", "Minor miracle",
    ]
    return random.choice(oxymorons)

def random_palindrome_word():
    words = ["racecar", "madam", "level", "radar", "civic", "refer", "noon", "kayak",
             "tenet", "stats", "solos", "rotor", "minim", "malam", "terret", "redder",
             "deified", "repoper", "malayalam", "tattarrattat"]
    return random.choice(words)

def anagram_generator(word):
    chars = list(word)
    random.shuffle(chars)
    return "".join(chars)
