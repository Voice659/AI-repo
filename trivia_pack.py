import random

def movie_trivia():
    qs = [
        ("What year was The Godfather released?", "1972"),
        ("Who directed Jurassic Park?", "Spielberg"),
        ("What movie won the first Oscar?", "Wings"),
        ("Who played Jack in Titanic?", "Leonardo DiCaprio"),
        ("What is the highest grossing film ever?", "Avatar"),
        ("What year was the first Star Wars film released?", "1977"),
        ("Who voiced Woody in Toy Story?", "Tom Hanks"),
        ("What movie has the most Oscars?", "Ben-Hur"),
        ("Who directed Pulp Fiction?", "Quentin Tarantino"),
        ("What was the first animated feature film?", "Snow White"),
        ("What movie features the song My Heart Will Go On?", "Titanic"),
        ("Who played The Joker in The Dark Knight?", "Heath Ledger"),
        ("What year was The Matrix released?", "1999"),
        ("Who directed Schindler's List?", "Spielberg"),
        ("What is the longest movie ever made?", "The Cure for Insomnia"),
    ]
    q, a = random.choice(qs)
    ans = input("Q: {} ".format(q)).strip().lower()
    if ans == a.lower(): print("Correct!")
    else: print("Wrong! Answer: {}".format(a))

def music_trivia():
    qs = [
        ("Who is the best-selling artist of all time?", "The Beatles"),
        ("What band sang Bohemian Rhapsody?", "Queen"),
        ("Who is the King of Pop?", "Michael Jackson"),
        ("What instrument has 88 keys?", "Piano"),
        ("Who wrote the song Imagine?", "John Lennon"),
        ("What music festival happened in 1969?", "Woodstock"),
        ("Who is known as the King of Rock and Roll?", "Elvis Presley"),
        ("What year was MTV launched?", "1981"),
        ("Who sang Like a Rolling Stone?", "Bob Dylan"),
        ("What is the best-selling album of all time?", "Thriller"),
        ("Who composed the Four Seasons?", "Vivaldi"),
        ("What instrument is Yo-Yo Ma famous for?", "Cello"),
        ("Who is the best-selling female artist?", "Madonna"),
        ("What band had the album The Dark Side of the Moon?", "Pink Floyd"),
        ("Who wrote the opera The Magic Flute?", "Mozart"),
    ]
    q, a = random.choice(qs)
    ans = input("Q: {} ".format(q)).strip().lower()
    if ans == a.lower(): print("Correct!")
    else: print("Wrong! Answer: {}".format(a))

def sports_trivia():
    qs = [
        ("What sport has the most participants worldwide?", "Football"),
        ("How many players on a basketball team?", "5"),
        ("What country invented football?", "England"),
        ("Who has the most Olympic gold medals?", "Michael Phelps"),
        ("What sport is Wimbledon famous for?", "Tennis"),
        ("How many holes in a round of golf?", "18"),
        ("What is the fastest ball sport?", "Jai alai"),
        ("Who has the most home runs in MLB?", "Barry Bonds"),
        ("What country has won the most World Cups?", "Brazil"),
        ("How many Grand Slams in tennis per year?", "4"),
        ("What sport uses a shuttlecock?", "Badminton"),
        ("Who was the youngest F1 champion?", "Sebastian Vettel"),
        ("What is the oldest sport in the world?", "Running"),
        ("How many rings in the Olympic flag?", "5"),
        ("What country started sumo wrestling?", "Japan"),
    ]
    q, a = random.choice(qs)
    ans = input("Q: {} ".format(q)).strip().lower()
    if ans == a.lower(): print("Correct!")
    else: print("Wrong! Answer: {}".format(a))

def art_trivia():
    qs = [
        ("Who painted the Sistine Chapel ceiling?", "Michelangelo"),
        ("What art movement is Van Gogh associated with?", "Post-Impressionism"),
        ("Who sculpted David?", "Michelangelo"),
        ("What museum has the Mona Lisa?", "Louvre"),
        ("Who painted The Persistence of Memory?", "Dali"),
        ("What is the oldest known painting?", "Cave paintings"),
        ("Who painted Girl with a Pearl Earring?", "Vermeer"),
        ("What school was Raphael associated with?", "High Renaissance"),
        ("Who painted The Scream?", "Munch"),
        ("What art style uses small dots of color?", "Pointillism"),
        ("Who is the father of Cubism?", "Picasso"),
        ("What Japanese art form is woodblock printing?", "Ukiyo-e"),
        ("Who painted Water Lilies?", "Monet"),
        ("What museum has the most visitors?", "Louvre"),
        ("Who created the Virgin of the Rocks?", "Da Vinci"),
    ]
    q, a = random.choice(qs)
    ans = input("Q: {} ".format(q)).strip().lower()
    if ans == a.lower(): print("Correct!")
    else: print("Wrong! Answer: {}".format(a))

def food_trivia():
    qs = [
        ("What country invented pizza?", "Italy"),
        ("What is the hottest chili pepper?", "Carolina Reaper"),
        ("What fruit is the most popular in the world?", "Banana"),
        ("What spice is derived from crocus flowers?", "Saffron"),
        ("What country drinks the most coffee per capita?", "Finland"),
        ("What is the most expensive spice?", "Saffron"),
        ("What nut is used to make marzipan?", "Almond"),
        ("What country invented chocolate?", "Mexico"),
        ("What is the most consumed manufactured drink?", "Tea"),
        ("What fruit has the most vitamin C?", "Kakadu plum"),
        ("What is the oldest alcoholic drink?", "Mead"),
        ("What country eats the most chocolate?", "Switzerland"),
        ("What is the most popular pizza topping?", "Pepperoni"),
        ("What country invented sushi?", "Japan"),
        ("What is the world's most popular vegetable?", "Potato"),
    ]
    q, a = random.choice(qs)
    ans = input("Q: {} ".format(q)).strip().lower()
    if ans == a.lower(): print("Correct!")
    else: print("Wrong! Answer: {}".format(a))

def animal_trivia():
    qs = [
        ("What is the fastest land animal?", "Cheetah"),
        ("What animal has the longest lifespan?", "Bowhead whale"),
        ("What is the largest animal on Earth?", "Blue whale"),
        ("What animal can sleep for 3 years?", "Snail"),
        ("What is the smartest animal?", "Dolphin"),
        ("What animal has the longest migration?", "Arctic tern"),
        ("What is the smallest mammal?", "Bumblebee bat"),
        ("What animal is the tallest in the world?", "Giraffe"),
        ("What animal has the strongest bite?", "Crocodile"),
        ("What animal can regrow its limbs?", "Axolotl"),
        ("What is the most poisonous animal?", "Box jellyfish"),
        ("What animal has blue blood?", "Octopus"),
        ("What animal never sleeps?", "Bullfrog"),
        ("What animal has three hearts?", "Octopus"),
        ("What animal has the largest brain?", "Sperm whale"),
    ]
    q, a = random.choice(qs)
    ans = input("Q: {} ".format(q)).strip().lower()
    if ans == a.lower(): print("Correct!")
    else: print("Wrong! Answer: {}".format(a))

def tech_trivia():
    qs = [
        ("Who founded Microsoft?", "Bill Gates"),
        ("What year was the first iPhone released?", "2007"),
        ("What does AI stand for?", "Artificial Intelligence"),
        ("Who invented the World Wide Web?", "Tim Berners-Lee"),
        ("What was the first social media platform?", "Six Degrees"),
        ("What does URL stand for?", "Uniform Resource Locator"),
        ("Who created Linux?", "Linus Torvalds"),
        ("What year was Google founded?", "1998"),
        ("What does RAM stand for?", "Random Access Memory"),
        ("Who is the father of the computer?", "Charles Babbage"),
        ("What does USB stand for?", "Universal Serial Bus"),
        ("What was the first video game?", "Tennis for Two"),
        ("Who invented the telephone?", "Alexander Graham Bell"),
        ("What year was email invented?", "1971"),
        ("What does PDF stand for?", "Portable Document Format"),
    ]
    q, a = random.choice(qs)
    ans = input("Q: {} ".format(q)).strip().lower()
    if ans == a.lower(): print("Correct!")
    else: print("Wrong! Answer: {}".format(a))

def nature_trivia():
    qs = [
        ("What is the tallest tree species?", "Redwood"),
        ("What is the largest flower?", "Rafflesia"),
        ("What plant lives the longest?", "Bristlecone pine"),
        ("What is the fastest growing plant?", "Bamboo"),
        ("What is the most poisonous plant?", "Castor bean"),
        ("What plant eats insects?", "Venus flytrap"),
        ("What is the oldest living organism?", "Pando (aspen colony)"),
        ("What is the largest fruit?", "Jackfruit"),
        ("What plant has the largest seeds?", "Coconut"),
        ("What is the most common tree in the world?", "Red mangrove"),
        ("What plant is used to make chocolate?", "Cacao"),
        ("What is the national flower of Japan?", "Cherry blossom"),
        ("What plant produces coffee?", "Coffea"),
        ("What is the most expensive mushroom?", "Truffle"),
        ("What plant is the source of rubber?", "Rubber tree"),
    ]
    q, a = random.choice(qs)
    ans = input("Q: {} ".format(q)).strip().lower()
    if ans == a.lower(): print("Correct!")
    else: print("Wrong! Answer: {}".format(a))

def random_trivia_fact():
    facts = [
        "The Eiffel Tower was built for the 1889 World's Fair.",
        "The Amazon is the largest river by discharge volume.",
        "The Sahara Desert was once a lush green landscape.",
        "The Taj Mahal took 22 years to build.",
        "The Roman Empire lasted for over 1000 years.",
        "The shortest war in history was 38 minutes.",
        "The Great Wall of China is over 21,000 km long.",
        "The human body has 206 bones.",
        "The Earth orbits the Sun at 107,000 km/h.",
        "A day on Mercury is 59 Earth days.",
        "Light travels at 299,792 km per second.",
        "The brain has about 86 billion neurons.",
        "The heart beats about 100,000 times per day.",
        "There are over 7,000 languages spoken in the world.",
        "The first Olympic Games were in 776 BC.",
        "Shakespeare invented 1,700 English words.",
        "Cleopatra lived closer to the moon landing than to the pyramids.",
        "The Earth's core is as hot as the surface of the Sun.",
        "Bananas are berries, but strawberries are not.",
        "Honey never spoils.",
    ]
    return random.choice(facts)
