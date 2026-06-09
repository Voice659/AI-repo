import random, datetime, os, math, string, json, re, hashlib, base64, uuid, time, statistics
import space_data, mini_games, trivia_pack, word_play, art_extra
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

def main():
    clear()
    print("Welcome to hi.py! 345 commands.")
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
            HB.Enter()
            HB.Code()
        else:
            print("Unknown. Type 'h' for help.")

if __name__ == "__main__":
    main()