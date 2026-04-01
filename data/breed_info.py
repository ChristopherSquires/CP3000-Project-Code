"""
breed_info.py
-------------
Comprehensive information database for the 120 dog breeds present in the
Stanford Dogs Dataset (https://www.kaggle.com/datasets/jessicali9530/stanford-dogs-dataset).

Each entry maps a breed name (matching the dataset folder names, lower-cased
and hyphen-separated) to a dictionary of descriptive attributes.
"""

BREED_INFO: dict[str, dict] = {
    "affenpinscher": {
        "name": "Affenpinscher",
        "group": "Toy",
        "origin": "Germany",
        "lifespan": "12–15 years",
        "height": "23–30 cm (9–12 in)",
        "weight": "3–6 kg (7–13 lb)",
        "temperament": ["Stubborn", "Curious", "Playful", "Adventurous", "Active", "Fun-loving"],
        "description": (
            "The Affenpinscher, whose name means 'monkey terrier' in German, is a small but "
            "confident dog with a distinct monkey-like facial expression. Originally bred to "
            "rid kitchens and stables of rodents, they are now loyal and entertaining companions."
        ),
    },
    "afghan-hound": {
        "name": "Afghan Hound",
        "group": "Hound",
        "origin": "Afghanistan",
        "lifespan": "12–14 years",
        "height": "63–74 cm (25–29 in)",
        "weight": "23–27 kg (50–60 lb)",
        "temperament": ["Aloof", "Clownish", "Dignified", "Independent", "Happy"],
        "description": (
            "One of the oldest sighthound breeds, the Afghan Hound is renowned for its thick, "
            "silky, flowing coat and aristocratic bearing. Bred to course game over rugged "
            "Afghan terrain, it combines elegance with remarkable athleticism."
        ),
    },
    "african-hunting-dog": {
        "name": "African Wild Dog",
        "group": "Wild Canid",
        "origin": "Sub-Saharan Africa",
        "lifespan": "10–12 years",
        "height": "60–75 cm (24–30 in)",
        "weight": "18–36 kg (40–79 lb)",
        "temperament": ["Social", "Intelligent", "Cooperative"],
        "description": (
            "The African Wild Dog (Lycaon pictus) is a highly social, pack-hunting canid native "
            "to sub-Saharan Africa. Its mottled coat of yellow, black, and white is unique to "
            "each individual. It is listed as Endangered by the IUCN."
        ),
    },
    "airedale": {
        "name": "Airedale Terrier",
        "group": "Terrier",
        "origin": "England",
        "lifespan": "10–13 years",
        "height": "56–61 cm (22–24 in)",
        "weight": "18–29 kg (40–65 lb)",
        "temperament": ["Outgoing", "Friendly", "Alert", "Confident", "Intelligent", "Courageous"],
        "description": (
            "Known as the 'King of Terriers', the Airedale is the largest of all terrier breeds. "
            "Originally bred in the Aire Valley of Yorkshire for hunting otters and badgers, "
            "Airedales are versatile, energetic dogs that excel in many roles."
        ),
    },
    "american-staffordshire-terrier": {
        "name": "American Staffordshire Terrier",
        "group": "Terrier",
        "origin": "United States",
        "lifespan": "12–16 years",
        "height": "43–48 cm (17–19 in)",
        "weight": "25–40 kg (55–88 lb)",
        "temperament": ["Tenacious", "Friendly", "Devoted", "Loyal", "Attentive", "Courageous"],
        "description": (
            "The American Staffordshire Terrier is a strong, muscular, and agile breed that "
            "combines great strength with gentle playfulness. They are known for their loyalty "
            "and deep affection for their families."
        ),
    },
    "appenzeller": {
        "name": "Appenzeller Sennenhund",
        "group": "Working",
        "origin": "Switzerland",
        "lifespan": "12–14 years",
        "height": "50–56 cm (20–22 in)",
        "weight": "22–32 kg (49–71 lb)",
        "temperament": ["Self-assured", "Reliable", "Lively", "Fearless"],
        "description": (
            "The Appenzeller Sennenhund is a medium-sized herding breed from the Swiss Alps. "
            "It is one of four regional Swiss Mountain Dogs and is known for its tri-coloured "
            "coat, high energy, and versatility as a farm and family dog."
        ),
    },
    "basenji": {
        "name": "Basenji",
        "group": "Hound",
        "origin": "Central Africa",
        "lifespan": "13–14 years",
        "height": "40–43 cm (16–17 in)",
        "weight": "9–11 kg (22–24 lb)",
        "temperament": ["Energetic", "Alert", "Curious", "Playful", "Affectionate", "Intelligent"],
        "description": (
            "The Basenji is an ancient hunting breed from Central Africa, famous for being "
            "barkless (it produces a unique yodel-like sound). Alert, energetic, and remarkably "
            "cat-like in its cleanliness and independence."
        ),
    },
    "basset": {
        "name": "Basset Hound",
        "group": "Hound",
        "origin": "France / Great Britain",
        "lifespan": "10–12 years",
        "height": "30–38 cm (12–15 in)",
        "weight": "20–29 kg (44–64 lb)",
        "temperament": ["Tenacious", "Friendly", "Affectionate", "Devoted", "Sweet-tempered"],
        "description": (
            "The Basset Hound is a short-legged breed with an exceptional sense of smell, "
            "second only to the Bloodhound. Bred in France for hunting small game, Bassets "
            "are gentle, patient, and excellent family companions."
        ),
    },
    "beagle": {
        "name": "Beagle",
        "group": "Hound",
        "origin": "Great Britain",
        "lifespan": "12–15 years",
        "height": "33–41 cm (13–16 in)",
        "weight": "8–14 kg (18–30 lb)",
        "temperament": ["Amiable", "Even-tempered", "Excitable", "Determined", "Gentle"],
        "description": (
            "One of the most popular family dogs in the world, the Beagle is a small, compact "
            "scent hound. They are merry, friendly, and curious dogs that are great with "
            "children and other pets."
        ),
    },
    "black-and-tan-coonhound": {
        "name": "Black and Tan Coonhound",
        "group": "Hound",
        "origin": "United States",
        "lifespan": "10–12 years",
        "height": "58–69 cm (23–27 in)",
        "weight": "23–34 kg (50–75 lb)",
        "temperament": ["Adaptable", "Trusting", "Gentle", "Easygoing"],
        "description": (
            "Developed in the American South for tracking and treeing raccoons, the Black and "
            "Tan Coonhound is a large, working hound with a distinctive black coat and tan "
            "markings. They are tenacious on the trail but affectionate at home."
        ),
    },
    "bloodhound": {
        "name": "Bloodhound",
        "group": "Hound",
        "origin": "Belgium / Great Britain",
        "lifespan": "10–12 years",
        "height": "58–69 cm (23–27 in)",
        "weight": "36–50 kg (80–110 lb)",
        "temperament": ["Stubborn", "Affectionate", "Gentle", "Even-tempered"],
        "description": (
            "The Bloodhound has the most acute sense of smell of any dog breed and is famous "
            "for its ability to track a scent trail over enormous distances. Despite their "
            "powerful hunting instincts, Bloodhounds are gentle and affectionate family dogs."
        ),
    },
    "bluetick": {
        "name": "Bluetick Coonhound",
        "group": "Hound",
        "origin": "United States",
        "lifespan": "11–12 years",
        "height": "53–68 cm (21–27 in)",
        "weight": "20–36 kg (45–80 lb)",
        "temperament": ["Friendly", "Intelligent", "Active", "Aggressive on trail"],
        "description": (
            "The Bluetick Coonhound is an American hunting dog known for its striking blue-ticked "
            "coat and its ability to trail cold scents. They are passionate, determined hunters "
            "and loyal, affectionate companions."
        ),
    },
    "border-collie": {
        "name": "Border Collie",
        "group": "Herding",
        "origin": "Anglo-Scottish border region",
        "lifespan": "12–15 years",
        "height": "46–56 cm (18–22 in)",
        "weight": "14–20 kg (31–44 lb)",
        "temperament": ["Energetic", "Alert", "Responsive", "Tenacious", "Intelligent"],
        "description": (
            "Widely considered the most intelligent dog breed, the Border Collie is a highly "
            "energetic herding dog. They excel at almost every canine sport and activity, and "
            "they require significant mental and physical stimulation daily."
        ),
    },
    "border-terrier": {
        "name": "Border Terrier",
        "group": "Terrier",
        "origin": "Anglo-Scottish border region",
        "lifespan": "12–15 years",
        "height": "28–36 cm (11–14 in)",
        "weight": "5–7 kg (11–16 lb)",
        "temperament": ["Fearless", "Affectionate", "Alert", "Obedient", "Intelligent"],
        "description": (
            "The Border Terrier is a small but tough terrier originally bred to assist in "
            "fox hunts along the Anglo-Scottish border. Adaptable and good-natured, they "
            "make excellent family pets."
        ),
    },
    "borzoi": {
        "name": "Borzoi",
        "group": "Hound",
        "origin": "Russia",
        "lifespan": "9–14 years",
        "height": "68–85 cm (27–33 in)",
        "weight": "25–48 kg (55–105 lb)",
        "temperament": ["Respectful", "Athletic", "Intelligent", "Gentle", "Independent"],
        "description": (
            "The Borzoi, also known as the Russian Wolfhound, is an elegant sighthound bred by "
            "Russian aristocracy for wolf hunting. Graceful, swift, and gentle, they form strong "
            "bonds with their families while maintaining an independent spirit."
        ),
    },
    "boston-bull": {
        "name": "Boston Terrier",
        "group": "Non-Sporting",
        "origin": "United States",
        "lifespan": "11–13 years",
        "height": "38–43 cm (15–17 in)",
        "weight": "4.5–11 kg (10–25 lb)",
        "temperament": ["Friendly", "Lively", "Intelligent"],
        "description": (
            "The Boston Terrier, nicknamed the 'American Gentleman', is a compact, well-muscled "
            "breed with a tuxedo-like markings. They are lively, adaptable, and people-loving "
            "dogs that thrive in both apartments and houses."
        ),
    },
    "bouvier-des-flandres": {
        "name": "Bouvier des Flandres",
        "group": "Herding",
        "origin": "Belgium",
        "lifespan": "10–12 years",
        "height": "58–70 cm (23–28 in)",
        "weight": "27–54 kg (60–120 lb)",
        "temperament": ["Rational", "Agile", "Loyal", "Protective", "Gentle", "Intelligent"],
        "description": (
            "Originating in Flanders, the Bouvier des Flandres was bred for farm work including "
            "cattle droving. Today they excel as police, military, and guide dogs thanks to their "
            "intelligence, strength, and trainability."
        ),
    },
    "boxer": {
        "name": "Boxer",
        "group": "Working",
        "origin": "Germany",
        "lifespan": "10–12 years",
        "height": "53–63 cm (21–25 in)",
        "weight": "25–32 kg (55–71 lb)",
        "temperament": ["Devoted", "Fearless", "Friendly", "Loyal", "Playful", "Energetic"],
        "description": (
            "The Boxer is a medium-sized, muscular, and energetic breed developed in Germany. "
            "Known for their playful 'boxer-like' use of their front paws, they are affectionate "
            "and patient with children and devoted to their families."
        ),
    },
    "briard": {
        "name": "Briard",
        "group": "Herding",
        "origin": "France",
        "lifespan": "10–12 years",
        "height": "56–68 cm (22–27 in)",
        "weight": "30–45 kg (66–99 lb)",
        "temperament": ["Faithful", "Obedient", "Fearless", "Intelligent", "Loyal"],
        "description": (
            "The Briard is an ancient French herding and guardian breed known for its long, "
            "wavy coat. Described by Napoleon as 'the dog with a human brain', they are "
            "deeply loyal to their family and highly responsive to training."
        ),
    },
    "brittany-spaniel": {
        "name": "Brittany",
        "group": "Sporting",
        "origin": "France",
        "lifespan": "12–14 years",
        "height": "44–52 cm (17–21 in)",
        "weight": "14–18 kg (30–40 lb)",
        "temperament": ["Agile", "Adaptable", "Athletic", "Alert", "Intelligent"],
        "description": (
            "The Brittany is a versatile gun dog from the Brittany region of France. Compact "
            "and energetic, they are known for their bird-dog ability and their affectionate, "
            "eager-to-please nature, making them equally suited for hunting and family life."
        ),
    },
    "bull-mastiff": {
        "name": "Bullmastiff",
        "group": "Working",
        "origin": "England",
        "lifespan": "8–10 years",
        "height": "61–69 cm (24–27 in)",
        "weight": "45–59 kg (100–130 lb)",
        "temperament": ["Reliable", "Alert", "Devoted", "Loyal", "Reserved", "Calm"],
        "description": (
            "The Bullmastiff was developed by English gamekeepers in the 19th century by "
            "crossing the Bulldog with the Mastiff to create a fearless yet docile guard dog. "
            "They are powerful, confident, and deeply loyal to their families."
        ),
    },
    "cairn": {
        "name": "Cairn Terrier",
        "group": "Terrier",
        "origin": "Scotland",
        "lifespan": "13–14 years",
        "height": "28–33 cm (11–13 in)",
        "weight": "6–7.5 kg (13–17 lb)",
        "temperament": ["Hardy", "Fearless", "Assertive", "Alert", "Loyal", "Gay"],
        "description": (
            "The Cairn Terrier, one of Scotland's oldest working terriers, was originally bred "
            "to hunt foxes and other small animals among the cairns (rock piles) of the "
            "Scottish Highlands. Best known as Toto from 'The Wizard of Oz'."
        ),
    },
    "cardigan": {
        "name": "Cardigan Welsh Corgi",
        "group": "Herding",
        "origin": "Wales",
        "lifespan": "12–15 years",
        "height": "27–32 cm (11–13 in)",
        "weight": "11–17 kg (25–38 lb)",
        "temperament": ["Affectionate", "Devoted", "Alert", "Intelligent", "Loyal"],
        "description": (
            "One of the oldest herding breeds, the Cardigan Welsh Corgi is distinguished from "
            "the Pembroke by its long fox-like tail. An intelligent and sturdy herder, they "
            "are also devoted and playful family companions."
        ),
    },
    "chesapeake-bay-retriever": {
        "name": "Chesapeake Bay Retriever",
        "group": "Sporting",
        "origin": "United States",
        "lifespan": "10–13 years",
        "height": "53–66 cm (21–26 in)",
        "weight": "25–36 kg (55–80 lb)",
        "temperament": ["Affectionate", "Intelligent", "Quiet", "Dominant", "Happy", "Bright"],
        "description": (
            "The Chesapeake Bay Retriever, or 'Chessie', was developed on the shores of the "
            "Chesapeake Bay to retrieve ducks from the icy, rough waters. They are hardy, "
            "powerful swimmers with a distinctive oily, wavy coat."
        ),
    },
    "chihuahua": {
        "name": "Chihuahua",
        "group": "Toy",
        "origin": "Mexico",
        "lifespan": "12–20 years",
        "height": "15–23 cm (6–9 in)",
        "weight": "1.5–3 kg (3–7 lb)",
        "temperament": ["Devoted", "Lively", "Alert", "Quick", "Courageous"],
        "description": (
            "The Chihuahua is the world's smallest dog breed, named after the state of Chihuahua "
            "in Mexico. Despite their tiny size, they have enormous personalities—bold, loyal, "
            "and fiercely devoted to their owners."
        ),
    },
    "chow": {
        "name": "Chow Chow",
        "group": "Non-Sporting",
        "origin": "China",
        "lifespan": "9–15 years",
        "height": "43–51 cm (17–20 in)",
        "weight": "20–32 kg (44–70 lb)",
        "temperament": ["Aloof", "Independent", "Loyal", "Quiet"],
        "description": (
            "One of the oldest and most unique breeds, the Chow Chow is instantly recognizable "
            "by its lion-like ruff and distinctive blue-black tongue. Originally bred in China "
            "for hunting, herding, and protection, they are serious and dignified dogs."
        ),
    },
    "clumber": {
        "name": "Clumber Spaniel",
        "group": "Sporting",
        "origin": "England",
        "lifespan": "10–12 years",
        "height": "43–51 cm (17–20 in)",
        "weight": "25–38 kg (55–85 lb)",
        "temperament": ["Gentle", "Loyal", "Affectionate", "Calm", "Dignified"],
        "description": (
            "The heaviest of the spaniel breeds, the Clumber Spaniel is a low, long, and "
            "substantial dog with a thoughtful expression. They are unhurried but effective "
            "workers in the field, and gentle, loyal family companions."
        ),
    },
    "cocker-spaniel": {
        "name": "Cocker Spaniel",
        "group": "Sporting",
        "origin": "England",
        "lifespan": "12–15 years",
        "height": "36–43 cm (14–17 in)",
        "weight": "7–14 kg (15–31 lb)",
        "temperament": ["Playful", "Trainable", "Friendly", "Faithful", "Quiet", "Joyful"],
        "description": (
            "The Cocker Spaniel (American) is a cheerful, gentle-mannered sporting dog. "
            "Once America's most popular breed, they are beloved for their silky coat, "
            "expressive eyes, and sweet, eager-to-please temperament."
        ),
    },
    "collie": {
        "name": "Collie",
        "group": "Herding",
        "origin": "Scotland",
        "lifespan": "12–14 years",
        "height": "51–66 cm (20–26 in)",
        "weight": "18–34 kg (40–75 lb)",
        "temperament": ["Gentle", "Friendly", "Loyal", "Protective", "Intelligent"],
        "description": (
            "Famous for Lassie, the Collie is a beautiful, graceful, and loyal herding dog. "
            "Sensitive and highly intelligent, they bond closely with their families and are "
            "gentle and patient with children."
        ),
    },
    "curly-coated-retriever": {
        "name": "Curly-Coated Retriever",
        "group": "Sporting",
        "origin": "England",
        "lifespan": "10–12 years",
        "height": "58–69 cm (23–27 in)",
        "weight": "23–36 kg (51–80 lb)",
        "temperament": ["Trainable", "Proud", "Lively", "Intelligent", "Perceptive", "Self-confident"],
        "description": (
            "The Curly-Coated Retriever is one of the oldest retriever breeds, prized for its "
            "distinctive tight curls that protect against water and thorny bushes. An outstanding "
            "hunting companion and graceful show dog."
        ),
    },
    "dachshund": {
        "name": "Dachshund",
        "group": "Hound",
        "origin": "Germany",
        "lifespan": "12–16 years",
        "height": "13–23 cm (5–9 in)",
        "weight": "3.5–14.5 kg (8–32 lb)",
        "temperament": ["Stubborn", "Devoted", "Lively", "Playful", "Clever", "Courageous"],
        "description": (
            "The Dachshund ('badger dog' in German) was bred to scent, chase, and flush out "
            "badgers and other burrow-dwelling animals. Their distinctive elongated body and "
            "short legs allow them to pursue prey underground."
        ),
    },
    "dalmatian": {
        "name": "Dalmatian",
        "group": "Non-Sporting",
        "origin": "Croatia (Dalmatia)",
        "lifespan": "13–16 years",
        "height": "48–61 cm (19–24 in)",
        "weight": "20–32 kg (45–70 lb)",
        "temperament": ["Outgoing", "Friendly", "Energetic", "Playful", "Sensitive", "Intelligent"],
        "description": (
            "The Dalmatian, famous for its unique black or liver-spotted coat, has served as a "
            "carriage dog, war sentinel, and firehouse mascot. Athletic and energetic, they "
            "need plenty of exercise and mental stimulation."
        ),
    },
    "dandie-dinmont": {
        "name": "Dandie Dinmont Terrier",
        "group": "Terrier",
        "origin": "Scotland / England",
        "lifespan": "12–15 years",
        "height": "20–28 cm (8–11 in)",
        "weight": "8–11 kg (18–24 lb)",
        "temperament": ["Determined", "Reserved", "Affectionate", "Intelligent", "Independent"],
        "description": (
            "The Dandie Dinmont Terrier is a small, long-bodied Scottish breed with a "
            "distinctive large, dome-shaped head topped with a silky topknot. Named after a "
            "character in a Sir Walter Scott novel, they are tenacious hunters and devoted companions."
        ),
    },
    "doberman": {
        "name": "Doberman Pinscher",
        "group": "Working",
        "origin": "Germany",
        "lifespan": "10–13 years",
        "height": "63–72 cm (25–28 in)",
        "weight": "32–45 kg (71–99 lb)",
        "temperament": ["Energetic", "Alert", "Loyal", "Obedient", "Fearless", "Intelligent"],
        "description": (
            "Developed by German tax collector Louis Dobermann as an ideal guard dog, the "
            "Doberman Pinscher combines elegance with strength and ferocity. They are highly "
            "trainable, loyal to their families, and excel in police and military work."
        ),
    },
    "english-foxhound": {
        "name": "English Foxhound",
        "group": "Hound",
        "origin": "England",
        "lifespan": "10–13 years",
        "height": "58–64 cm (23–25 in)",
        "weight": "29–34 kg (65–75 lb)",
        "temperament": ["Gentle", "Sociable", "Active", "Tolerant"],
        "description": (
            "One of the oldest dog breeds in existence, the English Foxhound was bred specifically "
            "for foxhunting in packs. They are athletic, sturdy, and possess extraordinary stamina "
            "and an excellent nose."
        ),
    },
    "english-setter": {
        "name": "English Setter",
        "group": "Sporting",
        "origin": "England",
        "lifespan": "12 years",
        "height": "61–69 cm (24–27 in)",
        "weight": "20–36 kg (44–80 lb)",
        "temperament": ["Gentle", "Friendly", "Energetic", "Lively", "People-oriented"],
        "description": (
            "The English Setter is an elegant bird dog known for its speckled coat—a pattern "
            "called 'belton'. One of the oldest gun-dog breeds, they are gentle, affectionate, "
            "and full of energy both in the field and at home."
        ),
    },
    "english-springer": {
        "name": "English Springer Spaniel",
        "group": "Sporting",
        "origin": "England",
        "lifespan": "12–14 years",
        "height": "46–56 cm (18–22 in)",
        "weight": "18–25 kg (40–55 lb)",
        "temperament": ["Friendly", "Playful", "Alert", "Attentive", "Intelligent"],
        "description": (
            "The English Springer Spaniel is a friendly, eager-to-please gun dog with high "
            "endurance. They were bred to flush ('spring') game and retrieve shot birds, "
            "and are now popular both as sporting companions and family pets."
        ),
    },
    "entlebucher": {
        "name": "Entlebucher Mountain Dog",
        "group": "Working",
        "origin": "Switzerland",
        "lifespan": "11–15 years",
        "height": "44–52 cm (17–20 in)",
        "weight": "20–30 kg (44–66 lb)",
        "temperament": ["Devoted", "Lively", "Agile", "Self-confident", "Loyal"],
        "description": (
            "The smallest of the four Swiss Mountain Dogs, the Entlebucher is a compact and "
            "energetic herder. They are devoted to their families and make excellent "
            "watchdogs thanks to their alert and lively nature."
        ),
    },
    "eskimo-dog": {
        "name": "American Eskimo Dog",
        "group": "Non-Sporting",
        "origin": "United States",
        "lifespan": "13–15 years",
        "height": "23–48 cm (9–19 in)",
        "weight": "3–16 kg (6–35 lb)",
        "temperament": ["Playful", "Perky", "Alert", "Intelligent", "Friendly"],
        "description": (
            "Despite its name, the American Eskimo Dog is descended from European Spitz breeds "
            "and was popularized by travelling circuses in 19th century America. Intelligent and "
            "eager to please, they excel at obedience and agility."
        ),
    },
    "flat-coated-retriever": {
        "name": "Flat-Coated Retriever",
        "group": "Sporting",
        "origin": "England",
        "lifespan": "8–14 years",
        "height": "56–62 cm (22–24 in)",
        "weight": "25–36 kg (55–79 lb)",
        "temperament": ["Devoted", "Self-confident", "Optimistic", "Good-natured", "Intelligent"],
        "description": (
            "The Flat-Coated Retriever is a cheerful, active gun dog known for its 'forever "
            "young' attitude. Bred in the UK for retrieving on land and from water, they "
            "maintain a puppy-like enthusiasm throughout their lives."
        ),
    },
    "french-bulldog": {
        "name": "French Bulldog",
        "group": "Non-Sporting",
        "origin": "France / England",
        "lifespan": "10–14 years",
        "height": "28–33 cm (11–13 in)",
        "weight": "7–12 kg (16–28 lb)",
        "temperament": ["Easygoing", "Lively", "Sociable", "Alert", "Playful", "Bright"],
        "description": (
            "The French Bulldog, with its bat ears and compact muscular body, is one of the "
            "world's most popular small-dog breeds. They are adaptable, low-energy indoors, "
            "and thrive on human contact and attention."
        ),
    },
    "german-shepherd": {
        "name": "German Shepherd",
        "group": "Herding",
        "origin": "Germany",
        "lifespan": "9–13 years",
        "height": "55–65 cm (22–26 in)",
        "weight": "22–40 kg (50–88 lb)",
        "temperament": ["Obedient", "Loyal", "Curious", "Alert", "Confident", "Courageous", "Intelligent"],
        "description": (
            "The German Shepherd is one of the most popular dog breeds in the world, prized "
            "for its versatility, intelligence, and loyalty. They excel as police and military "
            "dogs, service animals, and devoted family companions."
        ),
    },
    "german-short-haired-pointer": {
        "name": "German Shorthaired Pointer",
        "group": "Sporting",
        "origin": "Germany",
        "lifespan": "12–14 years",
        "height": "53–64 cm (21–25 in)",
        "weight": "20–32 kg (45–71 lb)",
        "temperament": ["Affectionate", "Cooperative", "Bold", "Trainable", "Energetic", "Intelligent"],
        "description": (
            "The German Shorthaired Pointer is a versatile, high-energy hunting breed capable "
            "of working on land and in water with all types of game. They are friendly, "
            "intelligent, and enthusiastic sporting companions."
        ),
    },
    "golden-retriever": {
        "name": "Golden Retriever",
        "group": "Sporting",
        "origin": "Scotland",
        "lifespan": "10–12 years",
        "height": "51–61 cm (20–24 in)",
        "weight": "25–34 kg (55–75 lb)",
        "temperament": ["Trustworthy", "Reliable", "Friendly", "Kind", "Confident", "Intelligent"],
        "description": (
            "The Golden Retriever is one of the most popular dog breeds in the world, beloved "
            "for its friendly and tolerant attitude. They were originally bred to retrieve shot "
            "waterfowl and are now widely used as guide, hearing, and therapy dogs."
        ),
    },
    "gordon-setter": {
        "name": "Gordon Setter",
        "group": "Sporting",
        "origin": "Scotland",
        "lifespan": "10–12 years",
        "height": "58–69 cm (23–27 in)",
        "weight": "20–36 kg (45–80 lb)",
        "temperament": ["Alert", "Loyal", "Confident", "Fearless", "Gay"],
        "description": (
            "The Gordon Setter, developed by the Duke of Gordon in 18th-century Scotland, is "
            "the heaviest and most robust of the setter breeds. Bold and willing, they are "
            "devoted family dogs with strong hunting instincts."
        ),
    },
    "great-dane": {
        "name": "Great Dane",
        "group": "Working",
        "origin": "Germany",
        "lifespan": "8–10 years",
        "height": "71–86 cm (28–34 in)",
        "weight": "45–90 kg (100–200 lb)",
        "temperament": ["Friendly", "Devoted", "Reserved", "Gentle", "Loving", "Confident"],
        "description": (
            "Known as the 'Apollo of dogs', the Great Dane is one of the world's tallest breeds. "
            "Despite their imposing size, they are gentle giants—friendly, patient, and "
            "dependable companions that are wonderful with families."
        ),
    },
    "great-pyrenees": {
        "name": "Great Pyrenees",
        "group": "Working",
        "origin": "France / Spain",
        "lifespan": "10–12 years",
        "height": "65–82 cm (26–32 in)",
        "weight": "36–54 kg (80–120 lb)",
        "temperament": ["Strong-willed", "Fearless", "Confident", "Gentle", "Patient", "Calm"],
        "description": (
            "The Great Pyrenees is a large, majestic breed that served for centuries as a "
            "livestock guardian in the Pyrenees Mountains. They are calm, patient, and "
            "deeply devoted, with a natural instinct to protect their family."
        ),
    },
    "groenendael": {
        "name": "Belgian Sheepdog (Groenendael)",
        "group": "Herding",
        "origin": "Belgium",
        "lifespan": "12–14 years",
        "height": "56–66 cm (22–26 in)",
        "weight": "20–30 kg (44–66 lb)",
        "temperament": ["Obedient", "Loyal", "Alert", "Intelligent", "Energetic"],
        "description": (
            "The Groenendael is the most widely recognized of the four Belgian Shepherd varieties. "
            "With its black, flowing double coat and keen expression, it is an elegant and "
            "versatile working dog that excels in herding, protection, and sport."
        ),
    },
    "ibizan-hound": {
        "name": "Ibizan Hound",
        "group": "Hound",
        "origin": "Spain (Ibiza)",
        "lifespan": "12–14 years",
        "height": "57–74 cm (22–29 in)",
        "weight": "19–29 kg (42–65 lb)",
        "temperament": ["Engaging", "Active", "Even-tempered", "Affectionate"],
        "description": (
            "The Ibizan Hound is an ancient breed used by Egyptian pharaohs, later brought to "
            "the island of Ibiza. They are unique among sighthounds for hunting using scent, "
            "sight, and hearing. Athletic and energetic, they can jump great heights."
        ),
    },
    "irish-setter": {
        "name": "Irish Setter",
        "group": "Sporting",
        "origin": "Ireland",
        "lifespan": "11–15 years",
        "height": "61–69 cm (24–27 in)",
        "weight": "27–32 kg (60–71 lb)",
        "temperament": ["Energetic", "Lively", "Playful", "Companionable", "Affectionate"],
        "description": (
            "The Irish Setter is a stunning bird dog with a rich mahogany or chestnut-red coat. "
            "Renowned for their speed, enthusiasm, and stylish gait, they are rollicking, "
            "fun-loving companions both in the field and at home."
        ),
    },
    "irish-terrier": {
        "name": "Irish Terrier",
        "group": "Terrier",
        "origin": "Ireland",
        "lifespan": "13–15 years",
        "height": "45–48 cm (18–19 in)",
        "weight": "11–12 kg (25–27 lb)",
        "temperament": ["Lively", "Spirited", "Loyal", "Protective", "Intelligent"],
        "description": (
            "The Irish Terrier is one of the oldest terrier breeds and one of the first to be "
            "bred in Ireland. Known for their fiery red coats and reckless courage, they were "
            "called the 'daredevil' of the terrier family."
        ),
    },
    "irish-water-spaniel": {
        "name": "Irish Water Spaniel",
        "group": "Sporting",
        "origin": "Ireland",
        "lifespan": "10–12 years",
        "height": "51–58 cm (20–23 in)",
        "weight": "20–30 kg (45–65 lb)",
        "temperament": ["Hardworking", "Inquisitive", "Alert", "Clownish", "Loyal", "Trainable"],
        "description": (
            "The Irish Water Spaniel, the largest of the spaniels, sports a distinctive crisp "
            "liver-brown curly coat and a rat-like smooth tail. A skilled water retriever, "
            "they are playful, hardworking, and sometimes clownish."
        ),
    },
    "irish-wolfhound": {
        "name": "Irish Wolfhound",
        "group": "Hound",
        "origin": "Ireland",
        "lifespan": "6–10 years",
        "height": "71–90 cm (28–35 in)",
        "weight": "40–69 kg (90–152 lb)",
        "temperament": ["Loyal", "Sweet-tempered", "Thoughtful", "Generous", "Patient"],
        "description": (
            "The Irish Wolfhound is the tallest of all dog breeds and was bred in Ireland to "
            "hunt wolves and elk. Despite their immense size, they are gentle, patient, and "
            "noble animals, often described as 'gentle giants'."
        ),
    },
    "italian-greyhound": {
        "name": "Italian Greyhound",
        "group": "Toy",
        "origin": "Italy",
        "lifespan": "14–15 years",
        "height": "33–38 cm (13–15 in)",
        "weight": "3.5–5 kg (8–11 lb)",
        "temperament": ["Agile", "Alert", "Mischievous", "Athletic", "Loving", "Intelligent"],
        "description": (
            "The Italian Greyhound is a miniaturized sighthound that has been a lapdog of "
            "European nobility for centuries. Slender and elegant, they are affectionate and "
            "sensitive companions who love warmth and closeness."
        ),
    },
    "japanese-spaniel": {
        "name": "Japanese Chin",
        "group": "Toy",
        "origin": "Japan",
        "lifespan": "10–14 years",
        "height": "20–27 cm (8–11 in)",
        "weight": "1.4–6.8 kg (3–15 lb)",
        "temperament": ["Cat-like", "Intelligent", "Loyal", "Alert", "Independent"],
        "description": (
            "The Japanese Chin is an aristocratic toy breed with a distinctively cat-like "
            "personality—it uses its paws to wash its face and loves to perch on high places. "
            "A treasured companion of Japanese royalty for centuries."
        ),
    },
    "keeshond": {
        "name": "Keeshond",
        "group": "Non-Sporting",
        "origin": "Netherlands",
        "lifespan": "12–15 years",
        "height": "43–48 cm (17–19 in)",
        "weight": "14–18 kg (31–40 lb)",
        "temperament": ["Outgoing", "Playful", "Agile", "Obedient", "Alert", "Intelligent"],
        "description": (
            "The Keeshond (pronounced 'KAYS-hawnd') is the national dog of Holland, once "
            "serving as a barge watchdog on Dutch canals. Known for their spectacular 'spectacles' "
            "(shading and markings around the eyes) and plumed tail, they are friendly and family-oriented."
        ),
    },
    "kelpie": {
        "name": "Australian Kelpie",
        "group": "Herding",
        "origin": "Australia",
        "lifespan": "10–15 years",
        "height": "43–51 cm (17–20 in)",
        "weight": "14–21 kg (31–46 lb)",
        "temperament": ["Alert", "Energetic", "Loyal", "Intelligent", "Eager"],
        "description": (
            "The Australian Kelpie is a highly capable herding breed developed in Australia "
            "for mustering livestock across vast outback terrain. Tireless, independent, and "
            "extremely intelligent, they are workhorses of the Australian pastoral industry."
        ),
    },
    "kerry-blue-terrier": {
        "name": "Kerry Blue Terrier",
        "group": "Terrier",
        "origin": "Ireland",
        "lifespan": "13–15 years",
        "height": "44–51 cm (17–20 in)",
        "weight": "13–18 kg (29–40 lb)",
        "temperament": ["Playful", "Alert", "Adaptable", "Loyal", "Gentle"],
        "description": (
            "Named after County Kerry in Ireland, the Kerry Blue Terrier is known for its "
            "distinctive blue-grey wavy coat and versatility as a herder, hunter, and retriever. "
            "Spirited and strong, they are loyal and fun-loving family dogs."
        ),
    },
    "komondor": {
        "name": "Komondor",
        "group": "Working",
        "origin": "Hungary",
        "lifespan": "10–12 years",
        "height": "64–76 cm (25–30 in)",
        "weight": "36–61 kg (80–135 lb)",
        "temperament": ["Steady", "Fearless", "Loyal", "Gentle"],
        "description": (
            "The Komondor, Hungary's national dog, is instantly recognizable by its white "
            "corded coat—resembling a mop—which protects it from weather and predators. "
            "Originally a livestock guardian, they are powerful, independent, and fearlessly protective."
        ),
    },
    "kuvasz": {
        "name": "Kuvasz",
        "group": "Working",
        "origin": "Hungary",
        "lifespan": "10–12 years",
        "height": "66–76 cm (26–30 in)",
        "weight": "32–52 kg (70–115 lb)",
        "temperament": ["Clownish", "Patient", "Loyal", "Protective", "Independent", "Intelligent"],
        "description": (
            "The Kuvasz is an ancient Hungarian flock-guarding breed prized since the Middle Ages. "
            "With their pristine white double coat and noble bearing, they are devoted and "
            "courageous protectors with a gentle, patient nature."
        ),
    },
    "labrador-retriever": {
        "name": "Labrador Retriever",
        "group": "Sporting",
        "origin": "Canada",
        "lifespan": "10–14 years",
        "height": "54–62 cm (21–24 in)",
        "weight": "25–36 kg (55–80 lb)",
        "temperament": ["Outgoing", "Active", "Friendly", "Trusting", "Gentle", "Intelligent"],
        "description": (
            "The Labrador Retriever has been the most popular dog in the United States for "
            "decades. Originally from Newfoundland and bred to help fishermen, they are "
            "friendly, active, and outgoing, excelling as service and therapy dogs."
        ),
    },
    "lakeland-terrier": {
        "name": "Lakeland Terrier",
        "group": "Terrier",
        "origin": "England",
        "lifespan": "12–15 years",
        "height": "33–38 cm (13–15 in)",
        "weight": "7–8 kg (15–18 lb)",
        "temperament": ["Bold", "Friendly", "Confident", "Alert", "Independent", "Intelligent"],
        "description": (
            "The Lakeland Terrier, from the Lake District of England, was bred to hunt foxes "
            "that preyed on sheep in the harsh terrain. Small but hardy, they are bold and "
            "friendly dogs with a confident, alert expression."
        ),
    },
    "leonberg": {
        "name": "Leonberger",
        "group": "Working",
        "origin": "Germany",
        "lifespan": "8–9 years",
        "height": "65–80 cm (26–31 in)",
        "weight": "41–77 kg (90–170 lb)",
        "temperament": ["Fearless", "Obedient", "Loyal", "Companionable", "Gentle", "Playful"],
        "description": (
            "The Leonberger was created in the 19th century by Heinrich Essig of Leonberg, "
            "Germany, to resemble a lion. Combining the Saint Bernard, Newfoundland, and "
            "Great Pyrenees, they are gentle, patient, and affectionate family companions."
        ),
    },
    "lhasa": {
        "name": "Lhasa Apso",
        "group": "Non-Sporting",
        "origin": "Tibet",
        "lifespan": "12–15 years",
        "height": "25–28 cm (10–11 in)",
        "weight": "5–8 kg (12–18 lb)",
        "temperament": ["Obedient", "Fearless", "Lively", "Devoted", "Playful", "Assertive"],
        "description": (
            "The Lhasa Apso originated in Tibet as a sentinel dog in Buddhist monasteries, "
            "alerting monks to intruders. Their long, heavy coat, dark eyes, and proud bearing "
            "give them a regal appearance. They are independent yet loyal companions."
        ),
    },
    "malamute": {
        "name": "Alaskan Malamute",
        "group": "Working",
        "origin": "United States (Alaska)",
        "lifespan": "10–14 years",
        "height": "58–63 cm (23–25 in)",
        "weight": "34–38 kg (75–85 lb)",
        "temperament": ["Playful", "Devoted", "Loyal", "Dignified", "Friendly", "Affectionate"],
        "description": (
            "One of the oldest sled dog breeds, the Alaskan Malamute was bred by the Mahlemut "
            "Inuit people to haul heavy sleds across Arctic terrain. Strong, tireless, and "
            "independent, they are also affectionate and fun-loving."
        ),
    },
    "malinois": {
        "name": "Belgian Malinois",
        "group": "Herding",
        "origin": "Belgium",
        "lifespan": "14–16 years",
        "height": "56–66 cm (22–26 in)",
        "weight": "20–30 kg (44–66 lb)",
        "temperament": ["Alert", "Stubborn", "Confident", "Loyal", "Hard-working", "Protective"],
        "description": (
            "The Belgian Malinois is a world-class working dog and the preferred breed for "
            "military and police forces worldwide. Highly trainable, energetic, and driven, "
            "they form an intense bond with their handler and will work tirelessly."
        ),
    },
    "maltese-dog": {
        "name": "Maltese",
        "group": "Toy",
        "origin": "Mediterranean (Malta)",
        "lifespan": "12–15 years",
        "height": "20–25 cm (8–10 in)",
        "weight": "Under 3.2 kg (7 lb)",
        "temperament": ["Gentle", "Playful", "Fearless", "Lively", "Responsive", "Affectionate"],
        "description": (
            "The Maltese is one of the oldest toy breeds, with a history dating back at least "
            "2,000 years. Their long, silky white coat and dark expressive eyes give them a "
            "doll-like appearance. They are gentle, lively, and deeply affectionate."
        ),
    },
    "mexican-hairless": {
        "name": "Xoloitzcuintli (Mexican Hairless Dog)",
        "group": "Non-Sporting",
        "origin": "Mexico",
        "lifespan": "13–18 years",
        "height": "25–60 cm (10–24 in)",
        "weight": "3.6–23 kg (8–50 lb)",
        "temperament": ["Alert", "Loyal", "Calm", "Cheerful", "Athletic", "Companionable"],
        "description": (
            "The Xoloitzcuintli (Xolo) is one of the oldest and rarest breeds in the world, "
            "revered by the ancient Aztecs. This hairless (or coated) breed is considered "
            "Mexico's national dog and treasured as a calm, loyal companion."
        ),
    },
    "miniature-pinscher": {
        "name": "Miniature Pinscher",
        "group": "Toy",
        "origin": "Germany",
        "lifespan": "14–15 years",
        "height": "25–30 cm (10–12 in)",
        "weight": "3.5–5 kg (8–11 lb)",
        "temperament": ["Outgoing", "Playful", "Friendly", "Energetic", "Responsive", "Clever"],
        "description": (
            "Known as the 'King of Toys', the Miniature Pinscher (or Min Pin) is a compact, "
            "square-proportioned, and high-stepping breed. Despite resembling a small Doberman, "
            "they are an older and distinct German breed that was used to hunt vermin."
        ),
    },
    "miniature-poodle": {
        "name": "Miniature Poodle",
        "group": "Non-Sporting",
        "origin": "France / Germany",
        "lifespan": "14–18 years",
        "height": "28–38 cm (11–15 in)",
        "weight": "5–9 kg (12–20 lb)",
        "temperament": ["Faithful", "Energetic", "Trainable", "Instinctual", "Alert", "Intelligent"],
        "description": (
            "The Miniature Poodle shares all the characteristics of the Standard Poodle in a "
            "smaller package. Originally bred in Germany for water retrieval, all Poodle sizes "
            "are exceptionally intelligent and among the most trainable dog breeds."
        ),
    },
    "miniature-schnauzer": {
        "name": "Miniature Schnauzer",
        "group": "Terrier",
        "origin": "Germany",
        "lifespan": "12–15 years",
        "height": "30–36 cm (12–14 in)",
        "weight": "4.5–8 kg (11–18 lb)",
        "temperament": ["Obedient", "Fearless", "Friendly", "Spirited", "Alert", "Intelligent"],
        "description": (
            "The Miniature Schnauzer, the most popular of the three Schnauzer sizes, was "
            "developed in Germany to hunt rats on farms. They are alert, spirited, and "
            "intelligent with their signature bushy eyebrows and beard."
        ),
    },
    "newfoundland": {
        "name": "Newfoundland",
        "group": "Working",
        "origin": "Canada (Newfoundland)",
        "lifespan": "8–10 years",
        "height": "66–71 cm (26–28 in)",
        "weight": "45–68 kg (100–150 lb)",
        "temperament": ["Sweet-tempered", "Gentle", "Trainable", "Cheerful"],
        "description": (
            "The Newfoundland is a large, strong, and heavily coated working dog originally "
            "bred to help fishermen in Newfoundland. Remarkable water rescuers, they are "
            "sweet-tempered, patient, and devoted—ideal family and therapy dogs."
        ),
    },
    "norfolk-terrier": {
        "name": "Norfolk Terrier",
        "group": "Terrier",
        "origin": "England",
        "lifespan": "12–15 years",
        "height": "23–26 cm (9–10 in)",
        "weight": "5–5.4 kg (11–12 lb)",
        "temperament": ["Alert", "Fearless", "Self-confident", "Lovable", "Hardy"],
        "description": (
            "The Norfolk Terrier is one of the smallest working terriers and is identical to "
            "the Norwich Terrier except for its folded ears. Originally used to flush foxes "
            "from dens, they are spirited, affectionate, and adventurous."
        ),
    },
    "norwegian-elkhound": {
        "name": "Norwegian Elkhound",
        "group": "Hound",
        "origin": "Norway",
        "lifespan": "12–15 years",
        "height": "49–52 cm (19–21 in)",
        "weight": "20–23 kg (44–51 lb)",
        "temperament": ["Friendly", "Reliable", "Bold", "Alert", "Playful", "Loyal"],
        "description": (
            "The Norwegian Elkhound is one of the ancient Northern Spitz-type breeds, used "
            "for centuries to hunt moose and other big game in Scandinavia. Hardy, energetic, "
            "and fiercely loyal, they are one of the national dog breeds of Norway."
        ),
    },
    "norwich-terrier": {
        "name": "Norwich Terrier",
        "group": "Terrier",
        "origin": "England",
        "lifespan": "12–15 years",
        "height": "24–25 cm (9–10 in)",
        "weight": "5–5.4 kg (12 lb)",
        "temperament": ["Fearless", "Sensitive", "Self-confident", "Lovable", "Hardy"],
        "description": (
            "The Norwich Terrier is one of the smallest terrier breeds with erect ears (unlike "
            "the drop-eared Norfolk). Originally used by Cambridge University students as "
            "ratters, they are spirited, loyal, and adaptable companions."
        ),
    },
    "old-english-sheepdog": {
        "name": "Old English Sheepdog",
        "group": "Herding",
        "origin": "England",
        "lifespan": "10–12 years",
        "height": "56–61 cm (22–24 in)",
        "weight": "27–45 kg (60–101 lb)",
        "temperament": ["Playful", "Sociable", "Bubbly", "Gentle", "Loving", "Intelligent"],
        "description": (
            "The Old English Sheepdog, with its shaggy double coat and bear-like gait, is a "
            "beloved herding breed from England. Friendly and gentle with a clownish streak, "
            "they are devoted family dogs that adore children."
        ),
    },
    "otterhound": {
        "name": "Otterhound",
        "group": "Hound",
        "origin": "England",
        "lifespan": "10–13 years",
        "height": "61–69 cm (24–27 in)",
        "weight": "30–55 kg (66–121 lb)",
        "temperament": ["Boisterous", "Friendly", "Even-tempered", "Amiable"],
        "description": (
            "The Otterhound is a rare British breed originally developed to hunt otters in "
            "rivers. Known for its rough, shaggy coat, big nose, and webbed feet, it is one "
            "of the most endangered dog breeds in the world."
        ),
    },
    "papillon": {
        "name": "Papillon",
        "group": "Toy",
        "origin": "France / Belgium",
        "lifespan": "13–15 years",
        "height": "20–28 cm (8–11 in)",
        "weight": "3.6–5 kg (8–11 lb)",
        "temperament": ["Hardy", "Friendly", "Energetic", "Alert", "Intelligent"],
        "description": (
            "Named after the French word for butterfly due to its characteristic large, wing-like "
            "ears, the Papillon is a small but sturdy Continental Toy Spaniel. They are happy, "
            "alert, and highly intelligent, consistently ranking among the top breeds in obedience."
        ),
    },
    "pekinese": {
        "name": "Pekingese",
        "group": "Toy",
        "origin": "China",
        "lifespan": "12–15 years",
        "height": "15–23 cm (6–9 in)",
        "weight": "Under 6 kg (14 lb)",
        "temperament": ["Opinionated", "Stubborn", "Affectionate", "Aggressive", "Loyal", "Narcissistic"],
        "description": (
            "The Pekingese is one of the oldest toy breeds, created for Chinese royalty and "
            "associated with the Forbidden City for centuries. Dignified and independent, "
            "they carry themselves with imperial grace and are devoted to their chosen person."
        ),
    },
    "pembroke": {
        "name": "Pembroke Welsh Corgi",
        "group": "Herding",
        "origin": "Wales",
        "lifespan": "12–15 years",
        "height": "25–30 cm (10–12 in)",
        "weight": "Up to 14 kg (31 lb)",
        "temperament": ["Tenacious", "Friendly", "Outgoing", "Bold", "Playful", "Protective"],
        "description": (
            "The Pembroke Welsh Corgi, beloved by Queen Elizabeth II, is the most popular "
            "herding dog from Wales. Compact, athletic, and low-set, they are active and "
            "intelligent herders with a big-dog attitude in a small package."
        ),
    },
    "pomeranian": {
        "name": "Pomeranian",
        "group": "Toy",
        "origin": "Germany / Poland",
        "lifespan": "12–16 years",
        "height": "18–30 cm (7–12 in)",
        "weight": "1.9–3.5 kg (4–8 lb)",
        "temperament": ["Playful", "Friendly", "Sociable", "Extroverted", "Lively", "Active"],
        "description": (
            "The Pomeranian, a descendant of large Spitz sled dogs from northern Europe, is "
            "a tiny dog with a big personality. Beloved by Queen Victoria, they are vivacious, "
            "bold, and curious, wearing a spectacular fluffy double coat."
        ),
    },
    "pug": {
        "name": "Pug",
        "group": "Toy",
        "origin": "China",
        "lifespan": "12–15 years",
        "height": "25–36 cm (10–14 in)",
        "weight": "6–8 kg (14–18 lb)",
        "temperament": ["Docile", "Clever", "Charming", "Mischievous", "Stubborn", "Sociable"],
        "description": (
            "The Pug's motto is 'multum in parvo' (a lot in a little). This ancient Chinese "
            "breed was bred to be a lapdog for emperors. Compact, sturdy, and full of "
            "personality, Pugs are loving and attentive companions that live to be loved."
        ),
    },
    "redbone": {
        "name": "Redbone Coonhound",
        "group": "Hound",
        "origin": "United States",
        "lifespan": "12–14 years",
        "height": "53–68 cm (21–27 in)",
        "weight": "20–32 kg (45–70 lb)",
        "temperament": ["Eager", "Devoted", "Trainable", "Lively", "Active"],
        "description": (
            "The Redbone Coonhound is an American hunting breed developed for its ability to "
            "track and tree game, from raccoons to bears. Their striking red coat and musical "
            "voice have made them a beloved symbol of the American South."
        ),
    },
    "rhodesian-ridgeback": {
        "name": "Rhodesian Ridgeback",
        "group": "Hound",
        "origin": "Zimbabwe (Rhodesia)",
        "lifespan": "10–12 years",
        "height": "61–69 cm (24–27 in)",
        "weight": "29–41 kg (65–90 lb)",
        "temperament": ["Strong-willed", "Intelligent", "Mischievous", "Loyal", "Dignified", "Sensitive"],
        "description": (
            "The Rhodesian Ridgeback, developed in southern Africa to hunt lions alongside big-game "
            "hunters, is recognized by the distinctive ridge of hair running backward along its "
            "spine. Loyal, courageous, and intelligent, they are devoted family guardians."
        ),
    },
    "rottweiler": {
        "name": "Rottweiler",
        "group": "Working",
        "origin": "Germany",
        "lifespan": "8–10 years",
        "height": "56–69 cm (22–27 in)",
        "weight": "35–60 kg (77–132 lb)",
        "temperament": ["Devoted", "Obedient", "Fearless", "Alert", "Calm", "Good-natured", "Self-assured"],
        "description": (
            "The Rottweiler descends from the Roman drover dogs used to herd livestock and "
            "guard camps. A powerful breed with a natural guarding instinct, they are devoted "
            "to their families and—when properly trained—loyal, calm, and confident companions."
        ),
    },
    "saint-bernard": {
        "name": "Saint Bernard",
        "group": "Working",
        "origin": "Switzerland",
        "lifespan": "8–10 years",
        "height": "65–90 cm (26–35 in)",
        "weight": "64–120 kg (140–265 lb)",
        "temperament": ["Gentle", "Lively", "Watchful", "Friendly", "Calm"],
        "description": (
            "The Saint Bernard, famous for its Alpine rescue work, is one of the world's heaviest "
            "breeds. Bred by the monks of the Saint Bernard Pass in Switzerland, they are patient, "
            "gentle giants that are exceptionally good with children."
        ),
    },
    "saluki": {
        "name": "Saluki",
        "group": "Hound",
        "origin": "Middle East / Central Asia",
        "lifespan": "12–14 years",
        "height": "58–71 cm (23–28 in)",
        "weight": "16–29 kg (35–65 lb)",
        "temperament": ["Aloof", "Intelligent", "Reserved", "Gentle", "Quiet"],
        "description": (
            "The Saluki is one of the oldest known breeds, depicted in ancient Egyptian tombs "
            "and Sumerian carvings. Bred by nomadic tribes for hunting gazelles, they are "
            "graceful, swift sighthounds with a gentle, dignified temperament."
        ),
    },
    "samoyed": {
        "name": "Samoyed",
        "group": "Working",
        "origin": "Russia (Siberia)",
        "lifespan": "12–14 years",
        "height": "46–60 cm (18–24 in)",
        "weight": "16–30 kg (35–66 lb)",
        "temperament": ["Lively", "Sociable", "Playful", "Alert", "Stubborn", "Friendly"],
        "description": (
            "The Samoyed is a beautiful working breed from Siberia, bred by the Samoyedic peoples "
            "for herding reindeer and pulling sleds. Their permanent 'Samoyed smile' prevents "
            "drooling and icicle formation. Sociable and gentle, they thrive in families."
        ),
    },
    "schipperke": {
        "name": "Schipperke",
        "group": "Non-Sporting",
        "origin": "Belgium",
        "lifespan": "13–15 years",
        "height": "25–33 cm (10–13 in)",
        "weight": "3–9 kg (7–20 lb)",
        "temperament": ["Faithful", "Fearless", "Energetic", "Curious", "Confident", "Lively"],
        "description": (
            "The Schipperke ('little captain' in Flemish) was originally a Belgian barge and "
            "ratting dog. Small, nimble, and perpetually curious, they are known for their "
            "fox-like face, jet-black coat, and mischievous, inquisitive personality."
        ),
    },
    "scotch-terrier": {
        "name": "Scottish Terrier",
        "group": "Terrier",
        "origin": "Scotland",
        "lifespan": "11–13 years",
        "height": "25–28 cm (10–11 in)",
        "weight": "8–10 kg (19–23 lb)",
        "temperament": ["Feisty", "Alert", "Self-assured", "Playful", "Quick", "Independent"],
        "description": (
            "The Scottish Terrier ('Scottie') is one of the most iconic of Scottish breeds. "
            "With its distinctive long beard, bushy eyebrows, and compact body, the Scottie "
            "has a spirited, independent character and a feisty, dignified nature."
        ),
    },
    "sealyham-terrier": {
        "name": "Sealyham Terrier",
        "group": "Terrier",
        "origin": "Wales",
        "lifespan": "12–14 years",
        "height": "25–31 cm (10–12 in)",
        "weight": "8–9 kg (18–20 lb)",
        "temperament": ["Alert", "Outgoing", "Loyal", "Calm"],
        "description": (
            "The Sealyham Terrier was developed in the mid-19th century by Captain John Edwardes "
            "at Sealyham House in Wales. Once one of the most fashionable dogs in Britain, "
            "they are rare today but remain charming, friendly companions."
        ),
    },
    "shetland-sheepdog": {
        "name": "Shetland Sheepdog",
        "group": "Herding",
        "origin": "Scotland (Shetland Islands)",
        "lifespan": "12–13 years",
        "height": "33–41 cm (13–16 in)",
        "weight": "6–12 kg (14–27 lb)",
        "temperament": ["Playful", "Energetic", "Vocal", "Alert", "Loyal", "Gentle", "Intelligent"],
        "description": (
            "The Shetland Sheepdog (Sheltie) resembles a miniature Rough Collie and was bred "
            "on the harsh Shetland Islands for herding sheep and ponies. Highly intelligent and "
            "responsive, they excel at obedience, agility, and tracking."
        ),
    },
    "shih-tzu": {
        "name": "Shih Tzu",
        "group": "Toy",
        "origin": "Tibet / China",
        "lifespan": "10–16 years",
        "height": "20–28 cm (8–11 in)",
        "weight": "4–7.25 kg (9–16 lb)",
        "temperament": ["Playful", "Outgoing", "Alert", "Friendly", "Loyal", "Independent"],
        "description": (
            "The Shih Tzu ('lion dog' in Chinese) was bred to resemble the lions in ancient "
            "Oriental art. A treasured companion of Chinese royalty, they are affectionate, "
            "happy dogs with a luxurious flowing coat and unmistakable round, dark eyes."
        ),
    },
    "siberian-husky": {
        "name": "Siberian Husky",
        "group": "Working",
        "origin": "Russia (Siberia)",
        "lifespan": "12–14 years",
        "height": "51–60 cm (20–24 in)",
        "weight": "16–27 kg (35–60 lb)",
        "temperament": ["Outgoing", "Mischievous", "Loyal", "Gentle", "Alert", "Friendly"],
        "description": (
            "The Siberian Husky is a beautiful working sled dog, bred by the Chukchi people "
            "of northeastern Asia for endurance racing across vast frozen distances. Athletic, "
            "resilient, and friendly, they have a wolf-like appearance and playful spirit."
        ),
    },
    "silky-terrier": {
        "name": "Silky Terrier",
        "group": "Toy",
        "origin": "Australia",
        "lifespan": "12–15 years",
        "height": "23–26 cm (9–10 in)",
        "weight": "3.5–4.5 kg (8–10 lb)",
        "temperament": ["Friendly", "Alert", "Quick", "Responsive"],
        "description": (
            "The Silky Terrier (Australian Silky Terrier) was developed in Australia in the "
            "late 19th century from the Australian Terrier and the Yorkshire Terrier. Small "
            "but true terriers at heart, they are spirited, alert, and love to dig and hunt."
        ),
    },
    "soft-coated-wheaten-terrier": {
        "name": "Soft Coated Wheaten Terrier",
        "group": "Terrier",
        "origin": "Ireland",
        "lifespan": "12–15 years",
        "height": "44–50 cm (17–20 in)",
        "weight": "14–20 kg (30–45 lb)",
        "temperament": ["Playful", "Energetic", "Faithful", "Confident", "Spirited", "Intelligent"],
        "description": (
            "The Soft Coated Wheaten Terrier is a medium-sized Irish farm dog known for its "
            "silky, wheaten-coloured coat and exuberant greeting style (the 'Wheaten Greeting'). "
            "Loyal and energetic, they are excellent family dogs."
        ),
    },
    "staffordshire-bullterrier": {
        "name": "Staffordshire Bull Terrier",
        "group": "Terrier",
        "origin": "England",
        "lifespan": "12–14 years",
        "height": "36–41 cm (14–16 in)",
        "weight": "11–17 kg (24–38 lb)",
        "temperament": ["Bold", "Fearless", "Reliable", "Loyal", "Affectionate"],
        "description": (
            "The Staffordshire Bull Terrier is a courageous, highly intelligent breed, and one "
            "of only two breeds that the Kennel Club officially describes as 'totally reliable' "
            "with children. Deeply affectionate, they are sometimes called 'nanny dogs'."
        ),
    },
    "standard-poodle": {
        "name": "Standard Poodle",
        "group": "Non-Sporting",
        "origin": "Germany / France",
        "lifespan": "12–15 years",
        "height": "Over 38 cm (15 in)",
        "weight": "20–32 kg (44–71 lb)",
        "temperament": ["Faithful", "Trainable", "Energetic", "Instinctual", "Alert", "Intelligent"],
        "description": (
            "The Standard Poodle is the largest of the three poodle varieties and one of the "
            "most intelligent dog breeds. Originally a water retriever, they excel at virtually "
            "every dog sport and activity, from hunting to obedience to therapy work."
        ),
    },
    "standard-schnauzer": {
        "name": "Standard Schnauzer",
        "group": "Working",
        "origin": "Germany",
        "lifespan": "13–16 years",
        "height": "44–50 cm (17–20 in)",
        "weight": "14–20 kg (31–44 lb)",
        "temperament": ["Lively", "Playful", "Devoted", "Alert", "Intelligent"],
        "description": (
            "The Standard Schnauzer is the original of the three Schnauzer breeds and has "
            "served as a ratter, herder, watchdog, and messenger dog in wartime. Robust and "
            "spirited, they are devoted companions with a distinctive whiskered muzzle."
        ),
    },
    "sussex-spaniel": {
        "name": "Sussex Spaniel",
        "group": "Sporting",
        "origin": "England",
        "lifespan": "11–13 years",
        "height": "33–38 cm (13–15 in)",
        "weight": "16–20 kg (35–45 lb)",
        "temperament": ["Friendly", "Sociable", "Even-tempered", "Loyal"],
        "description": (
            "The Sussex Spaniel is one of the few dog breeds developed in England that came "
            "close to extinction. A low-to-the-ground golden-liver hunting dog, they are "
            "rare but celebrated for their cheerful, sociable nature."
        ),
    },
    "tibetan-mastiff": {
        "name": "Tibetan Mastiff",
        "group": "Working",
        "origin": "Tibet",
        "lifespan": "12–15 years",
        "height": "61–71 cm (24–28 in)",
        "weight": "45–160 kg (100–353 lb)",
        "temperament": ["Stubborn", "Tenacious", "Aloof", "Intelligent", "Protective", "Strong-willed"],
        "description": (
            "The Tibetan Mastiff is one of the most ancient and massive of all breeds, "
            "developed to protect Tibetan monasteries, villages, and livestock. Night-active "
            "guardians, they are devoted to their families but highly independent and wary of strangers."
        ),
    },
    "tibetan-terrier": {
        "name": "Tibetan Terrier",
        "group": "Non-Sporting",
        "origin": "Tibet",
        "lifespan": "12–15 years",
        "height": "35–41 cm (14–16 in)",
        "weight": "8–14 kg (18–30 lb)",
        "temperament": ["Gentle", "Lively", "Energetic", "Reserved", "Loyal", "Sensitive"],
        "description": (
            "Despite the name, the Tibetan Terrier is not a true terrier. Bred by Buddhist "
            "monks as a lucky charm, herder, and watchdog in the 'Lost Valley' of Tibet, "
            "they are gentle, sensitive, and highly adaptable companions."
        ),
    },
    "toy-poodle": {
        "name": "Toy Poodle",
        "group": "Toy",
        "origin": "France / Germany",
        "lifespan": "14–18 years",
        "height": "Under 25 cm (10 in)",
        "weight": "Under 4.5 kg (10 lb)",
        "temperament": ["Faithful", "Trainable", "Instinctual", "Active", "Alert", "Intelligent"],
        "description": (
            "The Toy Poodle is the smallest of the three Poodle varieties and combines the "
            "intelligence and trainability of the Standard with a convenient size. Lively "
            "and fun-loving, they are perfect apartment dogs and excellent therapy animals."
        ),
    },
    "toy-terrier": {
        "name": "English Toy Terrier",
        "group": "Toy",
        "origin": "England",
        "lifespan": "12–13 years",
        "height": "25–30 cm (10–12 in)",
        "weight": "2.7–3.6 kg (6–8 lb)",
        "temperament": ["Alert", "Energetic", "Discerning", "Loyal"],
        "description": (
            "The English Toy Terrier (Black & Tan) is the oldest of the toy breeds and a "
            "descendant of the rat-baiting Manchester Terrier. Elegant and alert, they are "
            "one of the rarest breeds in the world, prized for their loyalty and grace."
        ),
    },
    "vizsla": {
        "name": "Vizsla",
        "group": "Sporting",
        "origin": "Hungary",
        "lifespan": "12–15 years",
        "height": "53–64 cm (21–25 in)",
        "weight": "20–30 kg (44–66 lb)",
        "temperament": ["Energetic", "Loyal", "Gentle", "Affectionate", "Quiet", "Trainable"],
        "description": (
            "The Vizsla is Hungary's national breed, an outstanding hunting dog with a golden-rust "
            "coat. One of the 'velcro dogs', Vizslas form an exceptionally close bond with their "
            "owner and dislike being left alone. They are affectionate and high-energy."
        ),
    },
    "walker-hound": {
        "name": "Treeing Walker Coonhound",
        "group": "Hound",
        "origin": "United States",
        "lifespan": "12–13 years",
        "height": "51–69 cm (20–27 in)",
        "weight": "23–32 kg (50–70 lb)",
        "temperament": ["Intelligent", "Confident", "Alert", "Sociable"],
        "description": (
            "The Treeing Walker Coonhound is an American hunting breed descended from the "
            "English Foxhound. They are fast, competitive trail dogs known for their ability "
            "to track and tree a wide variety of game, from raccoons to cougars."
        ),
    },
    "weimaraner": {
        "name": "Weimaraner",
        "group": "Sporting",
        "origin": "Germany",
        "lifespan": "11–14 years",
        "height": "56–69 cm (22–27 in)",
        "weight": "25–40 kg (55–88 lb)",
        "temperament": ["Stubborn", "Energetic", "Alert", "Obedient", "Powerful", "Intelligent"],
        "description": (
            "The Weimaraner, known as the 'Grey Ghost', is a striking silver-grey breed "
            "developed for hunting large game in 19th-century Germany. Fearless and friendly, "
            "they are intensely loyal to their family and need plenty of exercise."
        ),
    },
    "welsh-springer-spaniel": {
        "name": "Welsh Springer Spaniel",
        "group": "Sporting",
        "origin": "Wales",
        "lifespan": "12–15 years",
        "height": "43–48 cm (17–19 in)",
        "weight": "16–20 kg (35–45 lb)",
        "temperament": ["Stubborn", "Reserved", "Playful", "Loyal", "Affectionate"],
        "description": (
            "The Welsh Springer Spaniel is an ancient breed depicted in tapestries from the "
            "14th century. A compact, versatile gun dog with a distinctive red-and-white coat, "
            "they are loyal and affectionate with their family but reserved with strangers."
        ),
    },
    "west-highland-white-terrier": {
        "name": "West Highland White Terrier",
        "group": "Terrier",
        "origin": "Scotland",
        "lifespan": "12–16 years",
        "height": "25–28 cm (10–11 in)",
        "weight": "6–10 kg (15–22 lb)",
        "temperament": ["Hardy", "Playful", "Alert", "Loyal", "Independent", "Friendly"],
        "description": (
            "The West Highland White Terrier ('Westie') is a small, sturdy Scottish terrier "
            "famous for its brilliant white coat and confident, friendly nature. Originally "
            "bred to hunt vermin in rocky terrain, they are peppy, self-assured companions."
        ),
    },
    "whippet": {
        "name": "Whippet",
        "group": "Hound",
        "origin": "England",
        "lifespan": "12–15 years",
        "height": "44–56 cm (17–22 in)",
        "weight": "12.5–13.5 kg (25–40 lb)",
        "temperament": ["Gentle", "Lively", "Playful", "Quiet", "Affectionate", "Intelligent"],
        "description": (
            "The Whippet, the fastest accelerating dog breed (up to 56 km/h), was developed "
            "in England for rabbit coursing and racing. Elegant and gentle, they are quiet "
            "and affectionate at home but explosive with energy in the field."
        ),
    },
    "wire-haired-fox-terrier": {
        "name": "Wire Fox Terrier",
        "group": "Terrier",
        "origin": "England",
        "lifespan": "13–14 years",
        "height": "36–41 cm (14–16 in)",
        "weight": "7–9 kg (15–20 lb)",
        "temperament": ["Bold", "Alert", "Confident", "Friendly", "Playful", "Lively"],
        "description": (
            "The Wire Fox Terrier was bred in England to flush foxes from their dens during "
            "the fox hunt. They have won more Best in Show titles at Westminster than any "
            "other breed—a testament to their stylish looks and vibrant, bold personality."
        ),
    },
    "scottish-deerhound": {
        "name": "Scottish Deerhound",
        "group": "Hound",
        "origin": "Scotland",
        "lifespan": "8–11 years",
        "height": "71–81 cm (28–32 in)",
        "weight": "34–50 kg (75–110 lb)",
        "temperament": ["Docile", "Friendly", "Gentle", "Dignified", "Obedient"],
        "description": (
            "The Scottish Deerhound is one of the tallest sighthound breeds, bred for centuries "
            "to course red deer in the Scottish Highlands. Regal and gentle, they are devoted "
            "companions with a calm, dignified temperament and a strong prey drive."
        ),
    },
    "bedlington-terrier": {
        "name": "Bedlington Terrier",
        "group": "Terrier",
        "origin": "England",
        "lifespan": "14–16 years",
        "height": "38–43 cm (15–17 in)",
        "weight": "8–10 kg (17–23 lb)",
        "temperament": ["Affectionate", "Spirited", "Intelligent", "Loyal", "Good-tempered"],
        "description": (
            "The Bedlington Terrier is a uniquely lamb-like terrier from Bedlington, "
            "Northumberland, England. Despite their gentle, fluffy appearance, they are "
            "swift, agile hunters with great stamina—once used to hunt vermin in mines."
        ),
    },
    "yorkshire-terrier": {
        "name": "Yorkshire Terrier",
        "group": "Toy",
        "origin": "England",
        "lifespan": "13–16 years",
        "height": "17–23 cm (7–9 in)",
        "weight": "Under 3.2 kg (7 lb)",
        "temperament": ["Bold", "Independent", "Confident", "Courageous", "Intelligent"],
        "description": (
            "The Yorkshire Terrier, or 'Yorkie', may be small but has a big-dog attitude. "
            "Developed in Yorkshire, England, to catch rats in clothing mills, today's Yorkies "
            "are glamorous, spirited companions with a floor-length silky blue-and-tan coat."
        ),
    },
}

# Alias map to handle dataset folder-name variations
# Key: a dataset folder name (lower-cased, hyphenated prefix removed as used by Stanford Dogs)
# Value: the canonical key in BREED_INFO
BREED_ALIASES: dict[str, str] = {
    "n02085620-chihuahua": "chihuahua",
    "n02085782-japanese_spaniel": "japanese-spaniel",
    "n02085936-maltese_dog": "maltese-dog",
    "n02086079-pekinese": "pekinese",
    "n02086240-shih-tzu": "shih-tzu",
    "n02086646-blenheim_spaniel": "cocker-spaniel",
    "n02086910-papillon": "papillon",
    "n02087046-toy_terrier": "toy-terrier",
    "n02087394-rhodesian_ridgeback": "rhodesian-ridgeback",
    "n02088094-afghan_hound": "afghan-hound",
    "n02088238-basset": "basset",
    "n02088364-beagle": "beagle",
    "n02088466-bloodhound": "bloodhound",
    "n02088632-bluetick": "bluetick",
    "n02089078-black-and-tan_coonhound": "black-and-tan-coonhound",
    "n02089867-walker_hound": "walker-hound",
    "n02089973-english_foxhound": "english-foxhound",
    "n02090379-redbone": "redbone",
    "n02090622-borzoi": "borzoi",
    "n02090721-irish_wolfhound": "irish-wolfhound",
    "n02091032-italian_greyhound": "italian-greyhound",
    "n02091134-whippet": "whippet",
    "n02091244-ibizan_hound": "ibizan-hound",
    "n02091467-norwegian_elkhound": "norwegian-elkhound",
    "n02091635-otterhound": "otterhound",
    "n02091831-saluki": "saluki",
    "n02092002-scottish_deerhound": "scottish-deerhound",
    "n02092339-weimaraner": "weimaraner",
    "n02093256-staffordshire_bullterrier": "staffordshire-bullterrier",
    "n02093428-american_staffordshire_terrier": "american-staffordshire-terrier",
    "n02093647-bedlington_terrier": "bedlington-terrier",
    "n02093754-border_terrier": "border-terrier",
    "n02093859-kerry_blue_terrier": "kerry-blue-terrier",
    "n02093991-irish_terrier": "irish-terrier",
    "n02094114-norfolk_terrier": "norfolk-terrier",
    "n02094258-norwich_terrier": "norwich-terrier",
    "n02094433-yorkshire_terrier": "yorkshire-terrier",
    "n02095314-wire-haired_fox_terrier": "wire-haired-fox-terrier",
    "n02095570-lakeland_terrier": "lakeland-terrier",
    "n02095889-sealyham_terrier": "sealyham-terrier",
    "n02096051-airedale": "airedale",
    "n02096177-cairn": "cairn",
    "n02096294-dandie_dinmont": "dandie-dinmont",
    "n02096437-boston_bull": "boston-bull",
    "n02096585-clumber": "clumber",
    "n02097047-miniature_schnauzer": "miniature-schnauzer",
    "n02097130-giant_schnauzer": "standard-schnauzer",
    "n02097209-standard_schnauzer": "standard-schnauzer",
    "n02097298-scotch_terrier": "scotch-terrier",
    "n02097474-tibetan_terrier": "tibetan-terrier",
    "n02097658-silky_terrier": "silky-terrier",
    "n02098105-soft-coated_wheaten_terrier": "soft-coated-wheaten-terrier",
    "n02098286-west_highland_white_terrier": "west-highland-white-terrier",
    "n02098413-lhasa": "lhasa",
    "n02099267-flat-coated_retriever": "flat-coated-retriever",
    "n02099429-curly-coated_retriever": "curly-coated-retriever",
    "n02099601-golden_retriever": "golden-retriever",
    "n02099712-labrador_retriever": "labrador-retriever",
    "n02099849-chesapeake_bay_retriever": "chesapeake-bay-retriever",
    "n02100236-german_short-haired_pointer": "german-short-haired-pointer",
    "n02100583-vizsla": "vizsla",
    "n02100735-english_setter": "english-setter",
    "n02100877-irish_setter": "irish-setter",
    "n02101006-gordon_setter": "gordon-setter",
    "n02101388-brittany_spaniel": "brittany-spaniel",
    "n02101556-clumber": "clumber",
    "n02102040-english_springer": "english-springer",
    "n02102177-welsh_springer_spaniel": "welsh-springer-spaniel",
    "n02102318-cocker_spaniel": "cocker-spaniel",
    "n02102480-sussex_spaniel": "sussex-spaniel",
    "n02102973-irish_water_spaniel": "irish-water-spaniel",
    "n02104029-kuvasz": "kuvasz",
    "n02104365-schipperke": "schipperke",
    "n02105056-groenendael": "groenendael",
    "n02105162-malinois": "malinois",
    "n02105251-briard": "briard",
    "n02105412-kelpie": "kelpie",
    "n02105505-komondor": "komondor",
    "n02105641-old_english_sheepdog": "old-english-sheepdog",
    "n02105855-shetland_sheepdog": "shetland-sheepdog",
    "n02106030-collie": "collie",
    "n02106166-border_collie": "border-collie",
    "n02106382-bouvier_des_flandres": "bouvier-des-flandres",
    "n02106550-rottweiler": "rottweiler",
    "n02106662-german_shepherd": "german-shepherd",
    "n02107142-doberman": "doberman",
    "n02107312-miniature_pinscher": "miniature-pinscher",
    "n02107574-greater_swiss_mountain_dog": "appenzeller",
    "n02107683-bernese_mountain_dog": "appenzeller",
    "n02107908-appenzeller": "appenzeller",
    "n02108000-entlebucher": "entlebucher",
    "n02108089-boxer": "boxer",
    "n02108422-bull_mastiff": "bull-mastiff",
    "n02108551-tibetan_mastiff": "tibetan-mastiff",
    "n02108915-french_bulldog": "french-bulldog",
    "n02109047-great_dane": "great-dane",
    "n02109525-saint_bernard": "saint-bernard",
    "n02109961-eskimo_dog": "eskimo-dog",
    "n02110063-malamute": "malamute",
    "n02110185-siberian_husky": "siberian-husky",
    "n02110627-affenpinscher": "affenpinscher",
    "n02110806-basenji": "basenji",
    "n02110958-pug": "pug",
    "n02111129-leonberg": "leonberg",
    "n02111277-newfoundland": "newfoundland",
    "n02111500-great_pyrenees": "great-pyrenees",
    "n02111889-samoyed": "samoyed",
    "n02112018-pomeranian": "pomeranian",
    "n02112137-chow": "chow",
    "n02112350-keeshond": "keeshond",
    "n02112706-brabancon_griffon": "affenpinscher",
    "n02113023-pembroke": "pembroke",
    "n02113186-cardigan": "cardigan",
    "n02113624-toy_poodle": "toy-poodle",
    "n02113712-miniature_poodle": "miniature-poodle",
    "n02113799-standard_poodle": "standard-poodle",
    "n02113978-mexican_hairless": "mexican-hairless",
    "n02115641-dingo": "basenji",
    "n02115913-dhole": "african-hunting-dog",
    "n02116738-african_hunting_dog": "african-hunting-dog",
}


def get_breed_info(breed_key: str) -> dict:
    """
    Return breed information for the given key.

    The key may be:
    - A canonical breed key (e.g. 'golden-retriever')
    - A Stanford Dogs Dataset folder name (e.g. 'n02099601-golden_retriever')
    - Any case variant of the above

    Returns a dict with breed details, or a minimal 'unknown' dict.
    """
    normalised = breed_key.strip().lower()

    # Direct lookup
    if normalised in BREED_INFO:
        return BREED_INFO[normalised]

    # Try alias map
    alias = BREED_ALIASES.get(normalised)
    if alias and alias in BREED_INFO:
        return BREED_INFO[alias]

    # Try partial / fuzzy match on canonical keys
    for key in BREED_INFO:
        if key in normalised or normalised in key:
            return BREED_INFO[key]

    # Try partial match on alias values
    for alias_key, canonical in BREED_ALIASES.items():
        if normalised in alias_key or alias_key in normalised:
            if canonical in BREED_INFO:
                return BREED_INFO[canonical]

    return {
        "name": breed_key.replace("-", " ").replace("_", " ").title(),
        "group": "Unknown",
        "origin": "Unknown",
        "lifespan": "Unknown",
        "height": "Unknown",
        "weight": "Unknown",
        "temperament": [],
        "description": "No detailed information is available for this breed.",
    }
