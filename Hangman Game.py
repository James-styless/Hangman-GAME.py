import random
words = ["Wilt Chamberlain", "Paul George","Zimmerman", "Kwantlen", "Rai", "Chris Paul", "James Harden", "Steve Kerr", "Lebron James", "Michael Jordan", "Kevin Durant", "Russell Westbook","Dennis Rodman", "Surrey", "Scott Skiles", "Stephen Curry", "Jaren Jackson", "Ja Morant", "Mike Dunleavy", "Shawn Bradley", "Shaquille O'Neal"]
import string
lives_visual_dict = {
        0: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / \\
               |
           """,
        1: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
            """,
        2: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """,
        3: """
                ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
            """,
        4: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,
        5: """
                ___________
               | /        
               |/        
               |          
               |          
               |
            """,
        6: """
               |
               |
               |
               |
               |
            """,
        7: "",
    }
def get_words(words):
    hangmanwords = random.choice(words)
    while '-' in hangmanwords or ' ' in hangmanwords:
        hangmanwords  = random.choice(words)
    
    return hangmanwords
def cliffhanger():
    hangmanwords = get_words(words)
    word_letters = set(hangmanwords)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7
        
    while len(letter) > 0 and lives > 0:
        print('You have', lives, 'lives left  and you have used these letters: ', ' ').join(used_letters)
        
        word_list = [letter if letter in used_letters else '-' for letter in words]
        print('Current Word: ', ' '.join(word_list))
        
        letter = input("Guess a letter:").upper()
    if letter in alphabet - used_letters:
        used_letters.add(letter)
        if letter in word_letters:
            word_letters.remove(letter)
            print('')

        else :
            lives = lives - 1 
            print('Letter is not in word.')

    elif letter in used_letters:
        print('You have already used that letter. Please try again.')
        
    else:
        print("Invalid Character. Please try again.")
    if lives == 0:
        print('You died,sorry. The word was', hangmanwords)
    else:      
        print('You have guessed the word! Congratulations')
        
if __name__ == '__main__':
    cliffhanger()