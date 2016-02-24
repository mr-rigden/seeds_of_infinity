import generators.misc as misc

def get_all_creatures():
    all_creatures = []
    all_creatures.extend(get_dragons())
    all_creatures.extend(get_elementals())
    all_creatures.extend(get_golems())
    all_creatures.extend(get_humanoids())
    all_creatures.extend(get_mythical_animals())
    all_creatures.extend(get_natural_animals())
    all_creatures.extend(get_supernatural_creatures())
    all_creatures_set = set(all_creatures)
    all_creatures = list(all_creatures_set)
    all_creatures.sort()
    return all_creatures

def get_dragons():
    dragons = []
    for color in misc.get_basic_colors():
        dragon = color + ' dragon'
        dragons.append(dragon)
    for metal in misc.get_metals():
        dragon = metal + ' dragon'
        dragons.append(dragon)
    for gem in misc.get_gems():
        dragon = gem + ' dragon'
        dragons.append(dragon)
    for element in misc.get_elements():
        dragon = element + ' elemental dragon'
        dragons.append(dragon)
    return dragons

def get_elementals():
    elementals = []
    for element in misc.get_elements():
        elemental = element + ' elemental'
        elementals.append(elemental)
    return elementals

def get_golems():
    golems = []
    for gem in misc.get_gems():
        golem = gem + ' golem'
        golems.append(golem)
    for metal in misc.get_metals():
        golem = metal + ' golem'
        golems.append(golem)
    for stone in misc.get_stones():
        golem = stone + ' golem'
        golems.append(golem)
    for stuff in misc.get_stuff():
        golem = stuff + ' golem'
        golems.append(golem)
    return golems

def get_humanoids():
    HUMANOIDS = [
        'dwarf',
        'dwarf',
        'elf',
        'fairy',
        'giant',
        'gnoll',
        'gnome',
        'goblin',
        'ghoul',
        'gremlin',
        'halfling',
        'hobgoblin',
        'human',
        'imp',
        'kobald',
        'leprechaun',
        'lizardfolk',
        'merfolk',
        'nephilim',
        'ogre',
        'pixie',
        'ratfolk',
        'satyr',
        'tengu',
        'treefolk',
        'troll',
        'vampire',
        'yeti',
        'zombie'
    ]
    return HUMANOIDS

def get_mythical_animals():
    mythical_animals = [
        'griffin',
        'sphinx',
    ]
    return mythical_animals

def get_natural_animals():
    NATURAL_ANIMALS = [
        'Aardvark',
        'Albatross',
        'Alligator',
        'Alpaca',
        'Ant',
        'Anteater',
        'Antelope',
        'Ape',
        'Armadillo',
        'Ass',
        'Donkey',
        'Baboon',
        'Badger',
        'Barracuda',
        'Bat',
        'Bear',
        'Beaver',
        'Bee',
        'Bison',
        'Boar',
        'Buffalo',
        'Camel',
        'Caribou',
        'Cheetah',
        'Chicken',
        'Chimpanzee',
        'Chinchilla',
        'Chipmonk',
        'Chough',
        'Clam',
        'Cobra',
        'Cockroach',
        'Cod',
        'Cormorant',
        'cougar',
        'Cow',
        'Coyote',
        'Crab',
        'Crane',
        'Crocodile',
        'Crow',
        'Curlew',
        'Deer',
        'Dinosaur',
        'dingo',
        'Dog',
        'Dogfish',
        'Dolphin',
        'Donkey',
        'Dotterel',
        'Dove',
        'Dragonfly',
        'Duck',
        'Dugong',
        'Dunlin',
        'Eagle',
        'earthworm',
        'earwig',
        'Echidna',
        'Eel',
        'Eland',
        'Elephant',
        'Elephant seal',
        'Elk',
        'Emu',
        'Falcon',
        'Ferret',
        'Finch',
        'Fish',
        'Flamingo',
        'Fly',
        'Fox',
        'Frog',
        'Gaur',
        'Gazelle',
        'gecko',
        'Gerbil',
        'Giant Panda',
        'Giraffe',
        'Gnat',
        'Gnu',
        'Goat',
        'Goose',
        'Goldfinch',
        'Goldfish',
        'gopher',
        'Gorilla',
        'Goshawk',
        'Grasshopper',
        'great white shark',
        'grizzly bear',
        'Grouse',
        'Guanaco',
        'Guinea fowl',
        'Guinea pig',
        'Gull',
        'Hamster',
        'Hare',
        'Hawk',
        'Hedgehog',
        'Heron',
        'Hermit crab',
        'Herring',
        'Hippopotamus',
        'Hornet',
        'Horse',
        'Human',
        'Hummingbird',
        'Hyena',
        'Jackal',
        'Jaguar',
        'Jay',
        'Jay, Blue',
        'Jellyfish',
        'Kangaroo',
        'Koala',
        'Komodo dragon',
        'Kouprey',
        'Kudu',
        'Lapwing',
        'Lark',
        'Lemur',
        'Leopard',
        'Lion',
        'Llama',
        'Lobster',
        'Locust',
        'Loris',
        'Louse',
        'Lyrebird',
        'macaw',
        'Magpie',
        'Mallard',
        'Manatee',
        'Marten',
        'Meerkat',
        'Mink',
        'Mole',
        'mongoose',
        'Monkey',
        'Moose',
        'Mouse',
        'Mosquito',
        'moth',
        'Mule',
        'Narwhal',
        'Newt',
        'Nightingale',
        'Octopus',
        'Okapi',
        'Opossum',
        'Oryx',
        'Ostrich',
        'Otter',
        'Owl',
        'Ox',
        'Oyster',
        'Panther',
        'Parrot',
        'Partridge',
        'Peacock',
        'Pelican',
        'Penguin',
        'Pheasant',
        'Pig',
        'Pigeon',
        'Piranha',
        'Pony',
        'Porcupine',
        'Porpoise',
        'possum',
        'Prairie Dog',
        'prawn',
        'puffin',
        'puma',
        'Quail',
        'Quelea',
        'Rabbit',
        'Raccoon',
        'Rail',
        'Ram',
        'Rat',
        'Rattlesnake',
        'Raven',
        'Red deer',
        'Red panda',
        'Reindeer',
        'Rhinoceros',
        'Robin',
        'rooster',
        'Rook',
        'Ruff',
        'Salamander',
        'Salmon',
        'Sand Dollar',
        'Sandpiper',
        'Sardine',
        'Scorpion',
        'Sea lion',
        'sea slug',
        'Sea Urchin',
        'Seahorse',
        'Seal',
        'Shark',
        'Sheep',
        'Shrew',
        'Shrimp',
        'Skunk',
        'sloth',
        'Snail',
        'Snake',
        'sparrow',
        'Spider',
        'sponge',
        'Squid',
        'Squirrel',
        'starfish',
        'Starling',
        'Stingray',
        'Stinkbug',
        'Stork',
        'Swallow',
        'Swan',
        'tang',
        'Tapir',
        'Tasmanian Devil',
        'Tarsier',
        'Termite',
        'Tiger',
        'Toad',
        'Trout',
        'Turkey',
        'Turtle',
        'Viper',
        'Vulture',
        'Wallaby',
        'Walrus',
        'Wasp',
        'Water buffalo',
        'Weasel',
        'Whale',
        'Wolf',
        'Wolverine',
        'Wombat',
        'Woodcock',
        'Woodpecker',
        'Worm',
        'Wren',
        'Yak',
        'Zebra'
    ]
    NATURAL_ANIMALS = [x.lower() for x in NATURAL_ANIMALS]
    return NATURAL_ANIMALS

def get_supernatural_creatures():
    supernatural_creatures = [
        'angel',
        'demon',
    ]
    return supernatural_creatures
