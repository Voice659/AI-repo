import random, datetime, os, math, string, json, re, hashlib, base64, uuid, time, statistics
import space_data, mini_games, trivia_pack, word_play, art_extra, world_data, story_data
import HubBasePE.Main as HB

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

facts = [
    "The first computer virus was created in 1983.",
    "Python was named after Monty Python's Flying Circus.",
    "The first programmer was Ada Lovelace in the 1840s.",
    "The first computer weighed 27 tons.",
    "JavaScript was created in 10 days in 1995.",
    "The QWERTY keyboard was designed in 1873.",
    "The first website is still online at info.cern.ch.",
    "The first computer mouse was made of wood.",
    "The first iPhone had no app store.",
    "Git was created by Linus Torvalds in 2005.",
    "There are over 700 programming languages.",
    "The @ symbol was chosen for email in 1971.",
    "CAPTCHA stands for Completely Automated Public Turing test.",
    "Linux has over 13 million lines of code.",
    "Google stored data on LEGO bricks.",
    "Java was originally called Oak.",
    "The first domain was symbolics.com.",
    "WiFi was invented in 1997.",
    "The first 1GB hard drive cost $40,000 in 1980.",
    "The first computer virus was written for Apple II.",
    "The first web browser was called WorldWideWeb.",
    "Python is named after a comedy group, not the snake.",
    "COBOL is over 60 years old and still in use.",
    "The first video game was Spacewar! in 1962.",
    "Floppy disks were actually hard when invented.",
    "The first programming language was Plankalkul in 1940s.",
    "Email is older than the World Wide Web.",
    "The first smartphone was IBM Simon in 1992.",
    "Google processes 3.5 billion searches per day.",
    "There are about 1.8 billion websites today.",
    "The first YouTube video was 'Me at the zoo' in 2005.",
    "The Amazon logo has a hidden smile from A to Z.",
    "The first tweet was sent by Jack Dorsey in 2006.",
    "Facebook was founded in a Harvard dorm room.",
    "Reddit was founded by two UVA roommates.",
    "Wikipedia has over 6 million articles in English.",
    "The first iPhone had 128MB of RAM.",
    "The Apollo 11 computer had 2KB of RAM.",
    "The Soviet Union created the first web game in 1950.",
    "There is a programming language called Brainfuck.",
    "A single Google search uses 1000 computers.",
    "The first antivirus was created in 1987.",
    "Bug in programming came from a real moth in 1947.",
    "The first hard drive stored 5MB in 1956.",
    "The first microprocessor was Intel 4004 in 1971.",
    "Pac-Man was created in 1980 by Toru Iwatani.",
    "The first computer was ENIAC in 1945.",
    "ENIAC weighed 27 tons and used 18000 vacuum tubes.",
    "The first laptop was the Osborne 1 in 1981.",
    "USB cables are designed to fit only one way.",
    "The honey badger is a mammal found in Africa.",
    "Octopuses have three hearts and blue blood.",
    "Bananas are berries, but strawberries are not.",
    "Cleopatra lived closer to the moon landing than to the pyramids.",
    "A day on Venus is longer than a year on Venus.",
    "Honey never spoils. Archaeologists found 3000-year-old honey.",
    "There are more trees on Earth than stars in the Milky Way.",
    "Wombat poop is cube-shaped.",
    "A group of flamingos is called a flamboyance.",
    "The shortest war in history was 38 minutes long.",
    "The Eiffel Tower grows 6 inches in summer due to heat.",
    "Sea horses mate for life and hold tails when swimming.",
    "The human stomach regenerates its lining every 3-4 days.",
    "The tongue is the only muscle attached at one end.",
    "Your nose and ears never stop growing.",
    "The circulatory system is 60,000 miles long.",
    "A cloud can weigh over a million pounds.",
    "Lightning strikes the Earth 100 times per second.",
    "The Earth's core is as hot as the sun's surface.",
    "There is a waterfall underwater in Denmark Strait.",
    "Antarctica is the world's largest desert.",
    "The largest living thing is a fungus in Oregon.",
    "The Great Wall of China is not visible from space.",
    "Mount Everest grows about 4mm every year.",
    "The Pacific Ocean is wider than the Moon.",
    "The Sahara desert was once a tropical rainforest.",
    "There are more stars in space than grains of sand on Earth.",
    "A neutron star can spin 600 times per second.",
    "Space is completely silent because there is no air.",
    "The ISS orbits Earth every 90 minutes.",
    "Footprints on the Moon will stay for millions of years.",
    "The sun produces enough energy in 1 second for 1 million years.",
    "Venus rotates backwards compared to most planets.",
    "Jupiter has the shortest day of all planets.",
    "A year on Mercury is 88 Earth days.",
    "Neptune was predicted mathematically before discovery.",
    "Pluto was discovered in 1930 and reclassified in 2006.",
    "The coldest place in the universe is on Earth in labs.",
    "The human brain generates enough electricity to light a bulb.",
    "You shed about 600,000 skin particles every hour.",
    "The average person walks the equivalent of 5 times around Earth.",
    "Your body has about 60,000 miles of blood vessels.",
    "The human eye can distinguish about 10 million colors.",
    "Your bones are 5 times stronger than steel by weight.",
    "Babies have about 300 bones, adults have 206.",
    "The strongest muscle in the body is the masseter (jaw).",
    "Your stomach acid can dissolve razor blades.",
    "You can survive without food for weeks but without sleep only days.",
    "Humans share 60% of DNA with bananas.",
    "Chimpanzees share 98% of DNA with humans.",
    "A single strand of DNA is 3 billion base pairs long.",
    "The first DNA was discovered in 1869 by Friedrich Miescher.",
    "CRISPR gene editing was discovered in 2012.",
    "The human genome has 20000-25000 genes.",
    "Water covers 71% of the Earth's surface.",
    "The Mariana Trench is 11km deep.",
    "Lake Baikal contains 20% of the world's fresh water.",
    "Amazon rainforest produces 20% of the world's oxygen.",
    "Coral reefs are home to 25% of marine life.",
    "The average lightning bolt is 5km long and 2cm wide.",
    "A jiffy is an actual unit of time: 1/100th of a second.",
    "The longest word in English has 189,819 letters.",
    "Vikings used to give kittens as wedding gifts.",
    "A group of porcupines is called a prickle.",
    "The first oranges weren't orange - they were green.",
    "Peanuts are not nuts - they are legumes.",
    "The national animal of Scotland is the unicorn.",
    "There is a species of jellyfish that is immortal.",
    "A day on Mars is only 40 minutes longer than Earth.",
    "The dot over the letter i is called a tittle.",
    "Coca-Cola was originally green.",
    "The shortest commercial flight is 1.7 miles long.",
    "Cows have best friends and get stressed when separated.",
    "The heart of a shrimp is located in its head.",
    "A crocodile cannot stick its tongue out.",
    "Sharks have been around longer than trees.",
    "Butterflies taste with their feet.",
    "An ostrich's eye is bigger than its brain.",
    "Honeybees can recognize human faces.",
    "Polar bears have black skin under their white fur.",
    "Dolphins sleep with one eye open.",
    "Elephants are the only mammals that can't jump.",
    "A cat has 32 muscles in each ear.",
    "Gorillas can catch human colds.",
    "A snail can sleep for three years.",
    "The fingerprints of koalas are nearly identical to humans.",
    "A blue whale's heart is the size of a small car.",
    "Camel milk does not curdle.",
    "The mantis shrimp has 12 color receptors (humans have 3).",
    "Sloths can hold their breath longer than dolphins.",
    "A group of owls is called a parliament.",
    "Rats laugh when tickled.",
    "Penguins propose to their mates with a pebble.",
    "The Bible is the most stolen book in the world.",
    "The Eiffel Tower was originally intended for Barcelona.",
    "The Statue of Liberty was originally copper-colored.",
    "There is a town in Norway called Hell that freezes over.",
    "The longest place name in the world is 85 letters long.",
    "Alaska is the easternmost and westernmost US state.",
    "Russia has 11 time zones.",
    "Canada has more lakes than the rest of the world combined.",
    "The driest place on Earth is in Antarctica.",
    "The hottest temperature recorded was 56.7C in Death Valley.",
    "The coldest temperature was -89.2C in Antarctica.",
    "The largest cave is in Vietnam - Son Doong cave.",
    "The deepest point is the Mariana Trench at 11km.",
    "The highest waterfall is Angel Falls in Venezuela.",
    "The oldest tree is 5,000 years old in California.",
    "The Sahara can reach 50C during the day and freezing at night.",
    "Lightning strikes Earth 8 million times per day.",
    "The Amazon is the largest river by water volume.",
    "Greenland is the largest island in the world.",
    "Indonesia is the largest archipelago with 17000 islands.",
    "The smallest country is Vatican City at 0.44 sq km.",
    "Mount Chimborazo is furthest from Earth's center.",
    "The Dead Sea is 430m below sea level.",
    "The Nile is the longest river at 6,650km.",
    "Lake Superior contains 10% of world's surface fresh water.",
    "Bamboo can grow 91cm in a single day.",
    "The Titan arum flower smells like rotting flesh.",
    "The largest flower is Rafflesia at 1m diameter.",
    "Cactus can survive for two years without water.",
    "A sunflower can grow up to 12 meters tall.",
    "Apples float on water because 25% of their volume is air.",
    "Bananas contain potassium which is radioactive.",
    "Pineapples take two years to grow.",
    "Strawberries have their seeds on the outside.",
    "An average person produces 25,000 liters of saliva in a lifetime.",
    "The human body contains enough iron to make a 3-inch nail.",
    "Your brain uses 20% of your body's oxygen and calories.",
    "The cornea is the only part with no blood supply.",
    "You are about 1cm taller in the morning than at night.",
    "The smallest bone is the stapes in the ear at 3mm.",
    "The femur is the longest bone in the human body.",
    "Fingernails grow faster than toenails.",
    "The appendix has a function - it stores good bacteria.",
    "Humans are the only animals that blush.",
    "The average person spends 1/3 of their life sleeping.",
    "Dreams last 20-25 minutes on average.",
    "Your nose can remember 50,000 different scents.",
    "Women's hearts beat faster than men's.",
    "The liver can regenerate itself completely.",
    "You lose about 50-100 hairs per day.",
    "The longest hiccuping spree lasted 68 years.",
    "The strongest muscle is the masseter (jaw muscle).",
    "Your skin weighs about twice as much as your brain.",
    "Yawning cools your brain down.",
    "Laughing can boost your immune system.",
    "The first successful heart transplant was in 1967.",
    "Penicillin was discovered by accident in 1928.",
    "DNA was first discovered in 1869.",
    "The human genome project took 13 years to complete.",
    "There are 37.2 trillion cells in the human body.",
    "Neurons can transmit signals at 268 mph.",
    "The placebo effect works even when you know it's placebo.",
    "Your gut microbiome weighs about 2kg.",
    "The first antibiotic was discovered before World War II.",
    "Vaccines save 2-3 million lives per year.",
    "Marie Curie died from radiation exposure.",
    "Einstein's brain was stolen after his death.",
    "Isaac Newton was born the same year Galileo died.",
    "Leonardo da Vinci could write with one hand and draw with the other.",
    "Shakespeare invented over 1700 English words.",
    "The first novel ever written was The Tale of Genji in 1008.",
    "Beethoven composed music after going completely deaf.",
    "Mozart wrote his first symphony at age 8.",
    "The Great Wall of China is over 13,000 miles long.",
    "The Colosseum could hold 80,000 spectators.",
    "The Aztecs built floating gardens called chinampas.",
    "The Rosetta Stone was discovered in 1799.",
    "The oldest known city is Jericho founded 9,000 BCE.",
    "The library of Alexandria was one of the largest in ancient world.",
    "The first Olympic Games were in 776 BCE.",
    "The Black Death killed 200 million people in the 1300s.",
    "Joan of Arc was 19 years old when she was executed.",
    "The Titanic was considered unsinkable.",
    "The first photograph was taken in 1826.",
    "The phonograph was invented by Edison in 1877.",
    "The telephone was accidentally invented by Bell.",
    "The lightbulb wasn't invented by Edison alone.",
    "The first radio broadcast was in 1906.",
    "Television was invented in 1927.",
    "The first computer programmer was Ada Lovelace.",
    "ENIAC was the first electronic computer in 1945.",
    "ARPANET was the precursor to the internet in 1969.",
    "The first email was sent in 1971.",
    "The World Wide Web was invented in 1989.",
    "The first Google search query was 'Stanford'.",
    "Facebook started with just Harvard students.",
    "The first iPhone was released in 2007.",
    "The Bitcoin whitepaper was published in 2008.",
    "Quantum computing was first proposed in 1982.",
    "The first AI program was written in 1951.",
    "Deep Blue beat Kasparov in chess in 1997.",
    "AlphaGo beat Lee Sedol in Go in 2016.",
    "GPT-3 was released in 2020 with 175 billion parameters.",
    "The first video game console was Magnavox Odyssey in 1972.",
    "Pong was the first successful arcade game in 1972.",
    "The Nintendo Entertainment System saved gaming in 1985.",
    "Minecraft is the best-selling game of all time.",
    "Tetris was created by Alexey Pajitnov in 1984.",
    "Mario's original name was Jumpman.",
    "Pac-Man was inspired by a pizza missing a slice.",
    "The Sims was originally called Project X.",
    "Grand Theft Auto started as a 2D top-down game.",
    "The first Final Fantasy game saved Square from bankruptcy.",
    "Mortal Kombat led to the creation of ESRB ratings.",
    "Doom was shareware and revolutionized FPS gaming.",
    "Sonic was created to compete with Mario.",
    "Halo was originally a real-time strategy game.",
    "The Legend of Zelda was inspired by Miyazaki's childhood.",
    "Pokemon was inspired by bug collecting as a child.",
    "Street Fighter II defined the fighting game genre.",
    "Metal Gear Solid pioneered stealth gameplay.",
    "Half-Life 2 is considered one of the greatest games.",
    "The Witcher 3 won over 800 game of the year awards.",
    "Dark Souls created a whole new genre of gaming.",
    "Fortnite popularized the battle royale genre.",
    "Among Us was released in 2018 but became viral in 2020.",
    "Stardew Valley was made entirely by one person.",
    "Undertale was made mostly by Toby Fox alone.",
    "The Oregon Trail was originally a text-based game.",
    "Space Invaders was so popular it caused a coin shortage.",
    "The arcade version of Pac-Man earned $1 billion in quarters.",
    "E.T. for Atari is considered the worst game ever.",
    "The Nintendo Switch is a hybrid console.",
    "PlayStation was originally a Nintendo collaboration.",
    "Xbox was Microsoft's answer to PlayStation.",
    "Sega stopped making consoles after Dreamcast.",
    "Steam started as a gaming platform in 2003.",
    "Twitch began as Justin.tv in 2007.",
    "eSports is now a billion dollar industry.",
    "The longest marathon gaming session is 135 hours.",
    "A speedrunner beat Super Mario in under 5 minutes.",
    "The first MMORPG was Meridian 59 in 1996.",
    "World of Warcraft peaked at 12 million subscribers.",
    "Minecraft has sold over 300 million copies.",
    "Roblox has over 200 million monthly active users.",
    "Tetris has been played more hours than any other game.",
    "The first easter egg in a game was in Adventure (1979).",
    "The Konami Code was created in 1986.",
    "The first mod chip was for the original PlayStation.",
    "DLC started as expansion packs for PC games.",
    "The first video game crash was in 1983.",
    "Japan has the most restrictive video game laws.",
    "Candy Crush makes over $1 million per day.",
    "Angry Birds was downloaded 2 billion times.",
    "Flappy Bird was removed by its creator.",
    "Geometry Dash was inspired by The Impossible Game.",
    "Clash of Clans popularized mobile strategy games.",
    "Mario Run was Nintendo's first mobile game.",
    "Pokemon Go made people walk more than ever before.",
    "Genshin Impact earned $1 billion in six months.",
    "Roblox was created in 2004 and released in 2006.",
    "The first emoji was created in 1999 in Japan.",
    "Social media platforms are designed to be addictive.",
    "The first hashtag was used on Twitter in 2007.",
    "YouTube was founded by three former PayPal employees.",
    "The first YouTube video was uploaded on April 23, 2005.",
    "Instagram was inspired by Polaroid instant cameras.",
    "Snapchat was originally called Picaboo.",
    "TikTok was launched internationally in 2018.",
    "Reddit was founded in 2005 by Alexis Ohanian.",
    "The 'like' button was originally a star on Facebook.",
    "Pinterest gets its name from pin + interest.",
    "LinkedIn was founded in 2002 by Reid Hoffman.",
    "Discord was created for gamers in 2015.",
    "WhatsApp was bought by Facebook for $19 billion.",
    "WeChat has over 1 billion monthly active users.",
    "Telegram was founded by the creator of VK.",
    "Signal is the most secure messaging app.",
    "Zoom became essential during the COVID-19 pandemic.",
    "Slack revolutionized workplace communication.",
    "GitHub was bought by Microsoft for $7.5 billion.",
    "Stack Overflow was created by Jeff Atwood and Joel Spolsky.",
    "Wikipedia is 5th most visited website in the world.",
    "Netflix started as a DVD rental service in 1997.",
    "Spotify changed the music industry forever.",
    "Amazon started by selling books online.",
    "Google was originally named Backrub.",
    "Yahoo was started by Jerry Yang and David Filo.",
    "Apple was founded in a garage by Jobs, Wozniak, and Wayne.",
    "Microsoft was founded by Bill Gates and Paul Allen.",
    "Tesla was founded in 2003 by Martin Eberhard.",
    "SpaceX was founded by Elon Musk in 2002.",
    "NVIDIA started by making graphics cards for gaming.",
    "AMD was founded in 1969 by Jerry Sanders.",
    "IBM was founded in 1911 as Computing-Tabulating-Recording.",
    "Intel was founded in 1968 by Gordon Moore and Robert Noyce.",
    "HP was founded in a garage in 1939.",
    "Dell was started in Michael Dell's dorm room.",
    "Oracle was founded in 1977 by Larry Ellison.",
    "Salesforce pioneered cloud computing in 1999.",
    "Adobe was founded in 1982 by John Warnock.",
    "Cisco was founded in 1984 by Leonard Bosack.",
    "Samsung started as a trading company in 1938.",
    "LG stands for Life is Good.",
    "Sony was founded in 1946 as Tokyo Tsushin Kogyo.",
    "Panasonic was founded in 1918 by Konosuke Matsushita.",
    "Nintendo was founded in 1889 as a playing card company.",
    "Sega was founded in 1960 as Service Games.",
    "Bandai Namco started as a toy company in 1950.",
    "Capcom was founded in 1979.",
    "Square Enix was formed by merging Square and Enix.",
    "Konami was founded in 1969.",
    "Ubisoft was founded in 1986 by five brothers.",
    "EA was founded in 1982 by Trip Hawkins.",
    "Activision was founded in 1979 by disgruntled Atari devs.",
    "Blizzard was founded in 1991 by three UCLA graduates.",
    "Bethesda was founded in 1986.",
    "CD Projekt Red was founded in 2002 in Poland.",
    "Rockstar Games was founded in 1998.",
    "Valve was founded in 1996 by Gabe Newell.",
    "Epic Games was founded in 1991 by Tim Sweeney.",
    "Unity was founded in 2004 in Denmark.",
    "Unreal Engine was first shown in 1998.",
    "HTML was created by Tim Berners-Lee in 1991.",
    "CSS was created by Håkon Wium Lie in 1994.",
    "JavaScript was created in 10 days in 1995 by Brendan Eich.",
    "TypeScript was released by Microsoft in 2012.",
    "Python was created by Guido van Rossum in 1991.",
    "Java was released by Sun Microsystems in 1995.",
    "C was created by Dennis Ritchie in 1972.",
    "C++ was created by Bjarne Stroustrup in 1985.",
    "C# was created by Microsoft in 2000.",
    "Ruby was created by Yukihiro Matsumoto in 1995.",
    "PHP was created by Rasmus Lerdorf in 1994.",
    "Swift was released by Apple in 2014.",
    "Kotlin was released by JetBrains in 2016.",
    "Go was created by Google in 2009.",
    "Rust was created by Mozilla in 2010.",
    "Dart was created by Google in 2011.",
    "Lua was created in 1993 at PUC-Rio.",
    "R was created by Ross Ihaka and Robert Gentleman in 1993.",
    "Perl was created by Larry Wall in 1987.",
    "Haskell was created in 1990.",
    "Lisp was created by John McCarthy in 1958.",
    "SQL was created by Donald Chamberlin and Raymond Boyce.",
    "Fortran was created by IBM in 1957.",
    "COBOL was created in 1959.",
    "Assembly language dates back to the 1940s.",
    "The Linux kernel was created by Linus Torvalds in 1991.",
    "The first open source license was the GNU GPL in 1989.",
    "The Apache server powered most of the early web.",
    "Nginx was created by Igor Sysoev in 2004.",
    "MySQL was created by Michael Widenius in 1995.",
    "PostgreSQL was created at UC Berkeley in 1986.",
    "SQLite is the most deployed database engine.",
    "MongoDB was created in 2007 by Dwight Merriman.",
    "Redis was created by Salvatore Sanfilippo in 2009.",
    "Docker was released in 2013.",
    "Kubernetes was created by Google in 2014.",
    "AWS was launched in 2006.",
    "Azure was launched by Microsoft in 2010.",
    "Google Cloud Platform was launched in 2008.",
    "Firebase was acquired by Google in 2014.",
    "Heroku was founded in 2007.",
    "Netlify was founded in 2014.",
    "Vercel was founded in 2015.",
    "Cloudflare was founded in 2009.",
    "The first datacenter was built by Google in 1998.",
    "Edge computing became popular in the 2010s.",
    "Serverless computing was popularized by AWS Lambda.",
    "Microservices architecture became popular in 2014.",
    "REST APIs were defined by Roy Fielding in 2000.",
    "GraphQL was created by Facebook in 2012.",
    "gRPC was created by Google in 2015.",
    "WebSocket was standardized in 2011.",
    "HTTP/2 was published in 2015.",
    "HTTP/3 uses QUIC protocol from Google.",
    "TLS was originally SSL created by Netscape.",
    "OAuth was created in 2007 by a group of developers.",
    "OpenID was created in 2005 by Brad Fitzpatrick.",
    "JWT was created in 2010 by Auth0.",
    "Vim was created by Bram Moolenaar in 1991.",
    "Emacs was created by Richard Stallman in 1984.",
    "VS Code was released by Microsoft in 2015.",
    "Atom was created by GitHub in 2014.",
    "Sublime Text was created by Jon Skinner in 2008.",
    "JetBrains started with IntelliJ IDEA in 2001.",
    "Eclipse was released by IBM in 2001.",
    "NetBeans was created by Sun Microsystems.",
    "Xcode is Apple's IDE for macOS development.",
    "Android Studio was announced in 2013.",
    "Visual Studio was first released in 1997.",
    "Git was created by Linus Torvalds in 2005.",
    "SVN was created by CollabNet in 2000.",
    "Mercurial was created in 2005 by Matt Mackall.",
    "CVS was the first version control system.",
    "Perforce was founded in 1995.",
    "Agile was formally defined in the Agile Manifesto in 2001.",
    "Scrum was coined by Jeff Sutherland and Ken Schwaber.",
    "Kanban originated from Toyota manufacturing.",
    "Waterfall model was introduced in 1970 by Winston Royce.",
]

more_facts = [
    "The fastest animal on land is the cheetah, reaching 120 km/h.",
    "A hummingbird can beat its wings up to 80 times per second.",
    "The Arctic tern migrates from pole to pole each year.",
    "Cows can walk up stairs but not down.",
    "A kangaroo cannot walk backwards.",
    "Starfish can regrow lost arms.",
    "The electric eel can generate 600 volts of electricity.",
    "A chameleon's tongue is twice the length of its body.",
    "The mimic octopus can impersonate 15 different species.",
    "Crows can recognize human faces and hold grudges.",
    "A group of flamingos is called a flamboyance.",
    "A wombat's pouch faces backwards to avoid dirt.",
    "Narwhals have a tusk that can grow up to 3 meters.",
    "The box jellyfish has 24 eyes but no brain.",
    "A slug has four noses.",
    "A butterfly has 12,000 eyes.",
    "The pistol shrimp can create a bubble as hot as the sun.",
    "The male seahorse gives birth to the young.",
    "Sea otters hold hands when sleeping to avoid drifting.",
    "A rhinoceros's horn is made of keratin, like human hair.",
    "Hippos secrete a natural sunscreen.",
    "The tardigrade can survive in outer space.",
    "A flea can jump 100 times its body length.",
    "The Komodo dragon has venomous bite.",
    "The platypus is one of the few venomous mammals.",
    "Emperor penguins can hold their breath for 20 minutes.",
    "A walrus can sleep on land or in water.",
    "The lyrebird can mimic almost any sound.",
    "The peregrine falcon is the fastest animal at 390 km/h.",
    "A camel's hump stores fat, not water.",
    "The giant panda spends 12 hours a day eating bamboo.",
    "Meerkats take turns standing guard duty.",
    "A cow produces 200,000 glasses of milk in its lifetime.",
    "The axolotl can regenerate entire limbs.",
    "A beaver's teeth never stop growing.",
    "The Portuguese man o' war is not a jellyfish.",
    "A barking spider is actually a bird.",
    "The frilled lizard runs on two legs when scared.",
    "A dingo is neither dog nor wolf but a separate species.",
    "The fennec fox has the largest ears relative to body size.",
    "Snow leopards can't roar but they can purr.",
    "A group of ferrets is called a business.",
    "Hedgehogs are immune to snake venom.",
    "A yak's milk has more fat than cow's milk.",
    "The shoebill stork looks prehistoric because it is.",
    "Giraffes have the same number of neck bones as humans.",
    "A tarantula can regrow lost legs.",
    "The slow loris has a toxic bite.",
    "A capybara is the world's largest rodent.",
    "Vampire bats don't suck blood - they lap it up.",
    "A moose can swim for hours without stopping.",
    "The jackrabbit can leap 3 meters in one bound.",
    "A skunk's spray can be smelled up to 1.5 km away.",
    "Orcas are actually dolphins, not whales.",
    "The horned lizard shoots blood from its eyes.",
    "A marmoset can rotate its head 180 degrees.",
    "The nightjar bird can enter a state of hibernation.",
    "Tapirs are related to rhinos and horses.",
    "A red panda is not related to the giant panda.",
    "The aye-aye taps on trees to find grubs.",
    "Bats are the only mammals that truly fly.",
    "A puffin can carry up to 60 fish in its beak.",
    "The ibis was worshipped in ancient Egypt.",
    "A peacock's tail is called a train with eye spots.",
    "The quokka is known as the happiest animal in the world.",
    "A manatee can hold its breath for 20 minutes.",
    "The tuatara has a third eye on top of its head.",
    "A woodpecker can peck 20 times per second.",
    "The leafy seadragon is a master of camouflage.",
    "Raccoons have extremely sensitive front paws.",
    "A marmot can whistle to warn others of danger.",
    "The kookaburra's call sounds like human laughter.",
    "A Mongolian death worm is legendary, not real.",
    "Dung beetles navigate by the Milky Way.",
    "The largest spider ever was the goliath birdeater.",
    "A coati is related to the raccoon.",
    "The hyena is more closely related to cats than dogs.",
    "A serval has the longest legs of any cat relative to body.",
    "The binturong smells like buttered popcorn.",
    "A muntjac deer is also called the barking deer.",
    "The tarsier has eyes bigger than its brain.",
    "A dik-dik is a tiny antelope named for its alarm call.",
    "The fossa is Madagascar's largest predator.",
    "A kinkajou is also called the honey bear.",
    "The echidna is one of only two monotremes.",
    "A bilby has a pouch that opens backwards.",
    "The numbat eats up to 20,000 termites per day.",
    "A quoll is a carnivorous marsupial.",
    "The Tasmanian devil has the strongest bite for its size.",
    "A wallaby is smaller than a kangaroo.",
    "The potoroo is the smallest kangaroo species.",
    "A sugar glider can glide up to 50 meters.",
    "The cuscus is a type of possum found in Australia.",
    "A bandicoot is a small marsupial omnivore.",
    "The tree kangaroo lives in trees instead of ground.",
    "A pademelon is a small forest-dwelling marsupial.",
    "The quokka is a type of wallaby found on Rottnest Island.",
    "A dibbler is a small carnivorous marsupial.",
    "The antechinus mates itself to death.",
    "A phascogale is also called the brush-tailed marsupial mouse.",
    "The kultarr is a mouse-like marsupial.",
    "A mulgara is a carnivorous marsupial from arid Australia.",
    "The boodie is a burrowing bettong.",
    "A woylie is a critically endangered marsupial.",
    "The bettong is a small hopping marsupial.",
    "A potoroo can collect food with its prehensile tail.",
    "The rufous rat-kangaroo is the smallest kangaroo.",
    "A hyrax is the closest living relative to the elephant.",
    "The tenrec is a hedgehog-like mammal from Madagascar.",
    "A zorilla is also called the striped polecat.",
    "The caracal is known for its ability to catch flying birds.",
    "A margay can rotate its ankles 180 degrees to climb down.",
    "The ocelot was once prized for its fur.",
    "A jaguarundi looks like a weasel and a cat combined.",
    "The kodkod is the smallest cat in the Americas.",
    "A colocolo is a rare South American wildcat.",
    "The sand cat can survive in temperatures over 50C.",
    "A black-footed cat is Africa's smallest wildcat.",
    "The Chinese mountain cat is one of the rarest cats.",
    "A jungle cat is also called the swamp cat.",
    "The fishing cat loves water and catches fish expertly.",
    "A flat-headed cat has partially webbed feet.",
    "The Iberian lynx is the most endangered cat species.",
    "A bobcat can survive in diverse habitats from desert to swamp.",
    "The lynx is known for its tufted ears and short tail.",
    "A cougar has more names than any other animal (puma, mountain lion, etc.).",
    "The clouded leopard has the largest canine teeth relative to skull.",
    "A snow leopard can leap 15 meters in one bound.",
    "The leopard is the most widespread big cat in the world.",
    "A jaguar has the strongest bite of all big cats.",
    "The tiger is the largest cat species in the world.",
    "A lion's roar can be heard 8 kilometers away.",
    "The cheetah cannot roar but instead purrs.",
    "A caracal can jump 3 meters high to catch birds.",
    "The serval has a 50% hunting success rate.",
    "A wildcat is the ancestor of all domestic cats.",
    "The Sphynx cat is not actually hairless - it has fine fuzz.",
    "Maine Coon cats are the largest domestic cat breed.",
    "Siamese cats are one of the oldest breeds.",
    "Persian cats are known for their long fur and flat face.",
    "Bengal cats have a wild-looking coat from Asian leopard cats.",
    "Ragdoll cats go limp when picked up.",
    "Scottish Fold cats have folded ears from a genetic mutation.",
    "Abyssinian cats are one of the oldest known breeds.",
    "Birman cats are known as the Sacred Cat of Burma.",
    "Norwegian Forest cats are built for cold climates.",
    "The Siberian cat is hypoallergenic for some people.",
    "British Shorthair is one of the most ancient cat breeds.",
    "Devon Rex cats have curly coats and large ears.",
    "The Egyptian Mau is the only naturally spotted domestic cat.",
    "Russian Blue cats are known for their silver-blue coat.",
    "The Cornish Rex has no guard hairs, only undercoat.",
    "Tonkinese cats are a cross between Siamese and Burmese.",
    "The Bombay cat looks like a miniature panther.",
    "Chartreux cats are the national cat of France.",
    "Turkish Van cats are known for loving water.",
    "American Shorthair cats came over on the Mayflower.",
    "The Manx cat has no tail due to a genetic mutation.",
    "Japanese Bobtail cats have a short bunny-like tail.",
    "The Korat cat is considered good luck in Thailand.",
    "LaPerm cats have curly fur from a genetic mutation.",
    "Singapura cats are one of the smallest cat breeds.",
    "The Sphynx was first bred in the 1960s in Canada.",
    "Ocicat cats look like wild ocelots but are domestic.",
    "The Pixie-bob is a breed that resembles a bobcat.",
    "Selkirk Rex cats have fluffy curly coats.",
    "The Sokoto cat is a rare breed from Kenya.",
    "Chausie cats are a hybrid of jungle cat and domestic cat.",
    "The Savannah cat is a hybrid of serval and domestic cat.",
    "Munchkin cats have short legs from a genetic mutation.",
    "Cymric cats are long-haired Manx cats.",
    "The Himalayan cat is a cross between Persian and Siamese.",
    "Burmilla cats are a cross between Chinchilla and Burmese.",
    "The American Curl has ears that curl backwards.",
    "Exotic Shorthair cats are short-haired Persians.",
    "The Nebelung cat has a shimmering blue coat.",
    "Oriental Shorthair cats come in over 300 colors.",
    "The Peterbald is a hairless breed from Russia.",
    "Burmese cats are known for their golden eyes.",
    "The Colorpoint Shorthair is a Siamese variant.",
    "Havana Brown cats have rich mahogany coats.",
    "The Australian Mist is a spotted or marbled cat breed.",
]
jokes = [
    "Why do programmers prefer dark mode? Light attracts bugs.",
    "Why was the Python dev sad? Too many problems.",
    "Why did the dev go broke? He used up his cache.",
    "How many programmers to change a light bulb? None, that's hardware.",
    "Why do Java devs wear glasses? They can't C#.",
    "A SQL query walks into a bar and asks for two tables.",
    "Why do programmers always mix up Halloween and Christmas? Because Oct 31 equals Dec 25.",
    "There are 10 types of people: those who understand binary and those who don't.",
    "A programmer's wife says: 'Go to the store and get milk. If they have eggs, get 12.' He comes back with 12 milks.",
    "Why did the programmer quit his job? He didn't get arrays.",
    "I would tell you a UDP joke but you might not get it.",
    "What's a computer's favorite snack? Microchips.",
    "Why was the computer cold? It left its Windows open.",
    "What do you call a fake noodle? An impasta.",
    "Why do we tell actors to break a leg? Because every play has a cast.",
    "What do you call a fish with no eyes? A fsh.",
    "Why don't scientists trust atoms? They make up everything.",
    "What's brown and sticky? A stick.",
    "How do you organize a space party? You planet.",
    "Why did the scarecrow win an award? He was outstanding in his field.",
    "I'm reading a book on anti-gravity. It's impossible to put down.",
    "What's orange and sounds like a parrot? A carrot.",
    "Why did the math book look so sad? It had too many problems.",
    "What do you call a bear with no teeth? A gummy bear.",
    "How does a penguin build a house? Igloos it together.",
    "Why don't eggs tell jokes? They'd crack each other up.",
    "What do you call a factory that sells okay products? A satis-factory.",
    "Did you hear about the restaurant on the moon? Great food, no atmosphere.",
    "What do you call a snowman with a six-pack? An abdominal snowman.",
    "Why did the bicycle fall over? It was two-tired.",
    "What do you call boomerang that won't come back? A stick.",
    "Why did the coffee file a police report? It got mugged.",
    "What's the best thing about Switzerland? I don't know, but the flag is a big plus.",
    "I invented a new word: Plagiarism.",
    "Why do cows have hooves instead of feet? Because they lactose.",
    "How do you catch a squirrel? Climb a tree and act like a nut.",
    "Why did the developer go broke? Because he used up all his cache.",
    "What do you call a belt made of watches? A waist of time.",
    "Parallel lines have so much in common. Too bad they'll never meet.",
    "I told my computer I needed a break and now it won't stop sending vacation ads.",
    "What do you get when you cross a snowman and a vampire? Frostbite.",
    "Why did the golfer wear two pairs of pants? In case he got a hole in one.",
    "What do you call a pony with a sore throat? A little horse.",
    "Singing in the shower is fun until you get soap in your mouth.",
    "I used to play piano by ear but now I use my hands.",
    "I told my wife she should embrace her mistakes. She gave me a hug.",
    "What do you call a fish wearing a bowtie? Sofishticated.",
    "What do you call a can opener that doesn't work? A can't opener.",
    "Why did the scarecrow become a programmer? He was outstanding in his field.",
    "What do you call a programmer from Finland? Nerdic.",
    "Why was the JavaScript developer sad? He didn't know how to 'null' his feelings.",
    "What's a programmer's favorite place? The Foo Bar.",
    "Why do programmers hate nature? Too many bugs.",
    "How do you comfort a JavaScript bug? You console it.",
    "Why did the developer go to therapy? He had too many emotional dependencies.",
    "What did the router say to the doctor? I need a bandwidth-aid.",
    "Why do programmers prefer iOS development? The Swift language is more his taste.",
    "What did the server say to the client? You've got no class.",
    "Why was the robot so happy? He had a motherboard.",
    "How does a computer greet you? It says 'Hello, World!'",
    "What did the computer do at lunchtime? Had a byte.",
    "Why did the computer keep freezing? It left its Windows open.",
    "What's a computer's first sign of aging? Loss of memory.",
    "Why did the computer go to the doctor? It had a virus.",
    "What do you call a computer that sings? A Dell.",
    "Why did the computer get glasses? It couldn't C.",
    "What did the computer say when it won? I'm processing!",
    "Why did the keyboard run away? It couldn't face the space bar.",
    "What do you call a keyboard in the shower? A key-board.",
    "Why did the mouse go to school? To learn how to click.",
    "What do you call a mouse that can't stop eating? A track-ball.",
    "Why did the monitor go to the hospital? It had screen cancer.",
    "What do you call a printer that sings? A laser jet.",
    "Why did the hard drive go to therapy? It had a bad sector.",
    "What do you call a USB drive that tells jokes? A pun drive.",
    "Why did the database break up? It had too many foreign keys.",
    "What do you call a query that goes to sleep? A sub-query.",
    "Why did the developer break up with his girlfriend? She had too many commits.",
    "What's a developer's favorite breakfast? A full-stack pancake.",
    "Why did the frontend developer go broke? He couldn't handle the back-end.",
    "What do you call a developer's pet? A code-pendant.",
    "Why did the software architect quit? He couldn't find the right abstraction.",
    "What's a developer's favorite song? The Git Up.",
    "Why did the programmer fail his driving test? He couldn't merge.",
    "What do you call a programmer who fails math? A null-pointer.",
    "Why did the Java developer need glasses? He couldn't C#.",
    "What do you call a Python developer from England? Guido van Rossum's cousin.",
    "Why did the Ruby developer go to the market? To get some gems.",
    "What do you call a developer who only uses Go? A gopher.",
    "Why did the Rust developer get promoted? He was memory-safe.",
    "What do you call a Scala developer? A functional person.",
    "Why did the Kotlin developer smile? He was null-safe.",
    "What do you call a TypeScript developer? A strongly typed person.",
    "Why did the PHP developer quit? He was tired of the $.",
    "What do you call a Perl developer? A regex wizard.",
    "Why did the C developer hate recursion? He couldn't handle the stack.",
    "What do you call a C++ developer? A pointer enthusiast.",
    "Why did the Assembly developer go crazy? Too many registers.",
    "What do you call a COBOL developer? Employed.",
    "Why did the SQL developer get all the dates? He knew how to join.",
    "What do you call a NoSQL developer? Unstructured.",
    "Why did the Docker developer get sick? Container fever.",
    "What do you call a Kubernetes developer? A cluster manager.",
    "Why did the cloud developer stay home? Too many AWS zones.",
    "What do you call a blockchain developer? A distributed person.",
    "Why did the AI developer get a girlfriend? He had good algorithms.",
    "What do you call a machine learning engineer? A data scientist's best friend.",
    "Why did the data scientist get divorced? Too many correlations.",
    "What do you call a deep learning model? A black box.",
    "Why did the neural network cry? It had too many layers.",
    "What do you call an AI that tells jokes? A stand-up algorithm.",
    "Why did the chatbot get fired? It couldn't understand the context.",
    "What do you call a robot chef? A byte of the apple.",
    "Why did the robot fail the test? It had a bug in its logic.",
    "What do you call a smart dog? A retriever augmented.",
    "Why did the algorithm break up? It was in a local minimum.",
    "What do you call a greedy algorithm? Selfish.",
    "Why did the dynamic programmer get rich? He knew how to optimize.",
    "What do you call a recursion that never ends? Stack overflow.",
    "Why did the binary tree get sad? It lost its root.",
    "What do you call a graph with no edges? Disconnected.",
    "Why did the link list go to therapy? It had a cycle.",
    "What do you call a hash map that lies? A hash of truth.",
    "Why did the queue get promoted? It was always in line.",
    "What do you call a stack with no push? Empty.",
    "Why did the array go to the doctor? It had an index out of bounds.",
    "What do you call a variable that never changes? Constant.",
    "Why did the function get lost? It had too many arguments.",
    "What do you call a boolean that lies? False.",
    "Why did the string get a haircut? It was too long.",
    "What do you call an integer that went to therapy? A floating point.",
    "Why did the char get lonely? It was single-quoted.",
    "What do you call a loop that never ends? Infinite.",
    "Why did the if-else break up? It couldn't decide.",
    "What do you call a try-catch block? A safety net.",
    "Why did the exception get a lawyer? It was thrown under the bus.",
    "What do you call a memory leak? A resource hog.",
    "Why did the pointer get lost? It was null.",
    "What do you call a buffer overflow? A security risk.",
    "Why did the thread freeze? Deadlock.",
    "What do you call a mutex? A lock picker.",
    "Why did the CPU get hot? Too many cycles.",
    "What do you call a GPU? A graphics processor.",
    "Why did the RAM get promoted? It had good memory.",
    "What do you call a hard drive failure? A crash.",
    "Why did the SSD get sad? It had worn out.",
    "What do you call a network cable? A wire tap.",
    "Why did the packet get lost? Its TTL expired.",
    "What do you call a firewall? A gate keeper.",
    "Why did the VPN get a job? It was a good tunnel.",
    "What do you call a proxy? A middle man.",
    "Why did the API get angry? Too many requests.",
    "What do you call a REST call? A stateless transaction.",
    "Why did the JSON get married? It had a good structure.",
    "What do you call an XML parser? A pain in the neck.",
    "Why did the YAML get a hobby? Too much indentation.",
    "What do you call a CI/CD pipeline? A deployment machine.",
    "Why did the test pass? It had good coverage.",
    "What do you call a bug that's hard to find? A feature.",
    "Why did the developer love his job? He found his niche.",
    "What do you call a developer who never commits? A freelancer.",
    "Why did the open source project succeed? Many contributors.",
    "What do you call a closed source project? Proprietary.",
    "Why did the startup fail? It ran out of runway.",
    "What do you call a successful startup? A unicorn.",
    "Why did the venture capitalist invest? He saw potential.",
    "What do you call an IPO? A payday.",
    "Why did the CEO code? He missed the good old days.",
    "What do you call a CTO who codes? Technical.",
    "Why did the PM change requirements? He had a vision.",
    "What do you call a designer who codes? A unicorn.",
    "Why did the QA engineer get promoted? He found all the bugs.",
    "What do you call a developer without bugs? A liar.",
    "Why did the code reviewer get annoyed? Too many nits.",
    "What do you call code review? A pull request.",
    "Why did the merge conflict happen? Two branches diverged.",
    "What do you call a git stash? A temporary save.",
    "Why did the rebase fail? Too many conflicts.",
    "What do you call a git log? A history lesson.",
    "Why did the developer use git blame? He was angry.",
    "What do you call a forked repo? A copy.",
    "Why did the pull request get rejected? It failed CI.",
    "What do you call a code freeze? A winter in development.",
    "Why did the developer take a vacation? He needed to git away.",
    "What do you call a programmer's funeral? A stack overflow.",
    "Why did the developer die early? Too much caffeine.",
    "What do you call a programmer's ghost? A spectre.",
    "Why did the developer dream in code? 0s and 1s.",
    "What do you call a sleeping programmer? A rest API.",
    "Why did the programmer meditate? To clear the cache.",
    "What do you call a programmer's love letter? An I/O U.",
    "Why did the programmer marry the database? They had a good relationship.",
    "What do you call a programmer's baby? A child class.",
    "Why did the programmer name his son Router? He wanted him to network.",
    "What do you call a programmer's dog? A byte bull.",
    "Why did the programmer get a cat? For purr-formance.",
    "What do you call a programmer's car? A Tesla model S.",
    "Why did the programmer buy a Mac? For the terminal.",
    "What do you call a programmer's phone? An iDevice.",
    "Why did the programmer switch to Linux? For sudo access.",
    "What do you call a programmer's desk? A workstation.",
    "Why did the programmer work at night? The compiler was faster.",
    "What do you call a programmer's favorite drink? Java.",
    "Why did the programmer drink coffee? To stay awake.",
    "What do you call a programmer's lunch? A byte to eat.",
    "Why did the programmer eat pizza? It was the only thing that compiled.",
    "What do you call a programmer's pizza? A slice of pi.",
    "Why did the programmer order sushi? For the raw data.",
    "What do you call a programmer's salad? A bit of greens.",
    "Why did the programmer go vegan? He wanted clean code.",
    "What do you call a programmer's workout? A loop in the park.",
    "Why did the programmer run? He was chasing a bug.",
    "What do you call a programmer's vacation? A breakpoint.",
    "Why did the programmer travel? To explore new frameworks.",
    "What do you call a programmer's favorite movie? The Matrix.",
    "Why did the programmer watch The Matrix? He wanted to see the source.",
    "What do you call a programmer's favorite book? The Pragmatic Programmer.",
    "Why did the programmer read documentation? He was desperate.",
    "What do you call a programmer without Stack Overflow? Lost.",
    "Why did the programmer use Google? He forgot the syntax.",
    "What do you call a programmer's search history? Code snippets.",
    "Why did the programmer close his browser? Too many tabs open.",
    "What do you call a programmer's home page? GitHub.",
    "Why did the programmer love GitHub? It was a social network for code.",
    "What do you call a programmer's side project? A startup.",
    "Why did the programmer start a blog? To share his knowledge.",
    "What do you call a programmer who podcasts? A thought leader.",
    "Why did the programmer write a book? To document his life.",
    "What do you call a programmer who teaches? A professor of code.",
    "Why did the programmer become a manager? He couldn't code anymore.",
    "What do you call a programmer who quits? Free.",
    "Why did the programmer return to coding? He missed the bugs.",
    "What do you call a retired programmer? A legacy developer.",
    "Why did the old programmer still code? For fun.",
    "What do you call a programmer's legacy? Their open source projects.",
    "Why did the programmer write comments? For his future self.",
    "What do you call a programmer with no comments? A genius or a madman.",
    "Why did the programmer avoid comments? Code should be self-documenting.",
    "What do you call a well-documented codebase? A rare sight.",
    "Why did the programmer write tests? For confidence.",
    "What do you call a test that never fails? A perfect test.",
    "Why did the programmer TDD? For peace of mind.",
    "What do you call code without tests? Legacy.",
    "Why did the programmer refactor? To pay off technical debt.",
    "What do you call a codebase after refactoring? Clean.",
    "Why did the programmer rewrite everything? He learned a new framework.",
    "What do you call a rewrite? A rewrite disaster.",
    "Why did the programmer stick with the old code? It worked.",
    "What do you call a stable system? A miracle.",
    "Why did the system go down? It needed maintenance.",
    "What do you call a five nines system? A dream.",
    "Why did the server crash? Too much traffic.",
    "What do you call a DDoS attack? A digital riot.",
    "Why did the website load slowly? Too many assets.",
    "What do you call a fast website? Optimized.",
    "Why did the developer optimize? For the users.",
    "What do you call a user? A customer.",
]

def show_fact():
    return random.choice(facts)

def show_joke():
    return random.choice(jokes)

def draw_diamond(n):
    lines = []
    for i in range(n):
        lines.append(" " * (n - i - 1) + "*" * (2 * i + 1))
    for i in range(n - 2, -1, -1):
        lines.append(" " * (n - i - 1) + "*" * (2 * i + 1))
    return "\n".join(lines)

def draw_tree(n):
    lines = []
    for i in range(n):
        lines.append(" " * (n - i - 1) + "*" * (2 * i + 1))
    lines.append(" " * (n - 2) + "|||")
    lines.append(" " * (n - 2) + "|||")
    return "\n".join(lines)

def draw_heart():
    lines = []
    for y in range(6, -1, -1):
        line = ""
        for x in range(7):
            eq1 = x * x + (y - abs(x)) ** 2
            if eq1 <= 9:
                line += "*"
            else:
                line += " "
        for x in range(7):
            eq2 = (6 - x) * (6 - x) + (y - abs(6 - x)) ** 2
            if eq2 <= 9:
                line += "*"
            else:
                line += " "
        lines.append(line)
    return "\n".join(lines)

def draw_star(n):
    lines = []
    for i in range(n):
        lines.append(" " * (n - i - 1) + "* " * (i + 1))
    for i in range(n - 2, -1, -1):
        lines.append(" " * (n - i - 1) + "* " * (i + 1))
    return "\n".join(lines)

def draw_cat():
    return r"""
  /\_/\
 ( o.o )
  > ^ <
"""

def draw_dog():
    return r"""
   __
  /  \
 | _  |
 |    |
  \__/
"""

def draw_fish():
    return r"""
><(((('>
"""

def fibonacci(limit):
    seq, a, b = [], 0, 1
    while a <= limit:
        seq.append(a)
        a, b = b, a + b
    return seq

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def analyze(text):
    vowels = sum(1 for c in text if c in "aeiouAEIOU")
    consonants = sum(1 for c in text if c.isalpha() and c not in "aeiouAEIOU")
    digits = sum(1 for c in text if c.isdigit())
    spaces = sum(1 for c in text if c.isspace())
    special = len(text) - vowels - consonants - digits - spaces
    words = len(text.split())
    return words, vowels, consonants, digits, spaces, special, text[::-1]

def factorial(n):
    if n < 0:
        return None
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def to_binary(n):
    return bin(n)[2:]

def to_hex(n):
    return hex(n)[2:].upper()

def to_octal(n):
    return oct(n)[2:]

def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def celsius_to_kelvin(c):
    return c + 273.15

def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(lb):
    return lb / 2.20462

def generate_password(length=16):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
    return "".join(random.choice(chars) for _ in range(length))

def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    print("I'm thinking of a number between 1 and 100.")
    while True:
        inp = input("Your guess (or 'back' to quit): ")
        if inp.lower() == "back":
            return
        try:
            guess = int(inp)
            attempts += 1
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print("Correct! You got it in {} tries!".format(attempts))
                return
        except ValueError:
            print("Enter a number.")

def hangman():
    words = ["python", "programming", "computer", "algorithm", "database",
             "network", "internet", "variable", "function", "recursion",
             "binary", "hexadecimal", "loop", "array", "string",
             "object", "class", "inheritance", "encryption", "protocol"]
    word = random.choice(words).lower()
    guessed = set()
    wrong = 0
    max_wrong = 6
    print("Hangman! Guess the word.")
    while wrong < max_wrong:
        display = "".join(c if c in guessed else "_" for c in word)
        print("Word: {}".format(display))
        print("Wrong: {}/{}".format(wrong, max_wrong))
        if "_" not in display:
            print("You won! The word was '{}'.".format(word))
            return
        letter = input("Guess a letter (or 'back'): ").lower()
        if letter == "back":
            return
        if len(letter) != 1 or not letter.isalpha():
            print("One letter please.")
            continue
        if letter in guessed:
            print("Already guessed.")
            continue
        guessed.add(letter)
        if letter not in word:
            wrong += 1
            print("Wrong!")
    print("You lost! The word was '{}'.".format(word))

def scramble_word():
    words = ["elephant", "bicycle", "umbrella", "keyboard", "monitor",
             "puzzle", "galaxy", "planet", "rocket", "dragon",
             "pirate", "castle", "tunnel", "laptop", "window",
             "forest", "garden", "bridge", "silver", "copper"]
    word = random.choice(words)
    scrambled = list(word)
    random.shuffle(scrambled)
    scrambled = "".join(scrambled)
    print("Unscramble this word: {}".format(scrambled))
    while True:
        guess = input("Your guess (or 'back'): ").lower()
        if guess == "back":
            return
        if guess == word:
            print("Correct!")
            return
        print("Wrong, try again!")

def magic_8_ball():
    responses = ["Yes.", "No.", "Ask again later.", "Definitely.", "Never.",
                 "Probably.", "I don't think so.", "Absolutely.", "Maybe.",
                 "Signs point to yes.", "Outlook not so good.", "Very doubtful.",
                 "Without a doubt.", "Cannot predict now.", "Concentrate and ask again.",
                 "My sources say no.", "Yes, in time.", "Don't count on it.",
                 "It is certain.", "My reply is no."]
    return random.choice(responses)

def caesar_cipher(text, shift):
    result = []
    for c in text:
        if c.isalpha():
            base = ord("A") if c.isupper() else ord("a")
            result.append(chr((ord(c) - base + shift) % 26 + base))
        else:
            result.append(c)
    return "".join(result)

def is_palindrome(text):
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]

def is_anagram(a, b):
    return sorted(a.lower().replace(" ", "")) == sorted(b.lower().replace(" ", ""))

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal"
    if bmi < 30:
        return "Overweight"
    return "Obese"

def zodiac_sign(month, day):
    signs = [
        (3, 21, "Aries"), (4, 20, "Taurus"), (5, 21, "Gemini"),
        (6, 21, "Cancer"), (7, 23, "Leo"), (8, 23, "Virgo"),
        (9, 23, "Libra"), (10, 23, "Scorpio"), (11, 22, "Sagittarius"),
        (12, 22, "Capricorn"), (1, 20, "Aquarius"), (2, 19, "Pisces"),
    ]
    for m, d, sign in signs:
        if (month == m and day >= d) or (month == m % 12 + 1 and day < (d if m < 12 else 21)):
            return sign
    return "Unknown"

def trivia_quiz():
    questions = [
        ("What is the capital of France?", "Paris"),
        ("What planet is known as the Red Planet?", "Mars"),
        ("What is the largest ocean?", "Pacific"),
        ("What is the chemical symbol for gold?", "Au"),
        ("What year did World War II end?", "1945"),
        ("What is the tallest mammal?", "Giraffe"),
        ("How many sides does a hexagon have?", "6"),
        ("What language has the most native speakers?", "Chinese"),
        ("What is the longest river in the world?", "Nile"),
        ("Who painted the Mona Lisa?", "Leonardo da Vinci"),
        ("What is the smallest country in the world?", "Vatican City"),
        ("What element is needed for combustion?", "Oxygen"),
        ("What is the speed of light in km/s?", "299792"),
        ("What is the largest organ in the human body?", "Skin"),
        ("What year was the Berlin Wall built?", "1961"),
    ]
    score = 0
    random.shuffle(questions)
    for q, a in questions:
        ans = input("Q: {} ".format(q)).strip().lower()
        if ans == a.lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong! Answer: {}".format(a))
    print("Score: {}/{}".format(score, len(questions)))

def to_morse(text):
    morse = {
        "A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....",
        "I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.",
        "Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-",
        "Y":"-.--","Z":"--..","0":"-----","1":".----","2":"..---","3":"...--","4":"....-",
        "5":".....","6":"-....","7":"--...","8":"---..","9":"----.",
    }
    result = []
    for c in text.upper():
        if c in morse:
            result.append(morse[c])
        elif c == " ":
            result.append("/")
    return " ".join(result)

def day_of_week(year, month, day):
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    try:
        dt = datetime.date(year, month, day)
        return days[dt.weekday()]
    except:
        return "Invalid date"

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def multiplication_table(n):
    lines = []
    for i in range(1, 11):
        lines.append("{} x {} = {}".format(n, i, n * i))
    return "\n".join(lines)

def progress_bar(current, total, width=30):
    filled = int(current / total * width)
    bar = "[" + "#" * filled + "-" * (width - filled) + "]"
    return "{} {:.1f}%".format(bar, current / total * 100)

def countdown(seconds):
    import time
    for i in range(seconds, 0, -1):
        print("{}...".format(i))
        time.sleep(1)
    print("Time's up!")

def random_name():
    first = ["Alex","Jordan","Morgan","Casey","Riley","Taylor","Sam","Quinn","Avery","Blake",
             "Charlie","Drew","Ellis","Finley","Harper","Jade","Kai","Logan","Mason","Nico",
             "Olive","Parker","Reese","Sage","Tatum","Uma","Vale","Wren","Xander","Zara"]
    last = ["Smith","Jones","Brown","Lee","Kim","Chen","Patel","Nguyen","Rivera","Singh",
            "Park","Yang","Liu","Garcia","Wilson","Johnson","Davis","Miller","Taylor","Moore",
            "Anderson","Jackson","White","Harris","Martin","Thompson","Robinson","Clark","Lewis","Walker"]
    return "{} {}".format(random.choice(first), random.choice(last))

def todo_manager():
    todos = []
    print("Todo manager. Commands: add <task>, done <n>, list, clear, back")
    while True:
        cmd = input("todo> ").strip().lower()
        if cmd == "back":
            return
        if cmd == "list":
            if not todos:
                print("No todos.")
            else:
                for i, t in enumerate(todos, 1):
                    print("{}. {}".format(i, t))
        elif cmd.startswith("add "):
            todos.append(cmd[4:])
            print("Added.")
        elif cmd.startswith("done "):
            try:
                idx = int(cmd[5:]) - 1
                if 0 <= idx < len(todos):
                    removed = todos.pop(idx)
                    print("Done: {}".format(removed))
                else:
                    print("Invalid index.")
            except:
                print("Usage: done <number>")
        elif cmd == "clear":
            todos.clear()
            print("Cleared.")
        else:
            print("Unknown command.")

def dice_roll(sides=6):
    return random.randint(1, sides)

def coin_flip():
    return "Heads" if random.randint(0, 1) == 0 else "Tails"

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    while True:
        user = input("Choose rock, paper, or scissors (or 'back'): ").lower()
        if user == "back":
            return
        if user not in choices:
            print("Invalid.")
            continue
        comp = random.choice(choices)
        print("Computer: {}".format(comp))
        if user == comp:
            print("Tie!")
        elif (user == "rock" and comp == "scissors") or \
             (user == "paper" and comp == "rock") or \
             (user == "scissors" and comp == "paper"):
            print("You win!")
        else:
            print("You lose!")

def show_calendar():
    try:
        y = int(input("Year: "))
        m = int(input("Month (1-12): "))
        print()
        print("    {} {}".format(datetime.date(y, m, 1).strftime("%B"), y))
        print("Mo Tu We Th Fr Sa Su")
        first = datetime.date(y, m, 1).weekday()
        days_in_month = (datetime.date(y, m + 1, 1) - datetime.date(y, m, 1)).days if m < 12 else 31
        line = "   " * first
        for d in range(1, days_in_month + 1):
            line += "{:2d} ".format(d)
            if (first + d) % 7 == 0:
                line += "\n"
        print(line)
    except:
        print("Invalid date.")

def simple_calculator():
    print("Calculator. Type expressions or 'back'.")
    while True:
        expr = input("calc> ").strip()
        if expr.lower() == "back":
            return
        try:
            result = eval(expr, {"__builtins__":{}}, {"math": math})
            print("= {}".format(result))
        except:
            print("Error.")

def draw_butterfly(n=4):
    lines = []
    for i in range(n):
        left = "*" * (i + 1)
        right = "*" * (i + 1)
        lines.append(left + " " * (2 * (n - i - 1)) + right)
    for i in range(n - 1, -1, -1):
        left = "*" * (i + 1)
        right = "*" * (i + 1)
        lines.append(left + " " * (2 * (n - i - 1)) + right)
    return "\n".join(lines)

def draw_rabbit():
    return r"""
  (\(\
  ( -.-)
  o_(")(")
"""

def draw_owl():
    return r"""
     ___
    ( o )
   ( o o )
    \___/
"""

def draw_snake():
    return r"""
    ~ ~ ~
   ~     ~
  ~  S   ~
   ~     ~
    ~ ~ ~
"""

def draw_house():
    lines = []
    size = 5
    for i in range(size):
        lines.append(" " * (size - i - 1) + "/" + " " * (2 * i) + "\\")
    lines.append("+" + "-" * (size * 2 - 2) + "+")
    for i in range(2):
        lines.append("|" + " " * (size * 2 - 2) + "|")
    lines.append("|" + " " * (size - 2) + "||" + " " * (size - 2) + "|")
    lines.append("|" + " " * (size * 2 - 2) + "|")
    lines.append("+" + "-" * (size * 2 - 2) + "+")
    return "\n".join(lines)

def draw_flower():
    return r"""
      @
     @@@
    @@@@@
   @@@@@@@
      |
     \|/
      |
"""

def draw_smile():
    return r"""
   #####
  #     #
 #  O O  #
 #   ^   #
  #  -  #
   #####
"""

def roll_multiple(num, sides=6):
    return [random.randint(1, sides) for _ in range(num)]

def card_draw():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    return "{} of {}".format(random.choice(ranks), random.choice(suits))

def high_low():
    print("High Low game. Guess if the next card is higher or lower.")
    deck = [r for r in range(2, 11) for _ in range(4)] + [10, 10, 10, 11]
    random.shuffle(deck)
    current = deck.pop()
    score = 0
    while deck:
        print("Current card: {}".format(current))
        guess = input("Higher or Lower? (h/l/back): ").lower()
        if guess == "back":
            print("Score: {}".format(score))
            return
        if guess not in ("h", "l"):
            continue
        next_card = deck.pop()
        print("Next card: {}".format(next_card))
        if (guess == "h" and next_card >= current) or (guess == "l" and next_card <= current):
            print("Correct!")
            score += 1
        else:
            print("Wrong! Score: {}".format(score))
            return
        current = next_card
    print("You went through the whole deck! Score: {}".format(score))

def riddle_game():
    riddles = [
        ("What has keys but can't open locks?", "piano"),
        ("What can travel around the world while staying in a corner?", "stamp"),
        ("What gets wetter the more it dries?", "towel"),
        ("What has a head and a tail but no body?", "coin"),
        ("What building has the most stories?", "library"),
        ("What month has 28 days?", "all of them"),
        ("What gets sharper the more you use it?", "brain"),
        ("What runs all around a yard but never moves?", "fence"),
        ("What has an eye but can't see?", "needle"),
        ("What has a neck but no head?", "bottle"),
        ("What can be cracked, made, and played?", "joke"),
        ("What has words but never speaks?", "book"),
        ("What can run but never walks?", "river"),
        ("What can fill a room but takes no space?", "light"),
        ("What gets harder to catch the faster you run?", "breath"),
        ("What goes through cities and fields but never moves?", "road"),
        ("What starts with T ends with T and has T in it?", "teapot"),
        ("What invention lets you look right through a wall?", "window"),
        ("What can you break even if you never pick it up?", "promise"),
        ("What goes up but never comes down?", "age"),
        ("What can you keep after giving to someone?", "your word"),
        ("What has many teeth but can't bite?", "comb"),
        ("What has a ring but no finger?", "phone"),
        ("What can you catch but not throw?", "cold"),
        ("What has one eye but can't see?", "needle"),
        ("What can you hold in your left hand but not in your right?", "right elbow"),
        ("What has cities but no houses?", "map"),
        ("What has a head and a tail but no body?", "coin"),
        ("What is full of holes but still holds water?", "sponge"),
        ("What building has the most stories?", "library"),
        ("What has legs but doesn't walk?", "table"),
        ("What can travel around the world while staying in a corner?", "stamp"),
        ("What has words but never speaks?", "book"),
        ("What begins with an E and only contains one letter?", "envelope"),
        ("What would you find in the middle of nowhere?", "the letter H"),
        ("What goes up when rain comes down?", "umbrella"),
        ("What five letter word becomes shorter when you add two letters?", "short"),
        ("What has a neck and a head but no body?", "shirt"),
        ("What tastes better than it smells?", "tongue"),
        ("What can you serve but never eat?", "tennis ball"),
        ("What has hands but can't clap?", "clock"),
        ("What can you break with one word?", "silence"),
        ("What can you make that no one can see?", "noise"),
        ("What grows larger the more you take away from it?", "hole"),
        ("What is seen in the middle of March and April?", "the letter R"),
        ("What has four wheels and flies?", "garbage truck"),
        ("What gets wetter and wetter the more it dries?", "towel"),
        ("What is always in front of you but can't be seen?", "future"),
        ("What can fill a room without taking any space?", "sound"),
    ]
    more_riddles = [
        ("What has a bottom at the top?", "legs"),
        ("What has keys but can't open doors?", "piano"),
        ("What month of the year has 28 days?", "all"),
        ("What starts with P and ends with E?", "post office"),
        ("What always ends everything?", "the letter G"),
        ("What has an end but no beginning?", "a circle"),
        ("What goes through doors but never goes in?", "keyhole"),
        ("What can shout but never speaks?", "echo"),
        ("What can bring back the dead?", "memory"),
        ("What can be stolen but never taken?", "heart"),
        ("What is always hungry but never eats?", "fire"),
        ("What can be felt but never touched?", "wind"),
        ("What can be seen but never touched?", "rainbow"),
        ("What runs but never walks?", "water"),
        ("What falls but never breaks?", "night"),
        ("What breaks but never falls?", "dawn"),
        ("What has roots but nobody sees?", "mountain"),
        ("What is tall when young and short when old?", "candle"),
        ("What has a single eye but cannot see?", "needle"),
        ("What has a tongue but cannot taste?", "shoe"),
        ("What can you break with a word?", "silence"),
        ("What gets sharper the more you use it?", "mind"),
        ("What has one head, one foot, and four legs?", "bed"),
        ("What has to be broken before you can use it?", "egg"),
        ("What is always coming but never arrives?", "tomorrow"),
        ("What can you keep after giving to someone?", "promise"),
        ("What goes up when the rain comes down?", "umbrella"),
        ("What can you hear but not touch or see?", "sound"),
        ("What has many teeth but can't bite?", "comb"),
        ("What has a ring but no finger?", "telephone"),
        ("What has a thumb and four fingers but is not alive?", "glove"),
        ("What can fly without wings?", "time"),
        ("What can grow but is not alive?", "crystal"),
        ("What has a spine but no bones?", "book"),
        ("What can dance without legs?", "flame"),
        ("What can sing without a mouth?", "wind"),
        ("What can cry without eyes?", "cloud"),
        ("What can smile without a face?", "moon"),
        ("What has a bed but never sleeps?", "river"),
        ("What has a bank but no money?", "river"),
        ("What has a mouth but never eats?", "river"),
        ("What can run but never walks, has a mouth but never talks?", "river"),
        ("What has a head and a tail but no body?", "coin"),
        ("What gets wetter the more it dries?", "towel"),
        ("What can be cracked, made, told, and played?", "joke"),
        ("What has a neck but no head?", "bottle"),
        ("What has a face and two hands but no arms?", "clock"),
        ("What has a cover but no pages?", "book cover"),
        ("What can travel around the world and stay in a corner?", "stamp"),
        ("What has a bottom at the top?", "legs"),
        ("What can you break even if you never pick it up?", "promise"),
        ("What is full of holes but still holds water?", "sponge"),
        ("What can you catch but not throw?", "cold"),
        ("What can you hold without ever touching?", "breath"),
        ("What can you see but never touch?", "stars"),
        ("What can touch you but you can never touch back?", "shadow"),
        ("What has a spine but cannot bend?", "cactus"),
        ("What has a shell but is not an egg?", "turtle"),
        ("What has a horn but cannot honk?", "rhino"),
        ("What has a hump but is not a camel?", "mountain"),
        ("What has a tail but is not an animal?", "kite"),
        ("What has a wing but cannot fly?", "airplane"),
        ("What has a heel but is not a shoe?", "bread"),
        ("What has a bridge but no water?", "nose"),
        ("What has a crown but no king?", "tooth"),
        ("What has a pole but no fish?", "totem"),
        ("What has a suit but no job?", "deck of cards"),
        ("What has a hat but no head?", "mushroom"),
        ("What has a nail but no finger?", "hammer"),
        ("What has a cap but no bottle?", "pen"),
        ("What has a tip but no money?", "pen"),
        ("What has a blade but no knife?", "fan"),
        ("What has a net but no fisherman?", "basketball"),
        ("What has a board but no game?", "chalkboard"),
        ("What has a screen but no movie?", "computer"),
        ("What has a mouse but no cat?", "computer"),
        ("What has a key but no lock?", "keyboard"),
        ("What has a menu but no restaurant?", "computer"),
        ("What has a window but no glass?", "operating system"),
        ("What has a file but no folder?", "database"),
        ("What has a table but no chair?", "database"),
        ("What has a field but no farm?", "form"),
        ("What has a record but no music?", "database"),
        ("What has a query but no question?", "SQL"),
        ("What has a server but no waiter?", "network"),
        ("What has a cloud but no rain?", "the internet"),
        ("What has a bug but no insect?", "software"),
        ("What has a code but no language?", "genetics"),
        ("What has a virus but no sickness?", "computer"),
        ("What has a firewall but no heat?", "network"),
        ("What has a cache but no treasure?", "processor"),
        ("What has a memory but no brain?", "computer"),
        ("What has a processor but no chef?", "computer"),
        ("What has a bit but no byte?", "binary"),
        ("What has a link but no chain?", "hyperlink"),
        ("What has a page but no book?", "website"),
        ("What has a site but no location?", "website"),
        ("What has a host but no party?", "server"),
        ("What has a domain but no ruler?", "website"),
        ("What has a path but no road?", "file system"),
        ("What has a root but no plant?", "file system"),
        ("What has a node but no tree?", "network"),
        ("What has a branch but no tree?", "git"),
        ("What has a commit but no crime?", "git"),
        ("What has a merge but no business?", "git"),
        ("What has a push but no pull?", "git"),
        ("What has a clone but no DNA?", "git"),
        ("What has a fork but no food?", "git"),
        ("What has a tag but no price?", "git"),
        ("What has a release but no prison?", "git"),
        ("What has a build but no construction?", "CI/CD"),
    ]
    all_riddles = riddles + more_riddles
    riddle, answer = random.choice(all_riddles)
    print("Riddle: {}".format(riddle))
    while True:
        g = input("Answer (or 'back'): ").lower().strip()
        if g == "back":
            print("Answer: {}".format(answer))
            return
        if g == answer:
            print("Correct!")
            return
        print("Nope, try again!")

def mean(nums):
    return sum(nums) / len(nums) if nums else 0

def median(nums):
    s = sorted(nums)
    n = len(s)
    if n == 0:
        return 0
    if n % 2 == 0:
        return (s[n//2-1] + s[n//2]) / 2
    return s[n//2]

def mode(nums):
    if not nums:
        return 0
    from collections import Counter
    c = Counter(nums)
    return c.most_common(1)[0][0]

def standard_deviation(nums):
    if len(nums) < 2:
        return 0
    m = mean(nums)
    var = sum((x - m) ** 2 for x in nums) / (len(nums) - 1)
    return math.sqrt(var)

def prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def to_roman(n):
    if n < 1 or n > 3999:
        return "Out of range"
    vals = [(1000,"M"),(900,"CM"),(500,"D"),(400,"CD"),(100,"C"),(90,"XC"),
            (50,"L"),(40,"XL"),(10,"X"),(9,"IX"),(5,"V"),(4,"IV"),(1,"I")]
    result = ""
    for v, s in vals:
        while n >= v:
            result += s
            n -= v
    return result

def from_roman(s):
    vals = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    result = 0
    prev = 0
    for c in reversed(s.upper()):
        v = vals.get(c, 0)
        if v < prev:
            result -= v
        else:
            result += v
        prev = v
    return result

def pig_latin(text):
    words = text.split()
    result = []
    for w in words:
        if w[0].lower() in "aeiou":
            result.append(w + "yay")
        else:
            result.append(w[1:] + w[0] + "ay")
    return " ".join(result)

def password_strength(pw):
    score = 0
    if len(pw) >= 8:
        score += 1
    if len(pw) >= 12:
        score += 1
    if any(c.islower() for c in pw):
        score += 1
    if any(c.isupper() for c in pw):
        score += 1
    if any(c.isdigit() for c in pw):
        score += 1
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in pw):
        score += 1
    if score <= 2:
        return "Weak"
    if score <= 4:
        return "Medium"
    return "Strong"

def binary_search_demo():
    data = sorted(random.sample(range(1, 200), 20))
    print("Sorted data: {}".format(data))
    target = int(input("Search for: "))
    left, right = 0, len(data) - 1
    steps = 0
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        if data[mid] == target:
            print("Found at index {} in {} steps.".format(mid, steps))
            return
        if data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print("Not found in {} steps.".format(steps))

def bubble_sort_demo():
    n = 10
    data = random.sample(range(1, 100), n)
    print("Before: {}".format(data))
    swapped = True
    passes = 0
    while swapped:
        swapped = False
        passes += 1
        for i in range(n - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
    print("After:  {}".format(data))
    print("Passes: {}".format(passes))

def solve_quadratic(a, b, c):
    d = b*b - 4*a*c
    if d < 0:
        return "No real solutions"
    x1 = (-b + math.sqrt(d)) / (2*a)
    x2 = (-b - math.sqrt(d)) / (2*a)
    if x1 == x2:
        return "x = {:.4f}".format(x1)
    return "x1 = {:.4f}, x2 = {:.4f}".format(x1, x2)

def typing_speed():
    import time
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python is a powerful programming language.",
        "Practice makes perfect every single day.",
        "Coding is fun and rewarding to learn.",
        "Hello world is the first program many write.",
    ]
    text = random.choice(sentences)
    print("Type this as fast as you can:")
    print("'{}'".format(text))
    input("Press Enter when ready...")
    start = time.time()
    typed = input("Type now: ")
    elapsed = time.time() - start
    correct = sum(1 for i in range(min(len(text), len(typed))) if text[i] == typed[i])
    accuracy = correct / len(text) * 100
    wpm = len(typed.split()) / (elapsed / 60)
    print("Time: {:.1f}s | Accuracy: {:.1f}% | Speed: {:.1f} WPM".format(elapsed, accuracy, wpm))

def show_quote():
    quotes = [
        "The best way to predict the future is to invent it. - Alan Kay",
        "Simplicity is the soul of efficiency. - Austin Freeman",
        "Talk is cheap. Show me the code. - Linus Torvalds",
        "Any fool can write code that a computer can understand. - Martin Fowler",
        "First solve the problem, then write the code. - John Johnson",
        "Code is like humor. When you have to explain it, it's bad. - Cory House",
        "Make it work, make it right, make it fast. - Kent Beck",
        "Programming isn't about what you know, it's about what you can figure out.",
        "The only way to learn programming is by writing code. - Dennis Ritchie",
        "Walking on water and developing software from a spec are easy if both are frozen.",
        "The function of good software is to make the complex appear simple. - Grady Booch",
        "Perfection is achieved not when there is nothing more to add, but when there is nothing to take away.",
        "A language that doesn't affect the way you think about programming is not worth knowing.",
        "Sometimes it pays to stay in bed on Monday rather than spending the rest of the week debugging.",
        "The best programs are written so that computing machines can perform them quickly.",
        "Always code as if the person who ends up maintaining your code is a violent psychopath.",
        "In programming, the hard part isn't solving problems, but deciding what problems to solve.",
        "Software is a great combination of art and engineering. - Bill Gates",
        "Before software can be immortal, it has to be useful. - Alan Perlis",
        "Beware of bugs in the above code; I have only proved it correct, not tried it. - Donald Knuth",
        "Programs must be written for people to read, and only incidentally for machines to execute. - Harold Abelson",
        "The best error message is the one that never shows up. - Thomas Fuchs",
        "Programming is the art of telling another human being what one wants the computer to do. - Donald Knuth",
        "Good code is its own best documentation. - Steve McConnell",
        "The most important property of a program is whether it accomplishes the intention of its user. - C.A.R. Hoare",
        "Measuring programming progress by lines of code is like measuring aircraft building progress by weight. - Bill Gates",
        "It's not a bug, it's an undocumented feature. - Anonymous",
        "Fix the cause, not the symptom. - Steve Maguire",
        "Code is like poetry, it should be clean and elegant. - Anonymous",
        "Simplicity is prerequisite for reliability. - Edsger Dijkstra",
        "If debugging is the process of removing bugs, then programming must be the process of putting them in. - Edsger Dijkstra",
        "The most dangerous phrase in the language is: We've always done it this way. - Grace Hopper",
        "A good programmer is someone who always looks both ways before crossing a one-way street. - Doug Linder",
        "Don't comment bad code, rewrite it. - Brian Kernighan",
        "Debugging is twice as hard as writing the code in the first place. - Brian Kernighan",
        "People don't care about what you say, they care about what you build. - Mark Zuckerberg",
        "The best way to learn to program is by doing it. - Anonymous",
        "The most disastrous thing that you can ever learn is your first programming language. - Alan Kay",
        "Computer science is no more about computers than astronomy is about telescopes. - Edsger Dijkstra",
        "The computer was born to solve problems that did not exist before. - Bill Gates",
        "Software is like entropy: it is difficult to grasp, weighs nothing, and obeys the Second Law of Thermodynamics.",
        "A good software engineer is a lazy software engineer. - Anonymous",
        "When debugging, novices insert corrective code; experts remove defective code. - Richard Pattis",
        "The purpose of software engineering is to control complexity, not to create it. - Dr. Pamela Zave",
        "Controlling complexity is the essence of computer programming. - Brian Kernighan",
        "Every great developer you know got there by solving problems they were unqualified to solve. - Patrick McKenzie",
        "The only way to learn a new programming language is by writing programs in it. - Dennis Ritchie",
        "Premature optimization is the root of all evil. - Donald Knuth",
        "Simplicity carried to the extreme becomes elegance. - Jon Franklin",
        "The most important skill for a programmer is the ability to effectively communicate ideas. - Anonymous",
        "A language that doesn't affect the way you think about programming is not worth knowing. - Alan Perlis",
        "There are only two kinds of languages: the ones people complain about and the ones nobody uses. - Bjarne Stroustrup",
        "In C++ it's harder to shoot yourself in the foot, but when you do, you blow off your whole leg. - Bjarne Stroustrup",
        "Python is executable pseudocode. - Bruce Eckel",
        "Life is too short to write C. - Anonymous",
        "Java is to JavaScript what car is to carpet. - Chris Heilmann",
        "Any sufficiently advanced technology is indistinguishable from magic. - Arthur C. Clarke",
        "The science of today is the technology of tomorrow. - Edward Teller",
        "The art of programming is the art of organizing complexity. - Edsger Dijkstra",
        "Computers are incredibly fast, accurate, and stupid. Human beings are incredibly slow, inaccurate, and brilliant. - Albert Einstein",
        "The best computer is a bicycle for the mind. - Steve Jobs",
        "Innovation is the ability to see change as an opportunity. - Peter Drucker",
        "The most powerful tool we have as developers is automation. - Scott Hanselman",
        "First learn computer science and all the theory. Next develop a programming style. Then forget all that and just hack. - George Carrette",
        "The key to performance is elegance, not battalions of special cases. - Jon Bentley",
        "I choose a lazy person to do a hard job. Because a lazy person will find an easy way to do it. - Bill Gates",
        "We have to stop optimizing for programmers and start optimizing for users. - Jeff Atwood",
        "Code never lies, comments sometimes do. - Ron Jeffries",
        "Always write code as if the person who ends up maintaining it is a violent psychopath who knows where you live.",
        "The earliest versions of software are the buggiest. - Anonymous",
        "Software is a great combination of art and engineering. - Bill Gates",
        "The best programs are the ones that do one thing and do it well. - Doug McIlroy",
        "Software engineering is the programming of things that are too complex to program. - Anonymous",
        "Programming is not about typing, it's about thinking. - Anonymous",
        "The computer was born to solve problems that did not exist before. - Bill Gates",
        "A programmer is a tool that converts caffeine into code. - Anonymous",
        "The three chief virtues of a programmer are: laziness, impatience, and hubris. - Larry Wall",
        "Laziness is the quality that makes you go to great effort to reduce overall energy expenditure.",
        "Impatience is the anger you feel when the computer is being lazy.",
        "Hubris is the quality that makes you write programs that other people don't want to say bad things about.",
        "The most pernicious aspect of computer programming is that the programmer is the first user. - Gerald Weinberg",
        "If you can't explain it simply, you don't understand it well enough. - Albert Einstein",
        "A computer lets you make more mistakes faster than any invention in human history. - Daniel Dennett",
        "Man is a slow, sloppy, and brilliant thinker; computers are fast, accurate, and stupid. - John Pfeiffer",
        "The most amazing achievement of the computer software industry is its continuing cancellation of the steady and staggering gains made by the computer hardware industry. - Henry Petroski",
        "Software is a gas; it expands to fill its container. - Nathan Myhrvold",
        "The best way to have a good idea is to have lots of ideas. - Linus Pauling",
        "An algorithm must be seen to be believed. - Donald Knuth",
        "The number of months to delivery is independent of the number of people on the team.",
        "Adding manpower to a late software project makes it later. - Fred Brooks",
        "The bearing of a child takes nine months, no matter how many women are assigned. - Fred Brooks",
        "What one programmer can do in one month, two programmers can do in two months. - Fred Brooks",
        "The first 90 percent of the code accounts for the first 90 percent of the development time. The remaining 10 percent of the code accounts for the other 90 percent of the development time. - Tom Cargill",
        "The more you plan, the longer it takes. - Anonymous",
        "Plan to throw one away; you will, anyhow. - Fred Brooks",
        "A good system cannot have a weak command language. - Anonymous",
        "One accurate measurement is worth a thousand expert opinions. - Grace Hopper",
        "It is easier to change the specification to fit the program than vice versa. - Alan Perlis",
        "Documentation is like sex: when it is good, it is very, very good; and when it is bad, it is better than nothing. - Dick Brandon",
        "Testing shows the presence, not the absence of bugs. - Edsger Dijkstra",
        "A test that proves the absence of bugs is impossible. - Anonymous",
        "If it's not tested, it's broken. - Anonymous",
        "The bitterness of poor quality remains long after the sweetness of meeting the schedule is forgotten.",
        "Quality is not an act, it is a habit. - Aristotle",
        "Real artists ship. - Steve Jobs",
        "The best is the enemy of the good. - Voltaire",
        "Perfection is achieved not when there is nothing more to add, but when there is nothing to take away. - Antoine de Saint-Exupery",
        "Everything should be made as simple as possible, but not simpler. - Albert Einstein",
        "The best code is no code at all. - Jeff Atwood",
        "If you can't do it simply, you can't do it at all. - Anonymous",
        "The most valuable of all talents is that of never using two words when one will do. - Thomas Jefferson",
        "The finest words in the world are only vain sounds, if you cannot understand them. - Anatole France",
        "Brevity is the soul of wit. - William Shakespeare",
        "The art of being wise is knowing what to overlook. - William James",
        "Learn the rules like a pro, so you can break them like an artist. - Pablo Picasso",
        "Any fool can know. The point is to understand. - Albert Einstein",
        "The important thing is not to stop questioning. - Albert Einstein",
        "Imagination is more important than knowledge. - Albert Einstein",
        "The true sign of intelligence is not knowledge but imagination. - Albert Einstein",
        "Energy cannot be created or destroyed, it can only be changed from one form to another. - Albert Einstein",
        "The only source of knowledge is experience. - Albert Einstein",
        "In the middle of difficulty lies opportunity. - Albert Einstein",
        "The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking. - Albert Einstein",
        "A person who never made a mistake never tried anything new. - Albert Einstein",
        "If you want to live a happy life, tie it to a goal, not to people or things. - Albert Einstein",
        "Learn from yesterday, live for today, hope for tomorrow. - Albert Einstein",
        "The only thing that interferes with my learning is my education. - Albert Einstein",
        "Creativity is intelligence having fun. - Albert Einstein",
        "Life is like riding a bicycle. To keep your balance, you must keep moving. - Albert Einstein",
        "It's not that I'm so smart, it's just that I stay with problems longer. - Albert Einstein",
        "Wisdom is not a product of schooling but of the lifelong attempt to acquire it. - Albert Einstein",
        "Try not to become a man of success, but rather try to become a man of value. - Albert Einstein",
        "The difference between stupidity and genius is that genius has its limits. - Albert Einstein",
        "Anyone who has never made a mistake has never tried anything new. - Albert Einstein",
        "The secret to creativity is knowing how to hide your sources. - Albert Einstein",
        "Two things are infinite: the universe and human stupidity; and I'm not sure about the universe. - Albert Einstein",
        "Logic will get you from A to B. Imagination will take you everywhere. - Albert Einstein",
        "The most beautiful thing we can experience is the mysterious. - Albert Einstein",
        "Science without religion is lame, religion without science is blind. - Albert Einstein",
        "Be a loner. That gives you time to wonder, to search for the truth. - Albert Einstein",
        "The value of a man should be seen in what he gives. - Albert Einstein",
        "Only a life lived for others is a life worthwhile. - Albert Einstein",
        "I have no special talents. I am only passionately curious. - Albert Einstein",
        "Great spirits have always encountered violent opposition from mediocre minds. - Albert Einstein",
        "Education is what remains after one has forgotten what one has learned in school. - Albert Einstein",
        "Black holes are where God divided by zero. - Steven Wright",
        "A computer once beat me at chess, but it was no match for me at kick boxing. - Emo Philips",
        "I just received a text from my refrigerator. It said: 'My cheese is your cheese'.",
        "If at first you don't succeed, call it version 1.0. - Anonymous",
        "My code doesn't have bugs, it just develops random features. - Anonymous",
        "A SQL query goes into a bar, walks up to two tables and asks: 'Can I join you?'",
        "I have a joke about recursion, but it's too recursive. - Anonymous",
        "Why was the developer's coffee cold? He left it in the class. - Anonymous",
        "Programming is the only profession where we build without blueprints. - Anonymous",
        "The best thing about a boolean is even if you are wrong, you are only off by a bit. - Anonymous",
        "I don't always test my code, but when I do, I do it in production. - Most Developers",
        "There are two hard problems in computer science: cache invalidation, naming things, and off-by-one errors.",
        "It works on my machine. - Every Developer Ever",
        "The cloud is just someone else's computer. - Anonymous",
        "There is no place like 127.0.0.1. - Anonymous",
        "ChatGPT is like having a junior developer who is very confident. - Anonymous",
        "The best debugger ever made is the one you think about before you write the code. - Anonymous",
        "If you think your code is perfect, you haven't tested it enough. - Anonymous",
        "You can't have a software crisis forever because eventually the software will be obsolete. - Anonymous",
        "To iterate is human, to recurse divine. - L. Peter Deutsch",
        "The best way to predict the future is to implement it. - Anonymous",
        "A hacker is someone who knows that there is a difference between the way things are and the way society tells us they are. - Anonymous",
        "The internet is the world's largest library. It's just that all the books are on the floor. - John Allen Paulos",
        "The world is full of magical things patiently waiting for our senses to grow sharper. - W.B. Yeats",
        "The most difficult thing is the decision to act, the rest is merely tenacity. - Amelia Earhart",
        "Start where you are. Use what you have. Do what you can. - Arthur Ashe",
        "The secret of getting ahead is getting started. - Mark Twain",
        "The future depends on what you do today. - Mahatma Gandhi",
        "It does not matter how slowly you go as long as you do not stop. - Confucius",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Your time is limited, so don't waste it living someone else's life. - Steve Jobs",
        "Everything around you that you call life was made up by people that were no smarter than you. - Steve Jobs",
        "Design is not just what it looks like and feels like. Design is how it works. - Steve Jobs",
        "Innovation distinguishes between a leader and a follower. - Steve Jobs",
        "Sometimes when you innovate, you make mistakes. It is best to admit them quickly, and get on with improving. - Steve Jobs",
        "Quality is more important than quantity. One home run is much better than two doubles. - Steve Jobs",
        "I'm convinced that about half of what separates successful entrepreneurs from the non-successful ones is pure perseverance. - Steve Jobs",
        "It's really hard to design products by focus groups. A lot of times, people don't know what they want until you show it to them. - Steve Jobs",
        "Being the richest man in the cemetery doesn't matter to me. Going to bed at night saying we've done something wonderful, that's what matters to me. - Steve Jobs",
        "My favorite things in life don't cost any money. It's really clear that the most precious resource we all have is time. - Steve Jobs",
        "Remembering that you are going to die is the best way I know to avoid the trap of thinking you have something to lose. - Steve Jobs",
        "The only way to be truly satisfied is to do what you believe is great work. - Steve Jobs",
        "You can't connect the dots looking forward; you can only connect them looking backwards. - Steve Jobs",
        "Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. - Steve Jobs",
        "The people who are crazy enough to think they can change the world are the ones who do. - Apple Ad",
        "We're here to put a dent in the universe. Otherwise why else even be here? - Steve Jobs",
        "Details matter, it's worth waiting to get it right. - Steve Jobs",
        "Stay hungry, stay foolish. - Steve Jobs",
        "I want to put a ding in the universe. - Steve Jobs",
        "Sometimes life hits you in the head with a brick. Don't lose faith. - Steve Jobs",
        "If you do something and it turns out pretty good, then you should go do something else wonderful, not dwell on it for too long. - Steve Jobs",
        "You can't just ask customers what they want and then try to give that to them. By the time you get it built, they'll want something new. - Steve Jobs",
        "We don't get a chance to do that many things, and every one should be really excellent. - Steve Jobs",
        "I would trade all of my technology for an afternoon with Socrates. - Steve Jobs",
        "Think different. - Apple Slogan",
        "The best way to predict the future is to invent it. - Alan Kay",
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "The way to get started is to quit talking and begin doing. - Walt Disney",
        "If life were predictable it would cease to be life, and be without flavor. - Eleanor Roosevelt",
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
        "The purpose of our lives is to be happy. - Dalai Lama",
        "Get busy living or get busy dying. - Stephen King",
        "The unexamined life is not worth living. - Socrates",
        "The good life is one inspired by love and guided by knowledge. - Bertrand Russell",
        "The only impossible journey is the one you never begin. - Tony Robbins",
        "It is during our darkest moments that we must focus to see the light. - Aristotle",
        "Be the change that you wish to see in the world. - Mahatma Gandhi",
        "An eye for an eye only ends up making the whole world blind. - Mahatma Gandhi",
        "Happiness is when what you think, what you say, and what you do are in harmony. - Mahatma Gandhi",
        "The weak can never forgive. Forgiveness is the attribute of the strong. - Mahatma Gandhi",
        "First they ignore you, then they laugh at you, then they fight you, then you win. - Mahatma Gandhi",
        "Live as if you were to die tomorrow. Learn as if you were to live forever. - Mahatma Gandhi",
        "The future depends on what you do today. - Mahatma Gandhi",
        "You must be the change you wish to see in the world. - Mahatma Gandhi",
        "No one can make you feel inferior without your consent. - Eleanor Roosevelt",
        "Great minds discuss ideas; average minds discuss events; small minds discuss people. - Eleanor Roosevelt",
        "The only thing we have to fear is fear itself. - Franklin D. Roosevelt",
        "When you reach the end of your rope, tie a knot in it and hang on. - Franklin D. Roosevelt",
        "The best leader is the one who inspires people to have confidence in themselves. - Eleanor Roosevelt",
        "If you want to go fast, go alone. If you want to go far, go together. - African Proverb",
        "The journey of a thousand miles begins with a single step. - Lao Tzu",
        "Nature does not hurry, yet everything is accomplished. - Lao Tzu",
        "When I let go of what I am, I become what I might be. - Lao Tzu",
        "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese Proverb",
        "A smooth sea never made a skilled sailor. - Franklin D. Roosevelt",
        "What we achieve inwardly will change outer reality. - Plutarch",
        "The mind is everything. What you think you become. - Buddha",
        "Health is the greatest gift, contentment the greatest wealth, faithfulness the best relationship. - Buddha",
        "Three things cannot be long hidden: the sun, the moon, and the truth. - Buddha",
        "In the end, only three things matter: how much you loved, how gently you lived, and how gracefully you let go of things not meant for you. - Buddha",
        "The trouble is, you think you have time. - Buddha",
        "A dog is the only thing on earth that loves you more than you love yourself. - Josh Billings",
        "The greatest pleasure of a dog is that you may make a fool of yourself with him and not only will he not scold you, but he will make a fool of himself too. - Samuel Butler",
        "Dogs do speak, but only to those who know how to listen. - Orhan Pamuk",
        "The better I get to know men, the more I find myself loving dogs. - Charles de Gaulle",
        "Dogs are not our whole life, but they make our lives whole. - Roger Caras",
        "Happiness is a warm puppy. - Charles M. Schulz",
        "A cat has absolute emotional honesty: human beings, for one reason or another, may hide their feelings, but a cat does not. - Ernest Hemingway",
        "One cat just leads to another. - Ernest Hemingway",
        "Time spent with cats is never wasted. - Sigmund Freud",
        "A cat can be trusted to purr when she is pleased. - Aldous Huxley",
        "Cats rule the world. - Jim Davis",
        "Dogs come when they're called; cats take a message and get back to you. - Mary Bly",
        "The clearest way into the Universe is through a forest wilderness. - John Muir",
        "In every walk with nature one receives far more than he seeks. - John Muir",
        "The mountains are calling and I must go. - John Muir",
        "Nature always wears the colors of the spirit. - Ralph Waldo Emerson",
        "Adopt the pace of nature: her secret is patience. - Ralph Waldo Emerson",
        "To the man who loves art for its own sake, it is frequently in its least important and lowliest manifestations that the keenest pleasure is to be derived. - Arthur Conan Doyle",
    ]
    return random.choice(quotes)

def show_more_quotes():
    additionals = [
        "Education is the most powerful weapon which you can use to change the world. - Nelson Mandela",
        "The function of education is to teach one to think intensively and to think critically. - Martin Luther King Jr.",
        "Intelligence plus character that is the goal of true education. - Martin Luther King Jr.",
        "The ultimate measure of a man is not where he stands in moments of comfort, but where he stands at times of challenge. - Martin Luther King Jr.",
        "Darkness cannot drive out darkness; only light can do that. Hate cannot drive out hate; only love can do that. - Martin Luther King Jr.",
        "I have decided to stick with love. Hate is too great a burden to bear. - Martin Luther King Jr.",
        "Faith is taking the first step even when you don't see the whole staircase. - Martin Luther King Jr.",
        "We must accept finite disappointment, but never lose infinite hope. - Martin Luther King Jr.",
        "The time is always right to do what is right. - Martin Luther King Jr.",
        "Life's most persistent and urgent question is, 'What are you doing for others?' - Martin Luther King Jr.",
        "The greatest wealth is to live content with little. - Plato",
        "Wise men speak because they have something to say; fools because they have to say something. - Plato",
        "Knowledge which is acquired under compulsion obtains no hold on the mind. - Plato",
        "Only the dead have seen the end of war. - Plato",
        "Necessity is the mother of invention. - Plato",
        "He who is not a good servant will not be a good master. - Plato",
        "Be kind, for everyone you meet is fighting a hard battle. - Plato",
        "The measure of a man is what he does with power. - Plato",
        "You can discover more about a person in an hour of play than in a year of conversation. - Plato",
        "At the touch of love everyone becomes a poet. - Plato",
        "Courage is knowing what not to fear. - Plato",
        "We are what we repeatedly do. Excellence, then, is not an act, but a habit. - Aristotle",
        "It is the mark of an educated mind to be able to entertain a thought without accepting it. - Aristotle",
        "Patience is bitter, but its fruit is sweet. - Aristotle",
        "The energy of the mind is the essence of life. - Aristotle",
        "Pleasure in the job puts perfection in the work. - Aristotle",
        "The whole is greater than the sum of its parts. - Aristotle",
        "Happiness depends upon ourselves. - Aristotle",
        "A friend to all is a friend to none. - Aristotle",
        "The worst form of inequality is to try to make unequal things equal. - Aristotle",
        "To avoid criticism say nothing, do nothing, be nothing. - Aristotle",
        "What is a friend? A single soul dwelling in two bodies. - Aristotle",
        "Wonder is the beginning of wisdom. - Socrates",
        "I cannot teach anybody anything, I can only make them think. - Socrates",
        "Contentment is natural wealth, luxury is artificial poverty. - Socrates",
        "The only true wisdom is in knowing you know nothing. - Socrates",
        "There is only one good, knowledge, and one evil, ignorance. - Socrates",
        "The unexamined life is not worth living. - Socrates",
        "I know that I am intelligent, because I know that I know nothing. - Socrates",
        "He who is not contented with what he has, would not be contented with what he would like to have. - Socrates",
        "To move the world, we must first move ourselves. - Socrates",
        "A system of morality which is based on relative emotional values is a mere illusion. - Socrates",
        "Virtue is knowledge. - Socrates",
        "Think not those faithful who praise all your words and actions, but those who kindly reprove your faults. - Socrates",
        "Nature and books belong to the eyes that see them. - Ralph Waldo Emerson",
        "The earth laughs in flowers. - Ralph Waldo Emerson",
        "To believe your own thought, to believe that what is true for you in your private heart is true for all men, that is genius. - Ralph Waldo Emerson",
        "Nothing great was ever achieved without enthusiasm. - Ralph Waldo Emerson",
        "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
        "Do not go where the path may lead, go instead where there is no path and leave a trail. - Ralph Waldo Emerson",
        "What you do speaks so loudly that I cannot hear what you say. - Ralph Waldo Emerson",
        "In every work of genius we recognize our own rejected thoughts. - Ralph Waldo Emerson",
        "Shallow men believe in luck. Strong men believe in cause and effect. - Ralph Waldo Emerson",
        "Always do what you are afraid to do. - Ralph Waldo Emerson",
        "For every minute you are angry you lose sixty seconds of happiness. - Ralph Waldo Emerson",
        "The sun shines and warms and lights us and we have no curiosity to know why this is so. - Ralph Waldo Emerson",
        "Money often costs too much. - Ralph Waldo Emerson",
        "A great man is always willing to be little. - Ralph Waldo Emerson",
        "The good news is that the moment you decide that what you know is more important than what you have been taught to remember, you will have shifted gears in your quest for abundance. - Wayne Dyer",
        "If you change the way you look at things, the things you look at change. - Wayne Dyer",
        "When you judge another, you do not define them, you define yourself. - Wayne Dyer",
        "You attract what you are, not what you want. - Wayne Dyer",
        "Abundance is not something we acquire. It is something we tune into. - Wayne Dyer",
        "You cannot always control what goes on outside. But you can always control what goes on inside. - Wayne Dyer",
        "Conflict cannot survive without your participation. - Wayne Dyer",
        "All blame is a waste of time. - Wayne Dyer",
        "Do not die with your music still inside you. - Wayne Dyer",
        "The power of intention is the power to manifest. - Wayne Dyer",
        "There is no scarcity of opportunity to make a living at what you love. - Wayne Dyer",
        "Everything you want is on the other side of fear. - Jack Canfield",
        "What we think, we become. - Buddha",
        "The mind is everything. What you think you become. - Buddha",
        "Peace comes from within. Do not seek it without. - Buddha",
        "Three things cannot long be hidden: the sun, the moon, and the truth. - Buddha",
        "An insincere and evil friend is more to be feared than a wild beast. - Buddha",
        "To conquer oneself is a greater victory than to conquer thousands in a battle. - Buddha",
        "The way is not in the sky. The way is in the heart. - Buddha",
        "Hatred does not cease by hatred, but only by love. - Buddha",
        "No one saves us but ourselves. No one can and no one may. We ourselves must walk the path. - Buddha",
        "Better than a thousand hollow words is one word that brings peace. - Buddha",
        "A jug fills drop by drop. - Buddha",
        "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment. - Buddha",
        "Even death is not to be feared by one who has lived wisely. - Buddha",
        "There is no path to happiness: happiness is the path. - Buddha",
        "The secret of health for both mind and body is not to mourn for the past, nor to worry about the future, but to live the present moment wisely and earnestly. - Buddha",
        "Your purpose in life is to find your purpose and give your whole heart and soul to it. - Buddha",
        "Thousands of candles can be lighted from a single candle, and the life of the candle will not be shortened. Happiness never decreases by being shared. - Buddha",
        "He who walks in the light is not afraid of the darkness. - Buddha",
        "The greatest gift is to give your love and compassion. - Buddha",
        "If you truly loved yourself, you could never hurt another. - Buddha",
        "We are shaped by our thoughts; we become what we think. - Buddha",
        "When the mind is pure, joy follows like a shadow that never leaves. - Buddha",
        "Happiness never decreases by being shared. - Buddha",
        "To enjoy good health, to bring true happiness to one's family, to bring peace to all, one must first discipline and control one's own mind. - Buddha",
        "A disciplined mind brings happiness. - Buddha",
        "All that we are is the result of what we have thought. - Buddha",
        "Do not overrate what you have received, nor envy others. He who envies others does not obtain peace of mind. - Buddha",
        "Speak only with intention to uplift and inspire. - Buddha",
        "Practice makes perfect. - Proverb",
        "Actions speak louder than words. - Proverb",
        "When in Rome, do as the Romans do. - Proverb",
        "The early bird catches the worm. - Proverb",
        "A picture is worth a thousand words. - Proverb",
        "All that glitters is not gold. - Proverb",
        "Better late than never. - Proverb",
        "Don't count your chickens before they hatch. - Proverb",
        "Every cloud has a silver lining. - Proverb",
        "Honesty is the best policy. - Proverb",
        "If it ain't broke, don't fix it. - Proverb",
        "Ignorance is bliss. - Proverb",
        "It takes two to tango. - Proverb",
        "Knowledge is power. - Proverb",
        "Laughter is the best medicine. - Proverb",
        "Look before you leap. - Proverb",
        "Practice what you preach. - Proverb",
        "The pen is mightier than the sword. - Proverb",
        "There's no place like home. - Proverb",
        "Too many cooks spoil the broth. - Proverb",
        "Where there's a will, there's a way. - Proverb",
        "You can't judge a book by its cover. - Proverb",
        "You reap what you sow. - Proverb",
        "Give a man a fish and you feed him for a day; teach a man to fish and you feed him for a lifetime. - Proverb",
        "Don't put all your eggs in one basket. - Proverb",
        "The grass is always greener on the other side. - Proverb",
        "Don't bite the hand that feeds you. - Proverb",
        "Rome wasn't built in a day. - Proverb",
        "What goes around comes around. - Proverb",
        "When life gives you lemons, make lemonade. - Proverb",
        "Fortune favors the bold. - Proverb",
        "Necessity is the mother of invention. - Proverb",
        "The squeaky wheel gets the grease. - Proverb",
        "Birds of a feather flock together. - Proverb",
        "A friend in need is a friend indeed. - Proverb",
        "Absence makes the heart grow fonder. - Proverb",
        "Easy come, easy go. - Proverb",
        "Haste makes waste. - Proverb",
        "If you can't beat them, join them. - Proverb",
        "Let sleeping dogs lie. - Proverb",
        "Old habits die hard. - Proverb",
        "Out of sight, out of mind. - Proverb",
        "Strike while the iron is hot. - Proverb",
        "The apple doesn't fall far from the tree. - Proverb",
        "Time heals all wounds. - Proverb",
        "Variety is the spice of life. - Proverb",
    ]
    return random.choice(additionals)

def random_animal():
    animals = [
        "Aardvark", "Albatross", "Alligator", "Alpaca", "Ant", "Anteater", "Antelope", "Ape",
        "Armadillo", "Baboon", "Badger", "Barracuda", "Bat", "Bear", "Beaver", "Bee",
        "Bison", "Boar", "Buffalo", "Butterfly", "Camel", "Capybara", "Caribou", "Cassowary",
        "Cat", "Caterpillar", "Cheetah", "Chicken", "Chimpanzee", "Chinchilla", "Cobra", "Cockroach",
        "Condor", "Cougar", "Cow", "Coyote", "Crab", "Crane", "Cricket", "Crocodile",
        "Crow", "Deer", "Dingo", "Dinosaur", "Dog", "Dolphin", "Donkey", "Dragonfly",
        "Duck", "Eagle", "Echidna", "Eel", "Elephant", "Elk", "Emu", "Falcon",
        "Ferret", "Finch", "Fish", "Flamingo", "Fly", "Fox", "Frog", "Gazelle",
        "Gecko", "Gibbon", "Giraffe", "Goat", "Goose", "Gorilla", "Grasshopper", "Grizzly",
        "Hamster", "Hare", "Hawk", "Hedgehog", "Heron", "Hippo", "Hornet", "Horse",
        "Hummingbird", "Hyena", "Ibis", "Iguana", "Impala", "Jackal", "Jaguar", "Jellyfish",
        "Kangaroo", "Koala", "Komodo", "Kookaburra", "Ladybug", "Lemur", "Leopard", "Lion",
        "Lizard", "Llama", "Lobster", "Lynx", "Macaw", "Magpie", "Manatee", "Mongoose",
        "Monkey", "Moose", "Mosquito", "Moth", "Mouse", "Narwhal", "Newt", "Nightingale",
        "Octopus", "Okapi", "Opossum", "Orangutan", "Orca", "Ostrich", "Otter", "Owl",
        "Panda", "Panther", "Parrot", "Peacock", "Pelican", "Penguin", "Pig", "Pigeon",
        "Platypus", "Polar Bear", "Porcupine", "Puma", "Quail", "Quelea", "Quokka", "Rabbit",
        "Raccoon", "Rat", "Rattlesnake", "Raven", "Reindeer", "Rhino", "Robin", "Rook",
        "Salamander", "Salmon", "Scorpion", "Seahorse", "Seal", "Shark", "Sheep", "Shrimp",
        "Skunk", "Sloth", "Snail", "Snake", "Sparrow", "Spider", "Squid", "Squirrel",
        "Starfish", "Stingray", "Stork", "Swan", "Tapir", "Tarantula", "Tiger", "Toad",
        "Tortoise", "Toucan", "Turkey", "Turtle", "Viper", "Vulture", "Wallaby", "Walrus",
        "Wasp", "Weasel", "Whale", "Wildcat", "Wolf", "Wolverine", "Wombat", "Woodpecker",
        "Worm", "Yak", "Zebra", "Zebu",
    ]
    return random.choice(animals)

def random_color():
    colors = [
        "Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Pink", "Brown",
        "Black", "White", "Gray", "Cyan", "Magenta", "Lime", "Maroon", "Navy",
        "Olive", "Teal", "Aqua", "Azure", "Beige", "Coral", "Crimson", "Emerald",
        "Fuchsia", "Gold", "Indigo", "Ivory", "Jade", "Lavender", "Lilac", "Mauve",
        "Mint", "Peach", "Plum", "Ruby", "Salmon", "Scarlet", "Silver", "Tan",
        "Turquoise", "Violet", "Wheat", "Amber", "Apricot", "Burgundy", "Chartreuse", "Copper",
        "Cream", "Denim", "Ebony", "Fawn", "Garnet", "Honey", "Khaki", "Lemon",
        "Mustard", "Ochre", "Periwinkle", "Pewter", "Rose", "Saffron", "Sapphire", "Sienna",
        "Sky", "Slate", "Steel", "Tangerine", "Taupe", "Topaz", "Vermilion", "Wine",
    ]
    return random.choice(colors)

def random_fruit():
    fruits = [
        "Apple", "Apricot", "Avocado", "Banana", "Blackberry", "Blueberry", "Boysenberry", "Cantaloupe",
        "Cherry", "Coconut", "Cranberry", "Date", "Dragonfruit", "Elderberry", "Fig", "Gooseberry",
        "Grape", "Grapefruit", "Guava", "Honeydew", "Jackfruit", "Kiwi", "Kumquat", "Lemon",
        "Lime", "Lychee", "Mango", "Mangosteen", "Mulberry", "Nectarine", "Olive", "Orange",
        "Papaya", "Passionfruit", "Peach", "Pear", "Persimmon", "Pineapple", "Plum", "Pomegranate",
        "Raspberry", "Rhubarb", "Strawberry", "Tangerine", "Ugli", "Watermelon", "Cucumber", "Pumpkin",
    ]
    return random.choice(fruits)

def random_vegetable():
    veggies = [
        "Artichoke", "Arugula", "Asparagus", "Beet", "Bell Pepper", "Bok Choy", "Broccoli", "Brussels Sprout",
        "Cabbage", "Carrot", "Cauliflower", "Celery", "Chard", "Chili", "Collard", "Corn",
        "Cucumber", "Eggplant", "Endive", "Fennel", "Garlic", "Ginger", "Green Bean", "Jalapeno",
        "Kale", "Leek", "Lettuce", "Mushroom", "Okra", "Onion", "Parsnip", "Pea",
        "Potato", "Pumpkin", "Radish", "Rutabaga", "Shallot", "Spinach", "Squash", "Sweet Potato",
        "Taro", "Tomato", "Turnip", "Wasabi", "Watercress", "Yam", "Zucchini", "Seaweed",
    ]
    return random.choice(veggies)

def random_element():
    elements = [
        ("Hydrogen", "H", 1), ("Helium", "He", 2), ("Lithium", "Li", 3), ("Beryllium", "Be", 4),
        ("Boron", "B", 5), ("Carbon", "C", 6), ("Nitrogen", "N", 7), ("Oxygen", "O", 8),
        ("Fluorine", "F", 9), ("Neon", "Ne", 10), ("Sodium", "Na", 11), ("Magnesium", "Mg", 12),
        ("Aluminum", "Al", 13), ("Silicon", "Si", 14), ("Phosphorus", "P", 15), ("Sulfur", "S", 16),
        ("Chlorine", "Cl", 17), ("Argon", "Ar", 18), ("Potassium", "K", 19), ("Calcium", "Ca", 20),
        ("Scandium", "Sc", 21), ("Titanium", "Ti", 22), ("Vanadium", "V", 23), ("Chromium", "Cr", 24),
        ("Manganese", "Mn", 25), ("Iron", "Fe", 26), ("Cobalt", "Co", 27), ("Nickel", "Ni", 28),
        ("Copper", "Cu", 29), ("Zinc", "Zn", 30), ("Gallium", "Ga", 31), ("Germanium", "Ge", 32),
        ("Arsenic", "As", 33), ("Selenium", "Se", 34), ("Bromine", "Br", 35), ("Krypton", "Kr", 36),
        ("Rubidium", "Rb", 37), ("Strontium", "Sr", 38), ("Yttrium", "Y", 39), ("Zirconium", "Zr", 40),
        ("Niobium", "Nb", 41), ("Molybdenum", "Mo", 42), ("Technetium", "Tc", 43), ("Ruthenium", "Ru", 44),
        ("Rhodium", "Rh", 45), ("Palladium", "Pd", 46), ("Silver", "Ag", 47), ("Cadmium", "Cd", 48),
        ("Indium", "In", 49), ("Tin", "Sn", 50), ("Antimony", "Sb", 51), ("Tellurium", "Te", 52),
        ("Iodine", "I", 53), ("Xenon", "Xe", 54), ("Cesium", "Cs", 55), ("Barium", "Ba", 56),
        ("Lanthanum", "La", 57), ("Cerium", "Ce", 58), ("Praseodymium", "Pr", 59), ("Neodymium", "Nd", 60),
        ("Promethium", "Pm", 61), ("Samarium", "Sm", 62), ("Europium", "Eu", 63), ("Gadolinium", "Gd", 64),
        ("Terbium", "Tb", 65), ("Dysprosium", "Dy", 66), ("Holmium", "Ho", 67), ("Erbium", "Er", 68),
        ("Thulium", "Tm", 69), ("Ytterbium", "Yb", 70), ("Lutetium", "Lu", 71), ("Hafnium", "Hf", 72),
        ("Tantalum", "Ta", 73), ("Tungsten", "W", 74), ("Rhenium", "Re", 75), ("Osmium", "Os", 76),
        ("Iridium", "Ir", 77), ("Platinum", "Pt", 78), ("Gold", "Au", 79), ("Mercury", "Hg", 80),
        ("Thallium", "Tl", 81), ("Lead", "Pb", 82), ("Bismuth", "Bi", 83), ("Polonium", "Po", 84),
        ("Astatine", "At", 85), ("Radon", "Rn", 86), ("Francium", "Fr", 87), ("Radium", "Ra", 88),
        ("Actinium", "Ac", 89), ("Thorium", "Th", 90), ("Protactinium", "Pa", 91), ("Uranium", "U", 92),
    ]
    return random.choice(elements)

def random_number():
    import time
    return random.randint(0, int(time.time()))

def random_uuid():
    import uuid
    return str(uuid.uuid4())

def draw_pyramid(n):
    lines = []
    for i in range(n):
        lines.append(" " * (n - i - 1) + "*" * (2 * i + 1))
    return "\n".join(lines)

def draw_triangle(n):
    lines = []
    for i in range(1, n + 1):
        lines.append("*" * i)
    return "\n".join(lines)

def draw_reverse_triangle(n):
    lines = []
    for i in range(n, 0, -1):
        lines.append("*" * i)
    return "\n".join(lines)

def draw_hourglass(n):
    lines = []
    for i in range(n, 0, -1):
        lines.append(" " * (n - i) + "*" * (2 * i - 1))
    for i in range(2, n + 1):
        lines.append(" " * (n - i) + "*" * (2 * i - 1))
    return "\n".join(lines)

def draw_circle(r):
    lines = []
    for y in range(-r, r + 1):
        line = ""
        for x in range(-r, r + 1):
            if x*x + y*y <= r*r:
                line += "*"
            else:
                line += " "
        lines.append(line)
    return "\n".join(lines)

def draw_pineapple():
    return r"""
    .   .
   .     .
  .       .
 .  .   .  .
.    . .    .
   .     .
  .       .
 .         .
.           .
   |||||
   |||||
"""

def draw_ghost():
    return r"""
      .-.
    .'   `.
   /       \
  |  0   0  |
  |    ^    |
  \   ---   /
   '.____.'
      ||
     /||\
    / || \
      ||
     /||\
    / || \
"""

def draw_alien():
    return r"""
     .---.
    /     \
   |  . .  |
   |  ' '  |
    \  ~  /
    _|___|_
   |       |
   |   @   |
   |_______|
"""

def draw_bird():
    return r"""
      __
   '-'  \
  /      |
 /   __  |
|   /  \ |
|   \__/ |
 \_______/
"""

def draw_turtle():
    return r"""
      _____
     /     \
    | . . . |
    |  ...  |
     \_____/
     /|   |\
    / |   | \
"""

def draw_unicorn():
    return r"""
        \
         \__
         /  \
        / . .\
       /  ___ \
      /  |   | \
     /   |   |  \
    /____|___|___\
         |   |
         |   |
         |   |
        /|\ /|\
"""

def draw_robot():
    return r"""
     .-""-.
    /      \
   | O    O |
   |    _   |
   |   ( )  |
    \  ___ /
   .'______'.
   |________|
"""

def draw_spaceship():
    return r"""
      /\
     /  \
    /    \
   /______\
   |      |
   |      |
  /|      |\
 / |      | \
/__|______|__\
   |      |
   |______|
"""

def draw_dragon():
    return r"""
      /\   /\
     /  \ /  \
    /    V    \
   |  (O) (O)  |
   |    ___    |
    \  /   \  /
     \/     \/
     /  ___  \
    /  |   |  \
   /   |___|   \
"""

def draw_crown():
    return r"""
   .-""-.
  / .--. \
 / /    \ \
/_/      \_\
|  \    /  |
|   \__/   |
|          |
|__________|
"""

def draw_castle():
    lines = []
    for i in range(5):
        line = ""
        for j in range(10):
            if (i == 0 and j in [0, 4, 5, 9]) or (i == 1 and j in [0, 4, 5, 9]) or (i == 2) or (i == 3) or (i == 4):
                line += "*" * (1 if j not in [2, 3, 7, 8] or i < 2 else 1)
            else:
                line += " "
        lines.append(line)
    return "\n".join(lines)

def draw_mountain():
    return r"""
       /\
      /  \
     /    \
    /______\
   /|      |\
  / |      | \
 /  |      |  \
/___|______|___\
"""

def draw_wave(n=5):
    lines = []
    for i in range(n):
        line = ""
        for j in range(40):
            val = math.sin(j * 0.5 - i * 0.5)
            if abs(val - (n//2 - i) * 0.3) < 0.3:
                line += "~"
            else:
                line += " "
        lines.append(line)
    return "\n".join(lines)

def draw_sun():
    return r"""
      \
   .  .  .
 .  .  .  .
.  .  O  .  .
 .  .  .  .
   .  .  .
      /
"""

def draw_moon():
    return r"""
     .-.
   .'   `.
  /       \
 |  O   O  |
 |    _    |
  \  ___  /
   `.____.'
"""

def draw_star_shape():
    return r"""
     /\
    /  \
   / /\ \
  / /__\ \
 /_/____\_\
   \    /
    \  /
     \/
"""

def draw_arrow_up(n):
    lines = []
    for i in range(n):
        lines.append(" " * (n - i - 1) + "*" * (2 * i + 1))
    for i in range(n // 2):
        lines.append(" " * (n - 2) + "|||")
    return "\n".join(lines)

def draw_arrow_down(n):
    lines = []
    for i in range(n // 2):
        lines.append(" " * (n - 2) + "|||")
    for i in range(n, 0, -1):
        lines.append(" " * (n - i) + "*" * (2 * i - 1))
    return "\n".join(lines)

def draw_arrow_left(n):
    lines = []
    for i in range(n):
        lines.append(" " * (n - i - 1) + "*" * (i + 1))
    for i in range(n - 2, -1, -1):
        lines.append(" " * (n - i - 1) + "*" * (i + 1))
    return "\n".join(lines)

def draw_arrow_right(n):
    lines = []
    for i in range(n):
        lines.append(" " * (n - 1) + "*" * (i + 1))
    for i in range(n - 2, -1, -1):
        lines.append(" " * (n - 1) + "*" * (i + 1))
    return "\n".join(lines)

def draw_dna():
    return r"""
    /\  /\
   /  \/  \
  /   /\   \
 /   /  \   \
 \  /    \  /
  \/      \/
  /\      /\
 /  \    /  \
/   \  /   \
\   \/   /
 \  /\  /
  \/  \/
"""

def draw_pacman():
    return r"""
    .-""-.
   / .--. \
  / /    \ \
 | |  __ | |
 | | |__|| |
  \ \    / /
   \ '--' /
    `-..-'
"""

def draw_bowtie(n=4):
    lines = []
    for i in range(n):
        lines.append("*" * (i + 1) + " " * (2 * (n - i - 1)) + "*" * (i + 1))
    for i in range(n - 1, -1, -1):
        lines.append("*" * (i + 1) + " " * (2 * (n - i - 1)) + "*" * (i + 1))
    return "\n".join(lines)

def draw_flag(n=5):
    lines = []
    for i in range(n):
        lines.append("|" + "*" * (n * 2))
    lines.append("|")
    lines.append("|")
    return "\n".join(lines)

def draw_stairs(n=5):
    lines = []
    for i in range(1, n + 1):
        lines.append(" " * (n - i) * 2 + "_|")
    return "\n".join(lines)

def draw_table(n=4):
    lines = []
    lines.append("+" + "-" * (n * 4 - 1) + "+")
    for i in range(n):
        lines.append("|" + " " * (n * 4 - 1) + "|")
    lines.append("+" + "-" * (n * 4 - 1) + "+")
    for i in range(n):
        lines.append("|" + " " * (n * 4 - 1) + "|")
    lines.append("+" + "-" * (n * 4 - 1) + "+")
    return "\n".join(lines)

def draw_candle():
    return r"""
      |
     / \
    / _ \
   |  |  |
   |  |  |
   |  |  |
   |  |  |
   |  |  |
   |  |  |
    \   /
     \ /
      .
      .
"""

def draw_lamp():
    return r"""
      .
     /|\
    / | \
   /  |  \
   |  |  |
   |  |  |
   |  |  |
   |  |  |
   |  |  |
   |  |  |
   |  |  |
  /   |   \
 /    |    \
/_____|_____\
"""

def draw_key():
    return r"""
      .-.
     /   \
    |  _  |
    | | | |
    | | | |
    | | | |
    | | | |
    | | | |
    |_| |_|
     /_\/_\
"""

def draw_lock():
    return r"""
     .-----.
    /       \
   |  .---.  |
   |  |   |  |
   |  '---'  |
   |         |
   | [_____] |
    \_______/
"""

def draw_phone():
    return r"""
     .-------.
    /         \
   |   O   O   |
   |           |
   |    ___    |
   |   |   |   |
   |   |___|   |
    \_________/
"""

def draw_tv():
    return r"""
     .----------.
    /            \
   |   _______    |
   |  |       |   |
   |  | SCREEN|   |
   |  |_______|   |
   |    ___       |
    \__/___\_____/
      |     |
      |     |
     _|     |_
    /________\
"""

def draw_envelope():
    return r"""
    .------------------.
   /                  /|
  /    .----------.  / |
 /    /          /  /  |
|    /          /  /   |
|   /          /  /    |
|  '----------'  /     |
|                /      |
'----------------'______|
"""

def draw_coffee():
    return r"""
      .-.
     /   \
    |  .  |
    |     |
    |     |
    |     |
     \___/
      | |
      | |
      | |
     /   \
    /_____\
"""

def draw_burger():
    return r"""
     .-""-.
    /      \
   |  ____  |
   | /    \ |
   || BURG ||
   | \____/ |
   |  ____  |
   | /    \ |
   || PATTY||
   | \____/ |
   |  ____  |
   | /    \ |
   || LETTU||
   | \____/ |
   |  ____  |
   | /    \ |
   || TOMAT||
   | \____/ |
   |        |
    \______/
"""

def draw_pizza():
    return r"""
       .-.
      /   \
     /  .  \
    / .   . \
   /  .  .   \
  / .    . .  \
 /_____________\
  \    ___    /
   \  /   \  /
    \/     \/
"""

def draw_ice_cream():
    return r"""
      .-.
     /   \
    | . . |
    |  .  |
     \___/
      | |
      | |
      | |
      | |
      | |
     /   \
    /_____\
"""

def draw_cake():
    return r"""
     .-------.
    /         \
   |  .   .   |
   |    .     |
   | .   .  . |
    \   ___  /
     |  | |  |
     |  | |  |
     |  | |  |
     |  | |  |
     |__| |__|
"""

def draw_house_with_sun():
    lines = []
    lines.append("        \\")
    lines.append("     .  .  .")
    lines.append("   .  .  .  .")
    lines.append("  .  .  O  .  .")
    lines.append("   .  .  .  .")
    lines.append("     .  .  .")
    lines.append("        /")
    lines.append("      /\\")
    lines.append("     /  \\")
    lines.append("    /    \\")
    lines.append("   /______\\")
    lines.append("   |      |")
    lines.append("   |  []  |")
    lines.append("   |      |")
    lines.append("   |____  |")
    lines.append("   |    | |")
    lines.append("   |____|_|")
    return "\n".join(lines)

def convert_seconds(seconds):
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    return "{}d {}h {}m {}s".format(days, hours, minutes, secs)

def generate_random_data(size=10):
    return [random.randint(1, 100) for _ in range(size)]

def random_shuffle_list(items):
    lst = items.copy()
    random.shuffle(lst)
    return lst

def flatten_list(nested):
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result

def chunk_list(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]

def unique_elements(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

def list_intersection(a, b):
    return list(set(a) & set(b))

def list_union(a, b):
    return list(set(a) | set(b))

def list_difference(a, b):
    return list(set(a) - set(b))

def list_symmetric_difference(a, b):
    return list(set(a) ^ set(b))

def rotate_list(lst, n):
    n = n % len(lst) if lst else 0
    return lst[n:] + lst[:n]

def find_all_indexes(lst, value):
    return [i for i, x in enumerate(lst) if x == value]

def split_evens_odds(nums):
    evens = [x for x in nums if x % 2 == 0]
    odds = [x for x in nums if x % 2 != 0]
    return evens, odds

def sum_digits(n):
    return sum(int(d) for d in str(abs(n)))

def reverse_number(n):
    return int(str(abs(n))[::-1]) * (-1 if n < 0 else 1)

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n

def is_perfect_number(n):
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def is_happy_number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1

def collatz_sequence(n):
    seq = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        seq.append(n)
    return seq

def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return [i for i, p in enumerate(primes) if p]

def nth_prime(n):
    count = 0
    num = 2
    while True:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1

def goldbach_conjecture(n):
    if n < 4 or n % 2 != 0:
        return None
    primes = sieve_of_eratosthenes(n)
    for p in primes:
        if n - p in primes:
            return (p, n - p)
    return None

def euler_totient(n):
    result = n
    p = 2
    temp = n
    while p * p <= temp:
        if temp % p == 0:
            while temp % p == 0:
                temp //= p
            result -= result // p
        p += 1
    if temp > 1:
        result -= result // temp
    return result

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def modular_inverse(a, m):
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        return None
    return x % m

def matrix_multiply(a, b):
    rows_a, cols_a = len(a), len(a[0])
    rows_b, cols_b = len(b), len(b[0])
    if cols_a != rows_b:
        return None
    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += a[i][k] * b[k][j]
    return result

def matrix_transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def matrix_determinant(m):
    n = len(m)
    if n == 1:
        return m[0][0]
    if n == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    det = 0
    for j in range(n):
        sub = [[m[i][k] for k in range(n) if k != j] for i in range(1, n)]
        det += m[0][j] * ((-1) ** j) * matrix_determinant(sub)
    return det

def dot_product(a, b):
    return sum(x * y for x, y in zip(a, b))

def cross_product(a, b):
    if len(a) != 3 or len(b) != 3:
        return None
    return [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0]
    ]

def vector_magnitude(v):
    return math.sqrt(sum(x * x for x in v))

def euclidean_distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))

def manhattan_distance(p1, p2):
    return sum(abs(a - b) for a, b in zip(p1, p2))

def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        return -1
    return sum(1 for a, b in zip(s1, s2) if a != b)

def levenshtein_distance(s1, s2):
    if len(s1) < len(s2):
        return levenshtein_distance(s2, s1)
    if len(s2) == 0:
        return len(s1)
    prev = list(range(len(s2) + 1))
    for i, c1 in enumerate(s1):
        curr = [i + 1]
        for j, c2 in enumerate(s2):
            cost = 0 if c1 == c2 else 1
            curr.append(min(curr[j] + 1, prev[j + 1] + 1, prev[j] + cost))
        prev = curr
    return prev[-1]

def to_base(n, base):
    if n == 0:
        return "0"
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    neg = n < 0
    n = abs(n)
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return "-" + result if neg else result

def from_base(s, base):
    return int(s, base) if base <= 36 else None

def sha256_hash(text):
    import hashlib
    return hashlib.sha256(text.encode()).hexdigest()

def md5_hash(text):
    import hashlib
    return hashlib.md5(text.encode()).hexdigest()

def base64_encode(text):
    import base64
    return base64.b64encode(text.encode()).decode()

def base64_decode(text):
    import base64
    try:
        return base64.b64decode(text).decode()
    except:
        return "Invalid base64"

def rot13(text):
    return caesar_cipher(text, 13)

def text_to_ascii(text):
    return [ord(c) for c in text]

def ascii_to_text(codes):
    return "".join(chr(c) for c in codes)

def count_words(text):
    return len(text.split())

def count_sentences(text):
    import re
    return len(re.findall(r'[.!?]+', text))

def count_paragraphs(text):
    return len([p for p in text.split('\n\n') if p.strip()])

def remove_duplicate_words(text):
    words = text.split()
    seen = set()
    result = []
    for w in words:
        if w.lower() not in seen:
            seen.add(w.lower())
            result.append(w)
    return " ".join(result)

def reverse_words(text):
    return " ".join(text.split()[::-1])

def reverse_word_order(text):
    return " ".join(text.split()[::-1])

def sort_words(text):
    return " ".join(sorted(text.split(), key=str.lower))

def shuffle_words(text):
    words = text.split()
    random.shuffle(words)
    return " ".join(words)

def acronym(text):
    return "".join(w[0].upper() for w in text.split() if w)

def capitalize_title(text):
    small_words = {"a", "an", "the", "and", "or", "but", "in", "on", "at", "to", "for", "of", "by", "with"}
    words = text.split()
    result = []
    for i, w in enumerate(words):
        if i == 0 or i == len(words) - 1 or w.lower() not in small_words:
            result.append(w.capitalize())
        else:
            result.append(w.lower())
    return " ".join(result)

def detect_language(text):
    languages = {
        "english": "the and is in it you that was for are",
        "spanish": "el la los las que y en por con su",
        "french": "le la les des dans est que pour avec sur",
        "german": "der die das und mit auf fur ist nicht",
        "italian": "il la le gli che e per con nel sul",
        "portuguese": "o a os as que para com por no na",
        "dutch": "de het een van en met voor niet op",
        "russian": "и в не на что с как это он мы",
        "japanese": "の は を が に で と も から する",
    }
    words = set(text.lower().split())
    best_score = 0
    best_lang = "Unknown"
    for lang, common in languages.items():
        score = sum(1 for w in common.split() if w in words)
        if score > best_score:
            best_score = score
            best_lang = lang
    return best_lang

def spell_check(text):
    common_words = {
        "the", "be", "to", "of", "and", "a", "in", "that", "have", "it",
        "for", "not", "on", "with", "he", "as", "you", "do", "at", "this",
        "but", "his", "by", "from", "they", "we", "say", "her", "she", "or",
        "an", "will", "my", "one", "all", "would", "there", "their", "what",
        "so", "up", "out", "if", "about", "who", "get", "which", "go", "me",
        "when", "make", "can", "like", "time", "no", "just", "him", "know",
        "take", "people", "into", "year", "your", "good", "some", "could",
        "them", "see", "other", "than", "then", "now", "look", "only", "come",
        "its", "over", "think", "also", "back", "after", "use", "two", "how",
        "our", "work", "first", "well", "way", "even", "new", "want", "because",
        "any", "these", "give", "day", "most", "us", "great", "between", "need",
    }
    words = text.split()
    misspelled = [w for w in words if w.lower() not in common_words]
    return misspelled

def word_frequency(text):
    freq = {}
    for w in text.lower().split():
        w = w.strip(".,!?;:'\"()[]{}")
        if w:
            freq[w] = freq.get(w, 0) + 1
    return dict(sorted(freq.items(), key=lambda x: -x[1]))

def longest_word(text):
    words = text.split()
    if not words:
        return ""
    return max(words, key=len)

def shortest_word(text):
    words = text.split()
    if not words:
        return ""
    return min(words, key=len)

def most_common_letter(text):
    letters = [c.lower() for c in text if c.isalpha()]
    if not letters:
        return None
    from collections import Counter
    return Counter(letters).most_common(1)[0]

def has_url(text):
    return "http://" in text.lower() or "https://" in text.lower() or "www." in text.lower()

def has_email(text):
    return "@" in text and "." in text[text.index("@"):]

def extract_numbers(text):
    import re
    return [int(x) for x in re.findall(r'\d+', text)]

def extract_emails(text):
    import re
    return re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', text)

def extract_urls(text):
    import re
    return re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', text)

def remove_html_tags(text):
    import re
    return re.sub(r'<[^>]+>', '', text)

def censor_bad_words(text):
    bad_words = {"bad", "evil", "terrible", "awful", "horrible", "nasty", "mean",
                 "stupid", "dumb", "ugly", "hate", "damn", "hell", "crap", "jerk"}
    words = text.split()
    result = []
    for w in words:
        if w.lower().strip(".,!?;:'\"") in bad_words:
            result.append("*" * len(w))
        else:
            result.append(w)
    return " ".join(result)

def suggest_emoji(text):
    emoji_map = {
        "happy": "😊", "sad": "😢", "love": "❤️", "cool": "😎", "funny": "😂",
        "angry": "😠", "cry": "😭", "wink": "😉", "shock": "😮", "sleep": "😴",
        "music": "🎵", "pizza": "🍕", "cat": "🐱", "dog": "🐶", "tree": "🌳",
        "sun": "☀️", "moon": "🌙", "star": "⭐", "fire": "🔥", "water": "💧",
    }
    for word, emoji in emoji_map.items():
        if word in text.lower():
            return emoji
    return "❓"

def format_json(data):
    import json
    try:
        obj = json.loads(data)
        return json.dumps(obj, indent=2)
    except:
        return "Invalid JSON"

def count_json_elements(data):
    import json
    try:
        obj = json.loads(data)
        if isinstance(obj, dict):
            return len(obj.keys())
        if isinstance(obj, list):
            return len(obj)
        return 1
    except:
        return 0

def csv_to_list(csv_text):
    lines = csv_text.strip().split('\n')
    if not lines:
        return []
    headers = lines[0].split(',')
    data = []
    for line in lines[1:]:
        if line.strip():
            values = line.split(',')
            row = {}
            for i, h in enumerate(headers):
                row[h.strip()] = values[i].strip() if i < len(values) else ""
            data.append(row)
    return data

def simulate_dice_rolls(num=1000, sides=6):
    counts = {i: 0 for i in range(1, sides + 1)}
    for _ in range(num):
        counts[random.randint(1, sides)] += 1
    return counts

def simulate_coin_flips(num=1000):
    heads = 0
    tails = 0
    for _ in range(num):
        if random.randint(0, 1) == 0:
            heads += 1
        else:
            tails += 1
    return heads, tails

def simulate_lottery(max_num=50, picks=6):
    numbers = list(range(1, max_num + 1))
    return sorted(random.sample(numbers, picks))

def birthday_paradox(num_people=23, trials=10000):
    shared = 0
    for _ in range(trials):
        birthdays = [random.randint(1, 365) for _ in range(num_people)]
        if len(set(birthdays)) < num_people:
            shared += 1
    return shared / trials * 100

def monty_hall_simulation(trials=10000):
    stick_wins = 0
    switch_wins = 0
    for _ in range(trials):
        car = random.randint(0, 2)
        choice = random.randint(0, 2)
        if choice == car:
            stick_wins += 1
        else:
            switch_wins += 1
    return stick_wins / trials * 100, switch_wins / trials * 100

def morse_to_text(morse_code):
    morse_map = {
        ".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E","..-.":"F","--.":"G",
        "....":"H","..":"I",".---":"J","-.-":"K",".-..":"L","--":"M","-.":"N",
        "---":"O",".--.":"P","--.-":"Q",".-.":"R","...":"S","-":"T","..-":"U",
        "...-":"V",".--":"W","-..-":"X","-.--":"Y","--..":"Z",
        "-----":"0",".----":"1","..---":"2","...--":"3","....-":"4",
        ".....":"5","-....":"6","--...":"7","---..":"8","----.":"9",
    }
    words = morse_code.split(" / ")
    result = []
    for word in words:
        letters = word.split()
        decoded = ""
        for letter in letters:
            if letter in morse_map:
                decoded += morse_map[letter]
        result.append(decoded)
    return " ".join(result)

def atbash_cipher(text):
    result = []
    for c in text:
        if c.isalpha():
            if c.isupper():
                result.append(chr(ord("Z") - (ord(c) - ord("A"))))
            else:
                result.append(chr(ord("z") - (ord(c) - ord("a"))))
        else:
            result.append(c)
    return "".join(result)

def vigenere_cipher(text, key, encrypt=True):
    result = []
    key = key.upper()
    key_idx = 0
    for c in text:
        if c.isalpha():
            shift = ord(key[key_idx % len(key)]) - ord("A")
            if not encrypt:
                shift = -shift
            base = ord("A") if c.isupper() else ord("a")
            result.append(chr((ord(c) - base + shift) % 26 + base))
            key_idx += 1
        else:
            result.append(c)
    return "".join(result)

def xor_cipher(text, key):
    result = []
    for i, c in enumerate(text):
        result.append(chr(ord(c) ^ ord(key[i % len(key)])))
    return "".join(result)

def substitution_cipher(text, key_map):
    result = []
    for c in text:
        if c.isalpha():
            if c.isupper():
                result.append(key_map.get(c, c))
            else:
                result.append(key_map.get(c.upper(), c).lower())
        else:
            result.append(c)
    return "".join(result)

def generate_nerd_dice():
    return [random.randint(1, 6) for _ in range(4)]

def poker_hand():
    suits = ["♠", "♥", "♦", "♣"]
    ranks = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    hand = []
    used = set()
    while len(hand) < 5:
        rank = random.choice(ranks)
        suit = random.choice(suits)
        card = (rank, suit)
        if card not in used:
            used.add(card)
            hand.append(card)
    return hand

def format_goldbach(limit):
    results = []
    for n in range(4, limit + 1, 2):
        pair = goldbach_conjecture(n)
        if pair:
            results.append("{} = {} + {}".format(n, pair[0], pair[1]))
    return "\n".join(results[:20])

def show_number_facts(num):
    facts = []
    if is_prime(num):
        facts.append("{} is prime.".format(num))
    if is_perfect_number(num):
        facts.append("{} is a perfect number.".format(num))
    if is_armstrong(num):
        facts.append("{} is an Armstrong number.".format(num))
    if is_happy_number(num):
        facts.append("{} is a happy number.".format(num))
    if num % 2 == 0:
        facts.append("{} is even.".format(num))
    else:
        facts.append("{} is odd.".format(num))
    return "\n".join(facts) if facts else "No special facts."

def temperature_summary(celsius):
    f = celsius_to_fahrenheit(celsius)
    k = celsius_to_kelvin(celsius)
    return "{}C = {}F = {}K".format(celsius, f, k)

def time_until_birthday(birth_month, birth_day):
    now = datetime.datetime.now()
    this_year = datetime.date(now.year, birth_month, birth_day)
    if this_year < now.date():
        this_year = datetime.date(now.year + 1, birth_month, birth_day)
    delta = this_year - now.date()
    return "{} days until your next birthday!".format(delta.days)

def days_since_birth(birth_year, birth_month, birth_day):
    try:
        birth = datetime.date(birth_year, birth_month, birth_day)
        delta = datetime.date.today() - birth
        return "You are {} days old.".format(delta.days)
    except:
        return "Invalid date."

def age_in_seconds(birth_year, birth_month, birth_day):
    try:
        birth = datetime.date(birth_year, birth_month, birth_day)
        delta = datetime.date.today() - birth
        return "You are about {} seconds old.".format(delta.days * 86400)
    except:
        return "Invalid date."

def current_time_info():
    now = datetime.datetime.now()
    return "Date: {}\nTime: {:02d}:{:02d}:{:02d}\nWeekday: {}".format(
        now.strftime("%B %d, %Y"), now.hour, now.minute, now.second,
        day_of_week(now.year, now.month, now.day))

def week_number():
    return "Week number: {}".format(datetime.date.today().isocalendar()[1])

def day_of_year():
    today = datetime.date.today()
    return "Day {} of {}".format(today.timetuple().tm_yday, today.year)

def next_full_moon():
    full_moons = ["Jan 7", "Feb 5", "Mar 7", "Apr 5", "May 5", "Jun 3",
                  "Jul 3", "Aug 1", "Aug 31", "Sep 29", "Oct 28", "Nov 27", "Dec 26"]
    now = datetime.datetime.now()
    for moon in full_moons:
        month_name, day = moon.split()
        months = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,
                  "Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
        moon_date = datetime.date(now.year, months[month_name], int(day))
        if moon_date >= now.date():
            return "Next full moon: {}".format(moon)
    return "Next full moon: Jan 7 next year."

def phases_of_moon():
    return random.choice(["New Moon", "Waxing Crescent", "First Quarter", "Waxing Gibbous",
                           "Full Moon", "Waning Gibbous", "Last Quarter", "Waning Crescent"])

def astrology_horoscope(sign):
    messages = [
        "Today is a great day for new beginnings.",
        "Trust your intuition - it will guide you.",
        "A surprise is coming your way.",
        "Focus on what matters most today.",
        "Your energy is magnetic today.",
        "Take time to reflect and recharge.",
        "An opportunity will present itself soon.",
        "Communication is key to solving a problem.",
        "You are stronger than you think.",
        "Change is coming, embrace it.",
        "A friend will need your help today.",
        "Creativity flows through you today.",
        "Patience will be rewarded.",
        "Look for the hidden meaning in events.",
        "Your kindness will come back to you.",
        "A new perspective will change everything.",
        "Trust the process, not the outcome.",
        "Something lost will be found today.",
        "Listen more than you speak.",
        "An old memory will bring you joy.",
    ]
    return "{}: {}".format(sign.capitalize(), random.choice(messages))

def numerology(number):
    while number > 9:
        number = sum(int(d) for d in str(number))
    meanings = {
        1: "Leadership, independence, innovation.",
        2: "Cooperation, balance, harmony.",
        3: "Creativity, expression, joy.",
        4: "Stability, discipline, hard work.",
        5: "Freedom, adventure, change.",
        6: "Love, family, responsibility.",
        7: "Wisdom, analysis, spirituality.",
        8: "Power, success, abundance.",
        9: "Completion, compassion, humanity.",
    }
    return "Life Path {}: {}".format(number, meanings.get(number, "Unknown"))

def chinese_zodiac(year):
    animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake",
               "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
    elements = ["Wood", "Wood", "Fire", "Fire", "Earth", "Earth",
                "Metal", "Metal", "Water", "Water"]
    animal = animals[(year - 4) % 12]
    element = elements[(year - 4) % 10]
    return "Year {}: {} {}".format(year, element, animal)

def tarot_card():
    cards = [
        "The Fool", "The Magician", "The High Priestess", "The Empress",
        "The Emperor", "The Hierophant", "The Lovers", "The Chariot",
        "Strength", "The Hermit", "Wheel of Fortune", "Justice",
        "The Hanged Man", "Death", "Temperance", "The Devil",
        "The Tower", "The Star", "The Moon", "The Sun",
        "Judgement", "The World",
    ]
    return "Your card: {}".format(random.choice(cards))

def crystal_ball():
    visions = [
        "I see a bright future ahead.",
        "The path is unclear, but the destination is worth it.",
        "A stranger will enter your life soon.",
        "Financial opportunity is on the horizon.",
        "Love is closer than you think.",
        "A journey will change your perspective.",
        "The answer lies within you.",
        "Success comes from perseverance.",
        "A lesson will be learned through challenge.",
        "The stars align in your favor.",
    ]
    return "The crystal ball says: {}".format(random.choice(visions))

def coffee_grounds():
    symbols = [
        ("A bird", "Freedom and perspective."),
        ("A tree", "Growth and stability."),
        ("A star", "Success and recognition."),
        ("A heart", "Love and compassion."),
        ("A circle", "Completion and unity."),
        ("A snake", "Transformation and healing."),
        ("A key", "New opportunities."),
        ("A cross", "Protection and balance."),
        ("A crown", "Achievement and honor."),
        ("A moon", "Intuition and mystery."),
        ("An eye", "Awareness and insight."),
        ("A fish", "Abundance and prosperity."),
    ]
    symbol, meaning = random.choice(symbols)
    return "You see {} in the coffee grounds: {}".format(symbol, meaning)

def magic_spell():
    spells = [
        "Abracadabra! A wish has been granted.",
        "Expecto Patronum! Happiness is coming.",
        "Wingardium Leviosa! Your spirits will lift.",
        "Alohomora! New opportunities will unlock.",
        "Lumos! Clarity will shine on a problem.",
        "Accio! What you seek will come to you.",
        "Revelio! A secret will be revealed.",
        "Obliviate! Let go of past worries.",
        "Expelliarmus! Remove negativity from your life.",
        "Avada Kedavra! End a bad habit forever.",
    ]
    return random.choice(spells)

def show_country_info():
    countries = [
        ("Japan", "Tokyo", "Japanese", 126, "Yen"),
        ("France", "Paris", "French", 67, "Euro"),
        ("Brazil", "Brasilia", "Portuguese", 213, "Real"),
        ("Australia", "Canberra", "English", 26, "Dollar"),
        ("Egypt", "Cairo", "Arabic", 104, "Pound"),
        ("Canada", "Ottawa", "English/French", 38, "Dollar"),
        ("India", "New Delhi", "Hindi/English", 1380, "Rupee"),
        ("Germany", "Berlin", "German", 83, "Euro"),
        ("Italy", "Rome", "Italian", 60, "Euro"),
        ("Spain", "Madrid", "Spanish", 47, "Euro"),
        ("South Korea", "Seoul", "Korean", 52, "Won"),
        ("Mexico", "Mexico City", "Spanish", 126, "Peso"),
        ("Argentina", "Buenos Aires", "Spanish", 45, "Peso"),
        ("Nigeria", "Abuja", "English", 206, "Naira"),
        ("Turkey", "Ankara", "Turkish", 84, "Lira"),
        ("Thailand", "Bangkok", "Thai", 70, "Baht"),
        ("Vietnam", "Hanoi", "Vietnamese", 97, "Dong"),
        ("Sweden", "Stockholm", "Swedish", 10, "Krona"),
        ("Norway", "Oslo", "Norwegian", 5, "Krone"),
        ("Netherlands", "Amsterdam", "Dutch", 17, "Euro"),
    ]
    country = random.choice(countries)
    name, capital, lang, pop, currency = country
    return "Country: {}\nCapital: {}\nLanguage: {}\nPopulation: {}M\nCurrency: {}".format(
        name, capital, lang, pop, currency)

def world_clock():
    import time
    cities = [
        ("New York", -5), ("London", 0), ("Paris", 1), ("Moscow", 3),
        ("Tokyo", 9), ("Beijing", 8), ("Sydney", 11), ("Dubai", 4),
        ("Singapore", 8), ("Los Angeles", -8), ("Chicago", -6), ("Berlin", 1),
        ("Rome", 1), ("Madrid", 1), ("Mumbai", 5.5), ("Seoul", 9),
        ("Istanbul", 3), ("Bangkok", 7), ("Cairo", 2), ("Toronto", -5),
    ]
    utc = datetime.datetime.utcnow()
    lines = []
    for city, offset in cities:
        local = utc + datetime.timedelta(hours=offset)
        lines.append("{:15s}: {:02d}:{:02d}".format(city, local.hour, local.minute))
    return "\n".join(lines)

def countdown_to_new_year():
    now = datetime.datetime.now()
    next_year = now.year + 1
    new_year = datetime.datetime(next_year, 1, 1, 0, 0, 0)
    delta = new_year - now
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return "{} days, {} hours, {} minutes, {} seconds until {}.".format(
        days, hours, minutes, seconds, next_year)

def countdown_to_christmas():
    now = datetime.datetime.now()
    christmas = datetime.datetime(now.year, 12, 25, 0, 0, 0)
    if now > christmas:
        christmas = datetime.datetime(now.year + 1, 12, 25, 0, 0, 0)
    delta = christmas - now
    days = delta.days
    hours, remainder = divmod(delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return "{} days, {} hours, {} minutes, {} seconds until Christmas.".format(
        days, hours, minutes, seconds)

def show_random_movie():
    movies = [
        "The Shawshank Redemption (1994)", "The Godfather (1972)", "Pulp Fiction (1994)",
        "The Dark Knight (2008)", "Schindler's List (1993)", "Forrest Gump (1994)",
        "Inception (2010)", "Fight Club (1999)", "The Matrix (1999)", "Goodfellas (1990)",
        "Seven (1995)", "The Silence of the Lambs (1991)", "Interstellar (2014)",
        "Parasite (2019)", "The Lord of the Rings (2001)", "Star Wars (1977)",
        "Back to the Future (1985)", "The Lion King (1994)", "Toy Story (1995)",
        "Avatar (2009)", "Titanic (1997)", "Jurassic Park (1993)", "E.T. (1982)",
        "Gladiator (2000)", "Braveheart (1995)", "The Green Mile (1999)",
        "The Prestige (2006)", "Memento (2000)", "The Departed (2006)",
        "WALL-E (2008)", "Up (2009)", "Finding Nemo (2003)", "Shrek (2001)",
        "The Truman Show (1998)", "Eternal Sunshine (2004)", "Her (2013)",
        "Blade Runner (1982)", "2001: A Space Odyssey (1968)", "Alien (1979)",
        "The Shining (1980)", "Psycho (1960)", "Jaws (1975)", "Die Hard (1988)",
        "Terminator 2 (1991)", "Mad Max: Fury Road (2015)", "Casablanca (1942)",
        "Gone with the Wind (1939)", "Citizen Kane (1941)", "The Wizard of Oz (1939)",
        "Snow White (1937)", "Pinocchio (1940)", "Dumbo (1941)", "Bambi (1942)",
    ]
    return "Movie: {}".format(random.choice(movies))

def show_random_book():
    books = [
        "To Kill a Mockingbird - Harper Lee", "1984 - George Orwell", "Pride and Prejudice - Jane Austen",
        "The Great Gatsby - F. Scott Fitzgerald", "Moby Dick - Herman Melville", "War and Peace - Leo Tolstoy",
        "Crime and Punishment - Fyodor Dostoevsky", "The Catcher in the Rye - J.D. Salinger",
        "The Lord of the Rings - J.R.R. Tolkien", "Harry Potter - J.K. Rowling",
        "The Hobbit - J.R.R. Tolkien", "Fahrenheit 451 - Ray Bradbury", "Dune - Frank Herbert",
        "Brave New World - Aldous Huxley", "The Hitchhiker's Guide to the Galaxy - Douglas Adams",
        "The Alchemist - Paulo Coelho", "The Da Vinci Code - Dan Brown",
        "The Chronicles of Narnia - C.S. Lewis", "The Little Prince - Antoine de Saint-Exupery",
        "Animal Farm - George Orwell", "Jane Eyre - Charlotte Bronte", "Wuthering Heights - Emily Bronte",
        "The Odyssey - Homer", "The Iliad - Homer", "Don Quixote - Miguel de Cervantes",
        "One Hundred Years of Solitude - Gabriel Garcia Marquez", "The Sun Also Rises - Ernest Hemingway",
        "For Whom the Bell Tolls - Ernest Hemingway", "Slaughterhouse-Five - Kurt Vonnegut",
        "Catch-22 - Joseph Heller", "The Grapes of Wrath - John Steinbeck",
        "Of Mice and Men - John Steinbeck", "The Scarlet Letter - Nathaniel Hawthorne",
        "Dracula - Bram Stoker", "Frankenstein - Mary Shelley", "The Picture of Dorian Gray - Oscar Wilde",
        "Alice in Wonderland - Lewis Carroll", "The Wonderful Wizard of Oz - L. Frank Baum",
        "Treasure Island - Robert Louis Stevenson", "Robinson Crusoe - Daniel Defoe",
        "Gulliver's Travels - Jonathan Swift", "The Three Musketeers - Alexandre Dumas",
        "Les Miserables - Victor Hugo", "The Hunchback of Notre Dame - Victor Hugo",
    ]
    return "Book: {}".format(random.choice(books))

def show_random_song():
    songs = [
        "Bohemian Rhapsody - Queen", "Stairway to Heaven - Led Zeppelin", "Imagine - John Lennon",
        "Hotel California - Eagles", "Smells Like Teen Spirit - Nirvana", "Billie Jean - Michael Jackson",
        "Like a Rolling Stone - Bob Dylan", "Respect - Aretha Franklin", "What's Going On - Marvin Gaye",
        "Yesterday - The Beatles", "Hey Jude - The Beatles", "Let It Be - The Beatles",
        "Purple Haze - Jimi Hendrix", "London Calling - The Clash", "Born to Run - Bruce Springsteen",
        "Thriller - Michael Jackson", "Beat It - Michael Jackson", "Sweet Child o' Mine - Guns N' Roses",
        "Welcome to the Jungle - Guns N' Roses", "November Rain - Guns N' Roses",
        "Back in Black - AC/DC", "Highway to Hell - AC/DC", "Thunderstruck - AC/DC",
        "Enter Sandman - Metallica", "Nothing Else Matters - Metallica", "One - Metallica",
        "Comfortably Numb - Pink Floyd", "Wish You Were Here - Pink Floyd", "Money - Pink Floyd",
        "Paranoid - Black Sabbath", "Iron Man - Black Sabbath", "Crazy Train - Ozzy Osbourne",
    ]
    return "Song: {}".format(random.choice(songs))

def show_random_recipe():
    recipes = [
        "Spaghetti Carbonara: pasta, eggs, bacon, parmesan, pepper",
        "Chicken Curry: chicken, curry powder, onion, garlic, coconut milk",
        "Caesar Salad: romaine, croutons, parmesan, caesar dressing",
        "Pancakes: flour, milk, eggs, sugar, baking powder, butter",
        "Omelette: eggs, cheese, mushrooms, onion, bell pepper",
        "Tomato Soup: tomatoes, onion, garlic, cream, basil",
        "Grilled Cheese: bread, cheese, butter",
        "French Toast: bread, eggs, milk, cinnamon, maple syrup",
        "Beef Stir Fry: beef, broccoli, soy sauce, ginger, garlic",
        "Chicken Noodle Soup: chicken, noodles, carrot, celery, onion",
        "Banana Bread: bananas, flour, sugar, eggs, butter, baking soda",
        "Chocolate Cake: flour, sugar, cocoa, eggs, butter, milk",
        "Guacamole: avocado, lime, onion, tomato, cilantro, salt",
        "Hummus: chickpeas, tahini, lemon, garlic, olive oil",
        "Sushi Rice: rice, vinegar, sugar, salt, seaweed",
        "Tacos: tortillas, beef, lettuce, cheese, salsa, sour cream",
        "Pizza Dough: flour, yeast, water, olive oil, salt",
        "Brownies: chocolate, butter, sugar, eggs, flour",
        "Mashed Potatoes: potatoes, butter, milk, garlic, salt",
        "Apple Pie: apples, sugar, cinnamon, flour, butter",
    ]
    return "Recipe: {}".format(random.choice(recipes))

def show_random_hobby():
    hobbies = [
        "Photography", "Painting", "Drawing", "Writing", "Reading", "Gardening",
        "Cooking", "Baking", "Hiking", "Camping", "Fishing", "Bird watching",
        "Knitting", "Sewing", "Woodworking", "Pottery", "Calligraphy", "Origami",
        "Cycling", "Running", "Swimming", "Yoga", "Dancing", "Singing",
        "Playing guitar", "Playing piano", "Drumming", "Violin", "Flute",
        "Chess", "Board games", "Video games", "Puzzles", "Sudoku", "Crosswords",
        "Collecting stamps", "Collecting coins", "Collecting cards",
        "Model building", "Lego", "Robotics", "Coding", "3D printing",
        "Astronomy", "Stargazing", "Meteorology", "Geology", "Archaeology",
        "Volunteering", "Mentoring", "Teaching", "Learning languages",
    ]
    return random.choice(hobbies)

def workout_routine():
    exercises = [
        "Push ups - 3 sets of 10", "Squats - 3 sets of 15", "Plank - 30 seconds",
        "Jumping jacks - 3 sets of 20", "Lunges - 3 sets of 10 each leg",
        "Burpees - 3 sets of 8", "Mountain climbers - 3 sets of 30 seconds",
        "Crunches - 3 sets of 15", "Leg raises - 3 sets of 12",
        "Bicycle crunches - 3 sets of 15", "Tricep dips - 3 sets of 10",
        "Wall sit - 30 seconds", "Glute bridge - 3 sets of 15",
        "Superman hold - 30 seconds", "High knees - 3 sets of 30 seconds",
    ]
    return "Workout: {}".format(random.choice(exercises))

def meditation_guide():
    steps = [
        "Find a quiet place and sit comfortably.",
        "Close your eyes and take a deep breath.",
        "Focus on your breath going in and out.",
        "Notice your thoughts without judging them.",
        "Gently bring your attention back to your breath.",
        "Scan your body from head to toe.",
        "Release any tension you find.",
        "Imagine a warm light surrounding you.",
        "Stay present in this moment.",
        "When ready, slowly open your eyes.",
    ]
    return "\n".join("{}. {}".format(i+1, s) for i, s in enumerate(steps))

def bmi_calculator():
    try:
        h = float(input("Height in meters: "))
        w = float(input("Weight in kg: "))
        bmi = w / (h * h)
        print("Your BMI is {:.2f}".format(bmi))
        print("Category: {}".format(bmi_category(bmi)))
    except:
        print("Invalid input.")

def tip_calculator():
    try:
        bill = float(input("Bill amount: $"))
        tip_pct = int(input("Tip percentage (10, 15, 20): ") or 15)
        people = int(input("Split between how many? ") or 1)
        tip = bill * tip_pct / 100
        total = bill + tip
        each = total / people
        print("Tip: ${:.2f}".format(tip))
        print("Total: ${:.2f}".format(total))
        print("Each pays: ${:.2f}".format(each))
    except:
        print("Invalid input.")

def loan_calculator():
    try:
        principal = float(input("Loan amount: $"))
        rate = float(input("Annual interest rate (%): ")) / 100 / 12
        months = int(input("Number of months: "))
        if rate == 0:
            monthly = principal / months
        else:
            monthly = principal * rate * (1 + rate) ** months / ((1 + rate) ** months - 1)
        total = monthly * months
        print("Monthly payment: ${:.2f}".format(monthly))
        print("Total payment: ${:.2f}".format(total))
        print("Total interest: ${:.2f}".format(total - principal))
    except:
        print("Invalid input.")

def savings_calculator():
    try:
        monthly = float(input("Monthly deposit: $"))
        rate = float(input("Annual interest rate (%): ")) / 100 / 12
        years = int(input("Years: "))
        months = years * 12
        total = 0
        for i in range(months):
            total = (total + monthly) * (1 + rate)
        print("After {} years: ${:.2f}".format(years, total))
        print("You contributed: ${:.2f}".format(monthly * months))
        print("Interest earned: ${:.2f}".format(total - monthly * months))
    except:
        print("Invalid input.")

def unit_converter():
    print("Convert: 1-length, 2-weight, 3-volume, 4-temperature, 5-speed")
    try:
        t = input("Choice: ")
        v = float(input("Value: "))
        if t == "1":
            print("1-m to ft, 2-ft to m, 3-km to mi, 4-mi to km")
            c = input(": ")
            if c == "1": print("{:.4f} ft".format(v * 3.28084))
            elif c == "2": print("{:.4f} m".format(v / 3.28084))
            elif c == "3": print("{:.4f} mi".format(v * 0.621371))
            elif c == "4": print("{:.4f} km".format(v / 0.621371))
        elif t == "2":
            print("1-kg to lb, 2-lb to kg, 3-oz to g, 4-g to oz")
            c = input(": ")
            if c == "1": print("{:.4f} lb".format(v * 2.20462))
            elif c == "2": print("{:.4f} kg".format(v / 2.20462))
            elif c == "3": print("{:.4f} g".format(v * 28.3495))
            elif c == "4": print("{:.4f} oz".format(v / 28.3495))
        elif t == "3":
            print("1-L to gal, 2-gal to L, 3-cup to mL, 4-mL to cup")
            c = input(": ")
            if c == "1": print("{:.4f} gal".format(v * 0.264172))
            elif c == "2": print("{:.4f} L".format(v / 0.264172))
            elif c == "3": print("{:.4f} mL".format(v * 236.588))
            elif c == "4": print("{:.4f} cup".format(v / 236.588))
        elif t == "4":
            print("1-C to F, 2-F to C, 3-C to K, 4-K to C")
            c = input(": ")
            if c == "1": print("{:.4f} F".format(v * 9/5 + 32))
            elif c == "2": print("{:.4f} C".format((v - 32) * 5/9))
            elif c == "3": print("{:.4f} K".format(v + 273.15))
            elif c == "4": print("{:.4f} C".format(v - 273.15))
        elif t == "5":
            print("1-kmh to mph, 2-mph to kmh, 3-ms to kmh, 4-kmh to ms")
            c = input(": ")
            if c == "1": print("{:.4f} mph".format(v * 0.621371))
            elif c == "2": print("{:.4f} kmh".format(v / 0.621371))
            elif c == "3": print("{:.4f} kmh".format(v * 3.6))
            elif c == "4": print("{:.4f} ms".format(v / 3.6))
    except:
        print("Invalid input.")

def discount_calculator():
    try:
        price = float(input("Original price: $"))
        discount = float(input("Discount percentage: "))
        saved = price * discount / 100
        final = price - saved
        print("You save: ${:.2f}".format(saved))
        print("Final price: ${:.2f}".format(final))
    except:
        print("Invalid input.")

def currency_converter():
    rates = {"usd": 1.0, "eur": 0.92, "gbp": 0.79, "jpy": 149.5, "cad": 1.36, "aud": 1.53, "chf": 0.88, "cny": 7.24, "inr": 83.0, "mxn": 17.1}
    try:
        amount = float(input("Amount: "))
        from_c = input("From (USD, EUR, GBP, JPY, CAD, AUD, CHF, CNY, INR, MXN): ").lower()
        to_c = input("To (same list): ").lower()
        if from_c in rates and to_c in rates:
            in_usd = amount / rates[from_c]
            result = in_usd * rates[to_c]
            print("{:.2f} {} = {:.2f} {}".format(amount, from_c.upper(), result, to_c.upper()))
        else:
            print("Unsupported currency.")
    except:
        print("Invalid input.")

def generate_planet_info():
    planets = [
        ("Mercury", 0.33, 4879, 57.9, "Gray", "None"),
        ("Venus", 4.87, 12104, 108.2, "Yellowish", "None"),
        ("Earth", 5.97, 12756, 149.6, "Blue/Green", "1 (Moon)"),
        ("Mars", 0.642, 6792, 227.9, "Red", "2 (Phobos, Deimos)"),
        ("Jupiter", 1898, 142984, 778.6, "Orange/White", "95"),
        ("Saturn", 568, 120536, 1433.5, "Yellow/Gold", "146"),
        ("Uranus", 86.8, 51118, 2872.5, "Cyan", "27"),
        ("Neptune", 102, 49528, 4495.1, "Blue", "16"),
    ]
    p = random.choice(planets)
    return "Planet: {} | Mass: {}e24 kg | Diameter: {} km | Dist from Sun: {}e6 km | Color: {} | Moons: {}".format(*p)

def show_astronomy_fact():
    facts = [
        "The Sun is 109 times wider than Earth.",
        "Light from the Sun takes 8 minutes to reach Earth.",
        "There are more stars than grains of sand on Earth.",
        "A year on Jupiter is 11.86 Earth years.",
        "Saturn's rings are made of ice and rock.",
        "Uranus rotates on its side.",
        "Neptune has the strongest winds in the solar system.",
        "Pluto was reclassified as a dwarf planet in 2006.",
        "The Moon is moving 3.8 cm away from Earth each year.",
        "The largest volcano is Olympus Mons on Mars.",
        "The Great Red Spot on Jupiter is a storm larger than Earth.",
        "Venus is the hottest planet at 475C.",
        "Mercury has no atmosphere.",
        "One day on Venus is longer than its year.",
        "Saturn would float in water because it's less dense.",
        "The Milky Way contains 100-400 billion stars.",
        "The nearest star is Proxima Centauri at 4.24 light years.",
        "Black holes can be the size of an atom.",
        "Neutron stars can spin 600 times per second.",
        "The universe is expanding faster than light.",
        "The Big Bang happened 13.8 billion years ago.",
        "Dark matter makes up 27% of the universe.",
        "Dark energy makes up 68% of the universe.",
        "The largest known star is UY Scuti.",
        "The coldest place in space is -272C.",
        "There is a giant cloud of alcohol in space.",
        "The sound of the Big Bang would be like a hum.",
        "The first star in the universe formed 400M years after Big Bang.",
        "Quasars are the brightest objects in the universe.",
        "A light year is about 9.5 trillion km.",
    ]
    return random.choice(facts)

def show_weather_fact():
    facts = [
        "Lightning strikes Earth about 100 times per second.",
        "The hottest temperature recorded was 56.7C in Death Valley.",
        "The coldest temperature was -89.2C in Antarctica.",
        "Rain contains vitamin B12.",
        "Hurricanes spin counterclockwise in the Northern Hemisphere.",
        "The wind can make icebergs 'sing'.",
        "Clouds can weigh over 500 tons.",
        "There are about 2,000 thunderstorms happening right now.",
        "The driest place on Earth is the Atacama Desert.",
        "The wettest place is Mawsynram, India.",
        "Snowflakes can be up to 2 inches wide.",
        "The fastest wind speed was 408 km/h.",
        "Rainbows appear as full circles from airplanes.",
        "Fog is just a cloud touching the ground.",
        "The UK has the most weather changes in the world.",
        "Butterflies can cause tornadoes? No, but chaos theory says maybe.",
        "Yellow snow means there is pollen in it.",
        "There is no sound in space because no air carries sound.",
        "Light travels faster than sound, so we see lightning before thunder.",
        "Heat lightning is just lightning far away.",
    ]
    return random.choice(facts)

def show_ocean_fact():
    facts = [
        "The ocean covers 71% of Earth's surface.",
        "Only 5% of the ocean has been explored.",
        "The Mariana Trench is 11km deep.",
        "The ocean has more artifacts than all museums combined.",
        "The Great Barrier Reef is visible from space.",
        "The largest ocean is the Pacific at 155M sq km.",
        "The smallest ocean is the Arctic at 14M sq km.",
        "Seawater is 3.5% salt on average.",
        "The ocean contains 97% of Earth's water.",
        "The longest mountain range is underwater (Mid-Atlantic Ridge).",
        "The ocean produces 50% of Earth's oxygen.",
        "Coral reefs are home to 25% of marine species.",
        "The ocean absorbs 30% of CO2 emissions.",
        "Tsunamis can travel at 800 km/h.",
        "The Sargasso Sea has no coastline.",
        "The Dead Sea is 10 times saltier than the ocean.",
        "The Red Sea is named for algae that can turn the water red.",
        "The Caribbean Sea is the deepest sea in the world.",
        "The Southern Ocean was officially recognized in 2000.",
        "Underwater volcanoes create new islands.",
    ]
    return random.choice(facts)

def space_mission_fact():
    missions = [
        "Apollo 11 landed the first humans on the Moon in 1969.",
        "Voyager 1 is the farthest human-made object from Earth.",
        "The ISS has been continuously occupied since 2000.",
        "Mars rovers have been exploring Mars since 1997.",
        "The Hubble Space Telescope launched in 1990.",
        "The James Webb Space Telescope launched in 2021.",
        "Sputnik 1 was the first satellite in 1957.",
        "Laika the dog was the first animal in orbit in 1957.",
        "Yuri Gagarin was the first human in space in 1961.",
        "Valentina Tereshkova was the first woman in space in 1963.",
        "Neil Armstrong took the first steps on the Moon in 1969.",
        "The Space Shuttle program ran from 1981 to 2011.",
        "The first space station was Salyut 1 in 1971.",
        "Mir space station operated from 1986 to 2001.",
        "SpaceX achieved the first reusable rocket landing in 2015.",
        "The Artemis program aims to return humans to the Moon.",
        "China's Tiangong space station was completed in 2022.",
        "The first all-civilian spaceflight was Inspiration4 in 2021.",
        "Space tourism started with Dennis Tito in 2001.",
        "The International Space Station weighs 420,000 kg.",
    ]
    return random.choice(missions)

def quiz_capital_cities():
    qs = [
        ("France", "Paris"), ("Japan", "Tokyo"), ("Brazil", "Brasilia"), ("Australia", "Canberra"),
        ("Egypt", "Cairo"), ("Canada", "Ottawa"), ("India", "New Delhi"), ("Germany", "Berlin"),
        ("Italy", "Rome"), ("Spain", "Madrid"), ("South Korea", "Seoul"), ("Mexico", "Mexico City"),
        ("Argentina", "Buenos Aires"), ("Nigeria", "Abuja"), ("Turkey", "Ankara"),
        ("Thailand", "Bangkok"), ("Vietnam", "Hanoi"), ("Sweden", "Stockholm"),
        ("Norway", "Oslo"), ("Netherlands", "Amsterdam"), ("Portugal", "Lisbon"),
        ("Poland", "Warsaw"), ("Greece", "Athens"), ("Ireland", "Dublin"),
        ("Denmark", "Copenhagen"), ("Finland", "Helsinki"), ("Austria", "Vienna"),
        ("Switzerland", "Bern"), ("Belgium", "Brussels"), ("Hungary", "Budapest"),
        ("Romania", "Bucharest"), ("Czech Republic", "Prague"), ("Chile", "Santiago"),
        ("Colombia", "Bogota"), ("Peru", "Lima"), ("Kenya", "Nairobi"),
        ("South Africa", "Pretoria"), ("Morocco", "Rabat"), ("Saudi Arabia", "Riyadh"),
        ("United Arab Emirates", "Abu Dhabi"), ("Qatar", "Doha"), ("Kuwait", "Kuwait City"),
        ("Oman", "Muscat"), ("Malaysia", "Kuala Lumpur"), ("Philippines", "Manila"),
        ("Indonesia", "Jakarta"), ("New Zealand", "Wellington"), ("Cuba", "Havana"),
        ("Jamaica", "Kingston"), ("Iceland", "Reykjavik"),
    ]
    score = 0
    random.shuffle(qs)
    for c, a in qs[:10]:
        ans = input("Capital of {}? ".format(c)).strip().lower()
        if ans == a.lower():
            print("Correct!"); score += 1
        else:
            print("Wrong! Answer: {}".format(a))
    print("Score: {}/10".format(score))

def quiz_flags():
    countries_desc = [
        ("Three vertical stripes: green, white, orange", "Ireland"),
        ("Red circle on white background", "Japan"),
        ("Stars and stripes", "USA"),
        ("Red and white with a maple leaf", "Canada"),
        ("Green, yellow, blue with a globe", "Brazil"),
        ("Union Jack on blue with stars", "Australia"),
        ("Tricolore: blue, white, red", "France"),
        ("Red, white, red with an eagle", "Austria"),
        ("White crescent and star on green", "Pakistan"),
        ("Red flag with a yellow star", "Vietnam"),
        ("Blue, yellow, red vertical stripes", "Romania"),
        ("White cross on red background", "Switzerland"),
        ("Green, white, orange tricolor", "India"),
        ("Red, black, green with white stripes", "Kenya"),
        ("Blue and white striped with sun", "Greece"),
        ("Red, white, blue horizontal stripes", "Netherlands"),
        ("Green, white, red vertical stripes", "Italy"),
        ("Red, yellow, red horizontal with an eagle", "Spain"),
        ("Red flag with five yellow stars", "China"),
        ("Blue and yellow horizontal stripes", "Ukraine"),
    ]
    desc, answer = random.choice(countries_desc)
    print("Describe: {}".format(desc))
    g = input("Which country? ").strip().lower()
    if g == answer.lower():
        print("Correct!")
    else:
        print("Wrong! It's {}".format(answer))

def quiz_math():
    ops = [("+", lambda a, b: a + b), ("-", lambda a, b: a - b), ("*", lambda a, b: a * b)]
    op, func = random.choice(ops)
    a, b = random.randint(1, 20), random.randint(1, 20)
    answer = func(a, b)
    print("{} {} {} = ?".format(a, op, b))
    try:
        g = float(input("Answer: "))
        if g == answer:
            print("Correct!")
        else:
            print("Wrong! Answer: {}".format(answer))
    except:
        print("Invalid. Answer: {}".format(answer))

def quiz_science():
    qs = [
        ("What is H2O?", "Water"), ("What planet is known as Red Planet?", "Mars"),
        ("What is the chemical symbol for gold?", "Au"), ("What gas do plants absorb?", "Carbon dioxide"),
        ("What is the hardest natural substance?", "Diamond"), ("What is the speed of light in km/s?", "299792"),
        ("What element is needed for combustion?", "Oxygen"), ("What is the largest organ?", "Skin"),
        ("How many bones in adult human?", "206"), ("What blood type is universal donor?", "O"),
        ("What planet is closest to the sun?", "Mercury"), ("What is the powerhouse of the cell?", "Mitochondria"),
        ("What gas makes up 78% of air?", "Nitrogen"), ("What is the study of fungi called?", "Mycology"),
        ("What is the SI unit of force?", "Newton"), ("What planet has the most moons?", "Saturn"),
        ("What element has atomic number 1?", "Hydrogen"), ("What is the largest mammal?", "Blue whale"),
        ("What is the smallest bone in the body?", "Stapes"), ("What vitamin does sun give?", "Vitamin D"),
    ]
    q, a = random.choice(qs)
    ans = input("Q: {} ".format(q)).strip().lower()
    if ans == a.lower():
        print("Correct!")
    else:
        print("Wrong! Answer: {}".format(a))

def quiz_history():
    qs = [
        ("What year did WW2 end?", "1945"), ("Who discovered America in 1492?", "Christopher Columbus"),
        ("What empire built the Colosseum?", "Roman"), ("Who wrote the Declaration of Independence?", "Thomas Jefferson"),
        ("What year did the Titanic sink?", "1912"), ("Who was the first US President?", "George Washington"),
        ("What year did the Berlin Wall fall?", "1989"), ("Who was the first Emperor of China?", "Qin Shi Huang"),
        ("What year did the Moon landing happen?", "1969"), ("Who invented the printing press?", "Johannes Gutenberg"),
        ("What country built the Great Wall?", "China"), ("What year did the French Revolution start?", "1789"),
        ("Who was the last Pharaoh of Egypt?", "Cleopatra"), ("What year was the UN founded?", "1945"),
        ("Who discovered penicillin?", "Alexander Fleming"), ("What year did the Cold War end?", "1991"),
        ("Who painted the Mona Lisa?", "Leonardo da Vinci"), ("What country gifted the Statue of Liberty?", "France"),
        ("What year did the Soviet Union collapse?", "1991"), ("Who was the first woman in space?", "Valentina Tereshkova"),
    ]
    q, a = random.choice(qs)
    ans = input("Q: {} ".format(q)).strip().lower()
    if ans == a.lower():
        print("Correct!")
    else:
        print("Wrong! Answer: {}".format(a))

def quiz_geography():
    qs = [
        ("What is the largest continent?", "Asia"), ("What is the smallest country?", "Vatican City"),
        ("What is the longest river?", "Nile"), ("What is the highest mountain?", "Everest"),
        ("What is the largest ocean?", "Pacific"), ("What is the largest desert?", "Antarctica"),
        ("What is the deepest lake?", "Baikal"), ("What is the largest island?", "Greenland"),
        ("What country has the most people?", "India"), ("What is the largest lake?", "Caspian Sea"),
        ("What is the largest country by area?", "Russia"), ("What is the smallest continent?", "Australia"),
        ("What country has the most time zones?", "France"), ("What is the longest mountain range?", "Andes"),
        ("What country has the most neighbors?", "China"), ("What is the largest bay?", "Bay of Bengal"),
        ("What is the largest gulf?", "Gulf of Mexico"), ("What country has the most lakes?", "Canada"),
        ("What is the largest delta?", "Ganges Delta"), ("What country has the most volcanoes?", "Indonesia"),
    ]
    q, a = random.choice(qs)
    ans = input("Q: {} ".format(q)).strip().lower()
    if ans == a.lower():
        print("Correct!")
    else:
        print("Wrong! Answer: {}".format(a))

def quiz_programming():
    qs = [
        ("What language runs in browsers?", "JavaScript"), ("What does HTML stand for?", "HyperText Markup Language"),
        ("What does CSS stand for?", "Cascading Style Sheets"), ("What is the 'this' keyword in JS?", "Context object"),
        ("What does API stand for?", "Application Programming Interface"), ("What does JSON stand for?", "JavaScript Object Notation"),
        ("What does SQL stand for?", "Structured Query Language"), ("What is 0101 in decimal?", "5"),
        ("What does DOM stand for?", "Document Object Model"), ("What company created Java?", "Sun Microsystems"),
        ("What language is Django based on?", "Python"), ("What does npm stand for?", "Node Package Manager"),
        ("What is 0xFF in decimal?", "255"), ("What does CRUD stand for?", "Create Read Update Delete"),
        ("What language was used for the first web page?", "HTML"), ("What is the most popular database?", "MySQL"),
        ("What language is used for iOS apps?", "Swift"), ("What company makes TypeScript?", "Microsoft"),
        ("What does OOP stand for?", "Object-Oriented Programming"), ("What is the brain of a computer?", "CPU"),
    ]
    q, a = random.choice(qs)
    ans = input("Q: {} ".format(q)).strip().lower()
    if ans == a.lower():
        print("Correct!")
    else:
        print("Wrong! Answer: {}".format(a))

def random_emoji():
    emojis = ["😀","😂","🤣","😊","😍","🤔","😎","🙌","💪","👍","👏","🎉","🎊","✨","🌟","🔥","💯","❤️","💙","💚","💛","💜","🖤","🤍","🐱","🐶","🐼","🐨","🦊","🐸","🐵","🦄","🐴","🐌","🐢","🐍","🦎","🦖","🦕","🐙","🦑","🦐","🦞","🦀","🐡","🐠","🐟","🐬","🐳","🐋","🦈","🐊","🐅","🐆","🦓","🦍","🦧","🐘","🦛","🦏","🐪","🐫","🦒","🦘","🐃","🐂","🐄","🐎","🐖","🐏","🐑","🦙","🐐","🦌","🐕","🐩","🐈","🐓","🦃","🦚","🦜","🦢","🦩","🐦","🐧","🕊️","🐇","🦝","🦡","🐁","🐀","🐹","🐿️","🦔","🐾","🐉","🐲","🌵","🎄","🌲","🌳","🌴","🌱","🌿","☘️","🍀","🎍","🎋","🍃","🍂","🍁","🍄","🌾","💐","🌷","🌹","🥀","🌺","🌸","🌼","🌻","🌞","🌝","🌛","🌜","🌚","🌕","🌖","🌗","🌘","🌑","🌒","🌓","🌔","🌙","🌎","🌍","🌏","🪐","💫","⭐","🌟","✨","⚡","☄️","💥","🔥","🌪️","🌈","☀️","🌤️","⛅","🌥️","☁️","🌦️","🌧️","⛈️","🌩️","🌨️","❄️","☃️","⛄","🌬️","💨","💧","💦","☔","☂️","🌊","🌫️","🍏","🍎","🍐","🍊","🍋","🍌","🍉","🍇","🍓","🫐","🍈","🍒","🍑","🥭","🍍","🥥","🥝","🍅","🍆","🥑","🥦","🥬","🥒","🌽","🥕","🧄","🧅","🥔","🍠","🥐","🍞","🥖","🥨","🧀","🥚","🍳","🥞","🧇","🥓","🥩","🍗","🍖","🦴","🌭","🍔","🍟","🍕","🫓","🥪","🥙","🧆","🌮","🌯","🥗","🥘","🫕","🥫","🍝","🍜","🍲","🍛","🍣","🍱","🥟","🦪","🍤","🍙","🍚","🍘","🍥","🥠","🥮","🍢","🍡","🍧","🍨","🍦","🥧","🧁","🍰","🎂","🍮","🍭","🍬","🍫","🍿","🍩","🍪","🌰","🥜","🍯","🥛","🍼","☕","🫖","🍵","🥤","🧃","🧋","🍶","🍺","🍻","🥂","🍷","🫗","🥃","🍸","🍹","🧉","🍾","🧊","🥄","🍴","🍽️","🥣","🥡","🥢","🧂","🎵","🎶","🎼","🎤","🎧","🎹","🥁","🎷","🎺","🎸","🪕","🎻","🎲","♟️","🎯","🎳","🎮","🕹️","🎰","🧩"]
    return random.choice(emojis)

def random_constellation():
    constellations = [
        "Orion", "Ursa Major", "Ursa Minor", "Cassiopeia", "Scorpius", "Leo", "Virgo", "Libra",
        "Gemini", "Taurus", "Aries", "Pisces", "Aquarius", "Capricornus", "Sagittarius", "Ophiuchus",
        "Cepheus", "Draco", "Cygnus", "Lyra", "Aquila", "Pegasus", "Andromeda", "Perseus",
        "Hercules", "Corona Borealis", "Bootes", "Canis Major", "Canis Minor", "Centaurus",
        "Carina", "Vela", "Puppis", "Hydra", "Crater", "Corvus", "Lupus", "Crux",
        "Phoenix", "Tucana", "Pavo", "Grus", "Indus", "Octans", "Ara", "Triangulum Australe",
        "Lacerta", "Vulpecula", "Delphinus", "Equuleus", "Scutum", "Sagitta", "Monoceros",
        "Lepus", "Columba", "Caelum", "Fornax", "Sculptor", "Horologium", "Reticulum",
        "Dorado", "Volans", "Mensa", "Pictor", "Antlia", "Pyxis", "Sextans", "Leo Minor",
    ]
    return random.choice(constellations)

def random_dinosaur():
    dinos = [
        "Tyrannosaurus Rex", "Triceratops", "Stegosaurus", "Velociraptor", "Brachiosaurus",
        "Diplodocus", "Ankylosaurus", "Pteranodon", "Plesiosaurus", "Iguanodon",
        "Parasaurolophus", "Spinosaurus", "Allosaurus", "Apatosaurus", "Archaeopteryx",
        "Deinonychus", "Gallimimus", "Pachycephalosaurus", "Carnotaurus", "Compsognathus",
        "Dilophosaurus", "Mosasaurus", "Oviraptor", "Protoceratops", "Styracosaurus",
        "Therizinosaurus", "Utahraptor", "Velociraptor", "Corythosaurus", "Lambeosaurus",
        "Maiasaura", "Edmontosaurus", "Hadrosaurus", "Anatosaurus", "Corythosaurus",
        "Hypsilophodon", "Dryosaurus", "Camptosaurus", "Ouranosaurus", "Muttaburrasaurus",
        "Amargasaurus", "Dicraeosaurus", "Brachytrachelopan", "Sauroposeidon", "Argentinosaurus",
        "Giganotosaurus", "Mapusaurus", "Carcharodontosaurus", "Acrocanthosaurus", "Baryonyx",
        "Suchomimus", "Irritator", "Cryolophosaurus", "Dilong", "Guanlong", "Yutyrannus",
        "Alioramus", "Tarbosaurus", "Daspletosaurus", "Albertosaurus", "Gorgosaurus",
    ]
    return random.choice(dinos)

def random_flower():
    flowers = [
        "Rose", "Tulip", "Sunflower", "Daisy", "Orchid", "Lily", "Lavender", "Jasmine",
        "Cherry Blossom", "Hibiscus", "Magnolia", "Peony", "Chrysanthemum", "Carnation",
        "Daffodil", "Iris", "Lotus", "Marigold", "Poppy", "Bluebell", "Crocus", "Snowdrop",
        "Hyacinth", "Wisteria", "Hydrangea", "Azalea", "Rhododendron", "Begonia", "Fuchsia",
        "Gardenia", "Camellia", "Dahlia", "Aster", "Zinnia", "Petunia", "Snapdragon",
        "Morning Glory", "Buttercup", "Foxglove", "Honeysuckle", "Clematis", "Ivy",
        "Geranium", "Impatiens", "Lantana", "Verbena", "Violet", "Pansy", "Primrose",
        "Cowslip", "Lobelia", "Alyssum", "Dusty Miller", "Heliotrope", "Nicotiana",
    ]
    return random.choice(flowers)

def random_gemstone():
    gems = [
        "Diamond", "Ruby", "Sapphire", "Emerald", "Amethyst", "Topaz", "Opal", "Pearl",
        "Garnet", "Peridot", "Turquoise", "Lapis Lazuli", "Moonstone", "Jade", "Onyx",
        "Citrine", "Aquamarine", "Morganite", "Tanzanite", "Alexandrite", "Tourmaline",
        "Spinel", "Zircon", "Oligoclase", "Labradorite", "Sunstone", "Bloodstone",
        "Carnelian", "Chrysoprase", "Heliotrope", "Jasper", "Malachite", "Azurite",
        "Rhodonite", "Sodalite", "Amber", "Coral", "Ivory", "Jet", "Obsidian",
        "Tektite", "Moldavite", "Serpentine", "Unakite", "Variscite", "Smithsonite",
    ]
    return random.choice(gems)

def random_mythical_creature():
    creatures = [
        "Dragon", "Phoenix", "Unicorn", "Griffin", "Centaur", "Minotaur", "Pegasus",
        "Sphinx", "Chimera", "Hydra", "Kraken", "Medusa", "Cyclops", "Cerberus",
        "Harpy", "Basilisk", "Manticore", "Siren", "Werewolf", "Vampire", "Zombie",
        "Golem", "Djinn", "Leprechaun", "Fairy", "Elf", "Dwarf", "Orc", "Troll",
        "Giant", "Yeti", "Loch Ness Monster", "Bigfoot", "Chupacabra", "Mothman",
        "Banshee", "Poltergeist", "Succubus", "Incubus", "Kitsune", "Tanuki",
        "Kappa", "Tengu", "Oni", "Yokai", "Naga", "Garuda", "Nandi", "Yali",
    ]
    return random.choice(creatures)

def random_planet_type():
    types = [
        "Terrestrial", "Gas Giant", "Ice Giant", "Dwarf Planet", "Super-Earth",
        "Hot Jupiter", "Ocean Planet", "Carbon Planet", "Iron Planet", "Lava Planet",
        "Desert Planet", "Ice Planet", "Rogue Planet", "Pulsar Planet", "Circumbinary Planet",
        "Mini-Neptune", "Sub-Earth", "Goldilocks Planet", "Eyeball Planet", "Hycean Planet",
    ]
    return random.choice(types)

def random_chemical_reaction():
    reactions = [
        "2H2 + O2 -> 2H2O", "C + O2 -> CO2", "Fe + S -> FeS",
        "N2 + 3H2 -> 2NH3", "2Na + Cl2 -> 2NaCl", "CaCO3 -> CaO + CO2",
        "2Mg + O2 -> 2MgO", "2K + 2H2O -> 2KOH + H2", "Zn + 2HCl -> ZnCl2 + H2",
        "2Al + 3CuO -> Al2O3 + 3Cu", "3Fe + 2O2 -> Fe3O4", "CH4 + 2O2 -> CO2 + 2H2O",
        "2CO + O2 -> 2CO2", "2NO + O2 -> 2NO2", "2SO2 + O2 -> 2SO3",
        "2H2O2 -> 2H2O + O2", "2KClO3 -> 2KCl + 3O2", "NH4Cl -> NH3 + HCl",
        "CuSO4 + Fe -> FeSO4 + Cu", "AgNO3 + NaCl -> AgCl + NaNO3",
        "NaOH + HCl -> NaCl + H2O", "2HNO3 + CuO -> Cu(NO3)2 + H2O",
        "C6H12O6 -> 2C2H5OH + 2CO2", "2C8H18 + 25O2 -> 16CO2 + 18H2O",
    ]
    return random.choice(reactions)

def random_mathematician():
    people = [
        ("Euclid", "Geometry"), ("Pythagoras", "Theorem"), ("Archimedes", "Pi approximation"),
        ("Leonardo Fibonacci", "Fibonacci sequence"), ("Rene Descartes", "Coordinate geometry"),
        ("Isaac Newton", "Calculus"), ("Gottfried Leibniz", "Calculus"), ("Carl Gauss", "Number theory"),
        ("Leonhard Euler", "Graph theory"), ("Bernhard Riemann", "Riemann hypothesis"),
        ("Alan Turing", "Computability"), ("John von Neumann", "Computer architecture"),
        ("Ada Lovelace", "First programmer"), ("Katherine Johnson", "NASA trajectories"),
        ("Emmy Noether", "Abstract algebra"), ("Sophie Germain", "Number theory"),
        ("Srinivasa Ramanujan", "Infinite series"), ("Henri Poincare", "Topology"),
        ("David Hilbert", "Hilbert's problems"), ("Kurt Godel", "Incompleteness theorems"),
        ("Georg Cantor", "Set theory"), ("Pierre de Fermat", "Fermat's last theorem"),
        ("Andrey Kolmogorov", "Probability"), ("John Nash", "Game theory"),
        ("Terence Tao", "Analysis"), ("Maryam Mirzakhani", "Hyperbolic geometry"),
    ]
    name, field = random.choice(people)
    return "{} - known for: {}".format(name, field)

def random_biologist():
    people = [
        ("Charles Darwin", "Evolution"), ("Gregor Mendel", "Genetics"),
        ("Louis Pasteur", "Germ theory"), ("Rosalind Franklin", "DNA structure"),
        ("James Watson", "DNA double helix"), ("Francis Crick", "DNA double helix"),
        ("Barbara McClintock", "Genetic transposition"), ("Alexander Fleming", "Penicillin"),
        ("Rachel Carson", "Environmental science"), ("Jane Goodall", "Primatology"),
        ("Ernst Haeckel", "Ecology"), ("Carl Linnaeus", "Taxonomy"),
        ("Antonie van Leeuwenhoek", "Microbiology"), ("Robert Hooke", "Cell theory"),
        ("Theodor Schwann", "Cell theory"), ("Lynn Margulis", "Endosymbiotic theory"),
        ("Severo Ochoa", "RNA synthesis"), ("Frederick Sanger", "DNA sequencing"),
        ("Kary Mullis", "PCR"), ("Jennifer Doudna", "CRISPR"),
        ("David Baltimore", "Virology"), ("Craig Venter", "Human genome"),
    ]
    name, field = random.choice(people)
    return "{} - known for: {}".format(name, field)

def random_physicist():
    people = [
        ("Albert Einstein", "Relativity"), ("Isaac Newton", "Laws of motion"),
        ("Niels Bohr", "Atomic model"), ("Max Planck", "Quantum theory"),
        ("Werner Heisenberg", "Uncertainty principle"), ("Erwin Schrodinger", "Wave equation"),
        ("Richard Feynman", "QED"), ("Stephen Hawking", "Black holes"),
        ("Marie Curie", "Radioactivity"), ("Galileo Galilei", "Heliocentrism"),
        ("Michael Faraday", "Electromagnetism"), ("James Clerk Maxwell", "Maxwell's equations"),
        ("Enrico Fermi", "Nuclear reactor"), ("Paul Dirac", "Antimatter"),
        ("Lise Meitner", "Nuclear fission"), ("Hans Bethe", "Stellar nucleosynthesis"),
        ("Johannes Kepler", "Planetary laws"), ("Edward Teller", "Hydrogen bomb"),
        ("Robert Oppenheimer", "Atomic bomb"), ("Carlo Rubbia", "W and Z bosons"),
        ("Murray Gell-Mann", "Quarks"), ("Peter Higgs", "Higgs boson"),
    ]
    name, field = random.choice(people)
    return "{} - known for: {}".format(name, field)

def random_inventor():
    people = [
        ("Thomas Edison", "Light bulb"), ("Nikola Tesla", "AC motor"),
        ("Alexander Graham Bell", "Telephone"), ("Johannes Gutenberg", "Printing press"),
        ("Wright Brothers", "Airplane"), ("Henry Ford", "Assembly line"),
        ("James Watt", "Steam engine"), ("Eli Whitney", "Cotton gin"),
        ("Alessandro Volta", "Battery"), ("Alfred Nobel", "Dynamite"),
        ("Guglielmo Marconi", "Radio"), ("Philo Farnsworth", "Television"),
        ("John Logie Baird", "Television"), ("Charles Babbage", "Computer"),
        ("Tim Berners-Lee", "World Wide Web"), ("Alan Turing", "Turing machine"),
        ("Grace Hopper", "Compiler"), ("Steve Jobs", "iPhone"),
        ("Bill Gates", "Windows"), ("Larry Page", "Google"),
        ("Jeff Bezos", "Amazon"), ("Elon Musk", "SpaceX"),
    ]
    name, field = random.choice(people)
    return "{} - invented: {}".format(name, field)

def random_nobel_prize():
    prizes = [
        ("Physics 2023", "Pierre Agostini, Ferenc Krausz, Anne L'Huillier", "Attosecond pulses"),
        ("Chemistry 2023", "Moungi Bawendi, Louis Brus, Alexei Ekimov", "Quantum dots"),
        ("Medicine 2023", "Katalin Kariko, Drew Weissman", "mRNA vaccines"),
        ("Literature 2023", "Jon Fosse", "Plays and prose"),
        ("Peace 2023", "Narges Mohammadi", "Women's rights in Iran"),
        ("Economics 2023", "Claudia Goldin", "Gender labor gaps"),
        ("Physics 2022", "Alain Aspect, John Clauser, Anton Zeilinger", "Quantum entanglement"),
        ("Chemistry 2022", "Carolyn Bertozzi, Morten Meldal, Barry Sharpless", "Click chemistry"),
        ("Medicine 2022", "Svante Paabo", "Neanderthal genome"),
        ("Literature 2022", "Annie Ernaux", "Autobiographical writing"),
        ("Peace 2022", "Ales Bialiatski, Memorial, Center for Civil Liberties", "Human rights"),
        ("Economics 2022", "Ben Bernanke, Douglas Diamond, Philip Dybvig", "Bank crises"),
        ("Physics 2021", "Syukuro Manabe, Klaus Hasselmann, Giorgio Parisi", "Climate modeling"),
        ("Chemistry 2021", "Benjamin List, David MacMillan", "Organocatalysis"),
        ("Medicine 2021", "David Julius, Ardem Patapoutian", "Temperature and touch receptors"),
        ("Literature 2021", "Abdulrazak Gurnah", "Colonialism narratives"),
        ("Peace 2021", "Maria Ressa, Dmitry Muratov", "Freedom of expression"),
        ("Economics 2021", "David Card, Joshua Angrist, Guido Imbens", "Causal inference"),
        ("Physics 2020", "Roger Penrose, Andrea Ghez, Reinhard Genzel", "Black holes"),
        ("Chemistry 2020", "Emmanuelle Charpentier, Jennifer Doudna", "CRISPR gene editing"),
        ("Medicine 2020", "Harvey Alter, Charles Rice, Michael Houghton", "Hepatitis C"),
        ("Literature 2020", "Louise Gluck", "Poetry"),
        ("Peace 2020", "World Food Programme", "Hunger relief"),
        ("Economics 2020", "Paul Milgrom, Robert Wilson", "Auction theory"),
        ("Physics 2019", "James Peebles, Michel Mayor, Didier Queloz", "Cosmic evolution"),
        ("Chemistry 2019", "John Goodenough, Stanley Whittingham, Akira Yoshino", "Lithium-ion batteries"),
        ("Medicine 2019", "William Kaelin, Peter Ratcliffe, Gregg Semenza", "Oxygen sensing"),
        ("Literature 2019", "Peter Handke", "Linguistic artistry"),
        ("Peace 2019", "Abiy Ahmed", "Ethiopia-Eritrea peace"),
        ("Economics 2019", "Abhijit Banerjee, Esther Duflo, Michael Kremer", "Poverty alleviation"),
        ("Physics 2018", "Arthur Ashkin, Gerard Mourou, Donna Strickland", "Laser physics"),
        ("Chemistry 2018", "Frances Arnold, George Smith, Gregory Winter", "Enzyme evolution"),
        ("Medicine 2018", "James Allison, Tasuku Honjo", "Cancer immunotherapy"),
        ("Literature 2018", "Olga Tokarczuk", "Narrative imagination"),
        ("Peace 2018", "Denis Mukwege, Nadia Murad", "Sexual violence justice"),
        ("Economics 2018", "William Nordhaus, Paul Romer", "Climate and innovation"),
        ("Physics 2017", "Rainer Weiss, Barry Barish, Kip Thorne", "Gravitational waves"),
        ("Chemistry 2017", "Jacques Dubochet, Joachim Frank, Richard Henderson", "Cryo-electron microscopy"),
        ("Medicine 2017", "Jeffrey Hall, Michael Rosbash, Michael Young", "Circadian rhythm genes"),
        ("Literature 2017", "Kazuo Ishiguro", "Novelist"),
        ("Peace 2017", "ICAN", "Nuclear weapons abolition"),
        ("Economics 2017", "Richard Thaler", "Behavioral economics"),
        ("Physics 2016", "David Thouless, Duncan Haldane, Michael Kosterlitz", "Topological phases"),
        ("Chemistry 2016", "Jean-Pierre Sauvage, Fraser Stoddart, Ben Feringa", "Molecular machines"),
        ("Medicine 2016", "Yoshinori Ohsumi", "Autophagy mechanisms"),
        ("Literature 2016", "Bob Dylan", "Songwriting"),
        ("Peace 2016", "Juan Manuel Santos", "Colombia peace process"),
        ("Economics 2016", "Oliver Hart, Bengt Holmstrom", "Contract theory"),
        ("Physics 2015", "Takaaki Kajita, Arthur McDonald", "Neutrino oscillations"),
        ("Chemistry 2015", "Tomas Lindahl, Paul Modrich, Aziz Sancar", "DNA repair"),
        ("Medicine 2015", "William Campbell, Satoshi Omura, Youyou Tu", "Parasite therapies"),
        ("Literature 2015", "Svetlana Alexievich", "Documentary writing"),
        ("Peace 2015", "National Dialogue Quartet", "Tunisian democracy"),
        ("Economics 2015", "Angus Deaton", "Consumption and welfare"),
        ("Physics 2014", "Isamu Akasaki, Hiroshi Amano, Shuji Nakamura", "Blue LEDs"),
        ("Chemistry 2014", "Eric Betzig, Stefan Hell, William Moerner", "Super-resolved microscopy"),
        ("Medicine 2014", "John O'Keefe, May-Britt Moser, Edvard Moser", "Grid cells in brain"),
        ("Literature 2014", "Patrick Modiano", "Memory and identity"),
        ("Peace 2014", "Kailash Satyarthi, Malala Yousafzai", "Children's education"),
        ("Economics 2014", "Jean Tirole", "Market regulation"),
        ("Physics 2013", "Francois Englert, Peter Higgs", "Higgs boson"),
        ("Chemistry 2013", "Martin Karplus, Michael Levitt, Arieh Warshel", "Computational chemistry"),
        ("Medicine 2013", "James Rothman, Randy Schekman, Thomas Sudhof", "Vesicle transport"),
        ("Literature 2013", "Alice Munro", "Short stories"),
        ("Peace 2013", "OPCW", "Chemical weapons destruction"),
        ("Economics 2013", "Eugene Fama, Lars Hansen, Robert Shiller", "Asset prices"),
        ("Physics 2012", "Serge Haroche, David Wineland", "Quantum optics"),
        ("Chemistry 2012", "Robert Lefkowitz, Brian Kobilka", "G-protein-coupled receptors"),
        ("Medicine 2012", "John Gurdon, Shinya Yamanaka", "Reprogrammed cells"),
        ("Literature 2012", "Mo Yan", "Hallucinatory realism"),
        ("Peace 2012", "European Union", "European integration"),
        ("Economics 2012", "Alvin Roth, Lloyd Shapley", "Market design"),
    ]
    entry = random.choice(prizes)
    return "{}: {} - {}".format(*entry)

def random_historic_event():
    events = [
        ("1776", "American Declaration of Independence signed"),
        ("1789", "French Revolution begins with storming of the Bastille"),
        ("1815", "Napoleon defeated at Waterloo"),
        ("1865", "US Civil War ends; Lincoln assassinated"),
        ("1914", "World War I begins"),
        ("1917", "Russian Revolution"),
        ("1918", "World War I ends; Spanish flu pandemic peaks"),
        ("1929", "Stock market crash starts Great Depression"),
        ("1933", "Hitler becomes Chancellor of Germany"),
        ("1939", "World War II begins with invasion of Poland"),
        ("1941", "Pearl Harbor attack; US enters WWII"),
        ("1945", "World War II ends; atomic bombs dropped on Japan"),
        ("1947", "India gains independence"),
        ("1948", "State of Israel established"),
        ("1949", "NATO founded; China becomes communist"),
        ("1953", "DNA structure discovered by Watson and Crick"),
        ("1955", "Warsaw Pact established"),
        ("1957", "Sputnik launched; Space Age begins"),
        ("1961", "Berlin Wall built; Yuri Gagarin in space"),
        ("1963", "JFK assassinated; I Have a Dream speech"),
        ("1964", "Civil Rights Act signed in USA"),
        ("1969", "Apollo 11 Moon landing"),
        ("1973", "Oil crisis"),
        ("1979", "Iranian Revolution; Soviet invasion of Afghanistan"),
        ("1981", "First IBM personal computer"),
        ("1985", "Mikhail Gorbachev becomes Soviet leader"),
        ("1986", "Chernobyl nuclear disaster"),
        ("1989", "Berlin Wall falls; Tiananmen Square protests"),
        ("1991", "Soviet Union dissolves; Gulf War"),
        ("1994", "Nelson Mandela becomes South African president"),
        ("1997", "Hong Kong returned to China"),
        ("2001", "9/11 terrorist attacks in USA"),
        ("2003", "Iraq War begins"),
        ("2004", "Indian Ocean tsunami kills 230,000"),
        ("2005", "Hurricane Katrina devastates New Orleans"),
        ("2007", "First iPhone released"),
        ("2008", "Global financial crisis"),
        ("2010", "Arab Spring begins in Tunisia"),
        ("2011", "Osama bin Laden killed"),
        ("2013", "Edward Snowden leaks NSA data"),
        ("2014", "Ebola outbreak in West Africa"),
        ("2015", "Paris climate agreement; Syrian refugee crisis"),
        ("2016", "Brexit referendum; Trump elected"),
        ("2017", "MeToo movement goes viral"),
        ("2019", "COVID-19 pandemic begins"),
        ("2020", "George Floyd protests worldwide"),
        ("2021", "US Capitol stormed; Biden inaugurated"),
        ("2022", "Russia invades Ukraine"),
        ("2023", "Israel-Hamas war begins"),
        ("2024", "AI regulation debates intensify"),
    ]
    year, event = random.choice(events)
    return "{}: {}".format(year, event)

def random_philosopher():
    philosophers = [
        ("Socrates", "Greek", "I know that I know nothing"),
        ("Plato", "Greek", "The Republic - ideal forms"),
        ("Aristotle", "Greek", "Logic, ethics, metaphysics"),
        ("Confucius", "Chinese", "Ethics and social harmony"),
        ("Laozi", "Chinese", "Taoism and natural harmony"),
        ("Buddha", "Indian", "The Four Noble Truths"),
        ("Descartes", "French", "I think, therefore I am"),
        ("Locke", "English", "Tabula rasa and natural rights"),
        ("Hume", "Scottish", "Empiricism and skepticism"),
        ("Kant", "German", "Categorical imperative"),
        ("Nietzsche", "German", "Will to power and Ubermensch"),
        ("Rousseau", "Swiss", "Social contract"),
        ("Marx", "German", "Dialectical materialism"),
        ("Beauvoir", "French", "Existentialism and feminism"),
        ("Camus", "French", "Absurdism"),
        ("Mill", "English", "Utilitarianism"),
        ("Hobbes", "English", "Leviathan and state of nature"),
        ("Schopenhauer", "German", "Will and pessimism"),
        ("Kierkegaard", "Danish", "Existentialism and faith"),
        ("Heidegger", "German", "Being and Time"),
        ("Wittgenstein", "Austrian", "Language games"),
        ("Arendt", "German", "Banality of evil"),
        ("Foucault", "French", "Power and knowledge"),
        ("Chomsky", "American", "Generative grammar"),
        ("Nussbaum", "American", "Capabilities approach"),
        ("Epicurus", "Greek", "Pursuit of pleasure and tranquility"),
        ("Plotinus", "Roman", "Neoplatonism"),
        ("Aquinas", "Italian", "Scholasticism and natural law"),
        ("Bacon", "English", "Scientific method"),
        ("Spinoza", "Dutch", "Pantheism and ethics"),
    ]
    name, origin, idea = random.choice(philosophers)
    return "{} ({}) - {}".format(name, origin, idea)

def random_scientific_law():
    laws = [
        ("Newton's First Law", "Object at rest stays at rest unless acted upon"),
        ("Newton's Second Law", "F = ma"),
        ("Newton's Third Law", "Equal and opposite reaction"),
        ("Universal Gravitation", "Every mass attracts every other mass"),
        ("Conservation of Energy", "Energy cannot be created or destroyed"),
        ("Conservation of Mass", "Mass is conserved in chemical reactions"),
        ("First Law of Thermodynamics", "Energy of isolated system is constant"),
        ("Second Law of Thermodynamics", "Entropy always increases"),
        ("Third Law of Thermodynamics", "Absolute zero is unattainable"),
        ("Ohm's Law", "V = IR"),
        ("Coulomb's Law", "Electric force inversely proportional to distance squared"),
        ("Faraday's Law", "Changing magnetic field induces electric current"),
        ("Maxwell's Equations", "Unified theory of electromagnetism"),
        ("General Relativity", "Gravity is curvature of spacetime"),
        ("Special Relativity", "E = mc^2; speed of light is constant"),
        ("Uncertainty Principle", "Cannot know position and momentum precisely"),
        ("Schrodinger's Equation", "Quantum state evolution"),
        ("Pauli Exclusion Principle", "No two electrons same quantum state"),
        ("Archimedes' Principle", "Buoyant force equals displaced fluid weight"),
        ("Pascal's Law", "Pressure transmitted equally in fluid"),
        ("Bernoulli's Principle", "Fast flow = low pressure"),
        ("Hooke's Law", "F = kx (spring force proportional to extension)"),
        ("Boyle's Law", "PV = constant at constant temperature"),
        ("Charles's Law", "V proportional to T at constant pressure"),
        ("Avogadro's Law", "Equal volumes have equal molecule count"),
        ("Ideal Gas Law", "PV = nRT"),
        ("Dalton's Law", "Total pressure = sum of partial pressures"),
        ("Le Chatelier's Principle", "Equilibrium responds to stress"),
        ("Mendel's Segregation", "Alleles separate during gamete formation"),
        ("Mendel's Independent Assortment", "Genes sort independently"),
        ("Hardy-Weinberg", "Allele frequencies constant without evolution"),
        ("Natural Selection", "Evolution by survival of the fittest"),
        ("Moore's Law", "Transistor density doubles every 2 years"),
        ("Metcalfe's Law", "Network value proportional to users squared"),
        ("Parkinson's Law", "Work expands to fill available time"),
        ("Murphy's Law", "Anything that can go wrong will go wrong"),
        ("Occam's Razor", "Simplest explanation is usually correct"),
        ("Brooks's Law", "Adding manpower to late project makes it later"),
    ]
    name, desc = random.choice(laws)
    return "{}: {}".format(name, desc)

def random_programming_language():
    langs = [
        ("Python", "Guido van Rossum", "1991", "General-purpose, readable syntax"),
        ("JavaScript", "Brendan Eich", "1995", "Web scripting"),
        ("Java", "James Gosling", "1995", "Write once run anywhere"),
        ("C", "Dennis Ritchie", "1972", "Systems programming"),
        ("C++", "Bjarne Stroustrup", "1985", "OOP and systems"),
        ("C#", "Microsoft", "2000", ".NET applications"),
        ("Ruby", "Yukihiro Matsumoto", "1995", "Developer happiness"),
        ("PHP", "Rasmus Lerdorf", "1994", "Web backend"),
        ("Swift", "Apple", "2014", "iOS development"),
        ("Kotlin", "JetBrains", "2011", "Android development"),
        ("TypeScript", "Microsoft", "2012", "Typed JavaScript"),
        ("Go", "Google", "2009", "Concurrency and systems"),
        ("Rust", "Mozilla", "2010", "Memory safety without GC"),
        ("Scala", "Martin Odersky", "2004", "FP and OOP hybrid"),
        ("Haskell", "Simon Peyton Jones", "1990", "Pure functional"),
        ("Lisp", "John McCarthy", "1958", "Symbolic AI"),
        ("Prolog", "Alain Colmerauer", "1972", "Logic programming"),
        ("SQL", "Donald Chamberlin", "1974", "Database queries"),
        ("R", "Ross Ihaka", "1993", "Statistical computing"),
        ("Julia", "Jeff Bezanson", "2012", "Scientific computing"),
        ("Perl", "Larry Wall", "1987", "Text processing"),
        ("Lua", "PUC-Rio", "1993", "Embedded scripting"),
        ("Dart", "Google", "2011", "Flutter apps"),
        ("Elixir", "Jose Valim", "2011", "Concurrent apps on Erlang VM"),
        ("Clojure", "Rich Hickey", "2007", "Modern Lisp on JVM"),
        ("F#", "Microsoft", "2005", ".NET functional"),
        ("COBOL", "Grace Hopper", "1959", "Business data processing"),
        ("Fortran", "IBM", "1957", "Scientific and numeric"),
        ("Ada", "Jean Ichbiah", "1980", "Defense and aerospace"),
        ("Smalltalk", "Alan Kay", "1972", "Pure OOP"),
        ("Erlang", "Ericsson", "1986", "Telecom concurrency"),
        ("Visual Basic", "Microsoft", "1991", "Windows GUI apps"),
        ("Assembly", "Various", "1949", "Low-level hardware"),
        ("MATLAB", "MathWorks", "1984", "Numerical computing"),
        ("Objective-C", "Brad Cox", "1984", "Apple ecosystem"),
        ("Delphi", "Borland", "1995", "Rapid Windows apps"),
        ("Scheme", "Gerald Sussman", "1975", "Simple functional Lisp"),
        ("Hack", "Facebook", "2014", "PHP variant with types"),
        ("Solidity", "Ethereum", "2015", "Smart contracts"),
        ("Zig", "Andrew Kelley", "2016", "Modern systems programming"),
    ]
    name, creator, year, use = random.choice(langs)
    return "{}: Created by {} in {} - {}".format(name, creator, year, use)

def random_algorithm():
    algos = [
        ("Binary Search", "O(log n)", "Find element in sorted array"),
        ("Bubble Sort", "O(n^2)", "Simple comparison sort"),
        ("Quick Sort", "O(n log n)", "Divide and conquer sort"),
        ("Merge Sort", "O(n log n)", "Stable divide and conquer sort"),
        ("Insertion Sort", "O(n^2)", "Build final array one element at a time"),
        ("Selection Sort", "O(n^2)", "Repeatedly find minimum element"),
        ("Heap Sort", "O(n log n)", "Sort using heap data structure"),
        ("Radix Sort", "O(nk)", "Non-comparative integer sort"),
        ("Dijkstra's Algorithm", "O(V^2)", "Shortest path in weighted graph"),
        ("Bellman-Ford", "O(VE)", "Shortest path with negative weights"),
        ("Floyd-Warshall", "O(V^3)", "All pairs shortest path"),
        ("Kruskal's Algorithm", "O(E log V)", "Minimum spanning tree"),
        ("Prim's Algorithm", "O(V^2)", "Minimum spanning tree"),
        ("A* Search", "O(b^d)", "Pathfinding with heuristic"),
        ("BFS", "O(V+E)", "Graph traversal level by level"),
        ("DFS", "O(V+E)", "Graph traversal depth first"),
        ("Inorder Traversal", "O(n)", "Binary tree inorder"),
        ("KMP", "O(n+m)", "Substring search"),
        ("Rabin-Karp", "O(n+m)", "Hash-based substring search"),
        ("Trie Search", "O(m)", "Prefix tree search"),
        ("Union-Find", "O(a(n))", "Disjoint set operations"),
        ("Dynamic Programming", "O(n^2)", "Solve via subproblems"),
        ("Greedy Algorithm", "O(n)", "Local optimal decisions"),
        ("Huffman Coding", "O(n log n)", "Lossless compression"),
        ("RSA", "O(n^3)", "Asymmetric cryptography"),
        ("AES", "O(n)", "Symmetric block cipher"),
        ("SHA-256", "O(n)", "Cryptographic hash"),
        ("PageRank", "O(n)", "Web page ranking"),
        ("K-means", "O(nki)", "Clustering algorithm"),
        ("Linear Regression", "O(n^2)", "Statistical modeling"),
        ("Gradient Descent", "O(n)", "Optimization algorithm"),
        ("Backpropagation", "O(n)", "Training neural networks"),
        ("Convolution", "O(n^2)", "Image processing"),
        ("FFT", "O(n log n)", "Signal processing"),
        ("Kalman Filter", "O(n^2)", "State estimation"),
        ("Hungarian Algorithm", "O(n^3)", "Assignment problem"),
        ("Simplex Algorithm", "O(n^2)", "Linear programming"),
    ]
    name, complexity, desc = random.choice(algos)
    return "{}: {} - {}".format(name, complexity, desc)

def random_data_structure():
    structs = [
        ("Array", "Contiguous memory, O(1) access"),
        ("Linked List", "Dynamic size, O(n) access"),
        ("Stack", "LIFO, O(1) push/pop"),
        ("Queue", "FIFO, O(1) enqueue/dequeue"),
        ("Priority Queue", "O(log n) insert/extract"),
        ("Hash Table", "O(1) average lookup"),
        ("Binary Search Tree", "O(log n) average search"),
        ("AVL Tree", "Self-balancing BST"),
        ("Red-Black Tree", "Self-balancing BST"),
        ("B-Tree", "Balanced tree for databases"),
        ("Trie", "Prefix tree, O(m) search"),
        ("Heap", "Complete binary tree"),
        ("Graph", "V vertices and E edges"),
        ("Adjacency Matrix", "O(V^2) storage"),
        ("Adjacency List", "O(V+E) storage"),
        ("Skip List", "Probabilistic sorted list"),
        ("Bloom Filter", "Probabilistic set membership"),
        ("Segment Tree", "Range queries and updates"),
        ("Fenwick Tree", "Prefix sums and updates"),
        ("Disjoint Set", "Union-find operations"),
        ("Suffix Array", "String processing"),
        ("Suffix Tree", "Advanced string search"),
        ("Rope", "String concat for text editors"),
        ("Binary Heap", "Priority queue using array"),
        ("Fibonacci Heap", "O(1) decrease-key"),
        ("Deque", "Double-ended queue"),
        ("Circular Buffer", "Fixed-size FIFO with wrap"),
        ("Sparse Matrix", "Efficient sparse storage"),
        ("Lookup Table", "Precomputed values"),
        ("Cache", "LRU/MRU temporal locality"),
    ]
    name, desc = random.choice(structs)
    return "{}: {}".format(name, desc)

def random_tech_company():
    companies = [
        ("Apple", "1976", "Cupertino", "Jobs, Wozniak", "iPhone, Mac, iPad", "3.0T"),
        ("Microsoft", "1975", "Redmond", "Gates, Allen", "Windows, Office, Azure", "2.8T"),
        ("Google", "1998", "Mountain View", "Page, Brin", "Search, Android, YouTube", "1.8T"),
        ("Amazon", "1994", "Seattle", "Bezos", "AWS, E-commerce, Alexa", "1.9T"),
        ("Meta", "2004", "Menlo Park", "Zuckerberg", "Facebook, Instagram, WhatsApp", "1.2T"),
        ("Tesla", "2003", "Austin", "Elon Musk", "Electric cars, Solar, SpaceX", "800B"),
        ("NVIDIA", "1993", "Santa Clara", "Jensen Huang", "GPUs, AI chips", "2.2T"),
        ("TSMC", "1987", "Hsinchu", "Morris Chang", "Semiconductor fabrication", "650B"),
        ("Samsung", "1938", "Seoul", "Lee Byung-chul", "Electronics, phones, chips", "400B"),
        ("Intel", "1968", "Santa Clara", "Moore, Noyce", "Processors, chips", "200B"),
        ("IBM", "1911", "Armonk", "Flint", "Mainframes, AI, cloud", "150B"),
        ("Oracle", "1977", "Austin", "Ellison", "Databases, cloud", "350B"),
        ("Cisco", "1984", "San Jose", "Bosack", "Networking equipment", "200B"),
        ("Adobe", "1982", "San Jose", "Warnock", "Creative software, PDF", "250B"),
        ("Salesforce", "1999", "San Francisco", "Benioff", "CRM, cloud", "250B"),
        ("Netflix", "1997", "Los Gatos", "Hastings", "Streaming, content", "200B"),
        ("Uber", "2009", "San Francisco", "Kalanick", "Ridesharing, delivery", "100B"),
        ("Airbnb", "2008", "San Francisco", "Chesky", "Home rental, travel", "100B"),
        ("Spotify", "2006", "Stockholm", "Daniel Ek", "Music streaming", "50B"),
        ("PayPal", "1998", "San Jose", "Thiel, Musk", "Payments, Venmo", "100B"),
        ("AMD", "1969", "Santa Clara", "Sanders", "CPUs, GPUs", "250B"),
        ("Qualcomm", "1985", "San Diego", "Jacobs", "Mobile chips, patents", "150B"),
        ("Shopify", "2006", "Ottawa", "Lutke", "E-commerce platform", "80B"),
        ("Square", "2009", "San Francisco", "Dorsey", "Payments, Cash App", "50B"),
        ("Zoom", "2011", "San Jose", "Yuan", "Video conferencing", "30B"),
        ("Slack", "2013", "San Francisco", "Butterfield", "Team communication", "30B"),
        ("Snapchat", "2011", "Santa Monica", "Spiegel", "Ephemeral messaging", "30B"),
        ("Pinterest", "2010", "San Francisco", "Silbermann", "Visual discovery", "20B"),
        ("LinkedIn", "2003", "Sunnyvale", "Hoffman", "Professional networking", "30B"),
        ("Reddit", "2005", "San Francisco", "Ohanian", "Social news", "20B"),
        ("TikTok", "2016", "Beijing", "Yiming", "Short video platform", "200B"),
        ("ByteDance", "2012", "Beijing", "Yiming", "AI content platform", "250B"),
        ("Alibaba", "1999", "Hangzhou", "Jack Ma", "E-commerce, cloud", "200B"),
        ("Tencent", "1998", "Shenzhen", "Ma Huateng", "Social media, games", "400B"),
        ("Baidu", "2000", "Beijing", "Robin Li", "Search, AI", "40B"),
        ("Xiaomi", "2010", "Beijing", "Lei Jun", "Phones, IoT", "50B"),
        ("Huawei", "1987", "Shenzhen", "Ren Zhengfei", "Telecom, phones", "100B"),
        ("Sony", "1946", "Tokyo", "Ibuka", "Electronics, games, media", "120B"),
        ("Nintendo", "1889", "Kyoto", "Yamauchi", "Gaming consoles", "70B"),
        ("SpaceX", "2002", "Hawthorne", "Elon Musk", "Rockets, Starlink", "150B"),
        ("Palantir", "2003", "Denver", "Thiel, Karp", "Data analytics", "40B"),
        ("Stripe", "2010", "San Francisco", "Collison", "Online payments", "50B"),
    ]
    name, year, hq, founders, products, value = random.choice(companies)
    return "{} ({}): {} - {} - {} [{}]".format(name, year, hq, founders, products, value)

def random_historical_figure():
    figures = [
        ("Alexander the Great", "356-323 BC", "Macedonia", "Conquered Persia to India"),
        ("Julius Caesar", "100-44 BC", "Rome", "Roman dictator, military general"),
        ("Cleopatra", "69-30 BC", "Egypt", "Last pharaoh of Egypt"),
        ("Genghis Khan", "1162-1227", "Mongolia", "Founded Mongol Empire"),
        ("Christopher Columbus", "1451-1506", "Genoa", "Discovered Americas for Spain"),
        ("Leonardo da Vinci", "1452-1519", "Italy", "Renaissance polymath"),
        ("William Shakespeare", "1564-1616", "England", "Playwright and poet"),
        ("Napoleon Bonaparte", "1769-1821", "France", "French emperor, military leader"),
        ("Abraham Lincoln", "1809-1865", "USA", "16th US President, ended slavery"),
        ("Charles Darwin", "1809-1882", "England", "Theory of evolution"),
        ("Marie Curie", "1867-1934", "Poland/France", "Radioactivity research"),
        ("Mahatma Gandhi", "1869-1948", "India", "Nonviolent resistance"),
        ("Winston Churchill", "1874-1965", "UK", "British PM during WWII"),
        ("Albert Einstein", "1879-1955", "Germany/USA", "Theory of relativity"),
        ("Franklin D. Roosevelt", "1882-1945", "USA", "32nd US President, New Deal"),
        ("Mao Zedong", "1893-1976", "China", "Founder of PRC"),
        ("Nelson Mandela", "1918-2013", "South Africa", "Anti-apartheid leader"),
        ("Martin Luther King Jr.", "1929-1968", "USA", "Civil rights leader"),
        ("Neil Armstrong", "1930-2012", "USA", "First man on the Moon"),
        ("Elvis Presley", "1935-1977", "USA", "King of Rock and Roll"),
        ("John Lennon", "1940-1980", "UK", "Beatles musician"),
        ("Muhammad Ali", "1942-2016", "USA", "Boxing champion"),
        ("Stephen Hawking", "1942-2018", "UK", "Cosmologist, black holes"),
        ("Steve Jobs", "1955-2011", "USA", "Apple co-founder"),
        ("Bill Gates", "1955-", "USA", "Microsoft co-founder"),
        ("Tim Berners-Lee", "1955-", "UK", "Invented World Wide Web"),
        ("Michael Jackson", "1958-2009", "USA", "King of Pop"),
        ("Barack Obama", "1961-", "USA", "44th US President"),
        ("Jeff Bezos", "1964-", "USA", "Amazon founder"),
        ("Elon Musk", "1971-", "South Africa/USA", "Tesla, SpaceX founder"),
        ("Malala Yousafzai", "1997-", "Pakistan", "Education activist"),
        ("Greta Thunberg", "2003-", "Sweden", "Climate activist"),
        ("Socrates", "470-399 BC", "Greece", "Western philosophy founder"),
        ("Aristotle", "384-322 BC", "Greece", "Philosopher, polymath"),
        ("Isaac Newton", "1643-1727", "England", "Physics, calculus"),
        ("Galileo Galilei", "1564-1642", "Italy", "Astronomy, physics"),
        ("Nikola Tesla", "1856-1943", "Serbia/USA", "AC electricity"),
        ("Thomas Edison", "1847-1931", "USA", "Light bulb, phonograph"),
        ("Alan Turing", "1912-1954", "UK", "Computer science pioneer"),
        ("Ada Lovelace", "1815-1852", "UK", "First computer programmer"),
        ("Florence Nightingale", "1820-1910", "UK", "Modern nursing"),
        ("Amelia Earhart", "1897-1937", "USA", "Aviation pioneer"),
        ("Frida Kahlo", "1907-1954", "Mexico", "Artist"),
        ("Walt Disney", "1901-1966", "USA", "Animation and theme parks"),
        ("Charlie Chaplin", "1889-1977", "UK", "Silent film actor"),
        ("Vincent van Gogh", "1853-1890", "Netherlands", "Post-Impressionist painter"),
        ("Pablo Picasso", "1881-1973", "Spain", "Cubist painter"),
        ("Johann Sebastian Bach", "1685-1750", "Germany", "Baroque composer"),
        ("Wolfgang Mozart", "1756-1791", "Austria", "Classical composer"),
        ("Ludwig van Beethoven", "1770-1827", "Germany", "Classical/Romantic composer"),
    ]
    name, life, origin, claim = random.choice(figures)
    return "{} ({}) from {}: {}".format(name, life, origin, claim)

def random_world_record():
    records = [
        ("Fastest land animal", "Cheetah, 120 km/h"),
        ("Largest mammal", "Blue whale, 30m, 200 tons"),
        ("Tallest building", "Burj Khalifa, 828m"),
        ("Longest river", "Nile, 6,650 km"),
        ("Largest desert", "Antarctica, 14 million km\u00b2"),
        ("Deepest ocean point", "Mariana Trench, 11,034m"),
        ("Highest mountain", "Mount Everest, 8,848m"),
        ("Largest ocean", "Pacific, 165 million km\u00b2"),
        ("Most populous country", "India, 1.4B"),
        ("Largest country by area", "Russia, 17.1M km\u00b2"),
        ("Oldest living tree", "Methuselah, 4,855 years"),
        ("Largest living structure", "Great Barrier Reef"),
        ("Most spoken language", "English, 1.5B speakers"),
        ("Fastest computer", "El Capitan, 2 EFLOPS"),
        ("Most expensive painting", "Salvator Mundi, $450M"),
        ("Largest stadium", "Rungrado May Day, 114,000 seats"),
        ("Most Olympic golds", "Michael Phelps, 23 golds"),
        ("Longest human life", "Jeanne Calment, 122 years"),
        ("Highest waterfall", "Angel Falls, 979m"),
        ("Largest cave", "Son Doong, Vietnam"),
        ("Deepest lake", "Lake Baikal, 1,642m"),
        ("Highest lake", "Lake Titicaca, 3,812m"),
        ("World's busiest airport", "Hartsfield-Jackson, 104M/year"),
        ("Longest bridge", "Danyang-Kunshan, 164.8 km"),
        ("Longest tunnel", "Gotthard Base, 57 km"),
        ("Tallest waterfall", "Tugela Falls, 948m"),
        ("Largest island", "Greenland, 2.16M km\u00b2"),
        ("Driest place", "Atacama Desert, <1mm rain/year"),
        ("Wettest place", "Mawsynram, India, 11,872mm/year"),
        ("Coldest inhabited place", "Oymyakon, -67.7C"),
        ("Hottest place", "Death Valley, 56.7C"),
        ("Windiest place", "Commonwealth Bay, 240 km/h"),
        ("Largest rainforest", "Amazon, 5.5M km\u00b2"),
        ("Largest coral reef", "Great Barrier Reef, 344,000 km\u00b2"),
        ("Largest volcano", "Mauna Loa, 9km from ocean floor"),
        ("Most active volcano", "Kilauea, Hawaii"),
        ("Largest asteroid", "Ceres, 940 km diameter"),
        ("Largest moon", "Ganymede, larger than Mercury"),
        ("Fastest spacecraft", "Parker Solar Probe, 692,000 km/h"),
        ("Most distant human object", "Voyager 1, 24B km away"),
    ]
    name, detail = random.choice(records)
    return "{}: {}".format(name, detail)

def random_math_fact():
    facts = [
        ("Pi", "3.14159... infinite non-repeating"),
        ("Golden Ratio", "1.618... found in nature and art"),
        ("Euler's Number e", "2.71828... base of natural log"),
        ("Zero", "Invented in India around 500 AD"),
        ("Infinity", "Symbol \u221e introduced by John Wallis in 1655"),
        ("Prime Numbers", "Infinite in number, proven by Euclid"),
        ("Imaginary Unit i", "Square root of -1"),
        ("Fibonacci Sequence", "0,1,1,2,3,5,8,13... appears in nature"),
        ("Catalan Numbers", "1,1,2,5,14,42... occur in combinatorics"),
        ("Mersenne Primes", "Primes of form 2^n-1"),
        ("Perfect Numbers", "Sum of divisors equals the number, e.g. 6, 28"),
        ("Amicable Numbers", "220 and 284: each is sum of proper divisors of the other"),
        ("Pythagorean Theorem", "a\u00b2 + b\u00b2 = c\u00b2 for right triangles"),
        ("Fermat's Last Theorem", "No integer solutions for x^n + y^n = z^n when n>2"),
        ("Four Color Theorem", "Any map can be colored with 4 colors without adjacent same"),
        ("Goldbach's Conjecture", "Every even number >2 is sum of two primes"),
        ("Riemann Hypothesis", "Zeros of zeta function lie on critical line (unproven)"),
        ("P vs NP", "Can hard problems be solved quickly? (unproven)"),
        ("Collatz Conjecture", "Always reach 1 by n/2 for even, 3n+1 for odd (unproven)"),
        ("Twin Prime Conjecture", "Infinite pairs of primes 2 apart (unproven)"),
        ("Poincare Conjecture", "Every simply connected 3-manifold is a sphere (proven)"),
        ("Goedel's Incompleteness", "Some true statements cannot be proven"),
        ("Banach-Tarski Paradox", "A sphere can be split and reassembled into two identical spheres"),
        ("Monty Hall Problem", "Switching doors gives 2/3 chance to win"),
        ("Birthday Paradox", "In a group of 23, 50% chance two share a birthday"),
        ("Benford's Law", "In real data, lower digits appear more often as first digit"),
        ("Euler's Identity", "e^(i*pi) + 1 = 0, the most beautiful equation"),
        ("Chaos Theory", "Sensitive dependence on initial conditions"),
        ("Fractal Dimension", "Coastline length depends on measurement scale"),
        ("Game Theory", "Prisoner's Dilemma shows cooperation vs defection"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_chemistry_fact():
    facts = [
        ("Water", "H2O - universal solvent"),
        ("Carbon", "Foundation of life; forms 4 bonds"),
        ("Oxygen", "O2 - essential for respiration"),
        ("Hydrogen", "Most abundant element in universe"),
        ("Helium", "Second most abundant; inert gas"),
        ("Gold", "Au - malleable, does not tarnish"),
        ("Silver", "Ag - best electrical conductor"),
        ("Iron", "Fe - core of Earth's magnetic field"),
        ("Uranium", "U - nuclear fuel"),
        ("Silicon", "Si - basis of semiconductors"),
        ("Nitrogen", "N2 - 78% of Earth's atmosphere"),
        ("Chlorine", "Cl - disinfectant, greenish gas"),
        ("Sodium", "Na - explosive in water"),
        ("Calcium", "Ca - bones and teeth"),
        ("Potassium", "K - essential for nerve function"),
        ("Phosphorus", "P - key in DNA and ATP"),
        ("Sulfur", "S - smell of rotten eggs"),
        ("Mercury", "Hg - only liquid metal at room temp"),
        ("Bromine", "Br - only liquid nonmetal at room temp"),
        ("Iodine", "I - disinfectant, sublimes"),
        ("Platinum", "Pt - catalytic converter"),
        ("Copper", "Cu - excellent conductor, reddish"),
        ("Aluminum", "Al - lightweight, abundant in crust"),
        ("Magnesium", "Mg - lightweight, burns bright"),
        ("Titanium", "Ti - strong, lightweight, biocompatible"),
        ("Lithium", "Li - batteries, lightest metal"),
        ("Cobalt", "Co - blue pigment, battery cathode"),
        ("Nickel", "Ni - coins, alloys, battery cathode"),
        ("Zinc", "Zn - galvanizing steel"),
        ("Tin", "Sn - cans, solder"),
        ("Lead", "Pb - dense, toxic, historical pipes"),
        ("Arsenic", "As - poison, semiconductor"),
        ("Neon", "Ne - red neon signs"),
        ("Xenon", "Xe - high-intensity lamps"),
        ("Radon", "Rn - radioactive indoor hazard"),
        ("Ozone", "O3 - UV protection layer"),
        ("Hydrogen Peroxide", "H2O2 - bleach and disinfectant"),
        ("Methane", "CH4 - natural gas"),
        ("Ethanol", "C2H5OH - alcohol fuel"),
        ("Acetic Acid", "CH3COOH - vinegar"),
        ("Sulfuric Acid", "H2SO4 - most produced chemical"),
        ("Ammonia", "NH3 - fertilizer"),
        ("Sodium Chloride", "NaCl - table salt"),
        ("Glucose", "C6H12O6 - simple sugar"),
        ("DNA", "Double helix of nucleotides"),
        ("ATP", "Adenosine triphosphate - cellular energy"),
        ("Chlorophyll", "Mg-centered molecule for photosynthesis"),
        ("Hemoglobin", "Fe-centered molecule for oxygen transport"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_biology_fact():
    facts = [
        ("Human DNA", "99.9% identical between any two people"),
        ("Brain", "~86 billion neurons, 100 trillion synapses"),
        ("Heart", "Beats ~100,000 times per day"),
        ("Lungs", "Contain ~300 million alveoli"),
        ("Liver", "Performs over 500 functions"),
        ("Skin", "Largest organ, ~2m\u00b2 surface area"),
        ("Bones", "206 in adult human body"),
        ("Muscles", "~640 skeletal muscles"),
        ("Blood", "~5 liters in average adult"),
        ("Red blood cells", "Live ~120 days, 25 trillion in body"),
        ("White blood cells", "Fight infection, many types"),
        ("DNA length", "2m per cell, 100B km total in body"),
        ("Stomach acid", "pH of 1-2, can dissolve metal"),
        ("Small intestine", "~6m long, most nutrient absorption"),
        ("Large intestine", "~1.5m long, water absorption"),
        ("Kidneys", "Filter 180 liters daily"),
        ("Eye", "Can distinguish 10 million colors"),
        ("Ear", "Can detect frequencies 20-20,000 Hz"),
        ("Nose", "Can detect ~1 trillion scents"),
        ("Human genome", "~20,000 protein-coding genes"),
        ("Bacteria in body", "~39 trillion, outnumber human cells"),
        ("Gut microbiome", "~1,000 species of bacteria"),
        ("Ribosomes", "Protein factories in every cell"),
        ("Mitochondria", "Powerhouse of the cell"),
        ("Cell membrane", "Fluid mosaic of lipids and proteins"),
        ("Endoplasmic Reticulum", "Protein and lipid synthesis"),
        ("Golgi apparatus", "Packaging and shipping center"),
        ("Lysosomes", "Cellular recycling and waste disposal"),
        ("Chromosomes", "23 pairs in humans"),
        ("Telomeres", "Protective caps on chromosomes, shorten with age"),
        ("CRISPR", "Gene editing technology from bacteria"),
        ("Stem cells", "Can differentiate into any cell type"),
        ("Antibodies", "Y-shaped proteins that tag pathogens"),
        ("Enzymes", "Biological catalysts"),
        ("Hormones", "Chemical messengers in blood"),
        ("Photosynthesis", "6CO2 + 6H2O -> C6H12O6 + 6O2"),
        ("Cellular respiration", "C6H12O6 + 6O2 -> 6CO2 + 6H2O + ATP"),
        ("Mitosis", "Cell division for growth and repair"),
        ("Meiosis", "Cell division for gametes"),
        ("Evolution", "Descent with modification over generations"),
        ("Natural selection", "Survival and reproduction of the fittest"),
        ("Genetic drift", "Random changes in gene frequency"),
        ("Gene flow", "Transfer of genes between populations"),
        ("Mutation", "Random change in DNA sequence"),
        ("Epigenetics", "Heritable changes not in DNA sequence"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_physics_fact():
    facts = [
        ("Speed of light", "299,792,458 m/s in vacuum"),
        ("Speed of sound", "343 m/s at sea level"),
        ("Gravity", "9.81 m/s\u00b2 on Earth"),
        ("Planck length", "1.616 x 10^-35 m, smallest meaningful length"),
        ("Planck time", "5.39 x 10^-44 s, smallest meaningful time"),
        ("Quantum entanglement", "Spooky action at a distance"),
        ("Wave-particle duality", "Light is both wave and particle"),
        ("Superposition", "Particle exists in all states until measured"),
        ("Schrodinger's Cat", "Alive and dead simultaneously"),
        ("Dark matter", "27% of universe, invisible"),
        ("Dark energy", "68% of universe, accelerating expansion"),
        ("Black hole", "Gravity so strong even light cannot escape"),
        ("Event horizon", "Point of no return around black hole"),
        ("Hawking radiation", "Black holes emit particles and evaporate"),
        ("Neutron star", "City-sized, spoonful weighs billions of tons"),
        ("Pulsar", "Rotating neutron star emitting radiation beams"),
        ("Quasar", "Bright center of distant galaxy"),
        ("Supernova", "Explosion of massive star"),
        ("Big Bang", "Universe began 13.8 billion years ago"),
        ("Cosmic microwave background", "Afterglow of Big Bang"),
        ("Expanding universe", "Galaxies moving apart, Hubble's Law"),
        ("Time dilation", "Time slows near speed of light or strong gravity"),
        ("Length contraction", "Objects shorten at high speed"),
        ("Mass-energy equivalence", "E = mc\u00b2"),
        ("Nuclear fusion", "Stars fuse hydrogen into helium"),
        ("Nuclear fission", "Atomic nucleus splits, releases energy"),
        ("Radioactive decay", "Unstable atoms emit radiation"),
        ("Electromagnetic spectrum", "Radio to gamma rays"),
        ("Photon", "Particle of light, zero mass"),
        ("Gluon", "Carries strong nuclear force"),
        ("Graviton", "Hypothetical gravity particle"),
        ("Higgs boson", "Gives mass to particles"),
        ("Standard Model", "Theory of fundamental particles and forces"),
        ("Antimatter", "Matter with opposite charge, annihilates on contact"),
        ("Quantum tunneling", "Particle passes through barrier impossible classically"),
        ("Superconductivity", "Zero resistance below certain temperature"),
        ("Bose-Einstein condensate", "Matter at near absolute zero"),
        ("Plasma", "Fourth state of matter, ionized gas"),
        ("Brownian motion", "Random movement of particles in fluid"),
        ("Doppler effect", "Change in frequency due to relative motion"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_geography_fact():
    facts = [
        ("Largest continent", "Asia, 44.58M km\u00b2"),
        ("Smallest continent", "Australia, 8.56M km\u00b2"),
        ("Most populous city", "Tokyo, 37M people"),
        ("Longest mountain range", "Andes, 7,000 km"),
        ("Deepest river", "Congo River, 220m deep"),
        ("Widest waterfall", "Khone Phapheng, 10.8 km wide"),
        ("Largest lake", "Caspian Sea, 371,000 km\u00b2"),
        ("Deepest canyon", "Yarlung Tsangpo, 5,300m deep"),
        ("Largest delta", "Ganges-Brahmaputra, 100,000 km\u00b2"),
        ("Largest peninsula", "Arabian Peninsula, 3.2M km\u00b2"),
        ("Largest gulf", "Gulf of Mexico, 1.6M km\u00b2"),
        ("Largest bay", "Bay of Bengal, 2.17M km\u00b2"),
        ("Largest archipelago", "Indonesia, 17,500 islands"),
        ("Largest atoll", "Kiritimati, 388 km\u00b2"),
        ("Highest capital", "La Paz, Bolivia, 3,640m"),
        ("Lowest capital", "Baku, Azerbaijan, -28m"),
        ("Northernmost capital", "Reykjavik, Iceland"),
        ("Southernmost capital", "Wellington, New Zealand"),
        ("Most remote island", "Tristan da Cunha"),
        ("Most remote city", "Perth, Australia"),
        ("Most multilingual country", "Papua New Guinea, 840 languages"),
        ("Smallest country", "Vatican City, 0.44 km\u00b2"),
        ("Largest country", "Russia, 17.1M km\u00b2"),
        ("Most forested country", "Suriname, 97% forest"),
        ("Least forested country", "Qatar, ~0% forest"),
        ("Highest road", "Khardung La, India, 5,359m"),
        ("Deepest road", "Tunnel Eiksund, Norway, -287m"),
        ("Longest road", "Pan-American Highway, 30,000 km"),
        ("Largest national park", "Northeast Greenland, 972,000 km\u00b2"),
        ("Most visited national park", "Great Smoky Mountains, 12M/year"),
        ("Largest urban area", "Guangzhou, 41M people"),
        ("Most densely populated", "Macau, 21,000/km\u00b2"),
        ("Least densely populated", "Greenland, 0.1/km\u00b2"),
        ("Highest GDP per capita", "Luxembourg, $140,000"),
        ("Lowest GDP per capita", "South Sudan, ~$400"),
        ("Most time zones", "France, 12 time zones"),
        ("Most neighbors", "China and Russia, 14 each"),
        ("First country to recognize Christmas", "Mexico, 1825"),
        ("Country with most lakes", "Canada, ~2M lakes"),
        ("Country with most rivers", "Bangladesh, ~700 rivers"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_astronomy_fact():
    facts = [
        ("Sun diameter", "1.39M km - 109x Earth"),
        ("Sun temperature", "5,500C surface, 15M C core"),
        ("Solar system age", "4.6 billion years"),
        ("Closest star", "Proxima Centauri, 4.24 light years"),
        ("Andromeda Galaxy", "2.5M light years away, on collision course"),
        ("Milky Way diameter", "100,000 light years"),
        ("Milky Way stars", "100-400 billion stars"),
        ("Observable universe", "93 billion light years across"),
        ("Estimated stars in universe", "200 billion trillion"),
        ("Estimated galaxies", "2 trillion"),
        ("Largest known star", "UY Scuti, 1,708x Sun radius"),
        ("Most massive star", "R136a1, 315x Sun mass"),
        ("Nearest black hole", "Gaia BH1, 1,560 light years away"),
        ("Fastest rotating star", "VFTS 102, 540 km/s at equator"),
        ("Hottest known star", "WR 102, 210,000C"),
        ("Coldest known star", "WISE 0855-0714, -23C"),
        ("Oldest known star", "HD 140283, 14.5B years (Methuselah star)"),
        ("First exoplanet found", "51 Pegasi b, 1995"),
        ("Most Earth-like exoplanet", "Proxima Centauri b"),
        ("TRAPPIST-1 system", "7 Earth-sized planets, 3 in habitable zone"),
        ("Kepler mission", "Confirmed 2,600+ exoplanets"),
        ("Hubble Space Telescope", "Launched 1990, still operating"),
        ("James Webb Space Telescope", "Launched 2021, infrared observatory"),
        ("ISS", "420 km altitude, 28,000 km/h"),
        ("Apollo program", "12 people walked on Moon 1969-1972"),
        ("Mars rovers", "Sojourner, Spirit, Opportunity, Curiosity, Perseverance"),
        ("Voyager 1", "Launched 1977, entered interstellar space 2012"),
        ("New Horizons", "Pluto flyby 2015"),
        ("Cassini", "Saturn orbiter 2004-2017"),
        ("Comet", "Icy body, tail when near Sun"),
        ("Asteroid", "Rocky body, mostly in asteroid belt"),
        ("Meteor", "Shooting star when entering atmosphere"),
        ("Meteorite", "Meteor that reaches ground"),
        ("Solar eclipse", "Moon blocks Sun"),
        ("Lunar eclipse", "Earth blocks Sun from Moon"),
        ("Tides", "Caused by Moon's gravity"),
        ("Aurora", "Solar particles interacting with magnetic field"),
        ("Van Allen belts", "Radiation zones around Earth"),
        ("Oort Cloud", "Spherical shell of icy objects, edge of solar system"),
        ("Kuiper Belt", "Region beyond Neptune with dwarf planets"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_psychology_fact():
    facts = [
        ("Confirmation bias", "We favor information that confirms our beliefs"),
        ("Dunning-Kruger effect", "Incompetent people overestimate their ability"),
        ("Cognitive dissonance", "Discomfort from contradictory beliefs"),
        ("Bystander effect", "Less likely to help when others are present"),
        ("Halo effect", "One positive trait influences perception"),
        ("Placebo effect", "Belief in treatment can cause real effects"),
        ("Nocebo effect", "Negative expectations cause negative effects"),
        ("Baader-Meinhof phenomenon", "Notice something after learning about it"),
        ("Sunk cost fallacy", "Continue because of past investment"),
        ("Anchoring bias", "Rely too much on first information"),
        ("Availability heuristic", "Overestimate likelihood of vivid events"),
        ("Self-serving bias", "Attribute success to self, failure to others"),
        ("Fundamental attribution error", "Overestimate personality, underestimate situation"),
        ("False consensus effect", "Overestimate how much others agree"),
        ("Spotlight effect", "Overestimate how much others notice us"),
        ("Mere exposure effect", "Familiar things are preferred"),
        ("Serial position effect", "Remember first and last items best"),
        ("Zeigarnik effect", "Remember unfinished tasks better"),
        ("Pygmalion effect", "Higher expectations lead to better performance"),
        ("Hawthorne effect", "Behavior changes when being observed"),
        ("Overconfidence effect", "We think we are better than average"),
        ("Optimism bias", "Underestimate personal risk"),
        ("Negativity bias", "Pay more attention to negative events"),
        ("Peak-end rule", "Judge experience by peak and end"),
        ("Framing effect", "Decisions affected by how options are presented"),
        ("Reactance", "Desire to restore freedom when restricted"),
        ("Social loafing", "Less effort in group than alone"),
        ("Groupthink", "Desire for harmony overrides realistic appraisal"),
        ("Deindividuation", "Loss of self-awareness in groups"),
        ("Stanford prison experiment", "Roles influence behavior dramatically"),
        ("Milgram experiment", "People obey authority even to harm others"),
        ("Little Albert experiment", "Classical conditioning of fear"),
        ("Pavlov's dogs", "Conditioned reflex learning"),
        ("Maslow's hierarchy", "Needs pyramid: physiological to self-actualization"),
        ("Freud's id/ego/superego", "Personality structure model"),
        ("Jung's archetypes", "Universal patterns in collective unconscious"),
        ("Skinner's operant conditioning", "Behavior shaped by reinforcement"),
        ("Bandura's social learning", "Learning by observing others"),
        ("Piaget's stages", "Cognitive development stages in children"),
        ("Vygotsky's ZPD", "Zone of proximal development"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_technology_fact():
    facts = [
        ("First computer", "ENIAC, 1945, 30 tons"),
        ("First microprocessor", "Intel 4004, 1971"),
        ("First hard drive", "IBM 350, 5MB, 1956"),
        ("First email", "Sent by Ray Tomlinson, 1971"),
        ("First website", "Created by Tim Berners-Lee, 1991"),
        ("First smartphone", "IBM Simon, 1994"),
        ("First search engine", "Archie, 1990"),
        ("First social network", "SixDegrees, 1997"),
        ("First video uploaded to YouTube", "Me at the zoo, 2005"),
        ("First tweet", "By Jack Dorsey, 2006"),
        ("First iPhone", "2007, no app store initially"),
        ("First Android phone", "HTC Dream, 2008"),
        ("First commercial flight", "1914, St. Petersburg-Tampa"),
        ("First airplane", "Wright Flyer, 1903"),
        ("First car", "Benz Patent Motorwagen, 1886"),
        ("First photograph", "1826 by Joseph Nicophore Niepce"),
        ("First motion picture", "Roundhay Garden Scene, 1888"),
        ("First telephone call", "Alexander Graham Bell, 1876"),
        ("First radio transmission", "Guglielmo Marconi, 1895"),
        ("First television", "Philo Farnsworth, 1927"),
        ("First transistor", "Bell Labs, 1947"),
        ("First integrated circuit", "Jack Kilby, 1958"),
        ("First video game", "Pong, 1972"),
        ("First 3D printer", "Chuck Hull, 1984"),
        ("First digital camera", "Kodak, 1975, 0.01 MP"),
        ("First GPS satellite", "1978"),
        ("First nuclear reactor", "Chicago Pile-1, 1942"),
        ("First MRI scan", "1977"),
        ("First artificial heart", "Jarvik-7, 1982"),
        ("First cloned mammal", "Dolly the sheep, 1996"),
        ("First robot", "Unimate, 1961"),
        ("First AI program", "Logic Theorist, 1956"),
        ("First chatbot", "ELIZA, 1966 by Joseph Weizenbaum"),
        ("First computer virus", "Creeper, 1971"),
        ("First worm", "Morris worm, 1988"),
        ("First domain name", "symbolics.com, 1985"),
        ("First Bitcoin transaction", "2009, 10 BTC for pizza"),
        ("First electric battery", "Voltaic pile, 1800"),
        ("First light bulb", "Edison, 1879 (carbon filament)"),
        ("First laser", "Theodore Maiman, 1960"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_geology_fact():
    facts = [
        ("Earth's core", "~5,700C, solid inner, liquid outer"),
        ("Earth's mantle", "2,900 km thick, convective rock"),
        ("Earth's crust", "5-70 km thick, thin compared to other layers"),
        ("Continental drift", "Pangea broke apart ~200M years ago"),
        ("Plate tectonics", "7 major plates moving ~2-15 cm/year"),
        ("Earthquakes", "~500,000 per year, 100,000 felt"),
        ("Volcanoes", "~1,500 active on land, many more underwater"),
        ("Rock cycle", "Igneous, sedimentary, metamorphic in continuous cycle"),
        ("Igneous rock", "Formed from cooled magma: granite, basalt"),
        ("Sedimentary rock", "Formed from compressed sediment: limestone, sandstone"),
        ("Metamorphic rock", "Changed by heat and pressure: marble, slate"),
        ("Fossil fuels", "Coal, oil, natural gas from ancient organic matter"),
        ("Carbon cycle", "Carbon moves between atmosphere, oceans, life, rocks"),
        ("Water cycle", "Evaporation, condensation, precipitation, collection"),
        ("Groundwater", "~30% of fresh water is underground"),
        ("Glaciers", "~10% of land, 69% of fresh water"),
        ("Ice ages", "Multiple glacial periods, last one 11,700 years ago"),
        ("Greenhouse effect", "Gases trap heat, essential for life"),
        ("Ozone layer", "Stratospheric ozone absorbs UV radiation"),
        ("Magnetosphere", "Earth's magnetic field protects from solar wind"),
        ("Aurora borealis", "Northern lights caused by solar particles"),
        ("El Nino", "Warming of Pacific Ocean, affects global weather"),
        ("La Nina", "Cooling of Pacific Ocean, opposite of El Nino"),
        ("Tsunami", "Caused by underwater earthquake or volcanic eruption"),
        ("Hurricane", "Tropical storm with winds >119 km/h"),
        ("Tornado", "Violent rotating column of air"),
        ("Monsoon", "Seasonal wind reversal bringing heavy rain"),
        ("Desertification", "Land degradation in dry areas"),
        ("Soil erosion", "Loss of topsoil by wind and water"),
        ("Mineral", "Naturally occurring inorganic solid with crystal structure"),
        ("Gemstone", "Rare, beautiful mineral: diamond, ruby, emerald"),
        ("Quartz", "Most abundant mineral on Earth's surface"),
        ("Feldspar", "~60% of Earth's crust"),
        ("Calcite", "Main component of limestone and marble"),
        ("Pyrite", "Fool's gold, iron sulfide"),
        ("Magnetite", "Naturally magnetic iron oxide"),
        ("Bauxite", "Main ore of aluminum"),
        ("Hematite", "Main ore of iron"),
        ("Coal formation", "Swamp plants -> peat -> lignite -> bituminous -> anthracite"),
        ("Oil formation", "Plankton -> kerogen -> oil and gas over millions of years"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_sports_fact():
    facts = [
        ("Olympics origin", "776 BC in Olympia, Greece"),
        ("Modern Olympics", "First held 1896 in Athens"),
        ("World Cup first", "1930 in Uruguay, won by Uruguay"),
        ("Most World Cup wins", "Brazil, 5 titles"),
        ("Most Olympic golds individual", "Michael Phelps, 23 golds"),
        ("Fastest 100m sprint", "Usain Bolt, 9.58s"),
        ("Fastest marathon", "Kelvin Kiptum, 2:00:35"),
        ("Highest paid athlete", "Cristiano Ronaldo, ~$260M/year"),
        ("Largest sports stadium", "Narendra Modi Stadium, 132,000"),
        ("Most popular sport", "Soccer, 3.5B fans"),
        ("Basketball inventor", "James Naismith, 1891"),
        ("Volleyball inventor", "William Morgan, 1895"),
        ("Baseball origin", "1839 by Abner Doubleday (disputed)"),
        ("Tennis origin", "1873 by Walter Wingfield"),
        ("Golf origin", "15th century Scotland"),
        ("Boxing history", "Ancient Greece, modern rules 1867"),
        ("Martial arts origin", "Various ancient Asian traditions"),
        ("Karate", "Okinawa, Japan"),
        ("Taekwondo", "Korea, 1950s"),
        ("Judo", "Japan, 1882 by Jigoro Kano"),
        ("Sumo", "Ancient Japanese tradition"),
        ("Wrestling", "One of oldest sports"),
        ("Fencing", "Modern form 19th century"),
        ("Swimming", "Olympic sport since 1896"),
        ("Track and field", "Core Olympic sports"),
        ("Cricket origin", "16th century England"),
        ("Rugby origin", "1823 Rugby School, England"),
        ("Ice hockey", "Canada, 1875"),
        ("Figure skating", "Olympic since 1908"),
        ("Skiing", "Ancient Nordic tradition"),
        ("Snowboarding", "1965 by Sherman Poppen"),
        ("Surfing", "Ancient Polynesian"),
        ("Skateboarding", "1950s California"),
        ("Formula 1", "First championship 1950"),
        ("NBA founded", "1946 as BAA"),
        ("NFL founded", "1920 as APFA"),
        ("First Super Bowl", "1967, Green Bay Packers won"),
        ("World Series", "First 1903"),
        ("Grand Slam tennis", "Australian, French, Wimbledon, US Open"),
        ("Tour de France", "First 1903"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_music_fact():
    facts = [
        ("Oldest known song", "Hurrian Hymn No. 6, ~1400 BC"),
        ("First recorded music", "Edison phonograph, 1877"),
        ("First commercial recording", "1901, Berliner Gramophone"),
        ("Most streamed artist", "Drake, >80B streams"),
        ("Best-selling album", "Thriller by Michael Jackson, 70M"),
        ("Best-selling single", "White Christmas by Bing Crosby, 50M"),
        ("Grammy first", "1959 ceremony"),
        ("Rock and roll origin", "1950s USA from blues and gospel"),
        ("Jazz origin", "Early 20th century New Orleans"),
        ("Blues origin", "Late 19th century American South"),
        ("Hip hop origin", "1970s Bronx, New York"),
        ("Electronic music", "20th century with synthesizers"),
        ("Classical period", "1750-1820: Mozart, Haydn, Beethoven"),
        ("Baroque period", "1600-1750: Bach, Vivaldi, Handel"),
        ("Romantic period", "1820-1900: Chopin, Tchaikovsky, Brahms"),
        ("Modern classical", "1900-present: Stravinsky, Schoenberg"),
        ("First electric guitar", "1931 by Rickenbacker"),
        ("First synthesizer", "Moog modular, 1964"),
        ("Beatles", "Best-selling band, ~600M records"),
        ("Queen", "Bohemian Rhapsody iconic"),
        ("Pink Floyd", "Dark Side of the Moon sold 45M"),
        ("Led Zeppelin", "Rock icons, sold 300M records"),
        ("The Rolling Stones", "Formed 1962, still touring"),
        ("Madonna", "Best-selling female artist, 300M records"),
        ("Elvis Presley", "King of Rock and Roll, 500M records"),
        ("Frank Sinatra", "Iconic crooner, 150M records"),
        ("Bob Marley", "Reggae legend, 75M records"),
        ("Aretha Franklin", "Queen of Soul"),
        ("Prince", "Innovative musician, Purple Rain iconic"),
        ("David Bowie", "Musical chameleon, Starman"),
        ("Nirvana", "Grunge icons, Nevermind 1991"),
        ("Radiohead", "Alternative rock innovators"),
        ("Wu-Tang Clan", "Hip hop collective from Staten Island"),
        ("Tupac", "Influential rapper, 75M records"),
        ("The Notorious BIG", "East Coast hip hop legend"),
        ("Eminem", "Best-selling rapper, 220M records"),
        ("Taylor Swift", "Most awarded female artist"),
        ("Beyonce", "Cultural icon, 200M records"),
        ("Kanye West", "Influential producer and rapper"),
        ("Adele", "Multiple Grammy winner, soul voice"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_art_fact():
    facts = [
        ("Mona Lisa", "Da Vinci, 1503, Louvre, 77x53 cm"),
        ("The Last Supper", "Da Vinci, 1498, Milan"),
        ("Starry Night", "Van Gogh, 1889, MOMA"),
        ("The Scream", "Munch, 1893, Oslo"),
        ("Guernica", "Picasso, 1937, Madrid"),
        ("The Persistence of Memory", "Dali, 1931, melting clocks"),
        ("The Birth of Venus", "Botticelli, 1485, Florence"),
        ("School of Athens", "Raphael, 1511, Vatican"),
        ("Girl with a Pearl Earring", "Vermeer, 1665"),
        ("American Gothic", "Wood, 1930, Chicago"),
        ("The Thinker", "Rodin, 1880, sculpture"),
        ("David", "Michelangelo, 1504, Florence"),
        ("The Pieta", "Michelangelo, 1499, Vatican"),
        ("Sistine Chapel ceiling", "Michelangelo, 1512"),
        ("The Creation of Adam", "Michelangelo, Sistine Chapel"),
        ("Las Meninas", "Velazquez, 1656"),
        ("The Night Watch", "Rembrandt, 1642"),
        ("The Hay Wain", "Constable, 1821"),
        ("Water Lilies series", "Monet, ~250 paintings"),
        ("Impression Sunrise", "Monet, 1872, gave Impressionism its name"),
        ("The Kiss", "Klimt, 1908"),
        ("The Great Wave off Kanagawa", "Hokusai, 1831"),
        ("Cave paintings", "Lascaux, ~17,000 years old"),
        ("Cubism", "Picasso and Braque, 1907"),
        ("Surrealism", "Dali and Magritte, 1920s"),
        ("Abstract Expressionism", "Pollock, Rothko, 1940s"),
        ("Pop Art", "Warhol, Lichtenstein, 1950s"),
        ("Impressionism", "Monet, Renoir, Degas, 1870s"),
        ("Renaissance art", "14th-17th century rebirth of classical"),
        ("Baroque art", "17th century dramatic, ornate style"),
        ("Rococo art", "18th century decorative, playful"),
        ("Neoclassicism", "Late 18th century classical revival"),
        ("Romanticism", "19th century emotion and nature"),
        ("Art Nouveau", "1890-1910 organic, flowing lines"),
        ("Art Deco", "1920-1930 geometric, luxury"),
        ("Bauhaus", "1919-1933 functional design school"),
        ("Photography invented", "1830s by Daguerre and Talbot"),
        ("First film", "Lumiere brothers, 1895"),
        ("Street art", "Banksy, Basquiat"),
        ("Digital art", "Computer-generated, NFTs since 2014"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_medicine_fact():
    facts = [
        ("First vaccine", "Smallpox by Edward Jenner, 1796"),
        ("Penicillin discovered", "Alexander Fleming, 1928"),
        ("Insulin discovered", "Frederick Banting, 1921"),
        ("DNA structure discovered", "Watson and Crick, 1953"),
        ("First heart transplant", "Christiaan Barnard, 1967"),
        ("First kidney transplant", "Joseph Murray, 1954"),
        ("First liver transplant", "Thomas Starzl, 1963"),
        ("First lung transplant", "James Hardy, 1963"),
        ("First successful hand transplant", "1998"),
        ("First face transplant", "Isabelle Dinoire, 2005"),
        ("MRI invented", "Paul Lauterbur, 1973"),
        ("CT scan invented", "Godfrey Hounsfield, 1971"),
        ("Ultrasound in medicine", "Since 1950s"),
        ("X-ray discovered", "Wilhelm Rontgen, 1895"),
        ("ECG invented", "Willem Einthoven, 1903"),
        ("Stethoscope invented", "Rene Laennec, 1816"),
        ("Thermometer in medicine", "Santorio, 1612"),
        ("Blood types discovered", "Karl Landsteiner, 1901"),
        ("ABO blood system", "1900 by Karl Landsteiner"),
        ("Anesthesia first used", "Ether, 1846"),
        ("First antibiotic", "Penicillin, 1928"),
        ("Antiseptic surgery", "Joseph Lister, 1867"),
        ("Germ theory of disease", "Louis Pasteur, 1860s"),
        ("Hygiene and sanitation", "Semmelweis, 1847 handwashing"),
        ("First blood transfusion", "Jean-Baptiste Denys, 1667"),
        ("First successful blood transfusion", "1907"),
        ("Chemotherapy developed", "1940s"),
        ("First cancer treatment", "Radiation therapy, 1896"),
        ("Polio vaccine", "Jonas Salk, 1955"),
        ("Measles vaccine", "1963"),
        ("MMR vaccine", "1971"),
        ("COVID-19 vaccines", "mRNA technology, 2020"),
        ("Human genome sequenced", "2003, 13-year project"),
        ("CRISPR gene therapy", "First approved 2023"),
        ("First baby from IVF", "Louise Brown, 1978"),
        ("First cloned mammal", "Dolly the sheep, 1996"),
        ("First artificial heart", "Jarvik-7, 1982"),
        ("First cochlear implant", "1972"),
        ("First pacemaker", "1958"),
        ("First defibrillator", "1947"),
        ("Aspirin discovered", "Felix Hoffmann, 1897"),
        ("Morphine isolated", "1804 by Friedrich Serturner"),
        ("Quinine for malaria", "Cinchona bark, 17th century"),
        ("Vaccination", "Jenner coined term from vacca = cow"),
        ("World average life expectancy", "73 years in 2024"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_economics_fact():
    facts = [
        ("First coins", "Lydia (Turkey), ~600 BC"),
        ("First paper money", "China, 7th century AD"),
        ("First bank", "Bank of Venice, 1157"),
        ("First central bank", "Swedish Riksbank, 1668"),
        ("First stock exchange", "Amsterdam, 1602"),
        ("Wall Street origin", "1792 Buttonwood Agreement"),
        ("IPO first", "Dutch East India Company, 1602"),
        ("First credit card", "Diners Club, 1950"),
        ("First ATM", "London, 1967 by Barclays"),
        ("Bitcoin created", "2008 by Satoshi Nakamoto"),
        ("GDP concept", "Simon Kuznets, 1934"),
        ("Inflation", "Germany 1923: 29,500% monthly"),
        ("Hyperinflation worst", "Hungary 1946: 41.9 quadrillion % monthly"),
        ("Great Depression", "1929-1939, 25% unemployment"),
        ("2008 financial crisis", "Subprime mortgage collapse"),
        ("Recession definition", "2 consecutive quarters GDP decline"),
        ("Supply and demand", "Core economic principle"),
        ("Invisible hand", "Adam Smith, 1776"),
        ("Keynesian economics", "Government intervention to stabilize"),
        ("Monetarism", "Milton Friedman, money supply focus"),
        ("Trickle-down economics", "Benefits for rich flow to poor"),
        ("Minimum wage", "New Zealand 1894, first"),
        ("Progressive tax", "Higher income, higher rate"),
        ("Regressive tax", "Lower effective rate for higher income"),
        ("VAT introduced", "France 1954"),
        ("Gold standard", "Abandoned by US 1971"),
        ("Bretton Woods", "1944 fixed exchange rate system"),
        ("WTO founded", "1995"),
        ("IMF founded", "1944"),
        ("World Bank founded", "1944"),
        ("European Union", "1993 Maastricht Treaty"),
        ("Euro introduced", "1999 electronic, 2002 physical"),
        ("OPEC founded", "1960"),
        ("First modern corporation", "Dutch East India Company"),
        ("Largest company ever", "Saudi Aramco, $2.4T IPO"),
        ("Billionaire boom", "Most billionaires in US and China"),
        ("Universal basic income", "Pilot programs in Finland, Kenya"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_literature_fact():
    facts = [
        ("Epic of Gilgamesh", "~2100 BC, oldest known literature"),
        ("Iliad and Odyssey", "Homer, ~800 BC"),
        ("Mahabharata", "~400 BC, longest epic poem"),
        ("1001 Nights", "Arabic tales, compiled ~800 AD"),
        ("The Tale of Genji", "Murasaki Shikibu, 1008, first novel"),
        ("Divine Comedy", "Dante, 1320"),
        ("Canterbury Tales", "Chaucer, 1400"),
        ("Don Quixote", "Cervantes, 1605, first modern novel"),
        ("Pride and Prejudice", "Jane Austen, 1813"),
        ("Frankenstein", "Mary Shelley, 1818, early sci-fi"),
        ("Moby Dick", "Melville, 1851"),
        ("Les Miserables", "Hugo, 1862"),
        ("War and Peace", "Tolstoy, 1869"),
        ("Crime and Punishment", "Dostoevsky, 1866"),
        ("The Adventures of Huckleberry Finn", "Twain, 1884"),
        ("Ulysses", "Joyce, 1922, modernist masterpiece"),
        ("The Great Gatsby", "Fitzgerald, 1925"),
        ("One Hundred Years of Solitude", "Garcia Marquez, 1967"),
        ("1984", "George Orwell, 1949"),
        ("To Kill a Mockingbird", "Harper Lee, 1960"),
        ("Catch-22", "Joseph Heller, 1961"),
        ("The Lord of the Rings", "Tolkien, 1954-1955"),
        ("Harry Potter", "Rowling, 1997-2007, 500M copies"),
        ("The Little Prince", "Saint-Exupery, 1943"),
        ("The Alchemist", "Paulo Coelho, 1988"),
        ("Shakespeare wrote", "37 plays, 154 sonnets"),
        ("Most translated book", "The Bible, 3,400 languages"),
        ("Most translated single author", "Agatha Christie"),
        ("Best-selling fiction series", "Harry Potter, 500M"),
        ("Best-selling single book", "Don Quixote, 500M"),
        ("Nobel Prize in Literature", "First 1901, Sully Prudhomme"),
        ("Pulitzer Prize for Fiction", "First 1918"),
        ("Booker Prize", "First 1969"),
        ("Poetry origin", "Oral tradition, predates writing"),
        ("Haiku format", "5-7-5 syllables, Japanese"),
        ("Dystopian fiction", "Rise in 20th century"),
        ("Science fiction", "Verne, Wells, Asimov, Clarke"),
        ("Fantasy genre", "Tolkien defined modern fantasy"),
        ("Stream of consciousness", "Joyce, Woolf, Faulkner"),
        ("Beat generation", "Ginsberg, Kerouac, Burroughs 1950s"),
        ("Postmodern literature", "Pynchon, DeLillo, Wallace"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_movie():
    movies = [
        ("The Shawshank Redemption", "1994", "Frank Darabont", "Prison drama, 9.3 IMDB"),
        ("The Godfather", "1972", "Francis Ford Coppola", "Mafia epic, 9.2 IMDB"),
        ("The Dark Knight", "2008", "Christopher Nolan", "Batman, 9.0 IMDB"),
        ("Schindler's List", "1993", "Steven Spielberg", "Holocaust drama"),
        ("Pulp Fiction", "1994", "Quentin Tarantino", "Nonlinear crime"),
        ("The Lord of the Rings", "2001-2003", "Peter Jackson", "Fantasy trilogy"),
        ("Forrest Gump", "1994", "Robert Zemeckis", "Historical drama"),
        ("Inception", "2010", "Christopher Nolan", "Dream heist"),
        ("Fight Club", "1999", "David Fincher", "Psychological thriller"),
        ("The Matrix", "1999", "Wachowskis", "Sci-fi action"),
        ("Goodfellas", "1990", "Martin Scorsese", "Mobster classic"),
        ("Seven", "1995", "David Fincher", "Serial killer thriller"),
        ("The Silence of the Lambs", "1991", "Jonathan Demme", "Hannibal Lecter"),
        ("Saving Private Ryan", "1998", "Steven Spielberg", "WWII drama"),
        ("Interstellar", "2014", "Christopher Nolan", "Space exploration"),
        ("Parasite", "2019", "Bong Joon-ho", "Social thriller"),
        ("The Social Network", "2010", "David Fincher", "Facebook origin"),
        ("Gladiator", "2000", "Ridley Scott", "Roman epic"),
        ("The Departed", "2006", "Martin Scorsese", "Undercover crime"),
        ("Whiplash", "2014", "Damien Chazelle", "Jazz drummer"),
        ("La La Land", "2016", "Damien Chazelle", "Musical romance"),
        ("Joker", "2019", "Todd Phillips", "Psychological origin"),
        ("Avengers: Endgame", "2019", "Russo Brothers", "Superhero epic"),
        ("Titanic", "1997", "James Cameron", "Romance disaster"),
        ("Jurassic Park", "1993", "Steven Spielberg", "Dinosaur sci-fi"),
        ("Star Wars", "1977", "George Lucas", "Space opera"),
        ("E.T.", "1982", "Steven Spielberg", "Alien friendship"),
        ("Back to the Future", "1985", "Robert Zemeckis", "Time travel"),
        ("The Shining", "1980", "Stanley Kubrick", "Horror classic"),
        ("2001: A Space Odyssey", "1968", "Stanley Kubrick", "Sci-fi epic"),
        ("Alien", "1979", "Ridley Scott", "Sci-fi horror"),
        ("Blade Runner", "1982", "Ridley Scott", "Cyberpunk noir"),
        ("Casablanca", "1942", "Michael Curtiz", "War romance"),
        ("Citizen Kane", "1941", "Orson Welles", "Newspaper drama"),
        ("Psycho", "1960", "Alfred Hitchcock", "Horror thriller"),
        ("Rear Window", "1954", "Alfred Hitchcock", "Suspense"),
        ("Vertigo", "1958", "Alfred Hitchcock", "Psychological thriller"),
        ("Taxi Driver", "1976", "Martin Scorsese", "Psychological drama"),
        ("Apocalypse Now", "1979", "Francis Ford Coppola", "Vietnam war"),
        ("The Godfather Part II", "1974", "Coppola", "Mafia saga"),
    ]
    name, year, director, desc = random.choice(movies)
    return "{} ({}) by {} - {}".format(name, year, director, desc)

def random_song():
    songs = [
        ("Bohemian Rhapsody", "Queen", "1975", "Rock opera masterpiece"),
        ("Imagine", "John Lennon", "1971", "Peace anthem"),
        ("Stairway to Heaven", "Led Zeppelin", "1971", "Epic rock song"),
        ("Like a Rolling Stone", "Bob Dylan", "1965", "Folk rock revolution"),
        ("Smells Like Teen Spirit", "Nirvana", "1991", "Grunge anthem"),
        ("Respect", "Aretha Franklin", "1967", "Soul classic"),
        ("What's Going On", "Marvin Gaye", "1971", "Social commentary"),
        ("Billie Jean", "Michael Jackson", "1983", "Pop perfection"),
        ("Hotel California", "Eagles", "1977", "Iconic rock"),
        ("Sweet Child O' Mine", "Guns N' Roses", "1987", "Hard rock ballad"),
        ("Yesterday", "The Beatles", "1965", "Most covered song"),
        ("Hey Jude", "The Beatles", "1968", "Epic singalong"),
        ("Purple Haze", "Jimi Hendrix", "1967", "Psychedelic rock"),
        ("Satisfaction", "The Rolling Stones", "1965", "Riff classic"),
        ("Born to Run", "Bruce Springsteen", "1975", "Heartland rock"),
        ("London Calling", "The Clash", "1979", "Punk classic"),
        ("One", "U2", "1991", "Alternative rock"),
        ("Losing My Religion", "R.E.M.", "1991", "Alternative anthem"),
        ("Creep", "Radiohead", "1992", "Alternative masterpiece"),
        ("Wonderwall", "Oasis", "1995", "Britpop anthem"),
        ("Smells Like Victory", "Survivor", "1982", "Sports anthem"),
        ("Thriller", "Michael Jackson", "1982", "Pop culture phenomenon"),
        ("Dancing Queen", "ABBA", "1976", "Disco classic"),
        ("I Will Always Love You", "Whitney Houston", "1992", "Power ballad"),
        ("My Heart Will Go On", "Celine Dion", "1997", "Movie theme"),
        ("Someone Like You", "Adele", "2011", "Emotional ballad"),
        ("Rolling in the Deep", "Adele", "2010", "Soul pop"),
        ("Uptown Funk", "Bruno Mars", "2014", "Funk revival"),
        ("Shape of You", "Ed Sheeran", "2017", "Pop hit"),
        ("Bad Guy", "Billie Eilish", "2019", "Indie pop"),
        ("Blinding Lights", "The Weeknd", "2019", "Synthwave pop"),
        ("Old Town Road", "Lil Nas X", "2019", "Country trap"),
        ("Bohemian Rhapsody", "Queen", "1975", "Operatic rock"),
        ("Hallelujah", "Leonard Cohen", "1984", "Spiritual classic"),
        ("Bridge Over Troubled Water", "Simon & Garfunkel", "1970", "Folk ballad"),
        ("Let It Be", "The Beatles", "1970", "Comforting classic"),
        ("No Woman No Cry", "Bob Marley", "1974", "Reggae classic"),
        ("Redemption Song", "Bob Marley", "1980", "Freedom anthem"),
        ("Superstition", "Stevie Wonder", "1972", "Funk soul"),
        ("Let's Stay Together", "Al Green", "1971", "Soul ballad"),
    ]
    name, artist, year, desc = random.choice(songs)
    return "{} by {} ({}) - {}".format(name, artist, year, desc)

def random_book():
    books = [
        ("To Kill a Mockingbird", "Harper Lee", "1960", "Racial injustice in South"),
        ("1984", "George Orwell", "1949", "Totalitarian dystopia"),
        ("Pride and Prejudice", "Jane Austen", "1813", "Romance and class"),
        ("The Great Gatsby", "F. Scott Fitzgerald", "1925", "Jazz age tragedy"),
        ("Moby Dick", "Herman Melville", "1851", "Whaling obsession"),
        ("War and Peace", "Leo Tolstoy", "1869", "Napoleonic Russia"),
        ("Crime and Punishment", "Fyodor Dostoevsky", "1866", "Guilt and redemption"),
        ("The Catcher in the Rye", "J.D. Salinger", "1951", "Teen alienation"),
        ("Lord of the Flies", "William Golding", "1954", "Civilization vs savagery"),
        ("Brave New World", "Aldous Huxley", "1932", "Hedonistic dystopia"),
        ("Fahrenheit 451", "Ray Bradbury", "1953", "Censorship"),
        ("Slaughterhouse-Five", "Kurt Vonnegut", "1969", "War surrealism"),
        ("One Hundred Years of Solitude", "Gabriel Garcia Marquez", "1967", "Magical realism"),
        ("The Hobbit", "J.R.R. Tolkien", "1937", "Fantasy adventure"),
        ("Dune", "Frank Herbert", "1965", "Sci-fi epic"),
        ("Foundation", "Isaac Asimov", "1951", "Galactic empire"),
        ("Neuromancer", "William Gibson", "1984", "Cyberpunk origin"),
        ("The Handmaid's Tale", "Margaret Atwood", "1985", "Feminist dystopia"),
        ("Beloved", "Toni Morrison", "1987", "Slavery legacy"),
        ("The Road", "Cormac McCarthy", "2006", "Post-apocalyptic"),
        ("Gone Girl", "Gillian Flynn", "2012", "Psychological thriller"),
        ("The Da Vinci Code", "Dan Brown", "2003", "Religious thriller"),
        ("Harry Potter", "J.K. Rowling", "1997", "Wizard fantasy"),
        ("The Alchemist", "Paulo Coelho", "1988", "Journey and destiny"),
        ("Life of Pi", "Yann Martel", "2001", "Survival story"),
        ("The Kite Runner", "Khaled Hosseini", "2003", "Afghanistan drama"),
        ("The Book Thief", "Markus Zusak", "2005", "Nazi Germany"),
        ("The Hunger Games", "Suzanne Collins", "2008", "Dystopian arena"),
        ("The Martian", "Andy Weir", "2011", "Mars survival"),
        ("Ready Player One", "Ernest Cline", "2011", "VR treasure hunt"),
    ]
    name, author, year, desc = random.choice(books)
    return "{} by {} ({}) - {}".format(name, author, year, desc)

def random_cocktail():
    drinks = [
        ("Margarita", "Tequila, lime, triple sec, salt rim"),
        ("Martini", "Gin, vermouth, olive or twist"),
        ("Old Fashioned", "Bourbon, sugar, bitters, orange peel"),
        ("Mojito", "Rum, lime, mint, sugar, soda"),
        ("Piña Colada", "Rum, coconut cream, pineapple"),
        ("Daiquiri", "Rum, lime, sugar"),
        ("Whiskey Sour", "Whiskey, lemon, sugar, egg white"),
        ("Manhattan", "Rye, vermouth, bitters, cherry"),
        ("Negroni", "Gin, Campari, vermouth"),
        ("Cosmopolitan", "Vodka, cranberry, lime, triple sec"),
        ("Mai Tai", "Rum, orgeat, lime, orange liqueur"),
        ("Bloody Mary", "Vodka, tomato juice, spices"),
        ("Moscow Mule", "Vodka, ginger beer, lime"),
        ("Espresso Martini", "Vodka, coffee liqueur, espresso"),
        ("French 75", "Gin, champagne, lemon, sugar"),
        ("Sidecar", "Cognac, lemon, triple sec"),
        ("Mint Julep", "Bourbon, mint, sugar, crushed ice"),
        ("Paloma", "Tequila, grapefruit soda, lime"),
        ("Aperol Spritz", "Aperol, prosecco, soda"),
        ("Tom Collins", "Gin, lemon, sugar, soda"),
        ("Gin and Tonic", "Gin, tonic, lime"),
        ("Rum and Coke", "Rum, cola, lime"),
        ("Vodka Soda", "Vodka, soda water, lime"),
        ("Screwdriver", "Vodka, orange juice"),
        ("White Russian", "Vodka, coffee liqueur, cream"),
        ("Long Island Iced Tea", "Multiple liquors, cola, lemon"),
        ("Mimosa", "Champagne, orange juice"),
        ("Bellini", "Prosecco, peach puree"),
        ("Sangria", "Red wine, fruit, brandy"),
        ("Hot Toddy", "Whiskey, honey, lemon, hot water"),
        ("Irish Coffee", "Coffee, whiskey, cream, sugar"),
        ("Eggnog", "Milk, eggs, sugar, rum or bourbon"),
    ]
    name, recipe = random.choice(drinks)
    return "{}: {}".format(name, recipe)

def random_board_game():
    games = [
        ("Chess", "2 players", "~1500 years", "Strategy, 64 squares"),
        ("Go", "2 players", "~2500 years", "Territory capture, 19x19"),
        ("Monopoly", "2-8 players", "1935", "Real estate trading"),
        ("Scrabble", "2-4 players", "1938", "Word game"),
        ("Risk", "2-6 players", "1957", "World conquest"),
        ("Clue", "3-6 players", "1949", "Murder mystery"),
        ("Checkers", "2 players", "~3000 years", "Diagonal jumps"),
        ("Backgammon", "2 players", "~5000 years", "Race and strategy"),
        ("Settlers of Catan", "3-4 players", "1995", "Resource trading"),
        ("Ticket to Ride", "2-5 players", "2004", "Train route building"),
        ("Pandemic", "2-4 players", "2008", "Cooperative disease fighting"),
        ("Carcassonne", "2-5 players", "2000", "Tile placement"),
        ("Dominion", "2-4 players", "2008", "Deck building"),
        ("Twilight Struggle", "2 players", "2005", "Cold War"),
        ("Axis and Allies", "2-5 players", "1981", "WWII strategy"),
        ("Dungeons and Dragons", "3-6 players", "1974", "Fantasy RPG"),
        ("Magic: The Gathering", "2+ players", "1993", "Trading card game"),
        ("Uno", "2-10 players", "1971", "Card shedding"),
        ("Jenga", "1+ players", "1983", "Block stacking"),
        ("Connect Four", "2 players", "1974", "Four in a row"),
        ("Battleship", "2 players", "1931", "Naval guessing"),
        ("Trivial Pursuit", "2-6 players", "1981", "Trivia game"),
        ("Pictionary", "3+ players", "1985", "Drawing game"),
        ("Charades", "4+ players", "Ancient", "Acting game"),
        ("Codenames", "4+ players", "2015", "Word association"),
        ("Azul", "2-4 players", "2017", "Tile drafting"),
        ("Wingspan", "1-5 players", "2019", "Bird collection"),
        ("Terraforming Mars", "1-5 players", "2016", "Space strategy"),
        ("Scythe", "1-5 players", "2016", "Alt-history strategy"),
        ("Gloomhaven", "1-4 players", "2017", "Cooperative dungeon crawl"),
        ("7 Wonders", "2-7 players", "2010", "Civilization card game"),
        ("Splendor", "2-4 players", "2014", "Gem collection"),
        ("Brass: Birmingham", "2-4 players", "2018", "Industrial strategy"),
        ("Coup", "2-6 players", "2012", "Bluffing and deduction"),
        ("The Resistance", "5-10 players", "2009", "Social deduction"),
        ("Avalon", "5-10 players", "2010", "Social deduction"),
        ("Secret Hitler", "5-10 players", "2016", "Social deduction"),
        ("Werewolf", "8+ players", "1986", "Social deduction"),
        ("Exploding Kittens", "2-5 players", "2015", "Card game humor"),
        ("Cards Against Humanity", "4+ players", "2011", "Party humor"),
    ]
    name, players, year, desc = random.choice(games)
    return "{}: {} players, {} - {}".format(name, players, year, desc)

def random_videogame():
    games = [
        ("Super Mario Bros", "Nintendo", "1985", "Platformer icon"),
        ("The Legend of Zelda", "Nintendo", "1986", "Action adventure"),
        ("Tetris", "Alexey Pajitnov", "1984", "Puzzle classic"),
        ("Doom", "id Software", "1993", "FPS pioneer"),
        ("Final Fantasy VII", "Square", "1997", "JRPG masterpiece"),
        ("Half-Life 2", "Valve", "2004", "Sci-fi FPS"),
        ("Portal", "Valve", "2007", "Puzzle FPS"),
        ("The Witcher 3", "CD Projekt", "2015", "Open world RPG"),
        ("Red Dead Redemption 2", "Rockstar", "2018", "Western epic"),
        ("Grand Theft Auto V", "Rockstar", "2013", "Open world crime"),
        ("Minecraft", "Mojang", "2011", "Sandbox builder"),
        ("Fortnite", "Epic Games", "2017", "Battle royale"),
        ("World of Warcraft", "Blizzard", "2004", "MMORPG legend"),
        ("Dark Souls", "FromSoftware", "2011", "Action RPG hard"),
        ("Elden Ring", "FromSoftware", "2022", "Open world souls"),
        ("The Last of Us", "Naughty Dog", "2013", "Post-apocalyptic"),
        ("Uncharted 4", "Naughty Dog", "2016", "Adventure thriller"),
        ("God of War", "Santa Monica", "2018", "Norse mythology"),
        ("Spider-Man", "Insomniac", "2018", "Superhero open world"),
        ("Horizon Zero Dawn", "Guerrilla", "2017", "Robot dinosaurs"),
        ("The Elder Scrolls V", "Bethesda", "2011", "Open world fantasy"),
        ("Fallout 4", "Bethesda", "2015", "Post-apocalyptic RPG"),
        ("Cyberpunk 2077", "CD Projekt", "2020", "Open world sci-fi"),
        ("Baldur's Gate 3", "Larian", "2023", "CRPG masterpiece"),
        ("Mass Effect 2", "BioWare", "2010", "Space opera RPG"),
        ("Dragon Age Inquisition", "BioWare", "2014", "Fantasy RPG"),
        ("The Legend of Zelda Breath of the Wild", "Nintendo", "2017", "Open world"),
        ("Super Mario Odyssey", "Nintendo", "2017", "3D platformer"),
        ("Metroid Prime", "Retro Studios", "2002", "FPS adventure"),
        ("Halo 3", "Bungie", "2007", "Sci-fi FPS"),
        ("Gears of War", "Epic Games", "2006", "Cover shooter"),
        ("BioShock", "Irrational", "2007", "Underwater city"),
        ("System Shock 2", "Irrational", "1999", "Sci-fi horror"),
        ("Deus Ex", "Ion Storm", "2000", "Cyberpunk RPG"),
        ("Metal Gear Solid", "Konami", "1998", "Stealth action"),
        ("Resident Evil 4", "Capcom", "2005", "Survival horror"),
        ("Silent Hill 2", "Konami", "2001", "Psychological horror"),
        ("Street Fighter II", "Capcom", "1991", "Fighting game"),
        ("Tekken 3", "Bandai Namco", "1997", "3D fighter"),
        ("Super Smash Bros Ultimate", "Nintendo", "2018", "Crossover fighter"),
        ("Mario Kart 8", "Nintendo", "2014", "Kart racing"),
        ("Gran Turismo 3", "Polyphony", "2001", "Sim racing"),
        ("Civilization VI", "Firaxis", "2016", "Turn-based strategy"),
        ("StarCraft II", "Blizzard", "2010", "RTS"),
        ("Age of Empires II", "Ensemble", "1999", "Historical RTS"),
        ("Command and Conquer", "Westwood", "1995", "RTS legend"),
        ("SimCity 2000", "Maxis", "1993", "City builder"),
        ("The Sims 4", "Maxis", "2014", "Life simulation"),
        ("Animal Crossing", "Nintendo", "2020", "Life sim"),
        ("Stardew Valley", "ConcernedApe", "2016", "Farming sim"),
    ]
    name, developer, year, desc = random.choice(games)
    return "{} by {} ({}) - {}".format(name, developer, year, desc)

def random_tv_show():
    shows = [
        ("Breaking Bad", "2008-2013", "AMC", "Meth cooking drama"),
        ("Game of Thrones", "2011-2019", "HBO", "Fantasy epic"),
        ("The Office", "2005-2013", "NBC", "Mockumentary comedy"),
        ("Friends", "1994-2004", "NBC", "Sitcom classic"),
        ("Seinfeld", "1989-1998", "NBC", "Show about nothing"),
        ("Stranger Things", "2016-", "Netflix", "Sci-fi horror"),
        ("The Crown", "2016-", "Netflix", "Royal drama"),
        ("The Mandalorian", "2019-", "Disney+", "Star Wars bounty hunter"),
        ("Band of Brothers", "2001", "HBO", "WWII mini-series"),
        ("Chernobyl", "2019", "HBO", "Nuclear disaster drama"),
        ("Planet Earth", "2006", "BBC", "Nature documentary"),
        ("Black Mirror", "2011-", "Netflix", "Tech dystopia anthology"),
        ("The Simpsons", "1989-", "Fox", "Animated sitcom"),
        ("South Park", "1997-", "Comedy Central", "Animated satire"),
        ("Rick and Morty", "2013-", "Adult Swim", "Sci-fi animation"),
        ("The Wire", "2002-2008", "HBO", "Baltimore crime drama"),
        ("Sopranos", "1999-2007", "HBO", "Mobster drama"),
        ("Mad Men", "2007-2015", "AMC", "Advertising in 1960s"),
        ("Better Call Saul", "2015-2022", "AMC", "Breaking Bad prequel"),
        ("True Detective", "2014-", "HBO", "Anthology crime"),
        ("Fargo", "2014-", "FX", "Anthology crime"),
        ("Westworld", "2016-2022", "HBO", "AI western"),
        ("The Walking Dead", "2010-2022", "AMC", "Zombie survival"),
        ("Doctor Who", "1963-", "BBC", "Time travel sci-fi"),
        ("Sherlock", "2010-2017", "BBC", "Modern Holmes"),
        ("Peaky Blinders", "2013-2022", "BBC", "1920s gangster"),
        ("Downton Abbey", "2010-2015", "ITV", "British aristocratic"),
        ("The Americans", "2013-2018", "FX", "Cold War spies"),
        ("Narcos", "2015-2017", "Netflix", "Drug cartel drama"),
        ("Money Heist", "2017-2021", "Netflix", "Spanish heist"),
        ("Squid Game", "2021-", "Netflix", "Survival game"),
        ("Succession", "2018-2023", "HBO", "Media family power"),
        ("The Bear", "2022-", "Hulu", "Restaurant drama"),
        ("Ted Lasso", "2020-2023", "Apple+", "Soccer comedy"),
        ("Stranger Things", "2016-", "Netflix", "80s nostalgia"),
        ("Lost", "2004-2010", "ABC", "Island mystery"),
        ("Twin Peaks", "1990-1991", "ABC", "Surreal mystery"),
        ("The X-Files", "1993-2002", "Fox", "Paranormal FBI"),
        ("Buffy the Vampire Slayer", "1997-2003", "WB", "Supernatural drama"),
        ("Firefly", "2002", "Fox", "Space western"),
    ]
    name, years, network, desc = random.choice(shows)
    return "{} ({}): {} - {}".format(name, years, network, desc)

def random_space_mission():
    missions = [
        ("Sputnik 1", "1957", "Soviet Union", "First artificial satellite"),
        ("Apollo 11", "1969", "USA", "First Moon landing"),
        ("Voyager 1", "1977", "USA", "Interstellar space probe"),
        ("Voyager 2", "1977", "USA", "Only probe at Uranus/Neptune"),
        ("Hubble Space Telescope", "1990", "NASA/ESA", "Revolutionary space observatory"),
        ("International Space Station", "1998", "International", "Orbiting lab"),
        ("Mars Pathfinder", "1997", "NASA", "First Mars rover Sojourner"),
        ("Cassini-Huygens", "1997", "NASA/ESA", "Saturn system explorer"),
        ("Curiosity Rover", "2012", "NASA", "Mars science laboratory"),
        ("New Horizons", "2015", "NASA", "Pluto flyby"),
        ("James Webb Space Telescope", "2021", "NASA/ESA/CSA", "Infrared space telescope"),
        ("Artemis 1", "2022", "NASA", "Uncrewed Moon mission"),
        ("Perseverance Rover", "2021", "NASA", "Mars sample caching"),
        ("Ingenuity", "2021", "NASA", "First powered flight on Mars"),
        ("James Webb", "2021", "NASA", "Deep space imaging"),
        ("DART", "2022", "NASA", "Asteroid deflection test"),
        ("JUICE", "2023", "ESA", "Jupiter icy moons explorer"),
        ("Europa Clipper", "2024", "NASA", "Europa ocean exploration"),
        ("Chang'e 4", "2019", "China", "First landing on Moon far side"),
        ("Chang'e 5", "2020", "China", "Moon sample return"),
        ("Tianwen-1", "2021", "China", "Mars orbiter and rover"),
        ("Chandrayaan-3", "2023", "India", "First landing at Moon south pole"),
        ("Hayabusa2", "2018", "Japan", "Asteroid sample return"),
        ("BepiColombo", "2018", "ESA/JAXA", "Mercury orbiter"),
        ("Solar Orbiter", "2020", "ESA/NASA", "Sun close observation"),
        ("Parker Solar Probe", "2018", "NASA", "Touching the Sun"),
        ("Lunar Reconnaissance Orbiter", "2009", "NASA", "Moon mapping"),
        ("Mars Express", "2003", "ESA", "Mars orbiter"),
        ("Venus Express", "2005", "ESA", "Venus atmosphere study"),
        ("MESSENGER", "2011", "NASA", "First Mercury orbiter"),
        ("Dawn", "2011", "NASA", "Vesta and Ceres exploration"),
        ("Rosetta", "2014", "ESA", "Comet 67P rendezvous"),
        ("Stardust", "2004", "NASA", "Comet sample return"),
        ("Genesis", "2004", "NASA", "Solar wind sample return"),
        ("Luna 2", "1959", "Soviet Union", "First hit Moon surface"),
        ("Venera 7", "1970", "Soviet Union", "First landing on Venus"),
        ("Mars 3", "1971", "Soviet Union", "First Mars landing"),
        ("Pioneer 10", "1972", "NASA", "First Jupiter flyby"),
        ("Skylab", "1973", "NASA", "First US space station"),
        ("Mir", "1986", "Soviet Union", "Long-duration space station"),
    ]
    name, year, agency, desc = random.choice(missions)
    return "{} ({}): {} - {}".format(name, year, agency, desc)

def random_country_fact():
    facts = [
        ("Japan", "Over 6,800 islands"),
        ("Canada", "Largest coastline at 202,080 km"),
        ("Russia", "11 time zones"),
        ("Indonesia", "17,508 islands"),
        ("Brazil", "Covers 4 time zones"),
        ("Australia", "Home to 10,000 beaches"),
        ("India", "Over 1.4 billion people"),
        ("China", "World's longest wall (Great Wall)"),
        ("USA", "50 states, 3.8M square miles"),
        ("Chile", "Longest country N-S at 4,270 km"),
        ("Norway", "1,190 fjords"),
        ("New Zealand", "First country with universal suffrage 1893"),
        ("Switzerland", "4 national languages"),
        ("Belgium", "3 official languages"),
        ("South Africa", "11 official languages"),
        ("Papua New Guinea", "Over 800 languages"),
        ("Vatican City", "Smallest country at 0.44 km\u00b2"),
        ("Monaco", "Most densely populated"),
        ("Mongolia", "Least densely populated country"),
        ("Kazakhstan", "Largest landlocked country"),
        ("Maldives", "Lowest country, avg 1.5m above sea"),
        ("Nepal", "Contains 8 of 14 highest peaks"),
        ("Greece", "Over 6,000 islands, 227 inhabited"),
        ("Italy", "Most UNESCO World Heritage sites"),
        ("France", "Most visited country at 90M/year"),
        ("Spain", "Spanish is spoken in 20+ countries"),
        ("Portugal", "Oldest borders in Europe (1139)"),
        ("Ireland", "No snakes due to ice age isolation"),
        ("Iceland", "No standing army"),
        ("Finland", "181,888 lakes"),
        ("Sweden", "Over 267,570 islands"),
        ("Denmark", "Home to Legoland"),
        ("Poland", "First country to adopt written constitution in Europe 1791"),
        ("Ukraine", "Largest country in Europe"),
        ("Egypt", "99% population lives on 5% of land"),
        ("Kenya", "Great Rift Valley runs through it"),
        ("Nigeria", "Most populous in Africa at 220M"),
        ("Ethiopia", "Only African country never colonized"),
        ("Morocco", "Holds the Sahara's longest coastline"),
        ("Thailand", "Never colonized by Europeans"),
        ("Vietnam", "Over 3,000 km of coastline"),
        ("South Korea", "World's fastest internet speeds"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_language_fact():
    facts = [
        ("Mandarin Chinese", "Most native speakers, 920M"),
        ("Spanish", "Second most native, 475M speakers"),
        ("English", "Most total speakers, 1.5B"),
        ("Hindi", "350M native speakers"),
        ("Arabic", "310M native speakers, 28+ dialects"),
        ("Bengali", "230M native speakers"),
        ("Portuguese", "220M native speakers"),
        ("Russian", "155M native speakers"),
        ("Japanese", "125M native speakers"),
        ("French", "80M native, 320M total speakers"),
        ("German", "95M native speakers"),
        ("Korean", "77M speakers worldwide"),
        ("Italian", "67M speakers"),
        ("Turkish", "80M speakers"),
        ("Vietnamese", "85M speakers"),
        ("Tamil", "78M speakers"),
        ("Telugu", "82M speakers"),
        ("Marathi", "83M speakers"),
        ("Urdu", "70M speakers"),
        ("Persian", "70M speakers"),
        ("Polish", "45M speakers"),
        ("Dutch", "24M speakers"),
        ("Greek", "13M speakers"),
        ("Czech", "10M speakers"),
        ("Swedish", "10M speakers"),
        ("Hungarian", "13M speakers"),
        ("Romanian", "24M speakers"),
        ("Thai", "60M speakers"),
        ("Burmese", "33M speakers"),
        ("Malay", "80M speakers"),
        ("Swahili", "50M speakers, lingua franca E Africa"),
        ("Zulu", "12M speakers"),
        ("Amharic", "32M speakers"),
        ("Quechua", "8M speakers (Andes)"),
        ("Nahuatl", "1.7M speakers (Mexico)"),
        ("Maori", "150,000 speakers, New Zealand"),
        ("Hawaiian", "24,000 native speakers"),
        ("Esperanto", "2M speakers worldwide (constructed)"),
        ("Sign language", "70M deaf people use various sign languages"),
        ("Piraha", "Tribe in Brazil, no numbers or colors"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_food_fact():
    facts = [
        ("Pizza", "Italy, Margherita named after Queen 1889"),
        ("Sushi", "Japan, originated as fermented fish preservation"),
        ("Pasta", "Italy, 350+ shapes"),
        ("Chocolate", "Aztecs and Mayans, from cacao beans"),
        ("Coffee", "Ethiopia, discovered by goat herder legend"),
        ("Tea", "China, discovered ~2700 BC"),
        ("Bread", "Staple food for 30,000 years"),
        ("Cheese", "~4,000 varieties worldwide"),
        ("Wine", "Georgia 8000 years ago"),
        ("Beer", "Mesopotamia ~5,000 years ago"),
        ("Whiskey", "Scotland and Ireland, from malted barley"),
        ("Vodka", "Russia and Poland, from grains or potatoes"),
        ("Hamburger", "USA, Hamburg steak origin in Germany"),
        ("Hot dog", "USA, German frankfurter origin"),
        ("Tacos", "Mexico, pre-Columbian origin"),
        ("Curry", "Indian subcontinent, spice blend"),
        ("Sushi", "Japan, vinegared rice with seafood"),
        ("Ramen", "Japan, Chinese noodle soup origin"),
        ("Paella", "Spain, Valencia rice dish"),
        ("Kimchi", "Korea, fermented vegetables"),
        ("Pho", "Vietnam, noodle soup"),
        ("Satay", "Indonesia, grilled skewers with peanut sauce"),
        ("Croissant", "France, Austrian kipfel origin"),
        ("Baguette", "France, long bread loaf"),
        ("Schnitzel", "Austria, breaded fried meat"),
        ("Fondue", "Switzerland, melted cheese"),
        ("Tapas", "Spain, small savory dishes"),
        ("Dim sum", "China, small bite-sized portions"),
        ("Pad Thai", "Thailand, stir-fried noodles"),
        ("Miso soup", "Japan, fermented soybean paste"),
        ("Poutine", "Canada, fries with cheese curds and gravy"),
        ("Fish and chips", "UK, battered fish with fries"),
        ("BBQ", "USA, slow-cooked meat over smoke"),
        ("Tap water", "Japan has best tap water quality"),
        ("Most expensive spice", "Saffron, $10,000/kg"),
        ("Most consumed meat", "Pork globally"),
        ("Most calories per gram", "Fat, 9 cal/g"),
        ("Most eaten fruit", "Tomatoes by botanical definition"),
        ("World's hottest pepper", "Carolina Reaper, 2.2M SHU"),
        ("Largest food market", "France exports $75B wine annually"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_animal_fact_deep():
    facts = [
        ("Octopus", "3 hearts, blue blood, can change color instantly"),
        ("Mantis shrimp", "16 color receptors vs human 3, can punch like a bullet"),
        ("Platypus", "Venomous spurs on males, lays eggs, mammal"),
        ("Tardigrade", "Survives space vacuum, boiling, freezing, radiation"),
        ("Axolotl", "Neotenic salamander, regenerates limbs and spinal cord"),
        ("Peregrine falcon", "Fastest animal at 389 km/h dive"),
        ("Blue whale", "Largest animal ever, heart size of a car"),
        ("Hummingbird", "Wings beat 80 times per second"),
        ("Arctic fox", "Fur changes color white in winter, brown in summer"),
        ("Chameleon", "Changes color for communication, not camouflage"),
        ("Cuttlefish", "3 hearts, green-blue blood, instant camouflage"),
        ("Electric eel", "Produces 600V electric shock"),
        ("Box jellyfish", "Most venomous animal, 60 tentacles"),
        ("Honey badger", "Fearless, thick loose skin, fights large predators"),
        ("Naked mole rat", "Feels no pain, cancer-resistant, lives 30+ years"),
        ("Dolphin", "Uses echolocation, sleeps with half brain awake"),
        ("Bat", "Only flying mammal, uses echolocation"),
        ("Elephant", "Largest land animal, amazing memory"),
        ("Giraffe", "Tallest animal, 6 ft neck vertebrae"),
        ("Cheetah", "Fastest land animal, 120 km/h for short bursts"),
        ("Wolf", "Complex social pack structure"),
        ("Orca", "Apex predator, hunts in coordinated pods"),
        ("Honeybee", "Communicates with waggle dance"),
        ("Ant", "Carries 50x own weight"),
        ("Pistol shrimp", "Snaps claw to create cavitation bubble at 4,400C"),
        ("Sea horse", "Male gives birth"),
        ("Kiwi bird", "Lays largest egg relative to body size"),
        ("Emperor penguin", "Survives -60C winters in Antarctica"),
        ("Snow leopard", "Can leap 15m, lives at 6,000m altitude"),
        ("Komodo dragon", "Venomous bite, largest lizard at 3m"),
        ("Crocodile", "Survived dinosaurs, 3rd eyelid for underwater"),
        ("Frog", "Absorbs water through skin, some toxic"),
        ("Butterfly", "Tastes with feet, 12,000 species"),
        ("Firefly", "Bioluminescence for mating signals"),
        ("Anglerfish", "Deep sea, bioluminescent lure on head"),
        ("Fennec fox", "Smallest fox, large ears for heat regulation"),
        ("Capybara", "Largest rodent, semi-aquatic, friend of all animals"),
        ("Sloth", "Slowest mammal, algae grows on fur for camouflage"),
        ("Red panda", "Not closely related to giant panda"),
        ("Okapi", "Forest giraffe, striped legs like zebra"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_ocean_fact():
    facts = [
        ("Pacific Ocean", "165M km\u00b2, deepest ocean"),
        ("Atlantic Ocean", "106M km\u00b2, second largest"),
        ("Indian Ocean", "70M km\u00b2, warmest ocean"),
        ("Southern Ocean", "21M km\u00b2, around Antarctica"),
        ("Arctic Ocean", "14M km\u00b2, smallest, covered by ice"),
        ("Mariana Trench", "Deepest point at 11,034m"),
        ("Challenger Deep", "Deepest part of Mariana Trench"),
        ("Great Barrier Reef", "Largest ecosystem at 344,000 km\u00b2"),
        ("Mid-Atlantic Ridge", "Longest mountain range underwater"),
        ("Gulf Stream", "Warm current affecting Europe's climate"),
        ("El Nino", "Pacific warming every 2-7 years"),
        ("La Nina", "Pacific cooling, opposite of El Nino"),
        ("Ocean acidification", "CO2 absorption lowers pH"),
        ("Ocean currents", "Drive global heat distribution"),
        ("Coral bleaching", "Rising temperature kills coral"),
        ("Plastic pollution", "8M tons enter oceans annually"),
        ("Deep sea", "Below 200m, no light, high pressure"),
        ("Hydrothermal vents", "Deep sea, 400C water, unique life"),
        ("Oceanic crust", "Thinner and denser than continental"),
        ("Seafloor spreading", "New crust forms at mid-ocean ridges"),
        ("Tsunami waves", "Can travel 800 km/h in deep ocean"),
        ("Tides", "Caused by Moon and Sun gravity"),
        ("Wave energy", "Renewable energy from ocean waves"),
        ("Tidal energy", "Electricity from tidal movement"),
        ("Phytoplankton", "Produce 50% of Earth's oxygen"),
        ("Kelp forests", "Underwater ecosystems, carbon sequestration"),
        ("Posidonia oceanica", "Seagrass producing oxygen"),
        ("Marine protected areas", "8% of oceans protected"),
        ("Ocean warming", "90% of global warming goes to oceans"),
        ("Sea level rise", "3.7 mm/year on average rising"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_moon_fact():
    facts = [
        ("Moon diameter", "3,475 km, quarter of Earth"),
        ("Distance from Earth", "384,400 km average"),
        ("Moon gravity", "1/6 of Earth's gravity"),
        ("Moon origin", "Giant impact theory: Theia collision"),
        ("Moon phases", "29.5 days cycle"),
        ("Synchronous rotation", "Same side always faces Earth"),
        ("Dark side", "Not dark, just always faces away"),
        ("First landing", "Apollo 11, July 20, 1969"),
        ("Last human on Moon", "Apollo 17, December 1972"),
        ("Moonwalkers", "12 people have walked on the Moon"),
        ("Lunar maria", "Dark plains from ancient lava flows"),
        ("Moon craters", "Hundreds of thousands visible"),
        ("Tycho crater", "85 km, 108M years old"),
        ("Copernicus crater", "93 km, 800M years old"),
        ("South Pole-Aitken Basin", "Largest crater in solar system"),
        ("Moon quarantine", "Apollo astronauts quarantined on return"),
        ("Moon rocks", "842 lbs brought back by Apollo"),
        ("Moonquakes", "Weak moonquakes occur regularly"),
        ("No atmosphere", "Temperature ranges from -173C to 127C"),
        ("Moon dust", "Sharp, electrostatically charged, abrasive"),
        ("Blue Moon", "Second full moon in a calendar month"),
        ("Supermoon", "Full moon at closest approach to Earth"),
        ("Blood Moon", "Total lunar eclipse red color"),
        ("Harvest Moon", "Full moon closest to autumnal equinox"),
        ("Moon in culture", "Calendars, mythology, werewolves, poetry"),
        ("Moon conspiracy", "Moon hoax theory, debunked"),
        ("China's Chang'e program", "Landing on far side, 2019"),
        ("India's Chandrayaan", "First south pole landing, 2023"),
        ("Artemis program", "NASA plans to return humans by 2025"),
        ("Lunar Gateway", "Proposed Moon-orbiting space station"),
        ("Moon base", "Plans by NASA, ESA, China for permanent base"),
        ("Lunar resources", "Helium-3, water ice at poles"),
        ("Moon and tides", "Primary cause of Earth's ocean tides"),
        ("Moon formation", "Formed ~4.5B years ago"),
        ("Moon shrinking", "Moon has shrunk by ~50m in radius"),
        ("Moon's far side", "No direct radio contact possible"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_weather_fact():
    facts = [
        ("Lightning", "Strikes 100 times per second globally"),
        ("Thunder", "Sound of air expanding rapidly from lightning heat"),
        ("Rainbow", "Sunlight refracts through water droplets at 42 degrees"),
        ("Hurricane", "Tropical cyclone, winds >119 km/h"),
        ("Tornado", "Violent rotating column, up to 500 km/h"),
        ("Blizzard", "Snowstorm with winds >56 km/h, visibility <400m"),
        ("Drought", "Extended period of below-average rainfall"),
        ("Flood", "Overflow of water onto normally dry land"),
        ("Heat wave", "Prolonged period of excessive heat"),
        ("Cold wave", "Prolonged period of extreme cold"),
        ("Monsoon", "Seasonal wind reversal, heavy rainfall"),
        ("El Nino", "Warming of Pacific, disrupted weather"),
        ("La Nina", "Cooling of Pacific, opposite effects"),
        ("Cloud types", "Cirrus, Cumulus, Stratus, Nimbus"),
        ("Cirrus clouds", "High-altitude, thin, wispy, ice crystals"),
        ("Cumulus clouds", "Fluffy white, fair weather"),
        ("Stratus clouds", "Low, gray, blanket-like, drizzle"),
        ("Cumulonimbus", "Thunderstorm clouds, tall and dark"),
        ("Fog", "Cloud touching ground, <1 km visibility"),
        ("Hail", "Layered ice from strong thunderstorms"),
        ("Dew point", "Temperature at which air is saturated"),
        ("Humidity", "Water vapor content in the air"),
        ("Barometric pressure", "Weight of atmosphere at a point"),
        ("Wind chill", "Perceived temperature due to wind cooling"),
        ("Heat index", "Perceived temperature including humidity"),
        ("Jet stream", "Fast air currents, affect weather patterns"),
        ("Coriolis effect", "Deflection of moving air due to Earth rotation"),
        ("Greenhouse effect", "Gases trap heat, warming planet"),
        ("Urban heat island", "Cities warmer than surrounding areas"),
        ("Rain shadow", "Dry area on leeward side of mountains"),
        ("Microclimate", "Localized climate different from region"),
        ("Weather vs climate", "Weather = short term, climate = long term"),
        ("Polar vortex", "Cold air mass at poles, can expand south"),
        ("Atmospheric river", "Narrow band of concentrated moisture"),
        ("Downburst", "Strong downward wind from thunderstorm"),
        ("Dust devil", "Small, rotating column of dust"),
        ("Water spout", "Tornado over water"),
        ("Fire whirl", "Tornado-like vortex of flame and ash"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_invention():
    inventions = [
        ("Wheel", "~3500 BC, Mesopotamia", "Transportation"),
        ("Printing press", "~1440, Gutenberg", "Mass communication"),
        ("Steam engine", "1712, Thomas Newcomen", "Industrial Revolution"),
        ("Electricity", "1752, Franklin (discovery)", "Modern life"),
        ("Telegraph", "1837, Morse", "Long-distance communication"),
        ("Telephone", "1876, Alexander Bell", "Voice communication"),
        ("Light bulb", "1879, Thomas Edison", "Indoor lighting"),
        ("Radio", "1895, Marconi", "Wireless communication"),
        ("Airplane", "1903, Wright brothers", "Flight"),
        ("Penicillin", "1928, Alexander Fleming", "First antibiotic"),
        ("Television", "1927, Farnsworth", "Visual media"),
        ("Transistor", "1947, Bell Labs", "Modern electronics"),
        ("Integrated circuit", "1958, Jack Kilby", "Computer chips"),
        ("Laser", "1960, Theodore Maiman", "Precision technology"),
        ("Internet", "1969, ARPANET", "Global network"),
        ("Email", "1971, Ray Tomlinson", "Digital mail"),
        ("Microprocessor", "1971, Intel", "Computers for all"),
        ("Cell phone", "1973, Martin Cooper", "Mobile communication"),
        ("GPS", "1973, US DoD", "Global positioning"),
        ("PC", "1975, Altair 8800", "Personal computing"),
        ("World Wide Web", "1989, Tim Berners-Lee", "Information sharing"),
        ("Digital camera", "1975, Kodak", "Digital photography"),
        ("DNA fingerprinting", "1984, Alec Jeffreys", "Forensics"),
        ("CRISPR", "2012, Doudna/Charpentier", "Gene editing"),
        ("Artificial heart", "1982, Jarvik", "Medical implant"),
        ("MRI", "1977, Damadian", "Medical imaging"),
        ("CT scanner", "1971, Hounsfield", "3D X-ray imaging"),
        ("Ultrasound", "1956, Donald", "Prenatal imaging"),
        ("Pacemaker", "1958, Elmqvist", "Heart regulation"),
        ("Vaccination", "1796, Edward Jenner", "Disease prevention"),
        ("Anesthesia", "1846, Morton", "Painless surgery"),
        ("X-ray", "1895, Rontgen", "Internal imaging"),
        ("Aspirin", "1897, Hoffmann", "Pain relief"),
        ("Insulin", "1921, Banting", "Diabetes treatment"),
        ("Life support", "1950s", "Critical care"),
        ("Solar panel", "1954, Bell Labs", "Renewable energy"),
        ("Nuclear reactor", "1942, Fermi", "Nuclear power"),
        ("Wind turbine", "1887, Blyth", "Wind power"),
        ("Battery", "1800, Volta", "Portable power"),
        ("LED", "1962, Holonyak", "Efficient lighting"),
    ]
    name, year, impact = random.choice(inventions)
    return "{} ({}): {}".format(name, year, impact)

def random_quote():
    quotes = [
        "Be the change you wish to see in the world. - Mahatma Gandhi",
        "Imagination is more important than knowledge. - Albert Einstein",
        "The only way to do great work is to love what you do. - Steve Jobs",
        "In the middle of difficulty lies opportunity. - Albert Einstein",
        "The unexamined life is not worth living. - Socrates",
        "Cogito ergo sum. (I think, therefore I am) - Descartes",
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "The journey of a thousand miles begins with a single step. - Lao Tzu",
        "That which does not kill us makes us stronger. - Nietzsche",
        "I think, therefore I am. - Rene Descartes",
        "Simplicity is the ultimate sophistication. - Leonardo da Vinci",
        "Genius is one percent inspiration and ninety-nine percent perspiration. - Thomas Edison",
        "The important thing is not to stop questioning. - Albert Einstein",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The purpose of our lives is to be happy. - Dalai Lama",
        "Get busy living or get busy dying. - Stephen King",
        "You miss 100% of the shots you don't take. - Wayne Gretzky",
        "The best time to plant a tree was 20 years ago. The second best time is now. - Chinese proverb",
        "Knowledge is power. - Francis Bacon",
        "To be or not to be, that is the question. - Shakespeare",
        "All that glitters is not gold. - Shakespeare",
        "The only thing we have to fear is fear itself. - FDR",
        "Ask not what your country can do for you, ask what you can do for your country. - JFK",
        "I have a dream. - MLK",
        "The arc of the moral universe is long, but it bends toward justice. - MLK",
        "The only true wisdom is in knowing you know nothing. - Socrates",
        "Eureka! - Archimedes",
        "Give me a lever long enough and a fulcrum and I shall move the world. - Archimedes",
        "Nothing in excess. - Greek proverb",
        "Know thyself. - Socrates (inscribed at Delphi)",
        "Science is organized knowledge. - Herbert Spencer",
        "The good life is one inspired by love and guided by knowledge. - Bertrand Russell",
        "We are what we repeatedly do. Excellence, then, is not an act, but a habit. - Aristotle",
        "Happiness depends upon ourselves. - Aristotle",
        "Liberty consists in doing what one desires. - John Stuart Mill",
        "One person with a belief is equal to a force of 99 who have only interests. - J.S. Mill",
        "The only purpose for which power can be rightfully exercised over any member of a civilized community, against his will, is to prevent harm to others. - J.S. Mill",
        "If you want to find the secrets of the universe, think in terms of energy, frequency and vibration. - Nikola Tesla",
        "The present is theirs, but the future, for which I really worked, is mine. - Nikola Tesla",
        "Science without religion is lame, religion without science is blind. - Albert Einstein",
    ]
    return random.choice(quotes)

def random_holiday():
    holidays = [
        ("New Year's Day", "January 1", "Global celebration"),
        ("Chinese New Year", "Jan-Feb", "Lunar new year celebration"),
        ("Valentine's Day", "February 14", "Love and romance"),
        ("St. Patrick's Day", "March 17", "Irish heritage"),
        ("Easter", "March-April", "Christian resurrection"),
        ("April Fools' Day", "April 1", "Pranks and jokes"),
        ("Earth Day", "April 22", "Environmental awareness"),
        ("Labah Day", "May 1", "Workers' rights"),
        ("Mother's Day", "May (2nd Sunday)", "Honoring mothers"),
        ("Memorial Day", "May (last Monday)", "US war dead"),
        ("Dragon Boat Festival", "June (5th day 5th month)", "Chinese tradition"),
        ("Father's Day", "June (3rd Sunday)", "Honoring fathers"),
        ("Independence Day USA", "July 4", "American independence"),
        ("Bastille Day", "July 14", "French revolution"),
        ("Diwali", "Oct-Nov", "Hindu festival of lights"),
        ("Halloween", "October 31", "Costumes and candy"),
        ("Day of the Dead", "Nov 1-2", "Mexican remembrance"),
        ("Thanksgiving", "Nov (4th Thursday)", "US harvest holiday"),
        ("Hanukkah", "Nov-Dec", "Jewish festival of lights"),
        ("Christmas", "December 25", "Christian birth of Jesus"),
        ("Kwanzaa", "Dec 26-Jan 1", "African heritage"),
        ("New Year's Eve", "December 31", "Year-end celebration"),
        ("Ramadan", "9th month Islamic calendar", "Month of fasting"),
        ("Eid al-Fitr", "End of Ramadan", "Breaking the fast"),
        ("Eid al-Adha", "Feast of Sacrifice", "Abraham's devotion"),
        ("Vesak", "May full moon", "Buddha birth and enlightenment"),
        ("Holi", "March", "Hindu festival of colors"),
        ("Songkran", "April 13-15", "Thai New Year water festival"),
        ("Oktoberfest", "Sept-Oct", "German beer festival"),
        ("Carnival", "Feb-March", "Pre-Lent celebration"),
        ("Mardi Gras", "Fat Tuesday", "Last day before Lent"),
        ("Lent", "40 days before Easter", "Christian fasting period"),
        ("Passover", "March-April", "Jewish exodus from Egypt"),
        ("Rosh Hashanah", "Sept-Oct", "Jewish New Year"),
        ("Yom Kippur", "Sept-Oct", "Day of Atonement"),
        ("International Women's Day", "March 8", "Women's rights"),
        ("World Health Day", "April 7", "Global health awareness"),
        ("World Environment Day", "June 5", "Environmental action"),
        ("Human Rights Day", "December 10", "Universal rights"),
        ("International Day of Peace", "September 21", "Global peace"),
    ]
    name, date, desc = random.choice(holidays)
    return "{}: {} - {}".format(name, date, desc)

def random_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "What is a computer's favorite snack? Microchips!",
        "Why did the developer go broke? Because he used up all his cache.",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
        "Why was the JavaScript developer sad? Because he didn't know how to un-null his life.",
        "A SQL query walks into a bar, walks up to two tables and asks: Can I join you?",
        "There are only 10 kinds of people in the world: those who understand binary and those who don't.",
        "Why did the Python developer get stuck in the shower? Because the directions said lather, rinse, repeat.",
        "What do you call a fake noodle? An impasta.",
        "Why don't scientists trust atoms? Because they make up everything.",
        "Why did the scarecrow win an award? Because he was outstanding in his field.",
        "What do you call a fish with no eyes? A fsh.",
        "How do you organize a space party? You planet.",
        "What do you call a bear with no teeth? A gummy bear.",
        "Why did the bicycle fall over? Because it was two-tired.",
        "How do you make holy water? You boil the hell out of it.",
        "What do you call someone who speaks three languages? Trilingual. Two languages? Bilingual. One language? American.",
        "Why don't skeletons fight each other? They don't have the guts.",
        "What do you get when you cross a snowman and a vampire? Frostbite.",
        "Why did the math book look so sad? Because it had too many problems.",
        "What do you call a singing laptop? A Dell.",
        "Why did the computer go to the doctor? Because it had a virus.",
        "What's the best thing about Switzerland? I don't know, but the flag is a big plus.",
        "How does a penguin build its house? Igloos it together.",
        "Why did the golfer wear two pairs of pants? In case he got a hole in one.",
        "What do you call a factory that sells generally OK products? A satisfactory.",
        "How do you catch a squirrel? Climb a tree and act like a nut.",
        "Why did the coffee file a police report? It got mugged.",
        "What's orange and sounds like a parrot? A carrot.",
        "How do you keep a bagel from getting away? Put lox on it.",
        "What do you call a lazy kangaroo? A pouch potato.",
        "Why did the banana go to the doctor? Because it wasn't peeling well.",
        "What do you call a snowman with a six-pack? An abdominal snowman.",
        "Why did the picture go to jail? Because it was framed.",
        "What's the best time to go to the dentist? Tooth-hurty.",
        "Why don't eggs tell jokes? They'd crack up.",
        "What do you call a dog that can do magic? A labracadabrador.",
        "Why did the strawberry cry? Because its mother was in a jam.",
        "What do you call a pig that does karate? A pork chop.",
        "How do you make a tissue dance? Put a little boogie in it.",
        "Why did the scarecrow win an award? He was outstanding.",
        "What's brown and sticky? A stick.",
        "Why can't you give Elsa a balloon? Because she will let it go.",
        "How much does Santa pay for parking? Nothing, it's on the house.",
        "Why did the chicken cross the road? To get to the other side.",
        "What do you call a dinosaur with an extensive vocabulary? A thesaurus.",
        "Why did the music teacher go to jail? Because she got caught with the right notes.",
        "How does a train eat? It goes chew chew.",
        "Why did the cookie go to the hospital? Because it felt crummy.",
        "What do you call an alligator in a vest? An investigator.",
    ]
    return random.choice(jokes)

def random_puzzle():
    puzzles = [
        ("What has keys but no locks?", "A piano"),
        ("What can travel around the world while staying in a corner?", "A stamp"),
        ("What gets wetter the more it dries?", "A towel"),
        ("What can fill a room but takes up no space?", "Light"),
        ("What has a head and a tail but no body?", "A coin"),
        ("What has hands but can't clap?", "A clock"),
        ("What is full of holes but still holds water?", "A sponge"),
        ("What building has the most stories?", "A library"),
        ("What can you break even if you never pick it up?", "A promise"),
        ("What goes up but never comes down?", "Your age"),
        ("What has cities but no houses, forests but no trees?", "A map"),
        ("What invention lets you look right through a wall?", "A window"),
        ("What gets sharper the more you use it?", "Your brain"),
        ("What can you hold without ever touching?", "Your breath"),
        ("What has many teeth but can't bite?", "A comb"),
        ("What has a neck but no head?", "A bottle"),
        ("What can run but never walks?", "A river"),
        ("What has one eye but can't see?", "A needle"),
        ("What can you catch but not throw?", "A cold"),
        ("What belongs to you but others use it more?", "Your name"),
        ("What has a ring but no finger?", "A phone"),
        ("What has words but never speaks?", "A book"),
        ("What can you keep after giving to someone?", "Your word"),
        ("What starts with E, ends with E, but only has one letter?", "An envelope"),
        ("What has legs but doesn't walk?", "A table"),
        ("What can travel at any speed but never leaves its spot?", "A shadow"),
        ("What is always in front of you but can't be seen?", "The future"),
        ("What comes once in a minute, twice in a moment, but never in a thousand years?", "The letter M"),
        ("What is 3 feet long but has 365 pages?", "A calendar"),
        ("What can fly without wings?", "Time"),
        ("What has branches but no fruit?", "A bank"),
        ("What has a spine but no bones?", "A book"),
        ("What has ears but can't hear?", "Corn"),
        ("What can be cracked, made, told, and played?", "A joke"),
        ("What has a bottom at the top?", "Your legs"),
        ("What tastes better than it smells?", "A tongue"),
        ("What has an eye but can't see?", "A hurricane"),
        ("What has a head, a tail, is brown, and has no legs?", "A penny"),
        ("What gets bigger the more you take away from it?", "A hole"),
        ("What can you find at the end of a rainbow?", "The letter W"),
    ]
    riddle, answer = random.choice(puzzles)
    return "Riddle: {} | Answer: {}".format(riddle, answer)

def random_ai_fact():
    facts = [
        ("Turing Test", "Alan Turing proposed in 1950"),
        ("AI term coined", "John McCarthy, 1956 Dartmouth Conference"),
        ("First AI program", "Logic Theorist, 1956 by Newell and Simon"),
        ("ELIZA chatbot", "1966 by Joseph Weizenbaum"),
        ("Deep Blue", "Beat Kasparov at chess in 1997"),
        ("Watson", "IBM AI won Jeopardy! in 2011"),
        ("Siri", "Apple's virtual assistant launched 2011"),
        ("Alexa", "Amazon's assistant launched 2014"),
        ("AlphaGo", "Beat world Go champion Lee Sedol in 2016"),
        ("GPT-1", "OpenAI released 2018, 117M parameters"),
        ("GPT-2", "OpenAI 2019, 1.5B parameters"),
        ("GPT-3", "OpenAI 2020, 175B parameters"),
        ("GPT-4", "OpenAI 2023, multimodal"),
        ("DALL-E", "OpenAI image generation from text, 2021"),
        ("Stable Diffusion", "Open source image generation, 2022"),
        ("Midjourney", "AI art generation, 2022"),
        ("Copilot", "GitHub AI code completion, 2021"),
        ("Tesla Autopilot", "Self-driving AI since 2014"),
        ("GANs", "Generative Adversarial Networks by Ian Goodfellow 2014"),
        ("Transformers", "Attention is All You Need paper 2017"),
        ("BERT", "Google's NLP model 2018"),
        ("Reinforcement Learning", "AlphaGo, DQN, PPO algorithms"),
        ("Neural Networks", "Inspired by biological neurons"),
        ("Deep Learning", "Multiple layers in neural networks"),
        ("CNN", "Convolutional Neural Networks for images"),
        ("RNN", "Recurrent Neural Networks for sequences"),
        ("LSTM", "Long Short-Term Memory networks 1997"),
        ("Transfer Learning", "Pre-trained models adapted to new tasks"),
        ("Federated Learning", "Train models across decentralized devices"),
        ("Edge AI", "AI computation on local devices"),
        ("Explainable AI", "Making AI decisions interpretable"),
        ("AI Ethics", "Fairness, accountability, transparency"),
        ("AI Safety", "Ensuring AI aligns with human values"),
        ("AGI", "Artificial General Intelligence, still theoretical"),
        ("Singularity", "Hypothetical point of superhuman AI"),
        ("Machine Learning", "Algorithms that learn from data"),
        ("Supervised Learning", "Learning from labeled data"),
        ("Unsupervised Learning", "Finding patterns in unlabeled data"),
        ("Semi-supervised Learning", "Mix of labeled and unlabeled data"),
        ("Self-supervised Learning", "Model generates its own labels"),
        ("Prompt Engineering", "Crafting inputs for desired AI outputs"),
        ("RAG", "Retrieval Augmented Generation for accuracy"),
        ("Fine-tuning", "Adapting pre-trained model to specific task"),
        ("LoRA", "Low-Rank Adaptation for efficient fine-tuning"),
        ("Quantization", "Reducing model precision for efficiency"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_quantum_fact():
    facts = [
        ("Superposition", "Particle exists in all states until measured"),
        ("Entanglement", "Two particles instantaneously affect each other"),
        ("Quantum tunneling", "Particle passes through barrier classically impossible"),
        ("Wave function", "Mathematical description of quantum state"),
        ("Collapse", "Wave function collapses to definite state upon measurement"),
        ("Schrodinger equation", "Describes quantum system evolution"),
        ("Heisenberg uncertainty", "Cannot know position and momentum simultaneously"),
        ("Quantum decoherence", "Quantum states lose coherence from environment"),
        ("Quantum computing", "Uses qubits instead of classical bits"),
        ("Qubit", "Quantum bit, can be 0, 1, or both"),
        ("Quantum gate", "Basic quantum circuit operation"),
        ("Quantum algorithm", "Algorithm for quantum computers"),
        ("Shor's algorithm", "Factors large numbers exponentially faster"),
        ("Grover's algorithm", "Searches unsorted database quadratically faster"),
        ("Quantum supremacy", "Quantum computer solves problem classical cannot"),
        ("Quantum error correction", "Protects quantum information from errors"),
        ("Quantum cryptography", "Secure communication using quantum mechanics"),
        ("Quantum key distribution", "Share encryption keys with perfect security"),
        ("Quantum teleportation", "Transfer quantum state across distance"),
        ("Quantum annealing", "Optimization using quantum fluctuations"),
        ("Topological qubit", "More stable qubit using anyons"),
        ("Photon", "Quantum of light"),
        ("Electron spin", "Intrinsic angular momentum of electron"),
        ("Pauli exclusion", "No two fermions share same quantum state"),
        ("Bose-Einstein condensate", "Matter at near absolute zero"),
        ("Bell's theorem", "No local hidden variable theory possible"),
        ("Quantum field theory", "Quantum mechanics meets special relativity"),
        ("Standard Model", "Theory of fundamental particles and forces"),
        ("Higgs mechanism", "Gives mass to fundamental particles"),
        ("String theory", "Particles are vibrating strings"),
        ("Many worlds interpretation", "All quantum possibilities branch into parallel universes"),
        ("Copenhagen interpretation", "Wave function collapses upon measurement"),
        ("Pilot wave theory", "Deterministic quantum interpretation"),
        ("Quantum biology", "Quantum effects in living systems"),
        ("Quantum chemistry", "Quantum mechanics applied to molecules"),
        ("Quantum sensor", "Uses quantum effects for ultra-precise measurement"),
        ("Quantum imaging", "Imaging using quantum properties of light"),
        ("Quantum internet", "Network using quantum communication"),
        ("Quantum simulation", "Simulating quantum systems with quantum computers"),
        ("Dirac equation", "Relativistic quantum mechanics equation"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_space_object():
    objects = [
        ("Black hole", "Region where gravity prevents light escape"),
        ("Neutron star", "City-sized collapsed star, extremely dense"),
        ("Pulsar", "Rotating neutron star emitting beams"),
        ("Quasar", "Extremely bright active galactic nucleus"),
        ("Supernova", "Explosion of a massive star"),
        ("Nebula", "Cloud of gas and dust in space"),
        ("Galaxy", "Gravitationally bound system of stars"),
        ("Globular cluster", "Spherical collection of old stars"),
        ("Open cluster", "Loose group of young stars"),
        ("Asteroid", "Small rocky body orbiting the Sun"),
        ("Comet", "Icy body with tail when near Sun"),
        ("Meteor", "Shooting star entering atmosphere"),
        ("Meteorite", "Meteor that reaches ground"),
        ("Dwarf planet", "Pluto, Eris, Ceres, Makemake, Haumea"),
        ("Exoplanet", "Planet outside our solar system"),
        ("Hot Jupiter", "Gas giant very close to its star"),
        ("Super-Earth", "Rocky planet larger than Earth"),
        ("Rogue planet", "Planet not orbiting any star"),
        ("White dwarf", "Remnant of low-mass star after fusion ends"),
        ("Red giant", "Swollen star near end of life"),
        ("Blue giant", "Massive hot star"),
        ("Red dwarf", "Small cool star, very long-lived"),
        ("Brown dwarf", "Failed star, too small for fusion"),
        ("Variable star", "Star that changes brightness"),
        ("Binary star", "Two stars orbiting each other"),
        ("Cepheid variable", "Star used to measure cosmic distances"),
        ("Magnetar", "Neutron star with extreme magnetic field"),
        ("Microquasar", "Black hole consuming matter in binary system"),
        ("Blazar", "Quasar with jet pointed at Earth"),
        ("Seyfert galaxy", "Galaxy with active nucleus"),
        ("Elliptical galaxy", "Ellipsoidal galaxy of old stars"),
        ("Spiral galaxy", "Disc-shaped galaxy with spiral arms"),
        ("Irregular galaxy", "Galaxy without regular shape"),
        ("Interstellar medium", "Matter between star systems"),
        ("Cosmic dust", "Fine particles in space"),
        ("Dark nebula", "Cloud blocking light from behind"),
        ("Emission nebula", "Cloud glowing from ionized gas"),
        ("Reflection nebula", "Cloud reflecting starlight"),
        ("Planetary nebula", "Shell of gas from dying star"),
        ("Supernova remnant", "Expanding debris from supernova"),
    ]
    name, desc = random.choice(objects)
    return "{}: {}".format(name, desc)

def random_human_body_fact():
    facts = [
        ("Brain", "~86B neurons, 100T synapses, 3 lbs"),
        ("Heart", "Beats 100K times/day, pumps 7,500 liters"),
        ("Lungs", "300M alveoli, 10,000 L air/day"),
        ("Liver", "500+ functions, can regenerate"),
        ("Skin", "~2m\u00b2, sheds 30-40K cells/minute"),
        ("Bones", "206 bones, 300 at birth"),
        ("Muscles", "~640 muscles, strongest is masseter"),
        ("Blood", "5L, 25T RBCs, 120 day RBC lifespan"),
        ("DNA", "3B base pairs, ~20K genes"),
        ("Stomach", "pH 1-2, produces 2-3L gastric juice/day"),
        ("Small intestine", "6m long, 90% nutrient absorption"),
        ("Large intestine", "1.5m long, water absorption"),
        ("Pancreas", "Produces insulin and digestive enzymes"),
        ("Kidneys", "Filter 180L/day, produce 1.5L urine"),
        ("Bladder", "Holds 400-600mL urine"),
        ("Spleen", "Filters blood, immune function"),
        ("Gallbladder", "Stores bile, aids fat digestion"),
        ("Thyroid", "Regulates metabolism via hormones"),
        ("Pituitary gland", "Master gland controlling other hormones"),
        ("Adrenal glands", "Produce cortisol, adrenaline"),
        ("Thymus", "T-cell maturation, shrinks with age"),
        ("Appendix", "Immune function, gut bacteria reservoir"),
        ("Diaphragm", "Main breathing muscle"),
        ("Trachea", "10-12cm windpipe"),
        ("Esophagus", "25cm, connects mouth to stomach"),
        ("Larynx", "Voice box, contains vocal cords"),
        ("Eyes", "12M photoreceptors, 120M rods"),
        ("Ears", "Cochlea with 15K hair cells"),
        ("Nose", "Detects 1T+ scents via 400 receptors"),
        ("Tongue", "10K taste buds, 5 basic tastes"),
        ("Teeth", "32 adult teeth, enamel is hardest substance"),
        ("Nails", "Grow ~3mm/month"),
        ("Hair", "5M follicles, 100K on scalp"),
        ("Fat cells", "Number stabilizes in adulthood"),
        ("Neurons", "Transmit signals at 120 m/s"),
        ("Synapses", "Chemical/electrical junctions between neurons"),
        ("Neurotransmitters", "Dopamine, serotonin, GABA, glutamate"),
        ("Hormones", "Chemical messengers: insulin, adrenaline, estrogen"),
        ("Immune system", "WBCs, antibodies, complement system"),
        ("Lymphatic system", "Drains fluid, immune surveillance"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_architecture_fact():
    facts = [
        ("Burj Khalifa", "Dubai, 828m, tallest building"),
        ("Shanghai Tower", "Shanghai, 632m, twisted design"),
        ("Makkah Clock Tower", "Mecca, 601m, tallest clock tower"),
        ("Ping An Finance Center", "Shenzhen, 599m"),
        ("One World Trade Center", "NYC, 541m, tallest in US"),
        ("Taipei 101", "Taipei, 509m, bamboo-inspired design"),
        ("Petronas Towers", "Kuala Lumpur, 452m, twin towers"),
        ("Empire State Building", "NYC, 381m, art deco icon"),
        ("CN Tower", "Toronto, 553m, communications tower"),
        ("Eiffel Tower", "Paris, 330m, iron lattice tower"),
        ("Sydney Opera House", "Sydney, expressionist shells"),
        ("Taj Mahal", "Agra, marble mausoleum, 1632-1653"),
        ("Colosseum", "Rome, 70-80 AD, ancient amphitheater"),
        ("Great Wall of China", "21,196 km, ancient defense"),
        ("Machu Picchu", "Peru, 15th century Inca citadel"),
        ("Christ the Redeemer", "Rio de Janeiro, 30m statue"),
        ("Leaning Tower of Pisa", "Pisa, 56m, 3.97 degree tilt"),
        ("St. Peter's Basilica", "Vatican, largest church"),
        ("Notre Dame Cathedral", "Paris, 12th century gothic"),
        ("Sagrada Familia", "Barcelona, Gaudi, started 1882"),
        ("Louvre Pyramid", "Paris, glass pyramid entrance 1989"),
        ("Guggenheim Museum", "Bilbao, titanium curves"),
        ("Fallingwater", "Frank Lloyd Wright, waterfall house"),
        ("Villa Savoye", "Le Corbusier, modernist icon"),
        ("Seattle Space Needle", "184m, 1962 World's Fair"),
        ("Gateway Arch", "St. Louis, 192m stainless steel arch"),
        ("Panama Canal", "82 km, connects Atlantic and Pacific"),
        ("Millau Viaduct", "France, 343m, tallest bridge"),
        ("Channel Tunnel", "50 km, England-France undersea"),
        ("Hoover Dam", "Nevada, 221m, concrete arch-gravity"),
        ("Three Gorges Dam", "China, 181m, largest power station"),
        ("Itaipu Dam", "Brazil/Paraguay, second largest"),
        ("Angkor Wat", "Cambodia, 12th century temple complex"),
        ("Stonehenge", "UK, 2500 BC, megalithic monument"),
        ("Great Pyramid", "Egypt, 138m, 2560 BC"),
        ("Hagia Sophia", "Istanbul, 537 AD, cathedral/mosque"),
        ("Blue Mosque", "Istanbul, 6 minarets, 22 domes"),
        ("Dome of the Rock", "Jerusalem, 691 AD, Islamic shrine"),
        ("Forbidden City", "Beijing, 980 buildings, 1406-1420"),
        ("Temple of Heaven", "Beijing, 1420, imperial ceremony"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_energy_fact():
    facts = [
        ("Solar energy", "Sun provides 173,000 TW continuously"),
        ("Nuclear fusion", "Sun's energy source, H to He"),
        ("Nuclear fission", "Uranium atoms split for energy"),
        ("Wind energy", "Global capacity >800 GW"),
        ("Hydropower", "Largest renewable source, 16% of world"),
        ("Geothermal", "Heat from Earth's core"),
        ("Biomass", "Organic matter for fuel"),
        ("Tidal energy", "Energy from ocean tides"),
        ("Wave energy", "Energy from ocean surface waves"),
        ("Fossil fuels", "Coal, oil, gas - 80% of world energy"),
        ("Peak oil", "Maximum oil production rate"),
        ("Energy density", "Uranium: 24M kWh/kg, coal: 8 kWh/kg"),
        ("Efficiency", "LED: 80% efficient vs incandescent 5%"),
        ("Insulation", "Saves 30-50% heating/cooling energy"),
        ("Smart grid", "Digital electricity distribution"),
        ("Battery storage", "Lithium-ion dominates grid storage"),
        ("Hydrogen fuel", "Clean fuel, water as byproduct"),
        ("Green hydrogen", "Made via electrolysis using renewables"),
        ("Carbon capture", "Captures CO2 from power plants"),
        ("Photovoltaic effect", "Solar panels convert light to electricity"),
        ("Nuclear waste", "High-level waste remains dangerous 10,000 years"),
        ("Chernobyl", "1986 nuclear disaster, exclusion zone"),
        ("Fukushima", "2011 nuclear disaster from tsunami"),
        ("Three Mile Island", "1979 partial meltdown, USA"),
        ("Energy conservation", "Most cost-effective energy solution"),
        ("Passive house", "Ultra-efficient building standard"),
        ("District heating", "Central heat distributed to buildings"),
        ("Cogeneration", "Heat and power from same source"),
        ("Thermal mass", "Materials store heat to regulate temperature"),
        ("Heat pump", "Efficient heating/cooling using electricity"),
        ("Microgrid", "Local energy grid with independent control"),
        ("Net metering", "Credits for solar energy fed to grid"),
        ("Renewable portfolio", "States mandate renewable energy percentage"),
        ("Carbon tax", "Tax on carbon emissions"),
        ("Cap and trade", "Emissions trading system"),
        ("Energy poverty", "~1B people lack electricity access"),
        ("Offshore wind", "Faster consistent winds at sea"),
        ("Solar farm", "Large-scale solar power plants"),
        ("Concentrated solar", "Mirrors focus sunlight to heat fluid"),
        ("Fusion breakthrough", "2022 NIF achieved net energy gain"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_mythology_fact():
    facts = [
        ("Zeus", "Greek king of gods, thunder and lightning"),
        ("Hera", "Greek queen of gods, marriage"),
        ("Poseidon", "Greek god of the sea"),
        ("Athena", "Greek goddess of wisdom, war strategy"),
        ("Apollo", "Greek god of music, arts, prophecy"),
        ("Artemis", "Greek goddess of the hunt"),
        ("Ares", "Greek god of war"),
        ("Aphrodite", "Greek goddess of love and beauty"),
        ("Hermes", "Greek messenger god"),
        ("Dionysus", "Greek god of wine, theater"),
        ("Hades", "Greek god of the underworld"),
        ("Demeter", "Greek goddess of harvest"),
        ("Hephaestus", "Greek god of fire and forge"),
        ("Odin", "Norse king of gods, wisdom, war"),
        ("Thor", "Norse god of thunder, strength"),
        ("Loki", "Norse trickster god"),
        ("Freyja", "Norse goddess of love, fertility"),
        ("Frigg", "Norse queen of gods, motherhood"),
        ("Baldr", "Norse god of light and purity"),
        ("Heimdall", "Norse watchman of the gods"),
        ("Tyr", "Norse god of law and justice"),
        ("Ra", "Egyptian sun god, king of gods"),
        ("Osiris", "Egyptian god of underworld and rebirth"),
        ("Isis", "Egyptian goddess of magic and motherhood"),
        ("Horus", "Egyptian sky god, pharaoh protector"),
        ("Anubis", "Egyptian god of mummification"),
        ("Seth", "Egyptian god of chaos and storms"),
        ("Bastet", "Egyptian cat goddess of home"),
        ("Thoth", "Egyptian god of writing and wisdom"),
        ("Jupiter", "Roman king of gods"),
        ("Juno", "Roman queen of gods"),
        ("Mars", "Roman god of war"),
        ("Venus", "Roman goddess of love"),
        ("Mercury", "Roman messenger god"),
        ("Jade Emperor", "Chinese supreme deity"),
        ("Guan Yin", "Chinese goddess of mercy"),
        ("Amaterasu", "Japanese sun goddess"),
        ("Susanoo", "Japanese storm god"),
        ("Tsukuyomi", "Japanese moon god"),
        ("Brahma", "Hindu creator god"),
        ("Vishnu", "Hindu preserver god"),
        ("Shiva", "Hindu destroyer god"),
        ("Lakshmi", "Hindu goddess of wealth"),
        ("Saraswati", "Hindu goddess of knowledge"),
        ("Kali", "Hindu goddess of time and destruction"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_ocean_life_fact():
    facts = [
        ("Blue whale", "Largest animal, 30m, 200 tons"),
        ("Great white shark", "Largest predatory fish, 6m"),
        ("Whale shark", "Largest fish, filter feeder, 12m"),
        ("Killer whale", "Apex predator, intelligent pods"),
        ("Dolphin", "Uses echolocation, highly social"),
        ("Sea turtle", "Live 80+ years, return to birthplace"),
        ("Manta ray", "Wingspan up to 7m, filter feeder"),
        ("Jellyfish", "No brain, heart, or blood, 95% water"),
        ("Octopus", "3 hearts, 8 arms, incredible problem solver"),
        ("Cuttlefish", "3 hearts, camouflage master"),
        ("Seahorse", "Male gives birth, monogamous"),
        ("Clownfish", "All born male, dominant becomes female"),
        ("Anglerfish", "Bioluminescent lure, extreme deep sea"),
        ("Pufferfish", "Inflates, contains deadly tetrodotoxin"),
        ("Moray eel", "Second set of jaws in throat"),
        ("Lionfish", "Venomous spines, invasive Atlantic"),
        ("Barracuda", "Fast predator, fearsome teeth"),
        ("Parrotfish", "Eats coral, produces sand"),
        ("Starfish", "Can regenerate lost arms"),
        ("Sea anemone", "Clownfish partner, venomous tentacles"),
        ("Coral", "Colonial animals, build reefs"),
        ("Krill", "Foundation of Antarctic food chain"),
        ("Plankton", "Drifting organisms, base of food web"),
        ("Phytoplankton", "Produces 50% of Earth's oxygen"),
        ("Giant squid", "Deep sea, up to 13m, rarely seen"),
        ("Colossal squid", "Largest invertebrate, 14m+"),
        ("Narwhal", "Arctic whale with long tusk"),
        ("Walrus", "Large tusks, social on ice"),
        ("Humpback whale", "Complex songs, bubble net feeding"),
        ("Beluga whale", "White whale, communicative, 50+ sounds"),
        ("Sea otter", "Uses tools, densest fur"),
        ("Penguin", "Flightless bird, 18 species"),
        ("Flying fish", "Glides above water to escape predators"),
        ("Sailfish", "Fastest fish at 110 km/h"),
        ("Sunfish", "Heaviest bony fish at 2,300 kg"),
        ("Lobster", "Can live 100+ years, molts"),
        ("Crab", "10 legs, 6,000+ species"),
        ("Shrimp", "Pistol shrimp snaps claw at 4,400C"),
        ("Sea cucumber", "Ejects organs to escape predators"),
        ("Manatee", "Gentle giant, seagrass grazer"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_mountain_fact():
    facts = [
        ("Mount Everest", "8,848m, Nepal/Tibet, first climbed 1953"),
        ("K2", "8,611m, Pakistan/China, hardest 8000er"),
        ("Kangchenjunga", "8,586m, India/Nepal, third highest"),
        ("Lhotse", "8,516m, connected to Everest"),
        ("Makalu", "8,485m, Nepal/Tibet, pyramid shaped"),
        ("Cho Oyu", "8,188m, Nepal/Tibet, easiest 8000er"),
        ("Dhaulagiri", "8,167m, Nepal"),
        ("Manaslu", "8,163m, Nepal"),
        ("Nanga Parbat", "8,126m, Pakistan, killer mountain"),
        ("Annapurna", "8,091m, Nepal, highest death rate"),
        ("Gasherbrum I", "8,080m, Pakistan"),
        ("Broad Peak", "8,051m, Pakistan"),
        ("Gasherbrum II", "8,035m, Pakistan"),
        ("Shishapangma", "8,027m, Tibet, last 8000er climbed"),
        ("Mount Fuji", "3,776m, Japan, active volcano, iconic"),
        ("Matterhorn", "4,478m, Switzerland/Italy, iconic pyramid"),
        ("Mont Blanc", "4,809m, France/Italy, highest in Alps"),
        ("Denali", "6,190m, Alaska, highest in North America"),
        ("Aconcagua", "6,961m, Argentina, highest in Americas"),
        ("Mount Kilimanjaro", "5,895m, Tanzania, highest in Africa"),
        ("Mount Elbrus", "5,642m, Russia, highest in Europe"),
        ("Vinson Massif", "4,892m, Antarctica, highest on continent"),
        ("Mount Kosciuszko", "2,228m, Australia, highest in Australia"),
        ("Puncak Jaya", "4,884m, Indonesia, highest island peak"),
        ("Mauna Kea", "4,207m, Hawaii, 10,210m from seafloor"),
        ("Mount Whitney", "4,421m, California, highest in US lower 48"),
        ("Mount Rainier", "4,392m, Washington, active stratovolcano"),
        ("Table Mountain", "1,085m, South Africa, flat top landmark"),
        ("Mount Olympus", "2,918m, Greece, home of Greek gods"),
        ("Mount Sinai", "2,285m, Egypt, biblical significance"),
        ("Mount Ararat", "5,137m, Turkey, Noah's Ark legend"),
        ("Mount Cook", "3,724m, New Zealand, highest in NZ"),
        ("Mount Logan", "5,959m, Canada, highest in Canada"),
        ("Mount Erebus", "3,794m, Antarctica, active volcano"),
        ("Mount Etna", "3,357m, Italy, most active volcano in Europe"),
        ("Mount Vesuvius", "1,281m, Italy, destroyed Pompeii 79 AD"),
        ("Mount St. Helens", "2,549m, USA, erupted 1980"),
        ("Krakatoa", "813m, Indonesia, 1883 massive eruption"),
        ("Mount Pinatubo", "1,486m, Philippines, 1991 eruption"),
        ("Mauna Loa", "4,169m, Hawaii, largest volcano on Earth"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_river_fact():
    facts = [
        ("Nile", "6,650km, flows through 11 countries"),
        ("Amazon", "6,400km, largest by water volume"),
        ("Yangtze", "6,300km, China, Three Gorges Dam"),
        ("Mississippi", "6,275km, longest in North America"),
        ("Yenisei", "5,539km, Russia, flows to Arctic"),
        ("Yellow River", "5,464km, China, cradle of Chinese civilization"),
        ("Ob-Irtysh", "5,410km, Russia, Siberia"),
        ("Parana", "4,880km, South America"),
        ("Congo", "4,700km, Africa, deepest river at 220m"),
        ("Amur", "4,444km, Russia/China border"),
        ("Lena", "4,400km, Russia, flows to Arctic"),
        ("Mekong", "4,350km, SE Asia, 6 countries"),
        ("Niger", "4,180km, West Africa"),
        ("Brahmaputra", "3,969km, Tibet to Bangladesh"),
        ("Danube", "2,850km, 10 European countries"),
        ("Volga", "3,531km, longest in Europe"),
        ("Indus", "3,180km, Pakistan, Indus Valley civilization"),
        ("Ganges", "2,525km, India, sacred river"),
        ("Murray", "2,508km, Australia, longest in Australia"),
        ("Tigris", "1,950km, Iraq, ancient Mesopotamia"),
        ("Euphrates", "2,800km, Iraq, ancient Mesopotamia"),
        ("Thames", "346km, England, flows through London"),
        ("Seine", "777km, France, flows through Paris"),
        ("Rhine", "1,230km, Germany, major European waterway"),
        ("Po", "652km, Italy, longest in Italy"),
        ("Tagus", "1,007km, Spain/Portugal, longest in Iberia"),
        ("Loire", "1,012km, France, longest in France"),
        ("Dnipro", "2,201km, Ukraine, flows to Black Sea"),
        ("Ural", "2,428km, Russia, Europe-Asia border"),
        ("Rio Grande", "3,034km, US-Mexico border"),
        ("Yukon", "3,185km, Alaska"),
        ("Colorado", "2,334km, Grand Canyon"),
        ("Columbia", "2,000km, Pacific Northwest"),
        ("Snake River", "1,735km, US, largest tributary of Columbia"),
        ("Platte", "499km, Nebraska, shallow and wide"),
        ("Potomac", "652km, Washington DC area"),
        ("Hudson", "507km, New York"),
        ("Delaware", "484km, US east coast"),
        ("Sutlej", "1,450km, Pakistan, Indus tributary"),
        ("Godavari", "1,465km, India, second longest in India"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_desert_fact():
    facts = [
        ("Sahara", "9.2M km\u00b2, largest hot desert, Africa"),
        ("Arabian", "2.3M km\u00b2, Middle East"),
        ("Gobi", "1.3M km\u00b2, Mongolia/China, cold desert"),
        ("Kalahari", "900K km\u00b2, Southern Africa"),
        ("Great Victoria", "647K km\u00b2, Australia"),
        ("Patagonian", "670K km\u00b2, Argentina"),
        ("Syrian", "500K km\u00b2, Middle East"),
        ("Great Basin", "492K km\u00b2, USA"),
        ("Chihuahuan", "450K km\u00b2, Mexico/USA"),
        ("Karakum", "350K km\u00b2, Turkmenistan"),
        ("Colorado Plateau", "337K km\u00b2, USA"),
        ("Sonoran", "310K km\u00b2, USA/Mexico"),
        ("Kyzlkum", "298K km\u00b2, Uzbekistan"),
        ("Taklamakan", "270K km\u00b2, China"),
        ("Thar", "200K km\u00b2, India/Pakistan"),
        ("Namib", "81K km\u00b2, Namibia, oldest desert"),
        ("Dasht-e Lut", "52K km\u00b2, Iran, hottest surface temp"),
        ("Atacama", "105K km\u00b2, Chile, driest non-polar"),
        ("Antarctica", "14M km\u00b2, largest desert, polar"),
        ("Arctic", "5M km\u00b2, polar desert"),
        ("Rub' al Khali", "650K km\u00b2, Empty Quarter, Arabia"),
        ("Mojave", "124K km\u00b2, USA"),
        ("Sinai", "60K km\u00b2, Egypt"),
        ("Negev", "13K km\u00b2, Israel"),
        ("Dasht-e Kavir", "77K km\u00b2, Iran"),
        ("Betpak-Dala", "75K km\u00b2, Kazakhstan"),
        ("Ustyurt Plateau", "200K km\u00b2, Kazakhstan/Uzbekistan"),
        ("Rann of Kutch", "26K km\u00b2, India/Pakistan, salt desert"),
        ("Red Desert", "9.3K km\u00b2, Wyoming USA"),
        ("Sechura", "5K km\u00b2, Peru coastal desert"),
        ("Algodones Dunes", "0.5K km\u00b2, California"),
        ("White Sands", "710 km\u00b2, New Mexico, gypsum dunes"),
        ("Great Sandy", "360K km\u00b2, Australia"),
        ("Simpson", "176K km\u00b2, Australia"),
        ("Tanami", "185K km\u00b2, Australia"),
        ("Gibson", "155K km\u00b2, Australia"),
        ("Sturt Stony", "30K km\u00b2, Australia"),
        ("Little Sandy", "111K km\u00b2, Australia"),
        ("Strzelecki", "80K km\u00b2, Australia"),
        ("Painted Desert", "200 km\u00b2, Arizona USA"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_forest_fact():
    facts = [
        ("Amazon", "5.5M km\u00b2, 60% in Brazil"),
        ("Congo Basin", "3.7M km\u00b2, second largest"),
        ("Taiga", "17M km\u00b2, largest biome, Russia/Canada"),
        ("Temperate rainforest", "Pacific NW, New Zealand, Chile"),
        ("Daintree", "Australia, oldest rainforest at 180M years"),
        ("Borneo", "130M years old, orangutan habitat"),
        ("Sumatra", "Endangered tiger and elephant habitat"),
        ("Siberian taiga", "57% of all coniferous forest"),
        ("Mangrove", "Coastal trees, carbon storage"),
        ("Boreal forest", "28% of world's trees"),
        ("Redwood forest", "California, tallest trees at 115m"),
        ("Black Forest", "Germany, 6,000 km\u00b2, dense canopy"),
        ("Bialowieza", "Poland/Belarus, Europe's last old-growth"),
        ("Monteverde", "Costa Rica, cloud forest"),
        ("Amazon deforestation", "17% lost in 50 years"),
        ("Forest carbon", "Stores 45% of terrestrial carbon"),
        ("Deforestation rate", "10M ha/year lost globally"),
        ("Rewilding", "Restoring forests to native state"),
        ("Afforestation", "Planting forests for carbon offset"),
        ("Old-growth forest", "250+ years old, massive biodiversity"),
        ("Secondary forest", "Regrown after disturbance"),
        ("Forest canopy", "Layer absorbing 90% of sunlight"),
        ("Understory", "Shade-tolerant plants below canopy"),
        ("Forest floor", "Decomposition and nutrient recycling"),
        ("Mycorrhizal network", "Fungal connections between tree roots"),
        ("Carbon sequestration", "Forests absorb 2.6B tons CO2/year"),
        ("Amazon biodiversity", "40K plant species, 1,300 bird species"),
        ("Tropical forest", "50% of all species in 6% of land"),
        ("Fungi", "Essential decomposers in forest ecosystems"),
        ("Epiphytes", "Plants growing on trees, non-parasitic"),
        ("Liana", "Woody vines in tropical forests"),
        ("Forest fire", "Natural and human-caused, increasing"),
        ("Prescribed burn", "Controlled fire to reduce fuel"),
        ("Forest regeneration", "Natural regrowth after disturbance"),
        ("Seed dispersal", "Animals, wind, water spread seeds"),
        ("Canopy bridge", "Connecting fragmented forests"),
        ("Forest bathing", "Japanese Shinrin-yoku for health"),
        ("Ecotourism", "Sustainable forest tourism"),
        ("IUCN", "Protected area categories"),
        ("UN Decade on Restoration", "2021-2030 ecosystem restoration"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_volcano_fact():
    facts = [
        ("Mount Vesuvius", "Italy, 79 AD eruption destroyed Pompeii"),
        ("Mount Etna", "Italy, most active in Europe, 3,357m"),
        ("Krakatoa", "Indonesia, 1883, loudest explosion in history"),
        ("Mount Tambora", "Indonesia, 1815, caused Year Without Summer"),
        ("Mount St. Helens", "USA, 1980, killed 57, massive lateral blast"),
        ("Mauna Loa", "Hawaii, largest shield volcano on Earth"),
        ("Mauna Kea", "Hawaii, tallest from base at 10,210m"),
        ("Kilauea", "Hawaii, continuously erupting"),
        ("Eyjafjallajokull", "Iceland, 2010, disrupted air travel for weeks"),
        ("Mount Fuji", "Japan, 3,776m, dormant since 1707"),
        ("Mount Pinatubo", "Philippines, 1991, 2nd largest 20th century"),
        ("Mount Merapi", "Indonesia, most active in Indonesia"),
        ("Cotopaxi", "Ecuador, one of highest active at 5,897m"),
        ("Santorini", "Greece, ~1600 BC, may have ended Minoan civilization"),
        ("Yellowstone", "USA, supervolcano, last eruption 640,000 years ago"),
        ("Taupo", "New Zealand, supervolcano, 26,500 years ago"),
        ("Lake Toba", "Indonesia, supervolcano, 74,000 years ago"),
        ("Novarupta", "Alaska, 1912, largest 20th century eruption"),
        ("Paricutin", "Mexico, 1943-1952, born in farmer's field"),
        ("Mount Erebus", "Antarctica, southernmost active volcano"),
        ("Stromboli", "Italy, continuously erupting for 2,000+ years"),
        ("Mayon Volcano", "Philippines, perfect cone shape"),
        ("Mount Rainier", "USA, 4,392m, stratovolcano near Seattle"),
        ("Mount Kilimanjaro", "Tanzania, dormant, ice caps melting"),
        ("Mount Pelée", "Martinique, 1902, killed 30,000 by pyroclastic flow"),
        ("Nevado del Ruiz", "Colombia, 1985, lahar killed 23,000"),
        ("Mount Unzen", "Japan, 1792, deadliest eruption in Japan"),
        ("Mount Galeras", "Colombia, 1993, erupted during conference"),
        ("Pacaya", "Guatemala, active, popular tourist site"),
        ("Mount Nyiragongo", "Congo, lava lake, 2002 devastated Goma"),
        ("Erta Ale", "Ethiopia, permanent lava lake"),
        ("Fagradalsfjall", "Iceland, 2021-2023 eruptions near Reykjavik"),
        ("Olympus Mons", "Mars, largest volcano in solar system, 21.9km"),
        ("Io", "Jupiter's moon, most volcanically active body"),
        ("Ring of Fire", "75% of active volcanoes, Pacific basin"),
        ("Subduction zone", "Where one plate slides under another"),
        ("Hotspot volcano", "Hawaii, Yellowstone from mantle plumes"),
        ("Caldera", "Depression formed after magma chamber empties"),
        ("Pahoehoe", "Smooth ropy lava"),
        ("Aa lava", "Rough jagged lava"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_city_fact():
    facts = [
        ("Tokyo", "37M metro, 23 wards, world's largest metro"),
        ("Delhi", "32M people, India's capital"),
        ("Shanghai", "27M, China's financial hub"),
        ("Sao Paulo", "22M, largest in Americas"),
        ("Mumbai", "21M, Bollywood and financial capital"),
        ("Beijing", "21M, China's capital"),
        ("Cairo", "21M, largest in Africa"),
        ("Dhaka", "21M, Bangladesh capital, densely populated"),
        ("Mexico City", "22M, built on lake bed"),
        ("Osaka", "19M, Kansai region hub"),
        ("Karachi", "16M, Pakistan's largest city"),
        ("Istanbul", "16M, only city on two continents"),
        ("Buenos Aires", "16M, Paris of South America"),
        ("Kolkata", "15M, cultural capital of India"),
        ("Manila", "14M, Philippines capital"),
        ("Lagos", "15M, Nigeria's commercial capital"),
        ("London", "9.7M, UK capital, multicultural hub"),
        ("Paris", "11M, City of Light, romance capital"),
        ("New York", "19M metro, empire state of mind"),
        ("Los Angeles", "13M metro, Hollywood"),
        ("Singapore", "5.7M, city-state, clean and modern"),
        ("Hong Kong", "7.5M, skyline, harbor, finance"),
        ("Dubai", "3.3M, luxury, tallest building"),
        ("Seoul", "9.8M, K-pop and technology"),
        ("Bangkok", "10M, temples and street food"),
        ("Berlin", "3.7M, history and art scene"),
        ("Madrid", "6.7M, Spanish culture and food"),
        ("Rome", "4.2M, eternal city, ancient history"),
        ("Vienna", "1.9M, quality of life"),
        ("Sydney", "5.3M, harbor and opera house"),
        ("Toronto", "6.2M, multicultural Canadian hub"),
        ("San Francisco", "4.7M metro, tech hub"),
        ("Moscow", "12.5M, Russian capital"),
        ("Rio de Janeiro", "13.5M, beaches and carnival"),
        ("Cape Town", "4.6M, stunning natural beauty"),
        ("Mumbai", "21M, never sleeps, dreams and ambition"),
        ("Lima", "11M, Peruvian capital, ceviche capital"),
        ("Nairobi", "5.3M, tech hub of Africa"),
        ("Amsterdam", "2.4M, canals and cycling"),
        ("Stockholm", "2.4M, islands and design"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_flag_fact():
    facts = [
        ("USA", "13 stripes for colonies, 50 stars for states"),
        ("UK", "Union Jack combines England, Scotland, Ireland"),
        ("France", "Blue, white, red tricolor, liberty equality fraternity"),
        ("Germany", "Black, red, gold tricolor"),
        ("Japan", "Red sun on white field"),
        ("China", "Red flag with 5 yellow stars"),
        ("India", "Saffron, white, green with Ashoka Chakra"),
        ("Brazil", "Green, yellow, blue with stars and slogan"),
        ("Russia", "White, blue, red tricolor"),
        ("Italy", "Green, white, red tricolor"),
        ("Canada", "Red with white square and maple leaf"),
        ("Australia", "Blue with Union Jack and 6 white stars"),
        ("South Africa", "6 colors, Y shape, rainbow nation"),
        ("Argentina", "Light blue and white with sun"),
        ("Mexico", "Green, white, red with eagle eating snake"),
        ("Spain", "Red and yellow with coat of arms"),
        ("Sweden", "Blue with yellow Scandinavian cross"),
        ("Norway", "Red with blue and white cross"),
        ("Denmark", "Red with white cross, oldest flag in use"),
        ("Finland", "White with blue cross"),
        ("Greece", "9 blue and white stripes with cross"),
        ("Turkey", "Red with white crescent and star"),
        ("Israel", "White with blue Star of David and stripes"),
        ("Saudi Arabia", "Green with white inscription and sword"),
        ("Nigeria", "Green, white, green vertical stripes"),
        ("Kenya", "Black, red, green with shield"),
        ("Egypt", "Red, white, black with eagle"),
        ("South Korea", "White with yin-yang and trigrams"),
        ("Switzerland", "Red with white cross, square not rectangle"),
        ("Nepal", "Only non-rectangular national flag"),
        ("Jamaica", "Black, green, gold diagonal cross"),
        ("Ireland", "Green, white, orange tricolor"),
        ("Poland", "White on red, horizontal"),
        ("Netherlands", "Red, white, blue horizontal tricolor"),
        ("Belgium", "Black, yellow, red vertical"),
        ("Austria", "Red, white, red horizontal"),
        ("Switzerland", "Red with white cross"),
        ("Thailand", "Blue, white, red, white, blue stripes"),
        ("Vietnam", "Red with yellow star"),
        ("Morocco", "Red with green pentagram star"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_number_fact_deep():
    facts = [
        ("0", "Only number that when added to itself equals itself"),
        ("1", "The only positive integer neither prime nor composite"),
        ("2", "First prime, only even prime"),
        ("3", "First odd prime"),
        ("4", "First composite number"),
        ("5", "Number of platonic solids"),
        ("6", "First perfect number (1+2+3)"),
        ("7", "Lucky number, days of the week"),
        ("8", "First cubic number (2\u00b3)"),
        ("9", "Magic number, 3\u00b2"),
        ("10", "Base of decimal system"),
        ("11", "First palindromic prime"),
        ("12", "Dozen, highly composite"),
        ("13", "Unlucky in Western culture"),
        ("17", "Least random number in surveys"),
        ("21", "Blackjack winning hand"),
        ("28", "Second perfect number"),
        ("37", "Most common favorite number"),
        ("42", "Answer to life, the universe, and everything"),
        ("100", "Century, perfect square"),
        ("101", "First three-digit prime"),
        ("108", "Sacred in Hinduism and Buddhism"),
        ("144", "Gross, 12 squared"),
        ("365", "Days in a year"),
        ("496", "Third perfect number"),
        ("666", "Number of the beast"),
        ("1000", "Millennium"),
        ("1729", "Taxicab number, Hardy-Ramanujan"),
        ("8128", "Fourth perfect number"),
        ("142857", "Cyclic number, repeating 1/7"),
        ("6174", "Kaprekar's constant"),
        ("314159", "Pi as integer"),
        ("123456789", "Pandigital number"),
        ("987654321", "Reverse pandigital"),
        ("Fibonacci sequence", "0,1,1,2,3,5,8,13,21,34,55"),
        ("Catalan numbers", "1,1,2,5,14,42,132,429"),
        ("Mersenne primes", "Primes = 2^n-1"),
        ("Fermat numbers", "2^(2^n)+1"),
        ("Graham's number", "So large standard notation cannot express"),
        ("TREE(3)", "Enormous number from graph theory"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_history_fact_deep():
    facts = [
        ("Ancient Egypt", "3100 BC, 31 dynasties, pyramids"),
        ("Ancient Greece", "800 BC, democracy, philosophy, Olympics"),
        ("Roman Empire", "27 BC-476 AD, engineering law republic"),
        ("Byzantine Empire", "330-1453 AD, Greek Christian empire"),
        ("Mongol Empire", "1206-1368, largest contiguous land empire"),
        ("Ottoman Empire", "1299-1922, Islamic caliphate"),
        ("Persian Empire", "550-330 BC, Cyrus to Alexander"),
        ("Maurya Empire", "322-185 BC, first Indian empire"),
        ("Gupta Empire", "320-550 AD, golden age of India"),
        ("Tang Dynasty", "618-907, golden age of China"),
        ("Ming Dynasty", "1368-1644, Great Wall expansion"),
        ("Qing Dynasty", "1644-1912, last Chinese dynasty"),
        ("Aztec Empire", "1428-1521, central Mexico"),
        ("Inca Empire", "1438-1533, Andes mountain civilization"),
        ("Maya civilization", "2000 BC-900 AD, pyramids and calendar"),
        ("Viking Age", "793-1066, Norse exploration and raids"),
        ("Medieval Europe", "5th-15th century, feudalism, crusades"),
        ("Renaissance", "14th-17th century, rebirth of arts"),
        ("Age of Discovery", "15th-17th century, global exploration"),
        ("Industrial Revolution", "1760-1840, machines and factories"),
        ("French Revolution", "1789-1799, liberty equality fraternity"),
        ("American Revolution", "1775-1783, US independence"),
        ("Napoleonic Wars", "1803-1815, French domination of Europe"),
        ("World War I", "1914-1918, Great War, 16M deaths"),
        ("Russian Revolution", "1917, Bolsheviks seize power"),
        ("World War II", "1939-1945, 70-85M deaths"),
        ("Holocaust", "1941-1945, 6M Jews murdered by Nazis"),
        ("Cold War", "1947-1991, US vs Soviet Union"),
        ("Korean War", "1950-1953, still technically ongoing"),
        ("Vietnam War", "1955-1975, US involvement ended 1973"),
        ("Space Race", "1955-1975, US vs Soviet space competition"),
        ("Civil Rights Movement", "1954-1968, US racial equality"),
        ("Fall of Berlin Wall", "1989, end of Cold War symbol"),
        ("Dissolution of USSR", "1991, end of Soviet Union"),
        ("Digital Revolution", "1980s-present, computers and internet"),
        ("War on Terror", "2001-present, post-9/11 conflicts"),
        ("Arab Spring", "2010-2012, Middle East protests"),
        ("COVID-19 pandemic", "2019-2023, global health crisis"),
        ("Climate change era", "2000s-present, global warming urgency"),
        ("AI revolution", "2020s-present, artificial intelligence boom"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_lake_fact():
    facts = [
        ("Caspian Sea", "371K km\u00b2, largest lake, saltwater"),
        ("Lake Superior", "82.1K km\u00b2, largest freshwater"),
        ("Lake Victoria", "69.5K km\u00b2, Africa's largest"),
        ("Lake Huron", "59.6K km\u00b2, second Great Lake"),
        ("Lake Michigan", "58K km\u00b2, third Great Lake"),
        ("Lake Tanganyika", "32.9K km\u00b2, second deepest at 1,470m"),
        ("Lake Baikal", "31.7K km\u00b2, deepest at 1,642m, oldest at 25M years"),
        ("Great Bear Lake", "31.3K km\u00b2, Canada"),
        ("Lake Malawi", "29.6K km\u00b2, Africa"),
        ("Great Slave Lake", "28.6K km\u00b2, Canada, deepest in NA at 614m"),
        ("Lake Erie", "25.7K km\u00b2, shallowest Great Lake"),
        ("Lake Winnipeg", "24.5K km\u00b2, Canada"),
        ("Lake Ontario", "18.9K km\u00b2, smallest Great Lake"),
        ("Ladoga", "17.7K km\u00b2, Europe's largest"),
        ("Lake Balkhash", "16.4K km\u00b2, Kazakhstan, half fresh half salt"),
        ("Lake Onega", "9.7K km\u00b2, Europe's second largest"),
        ("Lake Titicaca", "8.3K km\u00b2, highest navigable at 3,812m"),
        ("Lake Nicaragua", "8.2K km\u00b2, freshwater sharks"),
        ("Lake Athabasca", "7.9K km\u00b2, Canada"),
        ("Lake Reindeer", "6.7K km\u00b2, Canada"),
        ("Lake Turkana", "6.4K km\u00b2, Kenya, jade color"),
        ("Lake Issyk-Kul", "6.2K km\u00b2, Kyrgyzstan, no outflow"),
        ("Lake Van", "3.7K km\u00b2, Turkey, soda lake"),
        ("Lake Tahoe", "487 km\u00b2, very clear, 501m deep"),
        ("Crater Lake", "53 km\u00b2, caldera lake, deepest in US at 594m"),
        ("Lake Geneva", "580 km\u00b2, Switzerland/France"),
        ("Lake Como", "146 km\u00b2, Italy, stunning scenery"),
        ("Lake Garda", "370 km\u00b2, Italy's largest"),
        ("Lake Lucerne", "114 km\u00b2, Switzerland"),
        ("Lake Bled", "1.5 km\u00b2, Slovenia, island church"),
        ("Lake Plitvice", "Plitvice Lakes National Park, Croatia"),
        ("Lake Wakatipu", "291 km\u00b2, New Zealand"),
        ("Lake Louise", "0.5 km\u00b2, Canada, turquoise color"),
        ("Pehoe Lake", "Chile, Torres del Paine backdrop"),
        ("Laguna Colorada", "Bolivia, red lake with flamingos"),
        ("Dead Sea", "605 km\u00b2, lowest point at -430m"),
        ("Salton Sea", "974 km\u00b2, California, accidental lake"),
        ("Lake Mead", "640 km\u00b2, largest US reservoir"),
        ("Lake Kariba", "5.6K km\u00b2, Zimbabwe/Zambia, largest dam lake"),
        ("Lake Volta", "8.5K km\u00b2, Ghana, largest man-made by area"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_island_fact():
    facts = [
        ("Greenland", "2.17M km\u00b2, largest island, mostly ice"),
        ("New Guinea", "785K km\u00b2, second largest, shared by 2 countries"),
        ("Borneo", "748K km\u00b2, shared by 3 countries"),
        ("Madagascar", "587K km\u00b2, unique wildlife"),
        ("Baffin Island", "507K km\u00b2, Canada"),
        ("Sumatra", "473K km\u00b2, Indonesia"),
        ("Honshu", "227K km\u00b2, main Japanese island"),
        ("Great Britain", "209K km\u00b2, UK's main island"),
        ("Ellesmere Island", "196K km\u00b2, Canada"),
        ("Victoria Island", "217K km\u00b2, Canada"),
        ("Sulawesi", "180K km\u00b2, Indonesia"),
        ("South Island", "150K km\u00b2, New Zealand"),
        ("Java", "138K km\u00b2, most populous island at 140M"),
        ("North Island", "114K km\u00b2, New Zealand"),
        ("Cuba", "105K km\u00b2, Caribbean largest"),
        ("Newfoundland", "109K km\u00b2, Canada"),
        ("Luzon", "109K km\u00b2, Philippines"),
        ("Iceland", "103K km\u00b2, land of fire and ice"),
        ("Mindanao", "97.5K km\u00b2, Philippines"),
        ("Ireland", "84.4K km\u00b2, emerald isle"),
        ("Hokkaido", "78.4K km\u00b2, Japan's northern island"),
        ("Sakhalin", "72.5K km\u00b2, Russia"),
        ("Hispaniola", "73.9K km\u00b2, Haiti and Dominican Republic"),
        ("Tasmania", "68.4K km\u00b2, Australia"),
        ("Sri Lanka", "65.6K km\u00b2, teardrop of India"),
        ("Kunashir", "1.5K km\u00b2, disputed Russia/Japan"),
        ("Bali", "5.8K km\u00b2, Indonesia, paradise island"),
        ("Phuket", "543 km\u00b2, Thailand's largest"),
        ("Santorini", "73 km\u00b2, Greece, caldera island"),
        ("Mykonos", "85 km\u00b2, Greece, party island"),
        ("Maldives", "298 km\u00b2 total, 26 atolls"),
        ("Fiji", "18.3K km\u00b2, 330 islands"),
        ("Hawaii Big Island", "10.4K km\u00b2, largest in Hawaii"),
        ("Maui", "1.9K km\u00b2, Hawaii"),
        ("Easter Island", "163 km\u00b2, moai statues"),
        ("Galapagos", "7.9K km\u00b2, Darwin's evolution inspiration"),
        ("Kauai", "1.4K km\u00b2, Hawaii, garden island"),
        ("Cebu", "4.9K km\u00b2, Philippines"),
        ("Hong Kong Island", "78 km\u00b2, financial hub"),
        ("Singapore", "728 km\u00b2, city-state island"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_planet_fact_deep():
    facts = [
        ("Mercury", "Smallest planet, 88-day year, no atmosphere"),
        ("Venus", "Hottest at 462C, rotates backwards, 243-day day"),
        ("Earth", "Only known life, 71% water, 24-hour day"),
        ("Mars", "Red planet, largest volcano Olympus Mons, frozen CO2"),
        ("Jupiter", "Largest planet, Great Red Spot storm, 79 moons"),
        ("Saturn", "Rings of ice and rock, least dense, 83 moons"),
        ("Uranus", "Rotates on its side, blue-green from methane"),
        ("Neptune", "Fastest winds at 2,100 km/h, 12th planet most distant"),
        ("Pluto", "Dwarf planet, heart-shaped glacier, 248-year orbit"),
        ("Ceres", "Largest asteroid, dwarf planet in asteroid belt"),
        ("Eris", "Most massive dwarf planet, 557-year orbit"),
        ("Makemake", "Dwarf planet in Kuiper belt, no atmosphere"),
        ("Haumea", "Football-shaped dwarf planet, fast rotation"),
        ("Kepler-452b", "Earth's cousin, 1,400 light years away"),
        ("TRAPPIST-1e", "Potentially habitable, 39 light years"),
        ("Proxima Centauri b", "Closest exoplanet at 4.2 light years"),
        ("55 Cancri e", "Super-Earth, diamond rich, 40 light years"),
        ("HD 189733b", "Blue planet, glass rain sideways"),
        ("WASP-12b", "Hot Jupiter, being consumed by its star"),
        ("Kepler-22b", "First in habitable zone, 600 light years"),
        ("GJ 1214b", "Water world, deep ocean planet"),
        ("TOI-700d", "Earth-sized in habitable zone, 100 light years"),
        ("LHS 1140b", "Super-Earth, potential atmosphere"),
        ("K2-18b", "Water vapor detected in atmosphere"),
        ("HD 209458b", "First transiting exoplanet found"),
        ("51 Pegasi b", "First exoplanet around Sun-like star"),
        ("Beta Pictoris b", "Directly imaged young planet"),
        ("HR 8799 system", "Four directly imaged planets"),
        ("Trappist-1 system", "7 Earth-sized planets, 3 in habitable zone"),
        ("Solar system age", "4.568 billion years"),
        ("Sun mass", "330,000 times Earth's mass"),
        ("Sun's fuel", "600M tons hydrogen/second into helium"),
        ("Sun's lifetime", "~10 billion years, halfway through"),
        ("Heliosphere", "Sun's magnetic field bubble, 120 AU"),
        ("Kuiper Belt", "30-50 AU, icy bodies beyond Neptune"),
        ("Oort Cloud", "2,000-100,000 AU, spherical shell of comets"),
        ("Termination shock", "Where solar wind slows to subsonic"),
        ("Heliopause", "Boundary of heliosphere"),
        ("Voyager 1", "Entered interstellar space 2012"),
        ("Interstellar medium", "Material between star systems"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_ocean_fact_deep():
    facts = [
        ("Pacific Ocean", "165.2M km\u00b2, 28% of Earth's surface"),
        ("Atlantic Ocean", "106.5M km\u00b2, S shape between continents"),
        ("Indian Ocean", "70.6M km\u00b2, warmest, 60% of global trade"),
        ("Southern Ocean", "21M km\u00b2, encircles Antarctica"),
        ("Arctic Ocean", "14.1M km\u00b2, smallest, mostly ice-covered"),
        ("Average depth", "3,688m average for all oceans"),
        ("Total volume", "1.332 billion km\u00b3 of water"),
        ("Deepest point", "Challenger Deep, Mariana Trench, 11,034m"),
        ("Ocean pressure", "At Challenger Deep: 1,100 atmospheres"),
        ("Ocean temperature", "Average 3.5C for deep ocean"),
        ("Ocean pH", "8.1 average, decreasing (acidifying)"),
        ("Ocean salinity", "35 parts per thousand average"),
        ("Sound speed", "~1,500 m/s in ocean water"),
        ("Ocean conveyor", "Global thermohaline circulation"),
        ("Gulf Stream", "Carries 1.2 PW of heat, affects Europe"),
        ("North Atlantic Gyre", "Large system of circular currents"),
        ("Pacific Gyre", "Contains Great Pacific Garbage Patch"),
        ("Mid-Atlantic Ridge", "65K km mountain range underwater"),
        ("Mariana Trench", "2,550 km long, 69 km wide trench"),
        ("Tonga Trench", "10,882m deep, second deepest"),
        ("Philippine Trench", "10,540m deep"),
        ("Kuril-Kamchatka Trench", "10,542m deep"),
        ("Japan Trench", "9,000m deep, 2011 earthquake zone"),
        ("Puerto Rico Trench", "8,376m deep, deepest in Atlantic"),
        ("South Sandwich Trench", "8,428m deep, Southern Ocean"),
        ("Ocean ridges", "Volcanic underwater mountain chains"),
        ("Seamount", "Underwater mountain, not reaching surface"),
        ("Guyot", "Flat-topped seamount"),
        ("Abyssal plain", "Flat deep ocean floor at 3,000-6,000m"),
        ("Continental shelf", "Submerged edge of continent, <200m deep"),
        ("Continental slope", "Steep drop-off from shelf to deep"),
        ("Submarine canyon", "Deep narrow valleys on continental slope"),
        ("Oceanic trench", "Deepest parts, subduction zones"),
        ("Hydrothermal vent", "Hot springs on ocean floor, extreme life"),
        ("Black smoker", "Hot vent emitting dark mineral particles"),
        ("Cold seep", "Methane seep supporting unique ecosystems"),
        ("Brine pool", "Extremely salty underwater lake"),
        ("Coral reef", "Most diverse marine ecosystem"),
        ("Kelp forest", "Cold water underwater forest"),
        ("Mangrove forest", "Coastal trees filtering saltwater"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_culture_fact():
    facts = [
        ("Tea ceremony", "Japan, elaborate ritual, zen influence"),
        ("Kimono", "Japan, traditional garment, formal occasions"),
        ("Sushi", "Japan, vinegared rice with fresh fish"),
        ("Kabuki", "Japan, stylized drama and dance theater"),
        ("Geisha", "Japan, traditional entertainers"),
        ("Hanami", "Japan, cherry blossom viewing tradition"),
        ("Chinese New Year", "Lunar new year, red envelopes, fireworks"),
        ("Dragon dance", "China, performed for celebrations"),
        ("Kung fu", "China, martial arts with philosophy"),
        ("Tai chi", "China, slow meditative martial art"),
        ("Feng shui", "China, spatial arrangement for harmony"),
        ("Diwali", "India, festival of lights, lamps and fireworks"),
        ("Holi", "India, color festival, spring celebration"),
        ("Yoga", "India, physical and spiritual practice"),
        ("Ayurveda", "India, traditional medicine system"),
        ("Bollywood", "India, film industry, song and dance"),
        ("Hijab", "Islamic modest dress"),
        ("Ramadan", "Islam, month of fasting from dawn to sunset"),
        ("Eid", "Islam, festival after Ramadan"),
        ("Hajj", "Islam, pilgrimage to Mecca"),
        ("Calligraphy", "Islamic art of beautiful writing"),
        ("Mardi Gras", "New Orleans, carnival celebration"),
        ("Cinco de Mayo", "Mexico, celebrates Mexican victory"),
        ("Day of the Dead", "Mexico, honoring deceased ancestors"),
        ("Flamenco", "Spain, passionate dance and guitar"),
        ("La Tomatina", "Spain, tomato throwing festival"),
        ("Oktoberfest", "Germany, beer festival in Munich"),
        ("Christmas market", "Germany, festive holiday markets"),
        ("Carnival", "Brazil, Rio samba parade"),
        ("Capoeira", "Brazil, martial art dance fusion"),
        ("Samba", "Brazil, rhythm and dance"),
        ("Maori haka", "New Zealand, war dance performance"),
        ("Didgeridoo", "Australia, Aboriginal wind instrument"),
        ("Dreamtime", "Australia, Aboriginal creation stories"),
        ("Viking history", "Scandinavia, Norse heritage"),
        ("Midsommar", "Sweden, summer solstice celebration"),
        ("Hygee", "Denmark, cozy contentment lifestyle"),
        ("Smorgasbord", "Sweden, buffet of traditional dishes"),
        ("Siesta", "Spain, afternoon rest tradition"),
        ("Fika", "Sweden, coffee and cake break tradition"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_famous_landmark():
    landmarks = [
        ("Great Wall of China", "China, 21,196 km, started 7th century BC"),
        ("Taj Mahal", "India, white marble mausoleum, 1632-1653"),
        ("Colosseum", "Italy, ancient amphitheater, 70-80 AD"),
        ("Machu Picchu", "Peru, 15th century Inca citadel, 2,430m"),
        ("Christ the Redeemer", "Brazil, 30m statue, 710m summit"),
        ("Petra", "Jordan, rock-cut architecture, 300 BC"),
        ("Chichen Itza", "Mexico, Maya pyramid, 600 AD"),
        ("Eiffel Tower", "France, 330m, 1889 World's Fair"),
        ("Sydney Opera House", "Australia, expressionist shells, 1973"),
        ("Stonehenge", "UK, megalithic monument, 2500 BC"),
        ("Angkor Wat", "Cambodia, 12th century temple complex"),
        ("Great Sphinx", "Egypt, limestone statue, 2500 BC"),
        ("Pyramids of Giza", "Egypt, 138m tallest, 2560 BC"),
        ("Statue of Liberty", "USA, 93m, France gift 1886"),
        ("Acropolis", "Greece, ancient citadel, 5th century BC"),
        ("Parthenon", "Greece, Athena temple, 432 BC"),
        ("Tower of London", "UK, historic castle, 1066"),
        ("Niagara Falls", "USA/Canada, 51m drop, 3 waterfalls"),
        ("Grand Canyon", "USA, 446km long, 1.8km deep"),
        ("Uluru", "Australia, 348m monolith, sacred to Anangu"),
        ("Mount Fuji", "Japan, 3,776m active volcano"),
        ("Great Barrier Reef", "Australia, 2,300km reef system"),
        ("Northern Lights", "Arctic, aurora borealis"),
        ("Matterhorn", "Switzerland/Italy, 4,478m iconic peak"),
        ("Table Mountain", "South Africa, 1,085m flat top"),
        ("Ha Long Bay", "Vietnam, 1,600 limestone islands"),
        ("Bagan", "Myanmar, 2,000+ ancient temples"),
        ("Borobudur", "Indonesia, 9th century Buddhist temple"),
        ("Notre Dame", "France, 12th century Gothic cathedral"),
        ("Sagrada Familia", "Spain, Gaudi basilica, started 1882"),
        ("Neuschwanstein Castle", "Germany, fairytale castle, 1886"),
        ("Alhambra", "Spain, Moorish palace fortress, 9th century"),
        ("Taj Mahal", "India, love monument"),
        ("Forbidden City", "China, 980 building imperial palace"),
        ("Mount Everest Base Camp", "Nepal/Tibet, 5,364m"),
        ("Dead Sea", "Jordan/Israel, -430m lowest point on land"),
        ("Milford Sound", "New Zealand, fiord in Fiordland"),
        ("Antelope Canyon", "USA, slot canyon in Arizona"),
        ("Blue Lagoon", "Iceland, geothermal spa"),
        ("Giant's Causeway", "Ireland, 40,000 basalt columns"),
    ]
    name, loc, detail = random.choice(landmarks)
    return "{} ({}): {}".format(name, loc, detail)

def random_weather_phenomenon():
    phenomena = [
        ("Aurora borealis", "Northern lights, solar particles hitting atmosphere"),
        ("Aurora australis", "Southern lights, same as northern"),
        ("Lightning", "Electrical discharge, 30,000C, 100M strikes/year"),
        ("Ball lightning", "Rare, luminous sphere during storms"),
        ("St. Elmo's fire", "Plasma glow from pointed objects in storms"),
        ("Fire rainbow", "Circumhorizontal arc, ice crystal halo"),
        ("Sun dog", "Bright spots beside the Sun at 22 degrees"),
        ("Moon halo", "Ring around the Moon from ice crystals"),
        ("Rainbow", "Sunlight refracted through water at 42 degree arc"),
        ("Double rainbow", "Second fainter rainbow with reversed colors"),
        ("Mirage", "Light refraction creating illusion of water"),
        ("Fata Morgana", "Complex mirage, objects stretched vertically"),
        ("Green flash", "Green spot at sunset/rise on clear horizon"),
        ("Brocken spectre", "Shadow of observer on cloud/mist below"),
        ("Glory", "Colorful rings around shadow on clouds"),
        ("Crepuscular rays", "Sunbeams through gaps in clouds"),
        ("Anticrepuscular rays", "Sunbeams converging opposite the Sun"),
        ("Cloud iridescence", "Pastel colors in clouds from diffraction"),
        ("Nacreous clouds", "Iridescent polar stratospheric clouds"),
        ("Noctilucent clouds", "Night-shining clouds at 80km altitude"),
        ("Mammatus clouds", "Pouch-like clouds under thunderstorm base"),
        ("Shelf cloud", "Low horizontal wedge at storm front"),
        ("Wall cloud", "Lowering cloud base of severe thunderstorm"),
        ("Funnel cloud", "Rotating cone not touching ground"),
        ("Tornado", "Violent rotating column touching ground"),
        ("Waterspout", "Tornado over water"),
        ("Fire whirl", "Rotating column of flame and ash"),
        ("Dust devil", "Small rotating column of dust"),
        ("Sandstorm", "Strong wind carrying sand"),
        ("Haboob", "Intense sandstorm wall in desert"),
        ("Thundersnow", "Thunderstorm with snow instead of rain"),
        ("Ice storm", "Rain freezing on surfaces"),
        ("Freezing fog", "Fog freezing on surfaces"),
        ("Graupel", "Soft hail, snow pellets"),
        ("Virga", "Rain evaporating before reaching ground"),
        ("Microburst", "Strong localized downdraft"),
        ("Derecho", "Widespread long-lived straight-line wind storm"),
        ("Polar vortex", "Large area of low pressure at poles"),
        ("Katabatic wind", "Dense cold air flowing downhill"),
        ("Chinook wind", "Warm dry wind down Rocky Mountains"),
    ]
    name, desc = random.choice(phenomena)
    return "{}: {}".format(name, desc)

def random_science_experiment():
    experiments = [
        ("Michelson-Morley", "1887, disproved luminiferous ether"),
        ("Cavendish experiment", "1797, first measured gravitational constant G"),
        ("Oil drop experiment", "1909, Millikan measured electron charge"),
        ("Double-slit experiment", "Light acts as both wave and particle"),
        ("Stern-Gerlach", "1922, showed spin quantization"),
        ("Photoelectric effect", "Einstein 1905, light as particles"),
        ("Franck-Hertz", "1914, confirmed quantized energy levels"),
        ("Davisson-Germer", "1927, electron diffraction demonstrated wave nature"),
        ("Compton scattering", "1923, photon particle nature confirmed"),
        ("Alpha particle scattering", "Rutherford 1909, discovered atomic nucleus"),
        ("Miller-Urey", "1953, amino acids from primordial soup"),
        ("Meselson-Stahl", "1958, proved DNA semi-conservative replication"),
        ("Hershey-Chase", "1952, confirmed DNA is genetic material"),
        ("Pavlov's dog", "Classical conditioning experiment"),
        ("Milgram experiment", "1961, obedience to authority"),
        ("Stanford prison", "1971, role influence on behavior"),
        ("Asch conformity", "1950s, group pressure on individual"),
        ("Bobo doll experiment", "1961, Bandura social learning"),
        ("Little Albert", "1920, Watson conditioned fear response"),
        ("Harlow's monkeys", "1958, contact comfort over food"),
        ("Tuskegee syphilis", "1932-1972, unethical medical study"),
        ("Luria-Delbruck", "1943, random mutation in bacteria"),
        ("Griffith's experiment", "1928, bacterial transformation"),
        ("Avery-MacLeod-McCarty", "1944, DNA as transforming principle"),
        ("Wohler synthesis", "1828, urea from inorganic, vitalism refuted"),
        ("Pasteur's swan-neck", "1861, disproved spontaneous generation"),
        ("Fleming's mold", "1928, discovered penicillin"),
        ("Galileo's Leaning Tower", "Dropped objects disproving Aristotle"),
        ("Galileo's telescope", "1610, discovered Jupiter's moons"),
        ("Newton's prism", "1666, white light splits into colors"),
        ("Foucault's pendulum", "1851, demonstrated Earth's rotation"),
        ("Joule's paddle wheel", "1843, mechanical equivalent of heat"),
        ("Brownian motion", "1827, random particle movement observed"),
        ("Cloud chamber", "1911, Wilson detected charged particles"),
        ("Geiger-Marsden", "1909, gold foil experiment, nucleus discovery"),
        ("Large Hadron Collider", "2012, discovered Higgs boson"),
        ("LIGO", "2015, first direct gravitational wave detection"),
        ("Event Horizon Telescope", "2019, first black hole image"),
        ("MRNA vaccine trials", "2020, effective COVID-19 vaccines"),
    ]
    name, year, desc = random.choice(experiments)
    return "{} ({}): {}".format(name, year, desc)

def show_help(role=None):
    print("15 - ASCII house            16 - ASCII flower")
    print("17 - ASCII smiley           18 - Fibonacci")
    print("19 - Prime check            20 - Factorial")
    print("21 - GCD                    22 - LCM")
    print("23 - Prime factors          24 - Text analyzer")
    print("25 - Binary                 26 - Hex")
    print("27 - Octal                  28 - Roman numerals")
    print("29 - Temperature conv       30 - Distance conv")
    print("31 - Weight conv            32 - Random password")
    print("33 - Password strength      34 - Pig Latin")
    print("35 - Guess number           36 - Hangman")
    print("37 - Word scramble          38 - Riddle game")
    print("39 - Trivia quiz            40 - Magic 8 ball")
    print("41 - Caesar cipher          42 - Palindrome")
    print("43 - Anagram                44 - BMI calculator")
    print("45 - Zodiac                 46 - Morse code")
    print("47 - Day of week            48 - Leap year")
    print("49 - Multiplication table   50 - Progress bar")
    print("51 - Countdown              52 - Random name")
    print("53 - Coin flip              54 - Dice roll")
    print("55 - Card draw              56 - High/Low game")
    print("57 - Rock paper scissors    58 - Todo manager")
    print("59 - Calendar               60 - Calculator")
    print("61 - Mean/Med/Mode          62 - Std deviation")
    print("63 - Quadratic              64 - Bubble sort")
    print("65 - Binary search          66 - Typing test")
    print("67 - Quote                  68 - More quotes")
    print("69 - Random animal          70 - Random color")
    print("71 - Random fruit           72 - Random vegetable")
    print("73 - Random element         74 - Random number")
    print("75 - Random UUID            76 - ASCII pyramid")
    print("77 - ASCII triangle         78 - ASCII rev triangle")
    print("79 - ASCII hourglass        80 - ASCII circle")
    print("81 - ASCII pineapple        82 - ASCII ghost")
    print("83 - ASCII alien            84 - ASCII bird")
    print("85 - ASCII turtle           86 - ASCII unicorn")
    print("87 - ASCII robot            88 - ASCII spaceship")
    print("89 - ASCII dragon           90 - ASCII crown")
    print("91 - ASCII castle           92 - ASCII mountain")
    print("93 - ASCII wave             94 - ASCII sun")
    print("95 - ASCII moon             96 - ASCII star shape")
    print("97 - ASCII arrow up         98 - ASCII arrow down")
    print("99 - ASCII arrow left       100 - ASCII arrow right")
    print("101 - ASCII DNA             102 - ASCII pacman")
    print("103 - ASCII bowtie          104 - ASCII flag")
    print("105 - ASCII stairs          106 - ASCII table")
    print("107 - ASCII candle          108 - ASCII lamp")
    print("109 - ASCII key             110 - ASCII lock")
    print("111 - ASCII phone           112 - ASCII TV")
    print("113 - ASCII envelope        114 - ASCII coffee")
    print("115 - ASCII burger          116 - ASCII pizza")
    print("117 - ASCII ice cream       118 - ASCII cake")
    print("119 - ASCII house+sun       120 - Convert seconds")
    print("121 - Random data           122 - Shuffle list")
    print("123 - Flatten list          124 - Chunk list")
    print("125 - Unique elements       126 - List intersect")
    print("127 - List union            128 - List difference")
    print("129 - List sym diff         130 - Rotate list")
    print("131 - Find indexes          132 - Split evens/odds")
    print("133 - Sum digits            134 - Reverse number")
    print("135 - Armstrong             136 - Perfect number")
    print("137 - Happy number          138 - Collatz seq")
    print("139 - Sieve of Eratosth     140 - Nth prime")
    print("141 - Goldbach              142 - Euler totient")
    print("143 - Ext GCD               144 - Mod inverse")
    print("145 - Matrix multiply       146 - Transpose")
    print("147 - Matrix det            148 - Dot product")
    print("149 - Cross product         150 - Vector magnitude")
    print("151 - Euclid distance       152 - Manhattan dist")
    print("153 - Hamming dist          154 - Levenshtein")
    print("155 - Base converter        156 - SHA256 hash")
    print("157 - MD5 hash              158 - Base64 encode")
    print("159 - Base64 decode         160 - ROT13")
    print("161 - Text to ASCII         162 - ASCII to text")
    print("163 - Count words           164 - Count sentences")
    print("165 - Count paragraphs      166 - Remove dup words")
    print("167 - Reverse words         168 - Sort words")
    print("169 - Shuffle words         170 - Acronym")
    print("171 - Capitalize title      172 - Detect language")
    print("173 - Spell check           174 - Word frequency")
    print("175 - Longest word          176 - Shortest word")
    print("177 - Common letter         178 - Has URL")
    print("179 - Has email             180 - Extract numbers")
    print("181 - Extract emails        182 - Extract URLs")
    print("183 - Remove HTML tags      184 - Censor words")
    print("185 - Suggest emoji         186 - Format JSON")
    print("187 - Count JSON elements   188 - CSV to list")
    print("189 - Dice roll sim         190 - Coin flip sim")
    print("191 - Lottery sim           192 - Birthday paradox")
    print("193 - Monty Hall sim        194 - Morse to text")
    print("195 - Atbash cipher         196 - Vigenere cipher")
    print("197 - XOR cipher            198 - Substitution cipher")
    print("199 - Nerd dice             200 - Poker hand")
    print("201 - Goldbach format       202 - Number facts")
    print("203 - Temp summary          204 - Days til birthday")
    print("205 - Days since birth      206 - Age in seconds")
    print("207 - Current time info     208 - Week number")
    print("209 - Day of year           210 - Next full moon")
    print("211 - Moon phase            212 - Horoscope")
    print("213 - Numerology            214 - Chinese zodiac")
    print("215 - Tarot                 216 - Crystal ball")
    print("217 - Coffee grounds        218 - Magic spell")
    print("219 - Country info          220 - World clock")
    print("221 - Countdown to NY       222 - Countdown Xmas")
    print("223 - Random movie          224 - Random book")
    print("225 - Random song           226 - Random recipe")
    print("227 - Random hobby          228 - Workout")
    print("229 - Meditation guide      230 - BMI calc")
    print("231 - Tip calculator        232 - Loan calculator")
    print("233 - Savings calculator    234 - Unit converter")
    print("235 - Discount calculator   236 - Currency converter")
    print("237 - Planet info           238 - Astronomy fact")
    print("239 - Weather fact          240 - Ocean fact")
    print("241 - Space mission fact     242 - Number guessing 2")
    print("243 - Color quiz            244 - Fruit quiz")
    print("245 - Animal quiz           246 - Country quiz")
    print("247 - Random emoji          248 - Random planet")
    print("249 - Random galaxy         250 - Random star")
    print("251 - Random asteroid       252 - Random comet")
    print("253 - Random nebula         254 - Random quasar")
    print("255 - Random black hole")
    print("256 - Capital city quiz     257 - Flag quiz")
    print("258 - Math quiz             259 - Science quiz")
    print("260 - History quiz          261 - Geography quiz")
    print("262 - Programming quiz      263 - Random emoji")
    print("264 - Random constellation  265 - Random dinosaur")
    print("266 - Random flower         267 - Random gemstone")
    print("268 - Mythical creature     269 - Planet type")
    print("270 - Chemical reaction     271 - Mathematician")
    print("272 - Biologist             273 - Physicist")
    print("274 - Inventor              275 - Planet weight")
    print("276 - Solar age             277 - Space distance")
    print("278 - Apollo missions       279 - Rocket facts")
    print("280 - Mars facts            281 - Jupiter facts")
    print("282 - Deep space fact       283 - Random moon")
    print("284 - Random exoplanet      285 - ISS crew")
    print("286 - Asteroid belt         287 - Tic Tac Toe")
    print("288 - Connect Four          289 - Word search")
    print("290 - Number puzzle         291 - Memory game")
    print("292 - Reaction game         293 - Binary search game")
    print("294 - Word association      295 - Rapid math")
    print("296 - Movie trivia          297 - Music trivia")
    print("298 - Sports trivia         299 - Art trivia")
    print("300 - Food trivia           301 - Animal trivia")
    print("302 - Tech trivia           303 - Nature trivia")
    print("304 - Random trivia         305 - Random sentence")
    print("306 - Random poem           307 - Haiku")
    print("308 - Tongue twister        309 - Proverb")
    print("310 - Idiom                 311 - Simile")
    print("312 - Metaphor              313 - Oxymoron")
    print("314 - Palindrome word       315 - Anagra")
    print("316 - Chessboard            317 - Sierpinski")
    print("318 - Radial star           319 - Spiral")
    print("320 - Maze                  321 - Target")
    print("322 - Snowflake             323 - Fractal tree")
    print("324 - Flower garden         325 - Cross")
    print("326 - Fence                 327 - Railroad")
    print("328 - Tunnel                329 - Lighthouse")
    print("330 - Rocket                331 - Submarine")
    print("332 - Helicopter            333 - Airplane")
    print("334 - Bicycle               335 - Umbrella")
    print("336 - Compass               337 - Web")
    print("338 - Bridge                339 - Castle tower")
    print("340 - Sword                 341 - Shield")
    print("342 - Anchor                343 - Crown king")
    print("344 - Throne")
    print("345 - HubBasePE (launch PE)")
    print("346 - Random country        347 - Country continent")
    print("348 - World population       349 - Largest cities")
    print("350 - World rivers           351 - World mountains")
    print("352 - World deserts          353 - World islands")
    print("354 - World lakes            355 - World wonders")
    print("356 - World currencies       357 - Flag description")
    print("358 - Random story           359 - Programming joke")
    print("360 - Animal joke            361 - Food joke")
    print("362 - Science joke           363 - Sports joke")
    print("364 - Music joke             365 - Math joke")
    print("366 - History joke           367 - Dad joke")
    print("368 - Conversation starter   369 - Philosophy question")
    print("370 - Nobel Prize            371 - Historic event")
    print("372 - Philosopher            373 - Scientific law")
    print("374 - Programming language   375 - Algorithm")
    print("376 - Data structure         377 - Tech company")
    print("378 - Historical figure      379 - World record")
    print("380 - Math fact              381 - Chemistry fact")
    print("382 - Biology fact           383 - Physics fact")
    print("384 - Geography fact         385 - Astronomy fact")
    print("386 - Psychology fact        387 - Technology fact")
    print("388 - Geology fact           389 - Sports fact")
    print("390 - Music fact             391 - Art fact")
    print("392 - Medicine fact          393 - Economics fact")
    print("394 - Literature fact        395 - Random movie")
    print("396 - Random song            397 - Random book")
    print("398 - Cocktail recipe        399 - Board game")
    print("400 - Video game             401 - TV show")
    print("402 - Space mission          403 - Country fact")
    print("404 - Language fact          405 - Food fact")
    print("406 - Animal fact            407 - Ocean fact")
    print("408 - Moon fact              409 - Weather fact")
    print("410 - Invention              411 - Random quote")
    print("412 - Holiday                413 - Random joke")
    print("414 - Puzzle                 415 - AI fact")
    print("416 - Quantum fact           417 - Space object")
    print("418 - Human body fact        419 - Architecture")
    print("420 - Energy fact            421 - Mythology fact")
    print("422 - Ocean life fact        423 - Mountain fact")
    print("424 - River fact             425 - Desert fact")
    print("426 - Forest fact            427 - Volcano fact")
    print("428 - City fact              429 - Flag fact")
    print("430 - Number fact            431 - History fact")
    print("432 - Lake fact              433 - Island fact")
    print("434 - Planet fact            435 - Ocean fact II")
    print("436 - Culture fact           437 - Famous landmark")
    print("438 - Weather phenomenon     439 - Science experiment")
    print("440 - Engineering fact       441 - Medicine fact II")
    print("442 - Bridge fact            443 - Tunnel fact")
    print("444 - Animal speed fact      445 - Unusual ability")
    print("446 - Dinosaur fact")
    print("447 - Space mission deep     448 - Natural disaster")
    print("449 - Climate fact            450 - Chemical element")
    print("451 - Programming term        452 - Festival")
    print("453 - Renewable energy fact")
    print()
    if role:
        print("=== {} COMMANDS ===".format(role))
        if role == "Admin":
            print("system_info - System information")
            print("list_users  - List online users")
            print("clear_logs  - Clear system logs")
            print("toggle_debug - Toggle debug mode")
        elif role == "Mod":
            print("featured_joke - Show featured joke")
            print("mute_user     - Mute a user")
            print("warn_user     - Warn a user")
        elif role == "Vip":
            print("vip_fact  - VIP exclusive fact")
            print("vip_quote - VIP exclusive quote")
        print()
    print("h  - Show this help")
    print("q  - Quit")
    print()

def check_role(pw):

    if pw == "A-52-80-A":
        return "Admin"
    if pw == "M-5280-M":
        return "Mod"
    if pw == "5280":
        return "Vip"
    return None

debug_mode = False

def toggle_debug():
    global debug_mode
    debug_mode = not debug_mode
    return "Debug mode is now {}.".format("ON" if debug_mode else "OFF")

def get_role_commands(role):
    if role == "Admin":
        return ["system_info", "list_users", "clear_logs", "toggle_debug", "reload_config"]
    if role == "Mod":
        return ["mute_user", "warn_user", "featured_joke", "pin_message"]
    if role == "Vip":
        return ["vip_joke", "vip_quote", "vip_fact", "skip_ad"]
    return []

def role_badge(role):
    badges = {"Admin": "[ADMIN]", "Mod": "[MOD]", "Vip": "[VIP]"}
    return badges.get(role, "")

def admin_system_info():
    import platform
    return "System: {}\nNode: {}\nPython: {}\nPlatform: {}".format(
        platform.system(), platform.node(), platform.python_version(), platform.platform())

def admin_list_users():
    return "Online users: you ({})".format("Admin")

def mod_featured_joke():
    return "FEATURED JOKE: Why did the Admin cross the road? To change permissions on the other side!"

def vip_extra_fact():
    return "VIP FACT: You are valued! Did you know? The first computer bug was a real moth."

def vip_extra_quote():
    return "VIP QUOTE: 'With great power comes great responsibility.' - Uncle Ben"

def random_engineering_fact():
    facts = [
        ("Brooklyn Bridge", "1883, longest suspension bridge then, 486m span"),
        ("Golden Gate Bridge", "1937, 1,280m suspension, international orange"),
        ("Channel Tunnel", "1994, 50.5km undersea tunnel, UK-France"),
        ("Panama Canal", "1914, 82km, connects Atlantic and Pacific"),
        ("Suez Canal", "1869, 193km, connects Med and Red Sea"),
        ("Hoover Dam", "1936, 221m concrete arch-gravity, 2GW power"),
        ("Three Gorges Dam", "2012, 181m, 22.5GW, largest power station"),
        ("Itaipu Dam", "1984, Brazil/Paraguay, 14GW"),
        ("Millau Viaduct", "2004, France, 343m tallest bridge pillar"),
        ("Akashi Kaikyo Bridge", "1998, Japan, 1,991m longest suspension span"),
        ("Palm Islands", "Dubai, artificial archipelago, visible from space"),
        ("Burj Al Arab", "1999, Dubai, 321m sail-shaped hotel"),
        ("International Space Station", "1998, 109m x 73m, 16 countries"),
        ("Large Hadron Collider", "2008, CERN, 27km circumference tunnel"),
        ("ITTOPF", "Floating platform for oil drilling"),
        ("Falkirk Wheel", "2002, Scotland, rotating boat lift"),
        ("Pao de Acucar cable car", "Rio, 1912, first aerial cable car in Brazil"),
        ("Eiffel Tower", "1889, 300m, 18,038 iron parts, 2.5M rivets"),
        ("Sydney Harbour Bridge", "1932, 1,149m steel arch, coat hanger"),
        ("CN Tower", "1976, Toronto, 553m communications tower"),
        ("Empire State Building", "1931, NYC, 381m, art deco, 102 floors"),
        ("Transamerica Pyramid", "1972, San Francisco, 260m, 48 floors"),
        ("Petronas Towers", "1998, KL, 452m twin towers, skybridge"),
        ("Taipei 101", "2004, Taiwan, 509m, damper tuned mass"),
        ("Shanghai Tower", "2015, 632m, twisted 120 degrees"),
        ("Burj Khalifa", "2010, Dubai, 828m, 163 floors"),
        ("Singapore Changi Airport", "Jewel waterfall, 2019, stunning architecture"),
        ("Denver International Airport", "Largest US airport, 137 km\u00b2"),
        ("King's Cross Station", "London, 1852, Harry Potter platform 9 3/4"),
        ("Guggenheim Bilbao", "1997, titanium curves, Frank Gehry"),
        ("Sydney Opera House", "1973, 1M+ roof tiles, sail shells"),
        ("Taj Mahal", "1653, marble inlay, Mughal engineering marvel"),
        ("Hagia Sophia", "537 AD, Istanbul, massive dome, cathedral/mosque"),
        ("Pantheon", "125 AD, Rome, unreinforced concrete dome, 43m span"),
        ("Roman aqueducts", "~500km total, gravity-fed water system"),
        ("Great Wall of China", "21,196km, watchtowers and fortifications"),
        ("Machu Picchu", "1450, Inca, dry stone construction, earthquake-proof"),
        ("Sukkur barrage", "1932, Pakistan, 1.4km across River Indus"),
        ("James Webb Space Telescope", "2021, 6.5m mirror, origami sunshield"),
        ("Apollo Saturn V", "1967, 110m tall, 2.8M kg thrust, 13 moon missions"),
    ]
    name, year, desc = random.choice(facts)
    return "{} ({}): {}".format(name, year, desc)

def random_medicine_fact_deep():
    facts = [
        ("Heart surgery", "First open heart 1953, bypass surgery 1960s"),
        ("Organ transplant", "First kidney 1954, heart 1967, liver 1967"),
        ("Stem cell therapy", "Bone marrow transplant 1968, first blood stem cells"),
        ("Gene therapy", "First approved 1990, ADA deficiency"),
        ("Immunotherapy", "Checkpoint inhibitors since 2011"),
        ("CAR-T cells", "Engineered immune cells attack cancer"),
        ("Antibiotics", "Penicillin 1928, golden age 1940-1960"),
        ("Vaccines", "Smallpox 1796, polio 1955, MMR 1971"),
        ("mRNA vaccines", "COVID-19 2020, revolutionary platform technology"),
        ("Insulin", "Discovered 1921, first protein sequenced"),
        ("Statins", "Cholesterol-lowering, 1987, Lipitor best-seller"),
        ("Aspirin", "1897, still widely used for pain and heart"),
        ("Anesthesia", "Ether 1846, revolutionized surgery"),
        ("X-rays", "1895 by Rontgen, first medical imaging"),
        ("CT scan", "1971, 3D X-ray, Hounsfield Nobel 1979"),
        ("MRI", "1973, Lauterbur, no radiation"),
        ("Ultrasound", "1950s, prenatal imaging"),
        ("PET scan", "1970s, metabolic imaging"),
        ("ECG", "1903, Einthoven, Nobel 1924"),
        ("Defibrillator", "1947, restores normal heart rhythm"),
        ("Pacemaker", "1958, implanted to regulate heartbeat"),
        ("Heart-lung machine", "1953, enabled open-heart surgery"),
        ("Dialysis", "1943, Kolff, kidney failure treatment"),
        ("Ventilator", "Iron lung 1928, modern ICU ventilators"),
        ("Prosthetics", "Ancient peg legs, modern bionic limbs"),
        ("Cochlear implant", "1972, restores hearing"),
        ("Retinal implant", "Argus II 2013, restores partial vision"),
        ("Vaccination schedule", "Childhood vaccines prevent 4M deaths/year"),
        ("Herd immunity", "Population protection through vaccination"),
        ("Antiseptic", "Lister 1867, carbolic acid, reduced infection"),
        ("Hygiene", "Semmelweis 1847, handwashing saves lives"),
        ("Sanitation", "Clean water prevents cholera and typhoid"),
        ("Eradication", "Smallpox eradicated 1980, polio nearly"),
        ("Tuberculosis", "1.5M deaths/year, drug-resistant strains"),
        ("Malaria", "619K deaths 2021, insecticide nets"),
        ("HIV/AIDS", "Peaked 2004, now manageable with ART"),
        ("Cancer", "Leading causes: lung, breast, colorectal"),
        ("Alzheimer's", "60-70% of dementia, no cure"),
        ("Diabetes", "537M adults, growing epidemic"),
        ("Obesity", "650M adults, BMI >30, global crisis"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_bridge_fact():
    facts = [
        ("Golden Gate Bridge", "San Francisco, 1,280m, 1937"),
        ("Brooklyn Bridge", "NYC, 486m, 1883, Gothic towers"),
        ("Tower Bridge", "London, 244m, 1894, bascule lift"),
        ("Millau Viaduct", "France, 2,460m, 2004, 343m tallest pillar"),
        ("Akashi Kaikyo", "Japan, 1,991m, 1998, longest suspension span"),
        ("Great Belt Bridge", "Denmark, 1,624m, 1998"),
        ("Runyang Bridge", "China, 1,490m, 2005"),
        ("Yi Sun-sin Bridge", "South Korea, 1,545m, 2012"),
        ("Xihoumen Bridge", "China, 1,650m, 2007"),
        ("Humber Bridge", "UK, 1,410m, 1981, longest in UK"),
        ("Verrazzano-Narrows", "NYC, 1,298m, 1964, connecting Brooklyn-Staten Isl"),
        ("Forth Bridge", "Scotland, 2,529m, 1890, cantilever rail"),
        ("Sydney Harbour Bridge", "1,149m, 1932, steel arch"),
        ("Harbor Bridge", "Bangkok, 1965"),
        ("Ponte Vecchio", "Florence, 1345, shops built on it"),
        ("Rialto Bridge", "Venice, 1591, stone arch across Grand Canal"),
        ("Charles Bridge", "Prague, 1402, 516m, 30 statues"),
        ("Stari Most", "Mostar, 1566, rebuilt 2004 after war"),
        ("Khaju Bridge", "Isfahan, 1650, bridge and dam"),
        ("Sidu River Bridge", "China, 1,222m, 496m highest deck"),
        ("Duge Bridge", "China, 565m high, 1340m span, 2016"),
        ("Baluarte Bridge", "Mexico, 1,124m, 403m high, 2012"),
        ("Royal Gorge Bridge", "USA, 384m, 291m above river, 1929"),
        ("Mackinac Bridge", "Michigan, 1,158m, 1957"),
        ("Sunshine Skyway", "Florida, 366m, 1987 cable-stayed"),
        ("Confederation Bridge", "Canada, 12.9km, 1997, fixed link PEI"),
        ("Oresund Bridge", "Denmark-Sweden, 7.8km, 2000, road and rail"),
        ("Tsing Ma Bridge", "Hong Kong, 1,377m, 1997, road and rail"),
        ("Lupu Bridge", "Shanghai, 550m, 2003, steel arch"),
        ("Chaotianmen Bridge", "Chongqing, 552m, 2009, longest steel arch"),
        ("Pont Alexandre III", "Paris, 107m, 1900, Beaux-Arts"),
        ("Mostar Bridge", "Bosnia, 1566, rebuilt symbol of unity"),
        ("Ponte 25 de Abril", "Lisbon, 2,277m, 1966, suspension"),
        ("Rio-Antirrio", "Greece, 2,252m, 2004, cable-stayed"),
        ("Vasco da Gama", "Lisbon, 17.2km, 1998, longest in Europe"),
        ("Padma Bridge", "Bangladesh, 6.15km, 2022"),
        ("Hong Kong-Zhuhai-Macao", "55km, 2018, longest sea crossing"),
        ("Danyang-Kunshan", "China, 164.8km, 2011, longest bridge of any kind"),
        ("Penang Bridge", "Malaysia, 13.5km, 1985"),
        ("Tengger-Skywalk", "China, glass-bottom bridge, 120m high"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_tunnel_fact():
    facts = [
        ("Channel Tunnel", "50.5km, 1994, UK-France, undersea"),
        ("Gotthard Base Tunnel", "57.1km, 2016, Swiss Alps, longest rail tunnel"),
        ("Seikan Tunnel", "53.9km, 1988, Japan, second longest, undersea"),
        ("Eurotunnel", "37.9km, undersea Channel Tunnel"),
        ("Lotschberg Base Tunnel", "34.6km, 2007, Switzerland"),
        ("New Guanjiao", "32.6km, 2014, China, highest altitude rail tunnel"),
        ("Yulhyeon Tunnel", "50.3km, 2016, South Korea"),
        ("Laerdal Tunnel", "24.5km, 2000, Norway, longest road tunnel"),
        ("Zhongnanshan", "18km, 2007, China, longest 2-lane"),
        ("Jinpingshan", "17.5km, 2012, China"),
        ("St. Gotthard Road Tunnel", "16.9km, 1980, Switzerland"),
        ("Mount Blanc Tunnel", "11.6km, 1965, France-Italy"),
        ("Fréjus Road Tunnel", "12.9km, 1980, France-Italy"),
        ("Mt. Baker Ridge", "1.3km, 1990, Seattle, largest diameter at 24m"),
        ("Eiksund Tunnel", "7.8km, 2008, Norway, -287m undersea deepest"),
        ("Ryfylke Tunnel", "14.5km, 2019, Norway, -292m deepest subsea"),
        ("Bømlafjord Tunnel", "7.9km, 2000, Norway"),
        ("Oslofjord Tunnel", "7.2km, 2000, Norway"),
        ("Hvalfjordur Tunnel", "5.8km, 1998, Iceland"),
        ("Eisenhower Tunnel", "2.7km, 1973, Colorado, 3,401m highest in US"),
        ("Holland Tunnel", "2.6km, 1927, NYC, first underwater vehicular"),
        ("Lincoln Tunnel", "2.4km, 1937, NYC"),
        ("Queens-Midtown Tunnel", "1.9km, 1940, NYC"),
        ("Brooklyn-Battery Tunnel", "2.8km, 1950, NYC, longest in US urban"),
        ("Antelope Hills", "1.7km, 1964, Arizona"),
        ("Ted Williams Tunnel", "1.2km, 1995, Boston"),
        ("Alameda Sains", "1.1km, 194o, Mexico City"),
        ("Tunnel of Eupalinos", "1km, 520 BC, Samos Greece, ancient engineering"),
        ("Appian Way", "Roman tunnels for roads, ~300 BC"),
        ("Fenghuoshan Tunnel", "1.3km, 2005, China, 4,905m highest railway"),
        ("Musha Tunnel", "20 km, 1998, Japan"),
        ("Oakland Bay Bridge", "tunnel portion, Yerba Buena Island"),
        ("Mersey Tunnel", "3.2km, 1971, Liverpool"),
        ("Dartford Crossing", "3.6km, 1963, London orbital"),
        ("Blackwall Tunnel", "2.5km, 1897, London"),
        ("Rotherhithe Tunnel", "1.5km, 1908, London"),
        ("Kanonersky Tunnel", "1.7km, 1986, St. Petersburg"),
        ("Santo Domingo Tunnel", "1.2km, Metro tunnel"),
        ("Crossrail", "21km, 2022, London Elizabeth Line"),
        ("Seoul Subway Tunnel", "deepest in Seoul metro"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_animal_speed_fact():
    facts = [
        ("Peregrine falcon", "389 km/h dive, fastest animal"),
        ("Golden eagle", "320 km/h dive"),
        ("White-throated needletail", "169 km/h horizontal flight"),
        ("Frigatebird", "153 km/h, highest speed-to-size ratio"),
        ("Spur-winged goose", "142 km/h, fastest bird in level flight"),
        ("Cheetah", "120 km/h land sprint, 0-100 in 3 sec"),
        ("Pronghorn antelope", "88 km/h, second fastest land"),
        ("Springbok", "88 km/h, leaps 4m high"),
        ("Wildebeest", "80 km/h, migration endurance"),
        ("Lion", "80 km/h, short burst hunter"),
        ("Blackbuck", "80 km/h, Indian antelope"),
        ("Brown hare", "72 km/h"),
        ("Horse", "72 km/h, thoroughbred"),
        ("Greyhound", "72 km/h, breed for racing"),
        ("Jackrabbit", "72 km/h"),
        ("Hyena", "60 km/h, pack hunter"),
        ("Zebra", "65 km/h, zigzag escape"),
        ("Grizzly bear", "56 km/h, surprisingly fast"),
        ("Elephant", "40 km/h despite 6 ton weight"),
        ("Black marlin", "129 km/h fastest fish"),
        ("Sailfish", "110 km/h, billfish family"),
        ("Swordfish", "97 km/h"),
        ("Yellowfin tuna", "76 km/h"),
        ("Porpoise", "56 km/h, fastest marine mammal"),
        ("Mako shark", "74 km/h, fastest shark"),
        ("Atlantic bluefin", "70 km/h"),
        ("Killer whale", "56 km/h, apex predator"),
        ("Dolphin", "60 km/h"),
        ("Giant tortoise", "0.3 km/h, slowest reptile"),
        ("Three-toed sloth", "0.24 km/h, slowest mammal"),
        ("Garden snail", "0.05 km/h, slowest animal"),
        ("Hummingbird", "385 body lengths/sec, fastest relative speed"),
        ("Gekko", "1m in 0.1 sec for tongue strike"),
        ("Mantis shrimp", "80 km/h punch acceleration"),
        ("Trap-jaw ant", "230 km/h jaw snap speed"),
        ("Boa constrictor", "Strikes at 2.7 m/s"),
        ("Cuttlefish", "Reacts in milliseconds, color change"),
        ("Archerfish", "Spits water at 2m/s at insects"),
        ("Chameleon", "Tongue at 5.8 m/s projectile"),
        ("Sea horse", "Slowest fish at 0.001 km/h"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_unusual_ability():
    abilities = [
        ("Echidna", "Lays eggs, but is a mammal (monotreme)"),
        ("Platypus", "Venomous spur, lays eggs, electroreception"),
        ("Tardigrade", "Survives -272C to 150C, radiation, vacuum, years without water"),
        ("Axolotl", "Regrows entire limbs, spinal cord, heart parts"),
        ("Immortal jellyfish", "Can revert to juvenile stage indefinitely"),
        ("Mimic octopus", "Imitates 15+ species including lionfish, flatfish, sea snakes"),
        ("Electric eel", "Generates 600V shocks, uses as radar"),
        ("Archerfish", "Shoots water jets up to 2m to knock insects into water"),
        ("Cheetah", "0 to 100 km/h in 3 seconds"),
        ("Chameleon", "Eyes move independently 360 degree, tongue at 5.8 m/s"),
        ("Trap-jaw ant", "Jaws snap at 230 km/h, fastest animal appendage"),
        ("Pistol shrimp", "Claw snaps at 4,400C for split second, creates cavitation"),
        ("Leaf-tailed gecko", "Perfect camouflage blending into tree bark"),
        ("Dragonfly", "Wings beat independently, hover, fly backward, 80% brain for vision"),
        ("Hummingbird", "Wings beat 80/s, only bird to fly backward"),
        ("Giraffe", "Neck 2.4m, 6 vertebrae like humans, 1.8m neck"),
        ("Giant panda", "False thumb for bamboo gripping"),
        ("Sloth", "Algae grows on fur for camouflage, metabolism extremely slow"),
        ("Ant", "Carries 50-100x body weight"),
        ("Dung beetle", "Strongest insect, pulls 1,141x body weight"),
        ("Bombardier beetle", "Sprays boiling chemicals at 100C from abdomen"),
        ("Pufferfish", "Inflates with water, deadly tetrodotoxin"),
        ("Poison dart frog", "One frog has enough toxin to kill 10 men"),
        ("Box jellyfish", "Most venomous, 24 eyes, active swimmer"),
        ("Star-nosed mole", "22 pink tentacles on nose, touches objects in 10ms"),
        ("Naked mole rat", "Feels no pain, cancer-resistant, lives 30+ years"),
        ("Planarian worm", "Splits into two, each regenerates full body"),
        ("Cicada", "17-year life cycle, spends most underground"),
        ("Spider silk", "Stronger than steel by weight, more elastic than nylon"),
        ("Baobab tree", "Stores 120K liters of water in trunk"),
        ("Venus flytrap", "Snap trap triggers in 100ms, counts touches"),
        ("Mimosa pudica", "Folds leaves instantly when touched"),
        ("Luna moth", "No mouth, lives only one week, just to mate"),
        ("Hatchetfish", "Bioluminescent underside, mimics sunlight to hide"),
        ("Eel", "Swims backwards, lives in freshwater but spawns in ocean"),
        ("Arctic tern", "Migrates 72,000 km annually, poles to poles"),
        ("Albatross", "Wingspan 3.5m, glides for hours without flapping"),
        ("Siberian tiger", "Weighs 300+ kg, survives -50C winters"),
        ("Camel", "Hump stores fat not water, goes weeks without water"),
        ("Koala", "Sleeps 20 hours/day, eats toxic eucalyptus"),
    ]
    name, ability = random.choice(abilities)
    return "{}: {}".format(name, ability)

def random_dinosaur_fact_deep():
    facts = [
        ("Tyrannosaurus Rex", "12m long, 8 tons, powerful jaws 12,000 lbs bite"),
        ("Triceratops", "9m, 12 tons, 3 horns, frill defense"),
        ("Stegosaurus", "9m, 5 tons, plates on back, tail spikes"),
        ("Brachiosaurus", "26m, 58 tons, long neck, tallest dinosaur"),
        ("Velociraptor", "2m, 15kg, feathered, intelligent pack hunter"),
        ("Spinosaurus", "18m, 20 tons, largest carnivorous, sail back"),
        ("Ankylosaurus", "9m, 6 tons, armored body, club tail"),
        ("Diplodocus", "27m, 15 tons, extremely long tail"),
        ("Parasaurolophus", "10m, 4 tons, head crest for communication"),
        ("Pterodactyl", "Wingspan 10m, not a dinosaur but pterosaur"),
        ("Mosasaurus", "18m, marine reptile, apex ocean predator"),
        ("Plesiosaurus", "15m, long neck, four flippers"),
        ("Allosaurus", "12m, 2.5 tons, dominant predator of late Jurassic"),
        ("Apatosaurus", "22m, 25 tons, former Brontosaurus"),
        ("Iguanodon", "10m, 5 tons, thumb spike defense"),
        ("Carnotaurus", "8m, 1.5 tons, two horns above eyes"),
        ("Giganotosaurus", "13m, 8 tons, larger than T-Rex"),
        ("Carcharodontosaurus", "12m, 7 tons, shark-toothed lizard"),
        ("Deinonychus", "3.4m, 80kg, sickle claw, raptor inspiration"),
        ("Gallimimus", "6m, 400kg, ostrich-like, fastest dinosaur"),
        ("Oviraptor", "2m, 35kg, beaked, brooded eggs"),
        ("Protoceratops", "2m, 200kg, early horned dinosaur"),
        ("Pachycephalosaurus", "4.5m, 500kg, dome-headed"),
        ("Therizinosaurus", "10m, 5 tons, 1m claws on arms"),
        ("Compsognathus", "1m, 3kg, one of smallest dinosaurs"),
        ("Microraptor", "0.8m, 1kg, four wings, gliding ability"),
        ("Dilophosaurus", "6m, 500kg, two head crests, spitter in movies"),
        ("Baryonyx", "9m, 2 tons, fish-eater, crocodile-like jaws"),
        ("Megalosaurus", "9m, 1.5 tons, first dinosaur named (1824)"),
        ("Coelophysis", "3m, 30kg, early dinosaur, Triassic"),
        ("Titanosaurus", "15-30m, 15-70 tons, massive sauropod"),
        ("Argentinosaurus", "35m, 90 tons, one of largest ever"),
        ("Mamenchisaurus", "26m, neck 11m, longest neck of any dinosaur"),
        ("Euoplocephalus", "5m, 2.5 tons, armored with tail club"),
        ("Corythosaurus", "9m, 4 tons, helmet-like head crest"),
        ("Velociraptor", "featured in Jurassic Park but much larger than real"),
        ("Troodon", "2.5m, 50kg, highest brain-to-body ratio"),
        ("K-T extinction", "66M years ago, asteroid caused mass extinction"),
        ("Dinosaur era", "Mesozoic Era: Triassic, Jurassic, Cretaceous"),
        ("Birds as dinosaurs", "Modern birds evolved from theropod dinosaurs"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_space_misson_deep():
    missions = [
        ("Apollo 8", "1968, first humans to orbit the Moon, iconic Earthrise photo"),
        ("Apollo 11", "1969, first Moon landing, Armstrong and Aldrin"),
        ("Apollo 13", "1970, 'Houston we have a problem', successful failure"),
        ("Apollo 17", "1972, last Moon landing, first geologist on Moon"),
        ("Skylab", "1973-1979, first US space station"),
        ("Space Shuttle", "1981-2011, reusable orbiter, 135 missions"),
        ("Challenger", "1986, disaster 73 sec after launch, 7 crew lost"),
        ("Columbia", "2003, disaster on re-entry, 7 crew lost"),
        ("Hubble repair", "1993-2009, 5 servicing missions, saved Hubble"),
        ("Mir space station", "1986-2001, Soviet/Russian, 15 years"),
        ("International Space Station", "1998-present, 16 countries, continuous habitation"),
        ("Mars Pathfinder", "1997, first Mars rover Sojourner"),
        ("Mars Exploration Rovers", "2004, Spirit and Opportunity, 15+ year mission"),
        ("Mars Science Laboratory", "2012, Curiosity rover, 1.5 billion cost"),
        ("Mars 2020", "2021, Perseverance rover and Ingenuity helicopter"),
        ("Viking 1 and 2", "1976, first US Mars landers"),
        ("Mars Reconnaissance Orbiter", "2006, high-resolution Mars imaging"),
        ("MAVEN", "2014, Mars atmosphere study"),
        ("Mars Express", "2003, European orbiter, found water ice"),
        ("ExoMars", "2016, ESA/Roscosmos, trace gas orbiter"),
        ("Venus Express", "2005, ESA, studied Venus atmosphere for 8 years"),
        ("Magellan", "1989, mapped Venus surface with radar"),
        ("MESSENGER", "2011, first Mercury orbiter, mapped whole surface"),
        ("BepiColombo", "2018, ESA/JAXA, en route to Mercury"),
        ("Cassini-Huygens", "1997-2017, Saturn system explorer"),
        ("Huygens probe", "2005, landed on Titan, Saturn's moon"),
        ("Galileo", "1989-2003, Jupiter orbiter, first asteroid flyby"),
        ("Juno", "2016-present, Jupiter polar orbiter"),
        ("JUICE", "2023, JUpiter ICy moons Explorer, ESA"),
        ("Europa Clipper", "2024, NASA, studying Europa ocean"),
        ("New Horizons", "2006-2015, Pluto flyby, now in Kuiper Belt"),
        ("Dawn", "2007-2018, Vesta and Ceres orbiter"),
        ("Rosetta", "2004-2016, comet 67P rendezvous and lander"),
        ("Philae lander", "2014, first comet landing, 60h battery"),
        ("Hayabusa", "2005, Japan, first asteroid sample return"),
        ("Hayabusa2", "2014-2020, Ryugu asteroid sample return"),
        ("OSIRIS-REx", "2016-2023, Bennu asteroid sample return"),
        ("Stardust", "1999-2006, comet Wild 2 sample return"),
        ("Genesis", "2001-2004, solar wind sample return"),
        ("WISE/NEOWISE", "2009, infrared sky survey, asteroid and comet discovery"),
        ("Kepler", "2009-2018, exoplanet discovery, 2,600+ confirmed"),
        ("TESS", "2018-present, exoplanet surveyor"),
        ("James Webb Space Telescope", "2021, infrared, successor to Hubble"),
        ("Chandra", "1999, X-ray observatory"),
        ("Spitzer", "2003-2020, infrared telescope"),
        ("Fermi", "2008, gamma-ray observatory"),
        ("Parker Solar Probe", "2018, touching the Sun at 692K km/h"),
        ("Solar Orbiter", "2020, ESA, studying Sun's poles"),
        ("STEREO", "2006, 3D views of Sun"),
        ("SOHO", "1995, solar observatory, discovered 3,000+ comets"),
        ("Voyager Golden Record", "Messages to space on Voyager 1 and 2"),
    ]
    name, year, desc = random.choice(missions)
    return "{} ({}): {}".format(name, year, desc)

def random_natural_disaster():
    disasters = [
        ("1900 Galveston hurricane", "8,000-12,000 dead, Category 4, US deadliest"),
        ("1970 Bhola cyclone", "300,000-500,000 dead, Bangladesh, deadliest tropical cyclone"),
        ("2004 Indian Ocean tsunami", "227,898 dead, 14 countries, 9.1 earthquake"),
        ("2010 Haiti earthquake", "160,000 dead, 7.0 Mw, Port-au-Prince"),
        ("2005 Kashmir earthquake", "87,000 dead, 7.6 Mw, Pakistan/India"),
        ("2011 Tohoku earthquake/tsunami", "19,759 dead, 9.0 Mw, Fukushima nuclear"),
        ("2008 Sichuan earthquake", "87,587 dead, 7.9 Mw, China"),
        ("1906 San Francisco earthquake", "3,000+ dead, 7.9 Mw, fire destroyed city"),
        ("1985 Mexico City earthquake", "10,000+ dead, 8.0 Mw"),
        ("1999 Izmit earthquake", "17,000+ dead, 7.6 Mw, Turkey"),
        ("1923 Great Kanto earthquake", "142,800 dead, 7.9 Mw, Tokyo/Yokohama"),
        ("2010 Eyjafjallajokull eruption", "Air travel halted 7 days, 20 countries closed"),
        ("1883 Krakatoa eruption", "36,417 dead, loudest sound in history"),
        ("1815 Mount Tambora eruption", "92,000 dead, Year Without Summer"),
        ("1980 Mount St. Helens", "57 dead, largest US volcanic eruption"),
        ("1986 Lake Nyos disaster", "1,746 dead, CO2 release from volcanic lake"),
        ("1931 China floods", "1-4 million dead, Yangtze River floods"),
        ("1887 Yellow River flood", "900,000-2M dead, worst flood in history"),
        ("1998 Yangtze floods", "3,704 dead, 223M affected"),
        ("2010 Pakistan floods", "2,000 dead, 20M affected, $43B damage"),
        ("1928 Okeechobee hurricane", "4,000+ dead, Florida, Category 5"),
        ("2005 Hurricane Katrina", "1,833 dead, $125B damage, New Orleans"),
        ("2013 Typhoon Haiyan", "6,300 dead, Philippines, 315 km/h winds"),
        ("2017 Hurricane Harvey", "107 dead, $125B, Houston catastrophic flooding"),
        ("2017 Hurricane Maria", "3,057 dead, Puerto Rico devastated"),
        ("1908 Tunguska event", "2,000 km\u00b2 forest flattened, airburst 3-10 MT"),
        ("2013 Chelyabinsk meteor", "1,500 injured, airburst 20km, 500 KT"),
        ("2018 Camp Fire", "85 dead, Butte County California, most destructive CA fire"),
        ("2019-2020 Australian bushfires", "34 dead, 18M ha, 1B animals killed"),
        ("2023 Maui wildfires", "100+ dead, Lahaina destroyed"),
        ("1930s Dust Bowl", "Severe drought/dust storms, US Great Plains"),
        ("2003 European heat wave", "70,000+ dead, worst in 500 years"),
        ("2010 Russian heat wave", "56,000 dead, wildfires"),
        ("2021 Pacific Northwest heat wave", "1,000+ dead, Lytton 49.6C Canada"),
        ("1918 Spanish flu", "50M dead, pandemic, 1/3 of world infected"),
        ("COVID-19 pandemic", "7M+ reported deaths, 2019-2023 global pandemic"),
        ("1347-1351 Black Death", "75-200M dead, 30-60% of Europe"),
        ("1984 Bhopal gas leak", "3,000-15,000 dead, worst industrial disaster"),
        ("2011 Deepwater Horizon", "11 dead, 4.9M barrels in Gulf of Mexico"),
        ("1986 Chernobyl", "~4,000 eventual deaths, nuclear disaster"),
        ("2011 Fukushima Daiichi", "Nuclear meltdown after tsunami"),
        ("1979 Three Mile Island", "Partial nuclear meltdown, no direct deaths"),
    ]
    name, detail = random.choice(disasters)
    return "{}: {}".format(name, detail)

def random_climate_fact():
    facts = [
        ("Global temperature rise", "1.2C above pre-industrial levels (2024)"),
        ("CO2 levels", "420+ ppm, highest in 4M years"),
        ("Sea level rise", "~3.7 mm/year, 20cm rise since 1901"),
        ("Arctic sea ice decline", "~13% per decade since 1979"),
        ("Greenland ice melt", "279 billion tons/year lost"),
        ("Antarctic ice melt", "148 billion tons/year lost"),
        ("Glacier retreat", "Almost all glaciers globally shrinking"),
        ("Ocean acidification", "~30% increase in acidity since industrial era"),
        ("Temperature record years", "2023 hottest year, 2016 second hottest"),
        ("Extreme weather increase", "Frequency and intensity rising globally"),
        ("Drought severity", "Increasing in Mediterranean, Africa, western US"),
        ("Wildfire season", "Lengthened, more severe globally"),
        ("Hurricane intensity", "Category 4-5 storms increasing"),
        ("Heavy rainfall", "More intense, increased flooding"),
        ("Heatwaves", "More frequent, longer, hotter"),
        ("Permafrost thaw", "Releasing methane, accelerating warming"),
        ("Methane emissions", "28x stronger greenhouse gas than CO2"),
        ("Nitrous oxide", "300x stronger than CO2, agriculture source"),
        ("Carbon budget", "Remaining ~500 GT CO2 for 1.5C target"),
        ("Paris Agreement", "2015, goal limit warming to 1.5-2C"),
        ("COP meetings", "Annual UN climate conferences since 1995"),
        ("Net zero targets", "Many countries target 2050 net zero emissions"),
        ("Renewable energy growth", "Solar and wind cheapest in many regions"),
        ("Electric vehicle adoption", "~18% of new car sales globally in 2023"),
        ("Deforestation", "10M ha/year lost, major carbon source"),
        ("Reforestation", "Nature-based carbon removal solution"),
        ("Carbon capture", "Direct air capture and CCS technologies"),
        ("Climate feedback loops", "Melting ice reduces albedo, amplifies warming"),
        ("Methane clathrate", "Frozen methane under ocean, risk of release"),
        ("Atlantic Meridional Overturning Circulation", "AMOC slowdown risk"),
        ("Gulf Stream stability", "At weakest in 1,000 years"),
        ("Tipping points", "Irreversible changes after certain thresholds"),
        ("Amazon dieback", "Risk of rainforest becoming savanna"),
        ("Coral reef loss", "90% of reefs may die at 1.5C warming"),
        ("Biodiversity loss", "1M species at risk of extinction"),
        ("Climate refugees", "Estimated 200M+ by 2050"),
        ("Climate adaptation", "Infrastructure, agriculture, coastal protection"),
        ("Green technology", "Falling costs making sustainable choices cheaper"),
        ("Youth climate movement", "Global activism led by young people"),
        ("IPCC reports", "UN scientific authority on climate change"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def random_chemical_element():
    elements = [
        ("Hydrogen", "H, 1, most abundant, 90% of atoms in universe"),
        ("Helium", "He, 2, inert gas, second most abundant"),
        ("Lithium", "Li, 3, lightest metal, batteries"),
        ("Beryllium", "Be, 4, light, strong, X-ray windows"),
        ("Boron", "B, 5, semiconductors, borosilicate glass"),
        ("Carbon", "C, 6, basis of all known life"),
        ("Nitrogen", "N, 7, 78% of air, essential for proteins"),
        ("Oxygen", "O, 8, 21% of air, essential for respiration"),
        ("Fluorine", "F, 9, most reactive element"),
        ("Neon", "Ne, 10, noble gas, red signs"),
        ("Sodium", "Na, 11, reactive metal, table salt NaCl"),
        ("Magnesium", "Mg, 12, lightweight, chlorophyll central atom"),
        ("Aluminum", "Al, 13, most abundant metal in crust"),
        ("Silicon", "Si, 14, semiconductor, computer chips"),
        ("Phosphorus", "P, 15, DNA backbone, ATP energy"),
        ("Sulfur", "S, 16, vulcanization, sulfuric acid production"),
        ("Chlorine", "Cl, 17, disinfectant, bleach"),
        ("Argon", "Ar, 18, inert gas, neon signs"),
        ("Potassium", "K, 19, essential for nerve function"),
        ("Calcium", "Ca, 20, bones, teeth, muscle function"),
        ("Scandium", "Sc, 21, aerospace alloys"),
        ("Titanium", "Ti, 22, strong, lightweight, biocompatible"),
        ("Vanadium", "V, 23, steel alloys"),
        ("Chromium", "Cr, 24, stainless steel, chrome plating"),
        ("Manganese", "Mn, 25, steel production"),
        ("Iron", "Fe, 26, most important industrial metal"),
        ("Cobalt", "Co, 27, battery cathodes, blue pigment"),
        ("Nickel", "Ni, 28, stainless steel, coinage"),
        ("Copper", "Cu, 29, electrical wiring, excellent conductor"),
        ("Zinc", "Zn, 30, galvanizing, battery anodes"),
        ("Gallium", "Ga, 31, melts in hand, semiconductors"),
        ("Germanium", "Ge, 32, semiconductor, fiber optics"),
        ("Arsenic", "As, 33, poison, semiconductor doping"),
        ("Selenium", "Se, 34, photocells, dandruff shampoo"),
        ("Bromine", "Br, 35, liquid nonmetal, flame retardants"),
        ("Krypton", "Kr, 36, noble gas, high-efficiency bulbs"),
        ("Rubidium", "Rb, 37, highly reactive, atomic clocks"),
        ("Strontium", "Sr, 38, red fireworks, bone-seeking"),
        ("Yttrium", "Y, 39, LED phosphors, superconductors"),
        ("Zirconium", "Zr, 40, nuclear fuel cladding"),
        ("Niobium", "Nb, 41, steel alloys, superconducting"),
        ("Molybdenum", "Mo, 42, steel alloys, enzyme cofactor"),
        ("Technetium", "Tc, 43, first man-made element"),
        ("Ruthenium", "Ru, 44, catalyst, hard alloys"),
        ("Rhodium", "Rh, 45, catalytic converters, expensive"),
        ("Palladium", "Pd, 46, catalytic converters, hydrogen storage"),
        ("Silver", "Ag, 47, best conductor, antimicrobial"),
        ("Cadmium", "Cd, 48, batteries, toxic"),
        ("Indium", "In, 49, touch screens, solar cells"),
        ("Tin", "Sn, 50, cans, solder"),
        ("Antimony", "Sb, 51, flame retardants"),
        ("Tellurium", "Te, 52, solar panels, thermoelectric"),
        ("Iodine", "I, 53, disinfectant, thyroid hormone"),
        ("Xenon", "Xe, 54, noble gas, high-intensity lamps"),
        ("Cesium", "Cs, 55, atomic clocks, most electropositive"),
        ("Barium", "Ba, 56, medical X-rays contrast"),
        ("Lanthanum", "La, 57, first lanthanide"),
        ("Cerium", "Ce, 58, catalytic converters, lighter flints"),
        ("Praseodymium", "Pr, 59, magnets, yellow pigment"),
        ("Neodymium", "Nd, 60, strongest permanent magnets"),
        ("Promethium", "Pm, 61, radioactive, glow paint"),
        ("Samarium", "Sm, 62, magnets, nuclear control rods"),
    ]
    name, detail = random.choice(elements)
    return "{}: {}".format(name, detail)

def random_programming_term():
    terms = [
        ("API", "Application Programming Interface - how components talk"),
        ("REST", "Representational State Transfer - web API architecture"),
        ("JSON", "JavaScript Object Notation - lightweight data format"),
        ("XML", "Extensible Markup Language - data format"),
        ("HTTP", "Hypertext Transfer Protocol - web communication"),
        ("HTTPS", "Secure HTTP with encryption (TLS/SSL)"),
        ("DNS", "Domain Name System - translates names to IPs"),
        ("TCP", "Transmission Control Protocol - reliable connection"),
        ("UDP", "User Datagram Protocol - fast, no guarantee"),
        ("IP", "Internet Protocol - addressing and routing"),
        ("SQL", "Structured Query Language - database queries"),
        ("NoSQL", "Non-tabular databases: MongoDB, DynamoDB"),
        ("ORM", "Object-Relational Mapping - bridges code and DB"),
        ("IDE", "Integrated Development Environment"),
        ("Git", "Distributed version control system"),
        ("CI/CD", "Continuous Integration/Continuous Deployment"),
        ("Docker", "Containerization platform"),
        ("Kubernetes", "Container orchestration system"),
        ("Microservices", "Architecture of small independent services"),
        ("Monolith", "Single application that handles all concerns"),
        ("Serverless", "Cloud functions without managing servers"),
        ("Edge computing", "Processing data near the source"),
        ("Cloud computing", "On-demand computing resources over internet"),
        ("SaaS", "Software as a Service - managed software"),
        ("PaaS", "Platform as a Service - managed deployment"),
        ("IaaS", "Infrastructure as a Service - virtual resources"),
        ("OOP", "Object-Oriented Programming paradigm"),
        ("FP", "Functional Programming paradigm"),
        ("AOP", "Aspect-Oriented Programming paradigm"),
        ("MVC", "Model-View-Controller pattern"),
        ("SOLID", "5 principles of object-oriented design"),
        ("DRY", "Don't Repeat Yourself - code reuse principle"),
        ("KISS", "Keep It Simple, Stupid - simplicity principle"),
        ("YAGNI", "You Aren't Gonna Need It - avoid overengineering"),
        ("Design patterns", "Singleton, Factory, Observer, Strategy, etc."),
        ("Algorithmic complexity", "Big O notation"),
        ("Time complexity", "How runtime scales with input size"),
        ("Space complexity", "How memory scales with input size"),
        ("Recursion", "Function calling itself"),
        ("Iteration", "Repeating with loops"),
        ("Memoization", "Caching function results for performance"),
        ("Lazy evaluation", "Compute only when needed"),
        ("Garbage collection", "Automatic memory management"),
        ("Multithreading", "Multiple threads in same process"),
        ("Concurrency", "Multiple tasks making progress simultaneously"),
        ("Parallelism", "Multiple tasks running at exact same time"),
        ("Synchronization", "Coordinating access to shared resources"),
        ("Deadlock", "Threads waiting for each other forever"),
        ("Race condition", "Unpredictable behavior from timing issues"),
    ]
    name, detail = random.choice(terms)
    return "{}: {}".format(name, detail)

def random_festival():
    festivals = [
        ("Diwali", "India, festival of lights, 5 days, lamps and fireworks"),
        ("Holi", "India, festival of colors, spring celebration"),
        ("Christmas", "Worldwide, December 25, gift-giving tradition"),
        ("Hanukkah", "Jewish, 8-day festival of lights"),
        ("Eid al-Fitr", "Islamic, breaking of Ramadan fast"),
        ("Chinese New Year", "China, 15 days, red envelopes and fireworks"),
        ("Songkran", "Thailand, water festival, Thai New Year"),
        ("Oktoberfest", "Germany, beer festival, 16 days"),
        ("Carnival", "Brazil, samba parades, before Lent"),
        ("Mardi Gras", "New Orleans, Fat Tuesday celebrations"),
        ("Day of the Dead", "Mexico, honoring ancestors, Nov 1-2"),
        ("La Tomatina", "Spain, tomato fight festival, August"),
        ("Running of the Bulls", "Spain, Pamplona, San Fermin"),
        ("Glastonbury", "UK, music festival, 5 days"),
        ("Coachella", "USA, music and arts festival, California"),
        ("Burning Man", "USA, Nevada, temporary community, art"),
        ("Edinburgh Fringe", "UK, largest arts festival, August"),
        ("Venice Carnival", "Italy, masks and costumes"),
        ("Rio Carnival", "Brazil, samba schools competition"),
        ("Notting Hill Carnival", "UK, London, Caribbean street festival"),
        ("Mardi Gras", "US, New Orleans, parades and beads"),
        ("Vivid Sydney", "Australia, light and music festival"),
        ("Cherry Blossom Festival", "Japan, hanami, April"),
        ("Gion Matsuri", "Japan, Kyoto, July, floats and parades"),
        ("Obon", "Japan, honoring ancestors, August"),
        ("Loy Krathong", "Thailand, floating lantern festival"),
        ("Yi Peng", "Thailand, lantern release festival"),
        ("That Luang Festival", "Laos, Buddhist temple festival"),
        ("Vesak", "Buddhist, Buddha birth/enlightenment/death"),
        ("Kumbh Mela", "India, world's largest religious gathering"),
        ("Durga Puja", "India, honoring goddess Durga, 10 days"),
        ("Ganesh Chaturthi", "India, elephant-headed god festival"),
        ("Paryushana", "Jain, 8-day fasting and reflection"),
        ("Okunchi", "Japan, Nagasaki, Chinese-influenced festival"),
        ("Seijin no Hi", "Japan, coming of age day"),
        ("Shichi-Go-San", "Japan, children celebration at 3-5-7"),
        ("Christmas markets", "Germany, mulled wine and crafts"),
        ("New Year's Eve", "Worldwide, fireworks and countdown"),
        ("Thanksgiving", "USA, family feast, November"),
        ("Halloween", "Worldwide, costumes, October 31"),
    ]
    name, loc, detail = random.choice(festivals)
    return "{} ({}): {}".format(name, loc, detail)

def random_renewable_fact():
    facts = [
        ("Solar power", "Cheapest electricity in history, $0.03/kWh"),
        ("Wind power", "Ongshore $0.03-0.05/kWh, offshore $0.05-0.08"),
        ("Hydropower", "16% of world electricity, 4,000 TWh/year"),
        ("Geothermal", "14 GW installed, Iceland gets 25% from geothermal"),
        ("Biomass", "Wood, crops, waste for heat and power"),
        ("Tidal power", "La Rance France 240MW, Sihwa South Korea 254MW"),
        ("Wave power", "Pelamis, Wave Hub, emerging technology"),
        ("Solar PV growth", "1 TW installed globally by 2022"),
        ("Solar thermal", "Concentrated solar power for heat storage"),
        ("Wind capacity", "900+ GW globally, China largest at 300 GW"),
        ("Offshore wind", "60 GW globally, UK and China leaders"),
        ("Hydrogen", "Green hydrogen from renewable electrolysis"),
        ("Battery storage", "Lithium-ion grid storage growing exponentially"),
        ("Pumped hydro", "95% of global energy storage capacity"),
        ("Smart grid", "Digital grid management for renewables"),
        ("Net metering", "Credits for solar sent to grid"),
        ("Community solar", "Shared solar installations for subscribers"),
        ("Microgrid", "Local independent grid with renewables"),
        ("Renewable target", "Many countries target 100% clean electricity"),
        ("100% renewable", "Costa Rica, Iceland, Norway near 100%"),
        ("Solar jobs", "4M+ jobs globally in solar industry"),
        ("Wind jobs", "1.4M jobs globally in wind industry"),
        ("Renewable investment", "$500B+ per year globally"),
        ("Levelized cost", "Solar and wind cheapest new electricity"),
        ("Grid parity", "Renewables cheaper than fossil fuels"),
        ("Peak sun hours", "Most useful solar resource measure"),
        ("Capacity factor", "Solar 15-25%, wind 30-50%, hydro 40-60%"),
        ("Intermittency", "Challenge: sun doesn't always shine"),
        ("Baseload", "Traditional coal/gas, renewables need storage"),
        ("Demand response", "Shifting electricity use to match supply"),
        ("Grid-scale batteries", "Tesla Megapack, Hornsdale 150MW"),
        ("Green certificates", "RECs, GOs for renewable attribution"),
        ("PPA", "Power Purchase Agreement for renewable energy"),
        ("Corporate renewable", "Google, Apple, Amazon 100% renewable"),
        ("RE100", "Corporate initiative for 100% renewable"),
        ("Renewable heat", "Solar thermal, heat pumps, biomass"),
        ("Renewable transport", "Electric vehicles, biofuels"),
        ("Green buildings", "LEED, Passive House, net zero energy"),
        ("Sustainable aviation", "Biofuels and hydrogen for airplanes"),
        ("COP28 target", "Triple renewable energy by 2030 agreed"),
    ]
    name, detail = random.choice(facts)
    return "{}: {}".format(name, detail)

def main():
    clear()
    print("Welcome to hi.py! 400 commands.")
    name = input("What's your name? ").strip() or "Stranger"

    pw = input("Role password (or press Enter for none): ").strip()
    role = check_role(pw) if pw else None
    if role:
        print("{} authenticated as {}!".format(name, role))
        print("You now have access to special commands.")
        extra_cmds = get_role_commands(role)
        if extra_cmds:
            print("Your extra commands: {}".format(", ".join(extra_cmds)))

    word, lang = random_greeting()
    badge = role_badge(role)
    print("{} {}, nice to meet you! {}".format(get_time_greeting(), name, badge))
    print("{} means hello in {}!".format(word, lang))
    print("Tip: type 'h' for commands.\n")
    show_help(role)
    while True:
        prompt = "{} {} >> ".format(badge, name).strip() if badge else "{} >> ".format(name)
        cmd = input(prompt).lower().strip()
        if cmd == "q":
            badge = role_badge(role)
            print("Goodbye {} {}!".format(badge, name).strip())
            break
        elif cmd == "h":
            show_help(role)
        elif cmd == "system_info" and role == "Admin":
            print(admin_system_info())
        elif cmd == "list_users" and role == "Admin":
            print(admin_list_users())
        elif cmd == "toggle_debug" and role == "Admin":
            print(toggle_debug())
        elif cmd == "featured_joke" and role == "Mod":
            print(mod_featured_joke())
        elif cmd == "vip_fact" and role == "Vip":
            print(vip_extra_fact())
        elif cmd == "vip_quote" and role == "Vip":
            print(vip_extra_quote())
        elif cmd in ("system_info","list_users","toggle_debug","featured_joke","vip_fact","vip_quote"):
            print("Access denied. You need a higher role.")
        elif cmd == "1":
            print("{} {}!".format(get_time_greeting(), name))
        elif cmd == "2":
            print(show_fact())
        elif cmd == "3":
            print(show_joke())
        elif cmd == "4":
            print(draw_diamond(7))
        elif cmd == "5":
            print(draw_tree(7))
        elif cmd == "6":
            print(draw_heart())
        elif cmd == "7":
            print(draw_star(5))
        elif cmd == "8":
            print(draw_cat())
        elif cmd == "9":
            print(draw_dog())
        elif cmd == "10":
            print(draw_fish())
        elif cmd == "11":
            print(draw_butterfly())
        elif cmd == "12":
            print(draw_rabbit())
        elif cmd == "13":
            print(draw_owl())
        elif cmd == "14":
            print(draw_snake())
        elif cmd == "15":
            print(draw_house())
        elif cmd == "16":
            print(draw_flower())
        elif cmd == "17":
            print(draw_smile())
        elif cmd == "18":
            seq = fibonacci(100)
            print("Fibonacci: {}".format(", ".join(str(x) for x in seq)))
        elif cmd == "19":
            try:
                n = int(input("Number: "))
                print("{} is {}prime.".format(n, "" if is_prime(n) else "not "))
            except:
                print("Not valid.")
        elif cmd == "20":
            try:
                n = int(input("Number: "))
                f = factorial(n)
                print("{}! = {}".format(n, f) if f else "Undefined.")
            except:
                print("Not valid.")
        elif cmd == "21":
            try:
                a, b = int(input("A: ")), int(input("B: "))
                print("GCD({},{}) = {}".format(a, b, gcd(a, b)))
            except:
                print("Not valid.")
        elif cmd == "22":
            try:
                a, b = int(input("A: ")), int(input("B: "))
                print("LCM({},{}) = {}".format(a, b, lcm(a, b)))
            except:
                print("Not valid.")
        elif cmd == "23":
            try:
                n = int(input("Number: "))
                print("Prime factors: {}".format(prime_factors(n)))
            except:
                print("Not valid.")
        elif cmd == "24":
            text = input("Text: ")
            w, v, c, d, s, sp, rev = analyze(text)
            print("Words:{} Vowels:{} Consonants:{} Digits:{} Spaces:{} Special:{}".format(w,v,c,d,s,sp))
            print("Reversed: {}".format(rev))
        elif cmd == "25":
            try:
                n = int(input("Number: "))
                print("Binary: {}".format(to_binary(n)))
            except:
                print("Not valid.")
        elif cmd == "26":
            try:
                n = int(input("Number: "))
                print("Hex: {}".format(to_hex(n)))
            except:
                print("Not valid.")
        elif cmd == "27":
            try:
                n = int(input("Number: "))
                print("Octal: {}".format(to_octal(n)))
            except:
                print("Not valid.")
        elif cmd == "28":
            try:
                n = int(input("Number (1-3999): "))
                print("Roman: {}".format(to_roman(n)))
            except:
                print("Not valid.")
        elif cmd == "29":
            try:
                v = float(input("Value: "))
                t = input("C to F or F to C? ").lower()
                if t == "c to f":
                    print("{} F".format(celsius_to_fahrenheit(v)))
                elif t == "f to c":
                    print("{} C".format(fahrenheit_to_celsius(v)))
                else:
                    print("Say 'C to F' or 'F to C'")
            except:
                print("Not valid.")
        elif cmd == "30":
            try:
                v = float(input("Value: "))
                t = input("km to miles or miles to km? ").lower()
                if "km" in t:
                    print("{:.3f} miles".format(km_to_miles(v)))
                else:
                    print("{:.3f} km".format(miles_to_km(v)))
            except:
                print("Not valid.")
        elif cmd == "31":
            try:
                v = float(input("Value: "))
                t = input("kg to lbs or lbs to kg? ").lower()
                if "kg" in t:
                    print("{:.3f} lbs".format(kg_to_pounds(v)))
                else:
                    print("{:.3f} kg".format(pounds_to_kg(v)))
            except:
                print("Not valid.")
        elif cmd == "32":
            try:
                n = int(input("Length (default 16): ") or 16)
                print("Password: {}".format(generate_password(n)))
            except:
                print("Not valid.")
        elif cmd == "33":
            pw = input("Enter a password: ")
            print("Strength: {}".format(password_strength(pw)))
        elif cmd == "34":
            text = input("Text: ")
            print("Pig Latin: {}".format(pig_latin(text)))
        elif cmd == "35":
            guess_number()
        elif cmd == "36":
            hangman()
        elif cmd == "37":
            scramble_word()
        elif cmd == "38":
            riddle_game()
        elif cmd == "39":
            trivia_quiz()
        elif cmd == "40":
            q = input("Ask the Magic 8 Ball: ")
            print(magic_8_ball())
        elif cmd == "41":
            text = input("Text: ")
            try:
                s = int(input("Shift: "))
                print("Encoded: {}".format(caesar_cipher(text, s)))
                print("Decoded: {}".format(caesar_cipher(text, -s)))
            except:
                print("Not valid.")
        elif cmd == "42":
            text = input("Text: ")
            print("Palindrome: {}".format("Yes" if is_palindrome(text) else "No"))
        elif cmd == "43":
            a = input("First: ")
            b = input("Second: ")
            print("Anagram: {}".format("Yes" if is_anagram(a, b) else "No"))
        elif cmd == "44":
            try:
                h = float(input("Height (m): "))
                w = float(input("Weight (kg): "))
                bmi = w / (h * h)
                print("BMI: {:.2f} - {}".format(bmi, bmi_category(bmi)))
            except:
                print("Not valid.")
        elif cmd == "45":
            try:
                m = int(input("Month (1-12): "))
                d = int(input("Day: "))
                print("Zodiac: {}".format(zodiac_sign(m, d)))
            except:
                print("Not valid.")
        elif cmd == "46":
            text = input("Text: ")
            print(to_morse(text))
        elif cmd == "47":
            try:
                y = int(input("Year: "))
                m = int(input("Month: "))
                d = int(input("Day: "))
                print(day_of_week(y, m, d))
            except:
                print("Not valid.")
        elif cmd == "48":
            try:
                y = int(input("Year: "))
                print("Leap year: {}".format("Yes" if is_leap_year(y) else "No"))
            except:
                print("Not valid.")
        elif cmd == "49":
            try:
                n = int(input("Number: "))
                print(multiplication_table(n))
            except:
                print("Not valid.")
        elif cmd == "50":
            for i in range(0, 101, 10):
                print(progress_bar(i, 100))
                import time
                time.sleep(0.1)
        elif cmd == "51":
            try:
                s = int(input("Seconds: "))
                countdown(s)
            except:
                print("Not valid.")
        elif cmd == "52":
            print(random_name())
            print(random_name())
            print(random_name())
        elif cmd == "53":
            print(coin_flip())
        elif cmd == "54":
            try:
                n = int(input("How many dice? "))
                s = int(input("Sides (6): ") or 6)
                rolls = roll_multiple(n, s)
                print("Rolls: {}".format(rolls))
                print("Sum: {}".format(sum(rolls)))
            except:
                print("Not valid.")
        elif cmd == "55":
            print(card_draw())
        elif cmd == "56":
            high_low()
        elif cmd == "57":
            rock_paper_scissors()
        elif cmd == "58":
            todo_manager()
        elif cmd == "59":
            show_calendar()
        elif cmd == "60":
            simple_calculator()
        elif cmd == "61":
            try:
                nums = [float(x) for x in input("Enter numbers separated by space: ").split()]
                print("Mean: {:.4f}".format(mean(nums)))
                print("Median: {:.4f}".format(median(nums)))
                print("Mode: {}".format(mode(nums)))
            except:
                print("Not valid.")
        elif cmd == "62":
            try:
                nums = [float(x) for x in input("Numbers: ").split()]
                print("Std Dev: {:.4f}".format(standard_deviation(nums)))
            except:
                print("Not valid.")
        elif cmd == "63":
            try:
                a = float(input("a: "))
                b = float(input("b: "))
                c = float(input("c: "))
                print(solve_quadratic(a, b, c))
            except:
                print("Not valid.")
        elif cmd == "64":
            bubble_sort_demo()
        elif cmd == "65":
            binary_search_demo()
        elif cmd == "66":
            typing_speed()
        elif cmd == "67":
            print(show_quote())
        elif cmd == "68":
            print(show_more_quotes())
        elif cmd == "69":
            print(random_animal())
        elif cmd == "70":
            print(random_color())
        elif cmd == "71":
            print(random_fruit())
        elif cmd == "72":
            print(random_vegetable())
        elif cmd == "73":
            name, sym, num = random_element()
            print("{} ({}) - Atomic #{}".format(name, sym, num))
        elif cmd == "74":
            print(random_number())
        elif cmd == "75":
            print(random_uuid())
        elif cmd == "76":
            print(draw_pyramid(7))
        elif cmd == "77":
            print(draw_triangle(7))
        elif cmd == "78":
            print(draw_reverse_triangle(7))
        elif cmd == "79":
            print(draw_hourglass(5))
        elif cmd == "80":
            print(draw_circle(5))
        elif cmd == "81":
            print(draw_pineapple())
        elif cmd == "82":
            print(draw_ghost())
        elif cmd == "83":
            print(draw_alien())
        elif cmd == "84":
            print(draw_bird())
        elif cmd == "85":
            print(draw_turtle())
        elif cmd == "86":
            print(draw_unicorn())
        elif cmd == "87":
            print(draw_robot())
        elif cmd == "88":
            print(draw_spaceship())
        elif cmd == "89":
            print(draw_dragon())
        elif cmd == "90":
            print(draw_crown())
        elif cmd == "91":
            print(draw_castle())
        elif cmd == "92":
            print(draw_mountain())
        elif cmd == "93":
            print(draw_wave())
        elif cmd == "94":
            print(draw_sun())
        elif cmd == "95":
            print(draw_moon())
        elif cmd == "96":
            print(draw_star_shape())
        elif cmd == "97":
            print(draw_arrow_up(7))
        elif cmd == "98":
            print(draw_arrow_down(7))
        elif cmd == "99":
            print(draw_arrow_left(5))
        elif cmd == "100":
            print(draw_arrow_right(5))
        elif cmd == "101":
            print(draw_dna())
        elif cmd == "102":
            print(draw_pacman())
        elif cmd == "103":
            print(draw_bowtie(5))
        elif cmd == "104":
            print(draw_flag(5))
        elif cmd == "105":
            print(draw_stairs(5))
        elif cmd == "106":
            print(draw_table(3))
        elif cmd == "107":
            print(draw_candle())
        elif cmd == "108":
            print(draw_lamp())
        elif cmd == "109":
            print(draw_key())
        elif cmd == "110":
            print(draw_lock())
        elif cmd == "111":
            print(draw_phone())
        elif cmd == "112":
            print(draw_tv())
        elif cmd == "113":
            print(draw_envelope())
        elif cmd == "114":
            print(draw_coffee())
        elif cmd == "115":
            print(draw_burger())
        elif cmd == "116":
            print(draw_pizza())
        elif cmd == "117":
            print(draw_ice_cream())
        elif cmd == "118":
            print(draw_cake())
        elif cmd == "119":
            print(draw_house_with_sun())
        elif cmd == "120":
            try:
                s = int(input("Seconds: "))
                print(convert_seconds(s))
            except:
                print("Not valid.")
        elif cmd == "121":
            try:
                n = int(input("Size: ") or 10)
                print(generate_random_data(n))
            except:
                print("Not valid.")
        elif cmd == "122":
            items = input("Items (space separated): ").split()
            print("Shuffled: {}".format(random_shuffle_list(items)))
        elif cmd == "123":
            try:
                lst = eval(input("Nested list: "))
                print(flatten_list(lst))
            except:
                print("Not valid.")
        elif cmd == "124":
            try:
                lst = input("Items: ").split()
                size = int(input("Chunk size: "))
                print(chunk_list(lst, size))
            except:
                print("Not valid.")
        elif cmd == "125":
            items = input("Items: ").split()
            print(unique_elements(items))
        elif cmd == "126":
            a = input("List A: ").split()
            b = input("List B: ").split()
            print(list_intersection(a, b))
        elif cmd == "127":
            a = input("List A: ").split()
            b = input("List B: ").split()
            print(list_union(a, b))
        elif cmd == "128":
            a = input("List A: ").split()
            b = input("List B: ").split()
            print(list_difference(a, b))
        elif cmd == "129":
            a = input("List A: ").split()
            b = input("List B: ").split()
            print(list_symmetric_difference(a, b))
        elif cmd == "130":
            try:
                lst = input("List: ").split()
                n = int(input("Rotate by: "))
                print(rotate_list(lst, n))
            except:
                print("Not valid.")
        elif cmd == "131":
            try:
                lst = input("List: ").split()
                val = input("Value: ")
                print(find_all_indexes(lst, val))
            except:
                print("Not valid.")
        elif cmd == "132":
            try:
                nums = [int(x) for x in input("Numbers: ").split()]
                e, o = split_evens_odds(nums)
                print("Evens: {} Odds: {}".format(e, o))
            except:
                print("Not valid.")
        elif cmd == "133":
            try:
                n = int(input("Number: "))
                print("Sum digits: {}".format(sum_digits(n)))
            except:
                print("Not valid.")
        elif cmd == "134":
            try:
                n = int(input("Number: "))
                print("Reversed: {}".format(reverse_number(n)))
            except:
                print("Not valid.")
        elif cmd == "135":
            try:
                n = int(input("Number: "))
                print("Armstrong: {}".format("Yes" if is_armstrong(n) else "No"))
            except:
                print("Not valid.")
        elif cmd == "136":
            try:
                n = int(input("Number: "))
                print("Perfect: {}".format("Yes" if is_perfect_number(n) else "No"))
            except:
                print("Not valid.")
        elif cmd == "137":
            try:
                n = int(input("Number: "))
                print("Happy: {}".format("Yes" if is_happy_number(n) else "No"))
            except:
                print("Not valid.")
        elif cmd == "138":
            try:
                n = int(input("Number: "))
                print(collatz_sequence(n))
            except:
                print("Not valid.")
        elif cmd == "139":
            try:
                n = int(input("Up to: "))
                primes = sieve_of_eratosthenes(n)
                print("Primes up to {}: {}".format(n, primes))
            except:
                print("Not valid.")
        elif cmd == "140":
            try:
                n = int(input("Which prime (nth): "))
                print("Prime #{}: {}".format(n, nth_prime(n)))
            except:
                print("Not valid.")
        elif cmd == "141":
            try:
                n = int(input("Even number > 2: "))
                print(goldbach_conjecture(n))
            except:
                print("Not valid.")
        elif cmd == "142":
            try:
                n = int(input("Number: "))
                print("Euler totient: {}".format(euler_totient(n)))
            except:
                print("Not valid.")
        elif cmd == "143":
            try:
                a, b = int(input("A: ")), int(input("B: "))
                g, x, y = extended_gcd(a, b)
                print("GCD = {} ({}*{} + {}*{})".format(g, a, x, b, y))
            except:
                print("Not valid.")
        elif cmd == "144":
            try:
                a = int(input("Number: "))
                m = int(input("Modulus: "))
                inv = modular_inverse(a, m)
                if inv:
                    print("Inverse: {}".format(inv))
                else:
                    print("No inverse exists.")
            except:
                print("Not valid.")
        elif cmd == "145":
            try:
                a = eval(input("Matrix A: "))
                b = eval(input("Matrix B: "))
                print(matrix_multiply(a, b))
            except:
                print("Not valid.")
        elif cmd == "146":
            try:
                m = eval(input("Matrix: "))
                print(matrix_transpose(m))
            except:
                print("Not valid.")
        elif cmd == "147":
            try:
                m = eval(input("Matrix: "))
                print("Determinant: {}".format(matrix_determinant(m)))
            except:
                print("Not valid.")
        elif cmd == "148":
            try:
                a = [float(x) for x in input("Vector A: ").split()]
                b = [float(x) for x in input("Vector B: ").split()]
                print("Dot product: {}".format(dot_product(a, b)))
            except:
                print("Not valid.")
        elif cmd == "149":
            try:
                a = [float(x) for x in input("Vector A (3D): ").split()]
                b = [float(x) for x in input("Vector B (3D): ").split()]
                print("Cross product: {}".format(cross_product(a, b)))
            except:
                print("Not valid.")
        elif cmd == "150":
            try:
                v = [float(x) for x in input("Vector: ").split()]
                print("Magnitude: {:.4f}".format(vector_magnitude(v)))
            except:
                print("Not valid.")
        elif cmd == "151":
            try:
                p1 = [float(x) for x in input("Point 1: ").split()]
                p2 = [float(x) for x in input("Point 2: ").split()]
                print("Euclidean dist: {:.4f}".format(euclidean_distance(p1, p2)))
            except:
                print("Not valid.")
        elif cmd == "152":
            try:
                p1 = [float(x) for x in input("Point 1: ").split()]
                p2 = [float(x) for x in input("Point 2: ").split()]
                print("Manhattan dist: {:.4f}".format(manhattan_distance(p1, p2)))
            except:
                print("Not valid.")
        elif cmd == "153":
            s1 = input("String 1: ")
            s2 = input("String 2: ")
            d = hamming_distance(s1, s2)
            if d == -1:
                print("Strings must be equal length.")
            else:
                print("Hamming dist: {}".format(d))
        elif cmd == "154":
            s1 = input("String 1: ")
            s2 = input("String 2: ")
            print("Levenshtein dist: {}".format(levenshtein_distance(s1, s2)))
        elif cmd == "155":
            try:
                n = int(input("Number: "))
                b = int(input("Base (2-36): "))
                print("Result: {}".format(to_base(n, b)))
            except:
                print("Not valid.")
        elif cmd == "156":
            text = input("Text: ")
            print(sha256_hash(text))
        elif cmd == "157":
            text = input("Text: ")
            print(md5_hash(text))
        elif cmd == "158":
            text = input("Text: ")
            print(base64_encode(text))
        elif cmd == "159":
            text = input("Base64: ")
            print(base64_decode(text))
        elif cmd == "160":
            text = input("Text: ")
            print("ROT13: {}".format(rot13(text)))
        elif cmd == "161":
            text = input("Text: ")
            print(text_to_ascii(text))
        elif cmd == "162":
            try:
                codes = [int(x) for x in input("ASCII codes: ").split()]
                print(ascii_to_text(codes))
            except:
                print("Not valid.")
        elif cmd == "163":
            text = input("Text: ")
            print("Words: {}".format(count_words(text)))
        elif cmd == "164":
            text = input("Text: ")
            print("Sentences: {}".format(count_sentences(text)))
        elif cmd == "165":
            text = input("Text: ")
            print("Paragraphs: {}".format(count_paragraphs(text)))
        elif cmd == "166":
            text = input("Text: ")
            print("Result: {}".format(remove_duplicate_words(text)))
        elif cmd == "167":
            text = input("Text: ")
            print("Reversed: {}".format(reverse_words(text)))
        elif cmd == "168":
            text = input("Text: ")
            print("Sorted: {}".format(sort_words(text)))
        elif cmd == "169":
            text = input("Text: ")
            print("Shuffled: {}".format(shuffle_words(text)))
        elif cmd == "170":
            text = input("Text: ")
            print("Acronym: {}".format(acronym(text)))
        elif cmd == "171":
            text = input("Text: ")
            print("Title: {}".format(capitalize_title(text)))
        elif cmd == "172":
            text = input("Text: ")
            print("Language: {}".format(detect_language(text)))
        elif cmd == "173":
            text = input("Text: ")
            bad = spell_check(text)
            if bad:
                print("Possible errors: {}".format(bad[:10]))
            else:
                print("All words look correct.")
        elif cmd == "174":
            text = input("Text: ")
            freq = word_frequency(text)
            for w, c in list(freq.items())[:15]:
                print("  {}: {}".format(w, c))
        elif cmd == "175":
            text = input("Text: ")
            print("Longest: {}".format(longest_word(text)))
        elif cmd == "176":
            text = input("Text: ")
            print("Shortest: {}".format(shortest_word(text)))
        elif cmd == "177":
            text = input("Text: ")
            letter, count = most_common_letter(text)
            print("Most common: '{}' ({} times)".format(letter, count))
        elif cmd == "178":
            text = input("Text: ")
            print("Has URL: {}".format("Yes" if has_url(text) else "No"))
        elif cmd == "179":
            text = input("Text: ")
            print("Has email: {}".format("Yes" if has_email(text) else "No"))
        elif cmd == "180":
            text = input("Text: ")
            print("Numbers: {}".format(extract_numbers(text)))
        elif cmd == "181":
            text = input("Text: ")
            print("Emails: {}".format(extract_emails(text)))
        elif cmd == "182":
            text = input("Text: ")
            print("URLs: {}".format(extract_urls(text)))
        elif cmd == "183":
            text = input("HTML: ")
            print("Text: {}".format(remove_html_tags(text)))
        elif cmd == "184":
            text = input("Text: ")
            print("Censored: {}".format(censor_bad_words(text)))
        elif cmd == "185":
            text = input("Text: ")
            print(suggest_emoji(text))
        elif cmd == "186":
            data = input("JSON: ")
            print(format_json(data))
        elif cmd == "187":
            data = input("JSON: ")
            print("Elements: {}".format(count_json_elements(data)))
        elif cmd == "188":
            csv_text = input("CSV: ")
            result = csv_to_list(csv_text)
            for row in result[:5]:
                print(row)
        elif cmd == "189":
            try:
                n = int(input("Rolls: ") or 1000)
                s = int(input("Sides: ") or 6)
                counts = simulate_dice_rolls(n, s)
                print(counts)
            except:
                print("Not valid.")
        elif cmd == "190":
            try:
                n = int(input("Flips: ") or 1000)
                heads, tails = simulate_coin_flips(n)
                print("Heads: {} Tails: {}".format(heads, tails))
            except:
                print("Not valid.")
        elif cmd == "191":
            print("Lottery numbers: {}".format(simulate_lottery()))
        elif cmd == "192":
            try:
                n = int(input("People: ") or 23)
                t = int(input("Trials: ") or 10000)
                pct = birthday_paradox(n, t)
                print("Probability of shared birthday: {:.1f}%".format(pct))
            except:
                print("Not valid.")
        elif cmd == "193":
            try:
                t = int(input("Trials: ") or 10000)
                stick, switch = monty_hall_simulation(t)
                print("Stick win: {:.1f}% Switch win: {:.1f}%".format(stick, switch))
            except:
                print("Not valid.")
        elif cmd == "194":
            code = input("Morse: ")
            print(morse_to_text(code))
        elif cmd == "195":
            text = input("Text: ")
            print("Atbash: {}".format(atbash_cipher(text)))
        elif cmd == "196":
            text = input("Text: ")
            key = input("Key: ")
            print("Vigenere: {}".format(vigenere_cipher(text, key)))
        elif cmd == "197":
            text = input("Text: ")
            key = input("Key: ")
            print("XOR: {}".format(xor_cipher(text, key)))
        elif cmd == "198":
            text = input("Text: ")
            print("Substitution with sample key...")
            print("(Try later)")
        elif cmd == "199":
            print("Nerd dice: {}".format(generate_nerd_dice()))
        elif cmd == "200":
            hand = poker_hand()
            print("Poker hand: {}".format(["{} of {}".format(r, s) for r, s in hand]))
        elif cmd == "201":
            try:
                n = int(input("Limit: ") or 50)
                print(format_goldbach(n))
            except:
                print("Not valid.")
        elif cmd == "202":
            try:
                n = int(input("Number: "))
                print(show_number_facts(n))
            except:
                print("Not valid.")
        elif cmd == "203":
            try:
                c = float(input("Celsius: "))
                print(temperature_summary(c))
            except:
                print("Not valid.")
        elif cmd == "204":
            try:
                m = int(input("Birth month: "))
                d = int(input("Birth day: "))
                print(time_until_birthday(m, d))
            except:
                print("Not valid.")
        elif cmd == "205":
            try:
                y = int(input("Birth year: "))
                m = int(input("Birth month: "))
                d = int(input("Birth day: "))
                print(days_since_birth(y, m, d))
            except:
                print("Not valid.")
        elif cmd == "206":
            try:
                y = int(input("Birth year: "))
                m = int(input("Birth month: "))
                d = int(input("Birth day: "))
                print(age_in_seconds(y, m, d))
            except:
                print("Not valid.")
        elif cmd == "207":
            print(current_time_info())
        elif cmd == "208":
            print(week_number())
        elif cmd == "209":
            print(day_of_year())
        elif cmd == "210":
            print(next_full_moon())
        elif cmd == "211":
            print(phases_of_moon())
        elif cmd == "212":
            sign = input("Your zodiac sign: ")
            print(astrology_horoscope(sign))
        elif cmd == "213":
            try:
                n = int(input("Your birth number: "))
                print(numerology(n))
            except:
                print("Not valid.")
        elif cmd == "214":
            try:
                y = int(input("Birth year: "))
                print(chinese_zodiac(y))
            except:
                print("Not valid.")
        elif cmd == "215":
            print(tarot_card())
        elif cmd == "216":
            print(crystal_ball())
        elif cmd == "217":
            print(coffee_grounds())
        elif cmd == "218":
            print(magic_spell())
        elif cmd == "219":
            print(show_country_info())
        elif cmd == "220":
            print(world_clock())
        elif cmd == "221":
            print(countdown_to_new_year())
        elif cmd == "222":
            print(countdown_to_christmas())
        elif cmd == "223":
            print(show_random_movie())
        elif cmd == "224":
            print(show_random_book())
        elif cmd == "225":
            print(show_random_song())
        elif cmd == "226":
            print(show_random_recipe())
        elif cmd == "227":
            print(show_random_hobby())
        elif cmd == "228":
            print(workout_routine())
        elif cmd == "229":
            print(meditation_guide())
        elif cmd == "230":
            bmi_calculator()
        elif cmd == "231":
            tip_calculator()
        elif cmd == "232":
            loan_calculator()
        elif cmd == "233":
            savings_calculator()
        elif cmd == "234":
            unit_converter()
        elif cmd == "235":
            discount_calculator()
        elif cmd == "236":
            currency_converter()
        elif cmd == "237":
            print(generate_planet_info())
        elif cmd == "238":
            print(show_astronomy_fact())
        elif cmd == "239":
            print(show_weather_fact())
        elif cmd == "240":
            print(show_ocean_fact())
        elif cmd == "241":
            print(space_mission_fact())
        elif cmd == "242":
            number2 = random.randint(1, 50)
            print("Guess a number between 1 and 50.")
            for _ in range(5):
                try:
                    g = int(input("Guess: "))
                    if g == number2:
                        print("Correct!"); break
                    print("Too high!" if g > number2 else "Too low!")
                except:
                    print("Invalid.")
            print("Number was: {}".format(number2))
        elif cmd == "243":
            print("Guess the color: {}".format(random_color()))
        elif cmd == "244":
            print("Guess the fruit: {}".format(random_fruit()))
        elif cmd == "245":
            print("Guess the animal: {}".format(random_animal()))
        elif cmd == "246":
            print("Guess the country: {}".format(show_country_info()))
        elif cmd == "247":
            print("Random emoji: {}".format(random.choice(["😊","😂","❤️","🔥","👍","🎉","✨","💪","🐱","🐶","🌺","🍕","🚀","⭐","🌙","☀️","🌈","🎵","💻","🍀"])))
        elif cmd == "248":
            planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune"]
            print("Random planet: {}".format(random.choice(planets)))
        elif cmd == "249":
            galaxies = ["Milky Way","Andromeda","Triangulum","Whirlpool","Sombrero","Pinwheel","Cartwheel","Black Eye","Cigar","Tadpole"]
            print("Random galaxy: {}".format(random.choice(galaxies)))
        elif cmd == "250":
            stars = ["Sun","Sirius","Betelgeuse","Rigel","Vega","Polaris","Alpha Centauri","Proxima","Antares","Aldebaran","Capella","Deneb"]
            print("Random star: {}".format(random.choice(stars)))
        elif cmd == "251":
            asteroids = ["Ceres","Vesta","Pallas","Hygiea","Eros","Itokawa","Bennu","Ryugu","Davida","Interamnia"]
            print("Random asteroid: {}".format(random.choice(asteroids)))
        elif cmd == "252":
            comets = ["Halley","Hale-Bopp","Shoemaker-Levy 9","Hyakutake","Neowise","Lovejoy","ISON","Encke","Tempel 1","Wild 2"]
            print("Random comet: {}".format(random.choice(comets)))
        elif cmd == "253":
            nebulaes = ["Orion","Eagle","Crab","Ring","Horsehead","Cat's Eye","Helix","Tarantula","Carina","Veil"]
            print("Random nebula: {}".format(random.choice(nebulaes)))
        elif cmd == "254":
            quasars = ["3C 273","3C 48","QSO J0313-1806","PKS 1302-102","APM 08279+5255","BR 1202-0725","SDSS J0100+2802","ULAS J1120+0641","PC 1247+3406","TON 618"]
            print("Random quasar: {}".format(random.choice(quasars)))
        elif cmd == "255":
            black_holes = ["Sagittarius A*","M87*","Cygnus X-1","TON 618","Holmberg 15A","IC 1101","Phoenix A","SDSS J140821","HLX-1","LB-1"]
            print("Random black hole: {}".format(random.choice(black_holes)))
        elif cmd == "256":
            quiz_capital_cities()
        elif cmd == "257":
            quiz_flags()
        elif cmd == "258":
            quiz_math()
        elif cmd == "259":
            quiz_science()
        elif cmd == "260":
            quiz_history()
        elif cmd == "261":
            quiz_geography()
        elif cmd == "262":
            quiz_programming()
        elif cmd == "263":
            print(random_emoji())
        elif cmd == "264":
            print("Constellation: {}".format(random_constellation()))
        elif cmd == "265":
            print("Dinosaur: {}".format(random_dinosaur()))
        elif cmd == "266":
            print("Flower: {}".format(random_flower()))
        elif cmd == "267":
            print("Gemstone: {}".format(random_gemstone()))
        elif cmd == "268":
            print("Mythical creature: {}".format(random_mythical_creature()))
        elif cmd == "269":
            print("Planet type: {}".format(random_planet_type()))
        elif cmd == "270":
            print("Reaction: {}".format(random_chemical_reaction()))
        elif cmd == "271":
            print(random_mathematician())
        elif cmd == "272":
            print(random_biologist())
        elif cmd == "273":
            print(random_physicist())
        elif cmd == "274":
            print(random_inventor())
        elif cmd == "275":
            try:
                w = float(input("Your weight in kg: "))
                print(space_data.planet_weight(w))
            except: print("Invalid.")
        elif cmd == "276":
            try:
                a = float(input("Your age in years: "))
                print(space_data.solar_system_age(a))
            except: print("Invalid.")
        elif cmd == "277":
            print(space_data.space_distance_scale())
        elif cmd == "278":
            print(space_data.apollo_missions())
        elif cmd == "279":
            print(space_data.rocket_facts())
        elif cmd == "280":
            print(space_data.mars_facts())
        elif cmd == "281":
            print(space_data.jupiter_facts())
        elif cmd == "282":
            print(space_data.deep_space_fact())
        elif cmd == "283":
            print("Moon: {}".format(space_data.random_moon()))
        elif cmd == "284":
            print("Exoplanet: {}".format(space_data.random_exoplanet()))
        elif cmd == "285":
            print(space_data.astronauts_on_iss())
        elif cmd == "286":
            print(space_data.asteroid_belt_fact())
        elif cmd == "287":
            mini_games.tic_tac_toe()
        elif cmd == "288":
            mini_games.connect_four()
        elif cmd == "289":
            mini_games.word_search_puzzle()
        elif cmd == "290":
            mini_games.number_puzzle()
        elif cmd == "291":
            mini_games.memory_challenge()
        elif cmd == "292":
            mini_games.reaction_game()
        elif cmd == "293":
            mini_games.guess_the_number_advanced()
        elif cmd == "294":
            mini_games.word_association()
        elif cmd == "295":
            mini_games.rapid_math()
        elif cmd == "296":
            trivia_pack.movie_trivia()
        elif cmd == "297":
            trivia_pack.music_trivia()
        elif cmd == "298":
            trivia_pack.sports_trivia()
        elif cmd == "299":
            trivia_pack.art_trivia()
        elif cmd == "300":
            trivia_pack.food_trivia()
        elif cmd == "301":
            trivia_pack.animal_trivia()
        elif cmd == "302":
            trivia_pack.tech_trivia()
        elif cmd == "303":
            trivia_pack.nature_trivia()
        elif cmd == "304":
            print(trivia_pack.random_trivia_fact())
        elif cmd == "305":
            print(word_play.random_sentence())
        elif cmd == "306":
            print(word_play.random_poem())
        elif cmd == "307":
            print(word_play.random_haiku())
        elif cmd == "308":
            print(word_play.random_tongue_twister())
        elif cmd == "309":
            print(word_play.random_proverb())
        elif cmd == "310":
            print(word_play.random_idiom())
        elif cmd == "311":
            print(word_play.random_simile())
        elif cmd == "312":
            print(word_play.random_metaphor())
        elif cmd == "313":
            print(word_play.random_oxymoron())
        elif cmd == "314":
            print("Palindrome word: {}".format(word_play.random_palindrome_word()))
        elif cmd == "315":
            w = input("Enter a word: ")
            print("Anagram: {}".format(word_play.anagram_generator(w)))
        elif cmd == "316":
            try:
                n = int(input("Size (4-12): ") or 8)
                print(art_extra.draw_chessboard(min(n, 12)))
            except: print("Invalid.")
        elif cmd == "317":
            print(art_extra.draw_sierpinski(4))
        elif cmd == "318":
            print(art_extra.draw_radial_star(5))
        elif cmd == "319":
            print(art_extra.draw_spiral(12))
        elif cmd == "320":
            print(art_extra.draw_maze())
        elif cmd == "321":
            print(art_extra.draw_target(5))
        elif cmd == "322":
            print(art_extra.draw_snowflake(5))
        elif cmd == "323":
            print(art_extra.draw_fractal_tree(3))
        elif cmd == "324":
            print(art_extra.draw_flower_garden())
        elif cmd == "325":
            print(art_extra.draw_cross())
        elif cmd == "326":
            print(art_extra.draw_fence(4))
        elif cmd == "327":
            print(art_extra.draw_railroad())
        elif cmd == "328":
            print(art_extra.draw_tunnel())
        elif cmd == "329":
            print(art_extra.draw_lighthouse())
        elif cmd == "330":
            print(art_extra.draw_rocket())
        elif cmd == "331":
            print(art_extra.draw_submarine())
        elif cmd == "332":
            print(art_extra.draw_helicopter())
        elif cmd == "333":
            print(art_extra.draw_airplane())
        elif cmd == "334":
            print(art_extra.draw_bicycle())
        elif cmd == "335":
            print(art_extra.draw_umbrella())
        elif cmd == "336":
            print(art_extra.draw_compass())
        elif cmd == "337":
            print(art_extra.draw_web())
        elif cmd == "338":
            print(art_extra.draw_bridge())
        elif cmd == "339":
            print(art_extra.draw_castle_tower())
        elif cmd == "340":
            print(art_extra.draw_sword())
        elif cmd == "341":
            print(art_extra.draw_shield())
        elif cmd == "342":
            print(art_extra.draw_anchor())
        elif cmd == "343":
            print(art_extra.draw_crown_king())
        elif cmd == "344":
            print(art_extra.draw_throne())
        elif cmd == "345":
            print("Launching HubBasePE...")
            global RA
            RA = 0
            HB.Enter()
            HB.Code()
        elif cmd == "346":
            print(world_data.random_country())
        elif cmd == "347":
            print(world_data.country_by_continent())
        elif cmd == "348":
            print(world_data.world_population())
        elif cmd == "349":
            print(world_data.largest_cities())
        elif cmd == "350":
            print(world_data.world_rivers())
        elif cmd == "351":
            print(world_data.world_mountains())
        elif cmd == "352":
            print(world_data.world_deserts())
        elif cmd == "353":
            print(world_data.world_islands())
        elif cmd == "354":
            print(world_data.world_lakes())
        elif cmd == "355":
            print(world_data.world_wonders())
        elif cmd == "356":
            print(world_data.world_currencies())
        elif cmd == "357":
            print(world_data.random_flag_description())
        elif cmd == "358":
            print(story_data.generate_story())
        elif cmd == "359":
            print(story_data.random_joke_theme("programming"))
        elif cmd == "360":
            print(story_data.random_joke_theme("animal"))
        elif cmd == "361":
            print(story_data.random_joke_theme("food"))
        elif cmd == "362":
            print(story_data.random_joke_theme("science"))
        elif cmd == "363":
            print(story_data.random_joke_theme("sports"))
        elif cmd == "364":
            print(story_data.random_joke_theme("music"))
        elif cmd == "365":
            print(story_data.random_joke_theme("math"))
        elif cmd == "366":
            print(story_data.random_joke_theme("history"))
        elif cmd == "367":
            print(story_data.random_dad_joke())
        elif cmd == "368":
            print(story_data.random_conversation_starter())
        elif cmd == "369":
            print(story_data.random_philosophical_question())
        elif cmd == "370":
            print(random_nobel_prize())
        elif cmd == "371":
            print(random_historic_event())
        elif cmd == "372":
            print(random_philosopher())
        elif cmd == "373":
            print(random_scientific_law())
        elif cmd == "374":
            print(random_programming_language())
        elif cmd == "375":
            print(random_algorithm())
        elif cmd == "376":
            print(random_data_structure())
        elif cmd == "377":
            print(random_tech_company())
        elif cmd == "378":
            print(random_historical_figure())
        elif cmd == "379":
            print(random_world_record())
        elif cmd == "380":
            print(random_math_fact())
        elif cmd == "381":
            print(random_chemistry_fact())
        elif cmd == "382":
            print(random_biology_fact())
        elif cmd == "383":
            print(random_physics_fact())
        elif cmd == "384":
            print(random_geography_fact())
        elif cmd == "385":
            print(random_astronomy_fact())
        elif cmd == "386":
            print(random_psychology_fact())
        elif cmd == "387":
            print(random_technology_fact())
        elif cmd == "388":
            print(random_geology_fact())
        elif cmd == "389":
            print(random_sports_fact())
        elif cmd == "390":
            print(random_music_fact())
        elif cmd == "391":
            print(random_art_fact())
        elif cmd == "392":
            print(random_medicine_fact())
        elif cmd == "393":
            print(random_economics_fact())
        elif cmd == "394":
            print(random_literature_fact())
        elif cmd == "395":
            print(random_movie())
        elif cmd == "396":
            print(random_song())
        elif cmd == "397":
            print(random_book())
        elif cmd == "398":
            print(random_cocktail())
        elif cmd == "399":
            print(random_board_game())
        elif cmd == "400":
            print(random_videogame())
        elif cmd == "401":
            print(random_tv_show())
        elif cmd == "402":
            print(random_space_mission())
        elif cmd == "403":
            print(random_country_fact())
        elif cmd == "404":
            print(random_language_fact())
        elif cmd == "405":
            print(random_food_fact())
        elif cmd == "406":
            print(random_animal_fact_deep())
        elif cmd == "407":
            print(random_ocean_fact())
        elif cmd == "408":
            print(random_moon_fact())
        elif cmd == "409":
            print(random_weather_fact())
        elif cmd == "410":
            print(random_invention())
        elif cmd == "411":
            print(random_quote())
        elif cmd == "412":
            print(random_holiday())
        elif cmd == "413":
            print(random_joke())
        elif cmd == "414":
            print(random_puzzle())
        elif cmd == "415":
            print(random_ai_fact())
        elif cmd == "416":
            print(random_quantum_fact())
        elif cmd == "417":
            print(random_space_object())
        elif cmd == "418":
            print(random_human_body_fact())
        elif cmd == "419":
            print(random_architecture_fact())
        elif cmd == "420":
            print(random_energy_fact())
        elif cmd == "421":
            print(random_mythology_fact())
        elif cmd == "422":
            print(random_ocean_life_fact())
        elif cmd == "423":
            print(random_mountain_fact())
        elif cmd == "424":
            print(random_river_fact())
        elif cmd == "425":
            print(random_desert_fact())
        elif cmd == "426":
            print(random_forest_fact())
        elif cmd == "427":
            print(random_volcano_fact())
        elif cmd == "428":
            print(random_city_fact())
        elif cmd == "429":
            print(random_flag_fact())
        elif cmd == "430":
            print(random_number_fact_deep())
        elif cmd == "431":
            print(random_history_fact_deep())
        elif cmd == "432":
            print(random_lake_fact())
        elif cmd == "433":
            print(random_island_fact())
        elif cmd == "434":
            print(random_planet_fact_deep())
        elif cmd == "435":
            print(random_ocean_fact_deep())
        elif cmd == "436":
            print(random_culture_fact())
        elif cmd == "437":
            print(random_famous_landmark())
        elif cmd == "438":
            print(random_weather_phenomenon())
        elif cmd == "439":
            print(random_science_experiment())
        elif cmd == "440":
            print(random_engineering_fact())
        elif cmd == "441":
            print(random_medicine_fact_deep())
        elif cmd == "442":
            print(random_bridge_fact())
        elif cmd == "443":
            print(random_tunnel_fact())
        elif cmd == "444":
            print(random_animal_speed_fact())
        elif cmd == "445":
            print(random_unusual_ability())
        elif cmd == "446":
            print(random_dinosaur_fact_deep())
        elif cmd == "447":
            print(random_space_misson_deep())
        elif cmd == "448":
            print(random_natural_disaster())
        elif cmd == "449":
            print(random_climate_fact())
        elif cmd == "450":
            print(random_chemical_element())
        elif cmd == "451":
            print(random_programming_term())
        elif cmd == "452":
            print(random_festival())
        elif cmd == "453":
            print(random_renewable_fact())
        else:
            print("Unknown. Type 'h' for help.")

if __name__ == "__main__":
    main()