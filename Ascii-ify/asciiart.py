
user_word = input("Enter a word to be ascii-ifed ")

ascii0= r' _______  ______   _______  ______   _______  _______  _______          __________________ _        _        _______  _        _______  _______  _______  _______  _______ _________                                              _______ '
ascii1 = r'(  ___  )(  ___ \ (  ____ \(  __  \ (  ____ \(  ____ \(  ____ \|\     /|\__   __/\__    _/| \    /\( \      (       )( (    /|(  ___  )(  ____ )(  ___  )(  ____ )(  ____ \\__   __/|\     /||\     /||\     /||\     /||\     /|/ ___   )'
ascii2 = r'| (   ) || (   ) )| (    \/| (  \  )| (    \/| (    \/| (    \/| )   ( |   ) (      )  (  |  \  / /| (      | () () ||  \  ( || (   ) || (    )|| (   ) || (    )|| (    \/   ) (   | )   ( || )   ( || )   ( |( \   / )( \   / )\/   )  |'
ascii3 = r'| (___) || (__/ / | |      | |   ) || (__    | (__    | |      | (___) |   | |      |  |  |  (_/ / | |      | || || ||   \ | || |   | || (____)|| |   | || (____)|| (_____    | |   | |   | || |   | || | _ | | \ (_) /  \ (_) /     /   )'
ascii4 = r'|  ___  ||  __ (  | |      | |   | ||  __)   |  __)   | | ____ |  ___  |   | |      |  |  |   _ (  | |      | |(_)| || (\ \) || |   | ||  _____)| |   | ||     __)(_____  )   | |   | |   | |( (   ) )| |( )| |  ) _ (    \   /     /   / '
ascii5 = r'| (   ) || (  \ \ | |      | |   ) || (      | (      | | \_  )| (   ) |   | |      |  |  |  ( \ \ | |      | |   | || | \   || |   | || (      | | /\| || (\ (         ) |   | |   | |   | | \ \_/ / | || || | / ( ) \    ) (     /   /  '
ascii6 = r'| )   ( || )___) )| (____/\| (__/  )| (____/\| )      | (___) || )   ( |___) (___|\_)  )  |  /  \ \| (____/\| )   ( || )  \  || (___) || )      | (_\ \ || ) \ \__/\____) |   | |   | (___) |  \   /  | () () |( /   \ )   | |    /   (_/\ '
ascii7 = r'|/     \||/ \___/ (_______/(______/ (_______/|/       (_______)|/     \|\_______/(____/   |_/    \/(_______/|/     \||/    )_)(_______)|/       (____\/_)|/   \__/\_______)   )_(   (_______)   \_/   (_______)|/     \|   \_/   (_______/'
# Each letter has width 9 and height of 8, put ascii in quotes
# Get location of each letter then add 9 to see next letter location

# Most of times, you need to do each line 8 times for it to get each letter

lis = [ascii0, ascii1, ascii2, ascii3, ascii4, ascii5, ascii6, ascii7]


#Get lines of each ascii

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

w = 9 

for a_line in lis:
    horizontal = ''  
    for chars in user_word: #Loop over letters in input
        ind = alphabet.index(chars.upper()) # Get all uppercase
        position = ind * w #Keep track of current position as its in the formula(current : current+9)
        charLine = a_line[position : position + w] #Get line of uppercase chars to convert
        horizontal += charLine #Get total horizontal word
    print(horizontal)
    
    
    
