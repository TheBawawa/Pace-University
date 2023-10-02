# Problem 02

print("Welcome to the Pokemon card price calculator! Please answer these questions:")
price = 5

# Ask for rarity
rarity = input("Is the card of a special rarity? (Y/N) ")

if rarity == "Y":
    uncommon = input("Is the card uncommon? (Y/N) ")
    if uncommon == "Y":
        price += 5
    elif uncommon == "N":
        rare = input("Is the card rare ? (Y/N) ")
        if rare == "Y":
            price += 15
        else:
        	print("The card has common rarity")


# Ask for holo
holographic = input("Is the card holographic? (Y/N) ")

if holographic == "Y":
    reverse_holo = input("Is the card a reverse holo? (Y/N) ")
    if reverse_holo == "Y":
        price += 10
    elif reverse_holo == "N":
        holo = input("Is the card a holo? (Y/N) ")
        if holo == "Y":
            price += 15
        elif holo == "N":
            full_holo = input("Is the card a full holo? (Y/N) ")
            if full_holo == "Y":
                price += 20
            else:
                print("The card is not holographic")

# Ask for special pokemon
special_pokemon = input("Is the card of a special Pokemon? (Y/N) ")

if special_pokemon == "Y":
    starter = input("Is the card a starter pokemon? (Y/N) ")
    if starter == "Y":
        price += 5
    elif starter == "N":
        legendary = input("Is the card a legendary pokemon? (Y/N) ")
        if legendary == "Y":
            price += 30
        else:
            print("The card is not a special pokemon")

print(f"The finale resale of this card is: {price}")
