"""System module."""
import sys
import random
import re

def main():
    """Generate random names."""
    print("Welcome to the Psych 'Sidekick Name Picker.'\n")
    print("A name just like Sean would pick for Gus:\n")

    first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'Beenie-Weenie'",
            "Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite'",
            'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
            'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat',
            'Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
            'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry',
            'Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
            'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"', 'Mergatroid',
            '"Mr Peabody"', 'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine',
            'Pennywhistle', 'Pitchfork Ben', 'Potato Bug', 'Pushmeet',
            'Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',
            "Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
            'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky',
            'Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',
            "Winston 'Jazz Hands'", 'Worms')

    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
            'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
            'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
            'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
            'Hootkins', 'Jefferson', 'Jenkins', 'Jingley-Schmidt', 'Johnson',
            'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
            'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
            'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
            'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
            'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
            'Stevens', 'Stroganoff', 'Sugar-Gold', 'Swackhamer', 'Tippins',
            'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
            'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
            'Woolysocks')
    middle = ()
    new_first = ()
    
    for name in first:
        if "'" in name:
            parts = name.split("'")
            new_first += (parts[0],)
            middle += (parts[1],)
        elif '"' in name:
            new_first += (name.replace('"', ''),)
        elif name.endswith(('Oil-Can', 'Ovaltine', 'Crab Meat')):
            middle += (name,)
        else:
             new_first += (name,)

    while True:
        first_name = random.choice(new_first)
        last_name = random.choice(last)
        middle_name = ""
        use_middle_name = random.choice([True, False])
        print(first_name)
        if use_middle_name:
            if random.random() < 0.5 or random.random() < 1/3:
                middle_name = random.choice(middle)

        print(first_name, middle_name, last_name, file = sys.stderr)
        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()
