import random
import sys
import time

def your_character(character):
    return 'Your Character: ' + character+ "\n"
def your_team(team):
    return 'Your Team: ' + team + "\n"
def boss_string(bosses):
    string = "Boss order: " + "\n"
    i = 1
    for boss in bosses:
        string += str(i)+": " + boss + "\n"
        i+=1
    return string

def other_restraints(game, other):
    num = int(game[1])
    string=""
    if other[1].get():
        if num > 6:
            characters = ['X', 'Zero', 'Axl']
            random.shuffle(characters)
            character = characters[0] + ' and ' + characters[1]
            string+= your_team(character)
        elif num > 4:
            character = random.choice(['X', 'Zero', 'X and Zero'])
            string+=  your_team(character) if 'and' in character else your_character(character)
        elif num == 4:
            character = random.choice(['X', 'Zero'])
            string+=  your_character(character)
        else:
            character = 'X'


    if other[2].get():
        armor_choices = {'x1': random.randint(2,4),
                        'x2': random.choice(['Base'] + range(1, 4)),
                        'x3': random.choice(range(1,6)+ ['Base','Golden']),
                        'x4': random.choice(range(1,5)+['Base', 'Ultimate']),
                        'x5': random.choice(['Base','Fourth', 'Falcon', 'Gaea', 'Ultimate']),
                        'x6': random.choice(['Base','Falcon', 'Blade', 'Shadow', 'Ultimate']),
                        'x8': random.choice(['Base', 'Icarus', 'Hermes', 'Ultimate', 'I+H'])}
        armor_choices['x7'] = armor_choices['x2']
        choice = armor_choices[game.lower()]
        string+=  str(choice) + " Armor Part(s) Max.\n"if type(choice) is int else str(choice)+" Armor X" +  "\n"
    if other[3].get():
        string+=  'Buster Only (X)' + "\n"if random.random() > 0.8 else 'Special Weapons Allowed (X)'+ "\n"
    if other[0].get():
        string+=  'Backtrack Allowed' + "\n"if random.random() <= 0.5 else 'No Backtracking'+ "\n"
    return string



def main(input, other):
    def randomizer(game):

        bosses = {'x1':['Flame Mammoth', 'Chill Penguin', 'Spark Mandrill',
                        'Armored Armadillo','Launch Octopus', 'Boomer Kuwanger',
                        'Sting Chameleon', 'Storm Eagle'],
                    'x2':['Wire Sponge', 'Wheel Gator', 'Bubble Crab',
                        'Flame Stag', 'Morph Moth', 'Magna Centipede',
                            'Crystal Snail', 'Overdrive Ostritch'],
                    'x3':['Blizzard Buffalo', 'Toxic Seahorse', 'Tunnel Rhino', 'Volt Catfish',
                            'Crush Crawfish', 'Neon Tiger', 'Gravity Beetle', 'Blast Hornet'],
                    'x4':['Web Spider', 'Split Mushroom', 'Cyber Peacock', 'Storm Owl',
                        'Magma Dragoon', 'Frost Walrus', 'Jet Stingray', 'Slash Beast'],
                    'x5':['Crescent Grizzly', 'Tidal Whale', 'Volt Kraken', 'Shining Firefly',
                        'Dark Necrobat', 'Spiral Pegasus', 'Burn Dinorex', 'Spiked Rosered'],
                    'x6':['Commander Yanmark', 'Shield Sheldon', 'Ground Scaravich', 'Blizzard Wolfang',
                        'Infinity Mijinion', 'Metal Shark Player', 'Blaze Heatnix', 'Rainy Turtloid'],
                    'x7':['Ride Boarski', 'Snipe Anteator', 'Vanishing Gungaroo', 'Flame Hyenard',
                        'Soldier Stonekong', 'Tornado Tonion', 'Splash Warfly', 'Wind Crowrang'],
                    'x8':['Optic Sunflower', 'Gravity Antonion', 'Dark Mantis', 'Bamboo Pandemonium',
                        'Gigabolt Man-O-War', 'Earthrock Trilobyte', 'Avalanche Yeti', 'Burn Rooster']}.get(game.lower(), None)
        if bosses:
            random.shuffle(bosses)
            string = boss_string(bosses)

            return string
        else:
            return "invalid game!"

    game = input
    #game = random.choice(["x"+str(i) for i in range(1,9)])
    if game == '':
        game = 'x'+str(random.randint(1,6))

    string = "MEGAMAN "+game.upper() + '\n'+other_restraints(game, other) + randomizer(game)

    return string




if __name__ == "__main__":
    print(main("", [str(False)]*4))
