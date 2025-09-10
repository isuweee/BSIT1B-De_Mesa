print("Let me suggest some good sh*t manga or manhwa for you")

man = input("What do you prefer? manga or manhwa: ").lower()
genre = input("What genre do u like? (action, romance, comedy, sports, horror): ").lower()
year = input("Well what era do u prefer? (2000s or 2010s): ").lower()

if man == 'manga':
    if year == '2000s':
        if genre == 'action':
            print("I suggest reading 'The King's Avatar'")
        elif genre == 'romance':
            print("Go read 'Citrus'")
        elif genre == 'comedy':
            print("Go read 'Gintama'")
        elif genre == 'sports':
            print("Try reading 'Hajime no Ippo'")
        elif genre == 'horror':
            print("Go read 'Gyo' by Junji Ito")
        else:
            print("Please re-do and pick on the available genre list")
    elif year == '2010s':
        if genre == 'action':
            print("I suggest reading 'Boruto'")
        elif genre == 'romance':
            print("Go read 'Horimiya'")
        elif genre == 'comedy':
            print("Go read 'Aosabi Aosabe'")
        elif genre == 'sports':
            print("Try reading 'Haikyuu'")
        elif genre == 'horror':
            print("Go read 'Mieruko-Chan'")
        else:
            print("Please re-do and pick on the available genre list")

if man == 'manhwa':
    if year == '2000s':
        if genre == 'action':
            print("I suggest reading 'Leviathan'")
        elif genre == 'romance':
            print("Go read 'I don't want this marriage'")
        elif genre == 'comedy':
            print("Go read 'Love Story'")
        elif genre == 'sports':
            print("Try reading 'Hajime no Ippo'")
        elif genre == 'horror':
            print("Go read 'The Boxer'")
        else:
            print("Please re-do and pick on the available genre list")
    elif year == '2010s':
        if genre == 'action':
            print("I suggest reading 'Solo Leveling'")
        elif genre == 'romance':
            print("Go read 'True Beauty'")
        elif genre == 'comedy':
            print("Go read 'The Greatest Estate Developer'")
        elif genre == 'sports':
            print("Try reading 'All Talents Are Mine'")
        elif genre == 'horror':
            print("Go read 'Shotgun Boy'")
        else:
            print("Please re-do and pick on the available genre list")
