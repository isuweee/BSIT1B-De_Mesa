print("Let me suggest some good stuff manga or manhwa for you")

man = input("What do you prefer? manga or manhwa: ").lower().strip()
genre = input("What genre do u like? (action, romance, comedy, sports, horror): ").lower().strip()
year = input("Well what era do u prefer? (2000s or 2010s): ").lower().strip()
duration = input("What about the duration or length of the read? (short, medium, long): ").lower().strip()

if man == 'manga':
    if year == '2000s':
        if genre == 'action':
            if duration == 'short':
                print("I suggest reading 'Fullmetal Alchemist' (108 chapters)")
            elif duration == 'medium':
                print("Try reading 'Samurai Deeper Kyo' (308 chapters)")
            elif duration == 'long':
                print("Check out 'Naruto' (700 chapters)")
        elif genre == 'romance':
            if duration == 'short':
                print("Go read 'Kimi ni Todoke' (123 chapters)")
            elif duration == 'medium':
                print("Try 'Fruits Basket' (136 chapters)")
            elif duration == 'long':
                print("Go for 'Boys Be...' (200+ chapters)")
        elif genre == 'comedy':
            if duration == 'short':
                print("Go read 'Ouran High School Host Club' (83 chapters)")
            elif duration == 'medium':
                print("Try 'Gintama' (200+ chapters early arcs)")
            elif duration == 'long':
                print("Check out 'One Piece' (1000+ chapters)")
        elif genre == 'sports':
            if duration == 'short':
                print("Try reading 'Kuroko no Basket' (275 chapters)")
            elif duration == 'medium':
                print("Go for 'Eyeshield 21' (333 chapters)")
            elif duration == 'long':
                print("Check out 'Hajime no Ippo' (1400+ chapters)")
        elif genre == 'horror':
            if duration == 'short':
                print("Go read 'Gyo' (20 chapters)")
            elif duration == 'medium':
                print("Try 'Tokyo Ghoul' (143 chapters)")
            elif duration == 'long':
                print("Go for 'Berserk' (380+ chapters)")
        else:
            print("Please re-do and pick a valid genre from the available list")
    
    elif year == '2010s':
        if genre == 'action':
            if duration == 'short':
                print("I suggest reading 'Attack on Titan' (139 chapters)")
            elif duration == 'medium':
                print("Try 'One Punch Man' (218+ chapters)")
            elif duration == 'long':
                print("Check out 'My Hero Academia' (400+ chapters, ongoing)")
        elif genre == 'romance':
            if duration == 'short':
                print("Go for 'Your Lie in April' (44 chapters)")
            elif duration == 'medium':
                print("Try 'Ao Haru Ride' (49 chapters)")
            elif duration == 'long':
                print("Go read 'Horimiya' (122 chapters)")
        elif genre == 'comedy':
            if duration == 'short':
                print("Go read 'Mob Psycho 100' (101 chapters)")
            elif duration == 'medium':
                print("Try 'Assassination Classroom' (180 chapters)")
            elif duration == 'long':
                print("Check out 'Gintama' (704 chapters)")
        elif genre == 'sports':
            if duration == 'short':
                print("Try reading 'Kuroko no Basket' (275 chapters)")
            elif duration == 'medium':
                print("Go for 'Haikyuu!!' (402 chapters)")
            elif duration == 'long':
                print("Check out 'Diamond no Ace' (400+ chapters)")
        elif genre == 'horror':
            if duration == 'short':
                print("Go read 'Mieruko-chan' (50+ chapters)")
            elif duration == 'medium':
                print("Go for 'Tokyo Ghoul:re' (179 chapters)")
            elif duration == 'long':
                print("Try 'The Promised Neverland' (181 chapters)")
        else:
            print("Please re-do and pick a valid genre from the available list")

elif man == 'manhwa':
    if year == '2000s':
        if genre == 'action':
            if duration == 'short':
                print("Try 'The Breaker' (72 chapters)")
            elif duration == 'medium':
                print("I suggest reading 'Leviathan' (214 chapters)")
            elif duration == 'long':
                print("Check out 'Noblesse' (544 chapters)")
        elif genre == 'romance':
            if duration == 'short':
                print("Go read 'I Don't Want This Marriage' (80 chapters)")
            elif duration == 'medium':
                print("Try 'Love in the Mask' (82 chapters)")
            elif duration == 'long':
                print("Go for 'Cheese in the Trap' (301 chapters)")
        elif genre == 'comedy':
            if duration == 'short':
                print("Go read 'Love Story' (20+ chapters)")
            elif duration == 'medium':
                print("Try 'The Gamer' (430+ chapters)")
            elif duration == 'long':
                print("Check out 'Tower of God' (500+ chapters)")
        elif genre == 'sports':
            if duration == 'short':
                print("Try reading 'Hot Blooded Woman' (65 chapters)")
            elif duration == 'medium':
                print("Go for 'Girls of the Wild's' (260 chapters)")
            elif duration == 'long':
                print("Check out 'The God of High School' (500+ chapters)")
        elif genre == 'horror':
            if duration == 'short':
                print("Go read 'Melvina's Therapy' (50 chapters)")
            elif duration == 'medium':
                print("Try 'Distant Sky' (100+ chapters)")
            elif duration == 'long':
                print("Go for 'Sweet Home' (141 chapters)")
        else:
            print("Please re-do and pick a valid genre from the available list")
    
    elif year == '2010s':
        if genre == 'action':
            if duration == 'short':
                print("I suggest reading 'Solo Leveling' (179 chapters)")
            elif duration == 'medium':
                print("Try 'The God of High School' (500+ chapters)")
            elif duration == 'long':
                print("Check out 'Omniscient Reader's Viewpoint' (550+ chapters)")
        elif genre == 'romance':
            if duration == 'short':
                print("Go read 'True Beauty' (250+ chapters)")
            elif duration == 'medium':
                print("Try 'Cheese in the Trap' (301 chapters)")
            elif duration == 'long':
                print("Go for 'Love Revolution' (500+ chapters)")
        elif genre == 'comedy':
            if duration == 'short':
                print("Go read 'The Greatest Estate Developer' (130+ chapters)")
            elif duration == 'medium':
                print("Try 'A Returner's Magic Should Be Special' (250+ chapters)")
            elif duration == 'long':
                print("Check out Yumi’s Cells (512 chapters)")
        elif genre == 'sports':
            if duration == 'short':
                print("Try reading 'The Boxer' (133 chapters)")
            elif duration == 'medium':
                print("Check out 'Girls of the Wild's' (260 chapters)")
            elif duration == 'long':
                print("Go for 'Wind Breaker' (400+ chapters)")
        elif genre == 'horror':
            if duration == 'short':
                print("Go read 'Shotgun Boy' (55 chapters)")
            elif duration == 'medium':
                print("Try 'Bastard' (93 chapters)")
            elif duration == 'long':
                print("Go for 'Sweet Home' (141 chapters)")
        else:
            print("Please re-do and pick a valid genre from the available list")
else:
    print("Please select a valid option for manga or manhwa.")
