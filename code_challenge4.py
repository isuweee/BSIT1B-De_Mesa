print("Let me suggest some good sh*t manga or manhwa for you")

man = input("What do you prefer? manga or manhwa: ").lower()
genre = input("What genre do u like? (action, romance, comedy, sports, horror): ").lower()
year = input("Well what era do u prefer? (2000s or 2010s): ").lower()
duration = input("What about the duration or length of the read? (short, medium, long): ").lower()

if man == 'manga':
    if year == '2000s':
        if genre == 'action':
            if duration == 'short':
                print("I suggest reading 'Samurai Deeper Kyo' (short action-packed read)")
            elif duration == 'medium':
                print("Try reading 'Fullmetal Alchemist' (perfect balance of length and story)")
            elif duration == 'long':
                print("Check out 'Naruto' (epic action series with long development)")
        elif genre == 'romance':
            if duration == 'short':
                print("Go read 'Kimi ni Todoke' (short and sweet romance)")
            elif duration == 'medium':
                print("Try 'Nodame Cantabile' (medium-length romance with comedy elements)")
            elif duration == 'long':
                print("Go for 'Fruits Basket' (long, but heartwarming romance story)")
        elif genre == 'comedy':
            if duration == 'short':
                print("Go read 'Gintama' (short arcs but full of laughs)")
            elif duration == 'medium':
                print("Try 'Ouran High School Host Club' (medium length with comedic moments)")
            elif duration == 'long':
                print("Check out 'One Piece' (long-running, full of comedy and adventure)")
        elif genre == 'sports':
            if duration == 'short':
                print("Try reading 'Eyeshield 21' (short but exciting football action)")
            elif duration == 'medium':
                print("Go for 'Hajime no Ippo' (classic boxing manga with medium-length arcs)")
            elif duration == 'long':
                print("Check out 'Kuroko no Basket' (long basketball series with tons of matches)")
        elif genre == 'horror':
            if duration == 'short':
                print("Go read 'Gyo' by Junji Ito (short and creepy horror story)")
            elif duration == 'medium':
                print("Try 'Tokyo Ghoul' (medium-length horror with deep story themes)")
            elif duration == 'long':
                print("Go for 'Berserk' (long, dark fantasy with horror elements)")
        else:
            print("Please re-do and pick a valid genre from the available list")
    
    elif year == '2010s':
        if genre == 'action':
            if duration == 'short':
                print("I suggest reading 'One Punch Man' (short and full of action-packed moments)")
            elif duration == 'medium':
                print("Try 'Attack on Titan' (medium length with gripping action and drama)")
            elif duration == 'long':
                print("Check out 'My Hero Academia' (long-running series with a lot of action)")
        elif genre == 'romance':
            if duration == 'short':
                print("Go read 'Horimiya' (short, cute, and fast-paced romance)")
            elif duration == 'medium':
                print("Try 'Lovely★Complex' (medium-length romance with comedy)")
            elif duration == 'long':
                print("Go for 'Your Lie in April' (long, emotional romance story)")
        elif genre == 'comedy':
            if duration == 'short':
                print("Go read 'One Punch Man' (short, funny with superhero antics)")
            elif duration == 'medium':
                print("Try 'Mob Psycho 100' (medium-length comedy with heart and action)")
            elif duration == 'long':
                print("Check out 'Gintama' (long series full of comedic and emotional moments)")
        elif genre == 'sports':
            if duration == 'short':
                print("Try reading 'Haikyuu!!' (short but high-paced volleyball action)")
            elif duration == 'medium':
                print("Go for 'Kuroko no Basket' (medium-length basketball series with great dynamics)")
            elif duration == 'long':
                print("Check out 'Yuri on Ice' (longer series with beautiful skating choreography)")
        elif genre == 'horror':
            if duration == 'short':
                print("Go read 'Mieruko-chan' (short and spooky horror with humor)")
            elif duration == 'medium':
                print("Try 'The Promised Neverland' (medium-length with psychological horror elements)")
            elif duration == 'long':
                print("Go for 'Tokyo Ghoul' (long horror series with action and dark themes)")
        else:
            print("Please re-do and pick a valid genre from the available list")

elif man == 'manhwa':
    if year == '2000s':
        if genre == 'action':
            if duration == 'short':
                print("I suggest reading 'Leviathan' (short, but impactful action story)")
            elif duration == 'medium':
                print("Try 'Noblesse' (medium-length with action and fantasy elements)")
            elif duration == 'long':
                print("Check out 'The Breaker' (long and intense action story)")
        elif genre == 'romance':
            if duration == 'short':
                print("Go read 'I Don't Want This Marriage' (short and emotional romance)")
            elif duration == 'medium':
                print("Try 'Love in the Mask' (medium-length romance with drama)")
            elif duration == 'long':
                print("Go for 'Cheese in the Trap' (long romance with depth and drama)")
        elif genre == 'comedy':
            if duration == 'short':
                print("Go read 'Love Story' (short and sweet comedic manhwa)")
            elif duration == 'medium':
                print("Try 'The Gamer' (medium-length with comedic elements mixed with gaming themes)")
            elif duration == 'long':
                print("Check out 'Tower of God' (long, with tons of comedy and adventure)")
        elif genre == 'sports':
            if duration == 'short':
                print("Try reading 'Hot Blooded Woman' (short sports-related manhwa with a focus on boxing)")
            elif duration == 'medium':
                print("Go for 'All Talents Are Mine' (medium-length with sports and talent themes)")
            elif duration == 'long':
                print("Check out 'God of High School' (long-running martial arts and tournament arcs)")
        elif genre == 'horror':
            if duration == 'short':
                print("Go read 'The Boxer' (short but brutal with psychological horror elements)")
            elif duration == 'medium':
                print("Try 'The Swordsman' (medium-length with horror and action themes)")
            elif duration == 'long':
                print("Go for 'Sweet Home' (long, dark horror with survival elements)")
        else:
            print("Please re-do and pick a valid genre from the available list")
    
    elif year == '2010s':
        if genre == 'action':
            if duration == 'short':
                print("I suggest reading 'Solo Leveling' (short action-packed adventure)")
            elif duration == 'medium':
                print("Try 'The God of High School' (medium-length martial arts with action)")
            elif duration == 'long':
                print("Check out 'Omniscient Reader's Viewpoint' (long with intricate world-building)")
        elif genre == 'romance':
            if duration == 'short':
                print("Go read 'True Beauty' (short, cute romance with beauty and comedy elements)")
            elif duration == 'medium':
                print("Try 'Cheese in the Trap' (medium-length romance with complex emotions)")
            elif duration == 'long':
                print("Go for 'Love Revolution' (long series, deep romance with high school drama)")
        elif genre == 'comedy':
            if duration == 'short':
                print("Go read 'The Greatest Estate Developer' (short but full of laughs and adventure)")
            elif duration == 'medium':
                print("Try 'A Returner's Magic Should Be Special' (medium-length with humor and magic)")
            elif duration == 'long':
                print("Check out 'Lore Olympus' (long, with comedy and romance)")
        elif genre == 'sports':
            if duration == 'short':
                print("Try reading 'Ace of Diamond' (short, intense baseball action)")
            elif duration == 'medium':
                print("Go for 'All Talents Are Mine' (medium length with sports themes and talent)")
            elif duration == 'long':
                print("Check out 'Yuri on Ice' (long, beautiful sports-related series with figure skating)")
        elif genre == 'horror':
            if duration == 'short':
                print("Go read 'Shotgun Boy' (short but eerie and full of thrills)")
            elif duration == 'medium':
                print("Try 'The Horizon' (medium-length with supernatural horror elements)")
            elif duration == 'long':
                print("Go for 'Bastard' (long, dark thriller with horror and mystery)")
        else:
            print("Please re-do and pick a valid genre from the available list")

else:
    print("Please select a valid option for manga or manhwa.")
