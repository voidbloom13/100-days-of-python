import random
words = open("wordlist.txt", "r").read().split("\n")
WORD = []
DISPLAYED_WORD = []
GUESSES = set()
LIVES = 7

# KNOWN ISSUE: If an invalid guess is made (repeat guess or non-single character guess), the next valid guess will iterate through all previous invalid guesses and count them toward the GUESSES set and LIVES counter.

def draw_title():
    print('''        
 _   _                                         
| | | |                                        
| |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
|  _  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
\\_| |_/\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/                       
          ''')
    
def generate_word():
    generated_word = words[random.randint(0,len(words) - 1)]
    global WORD
    for i in generated_word:
        WORD.append(i)
    global DISPLAYED_WORD
    for i in range(0, len(WORD)):
        DISPLAYED_WORD.append("_")
        
def guess_char():
    global LIVES
    global GUESSES
    print(" ".join(DISPLAYED_WORD))
    print(f"LIVES REMAINING: {LIVES}")
    
    # Shows guesses and guess validation
    if len(GUESSES) > 0:
        print(f"Current guesses: {", ".join(GUESSES)}")
    char_guess = input("Guess a letter: ").lower()
    if len(char_guess) != 1:
        print("\n\nInvalid guess. Please limit your guess to 1 character.")
        guess_char()
    if char_guess in GUESSES:
        print(f"\n\nYou already guessed '{char_guess}'.")
        guess_char()
    GUESSES.add(char_guess)
    
    # Checks if a successful guess was made and reduces the LIVES counter by 1 if no letters were guessed correctly
    disp_word_start = DISPLAYED_WORD.copy()
    for index,char in enumerate(WORD):
        if char_guess == char:
            print(f"\n\n'{char_guess}' was in the word.")
            DISPLAYED_WORD[index] = char_guess
    if disp_word_start == DISPLAYED_WORD:
        print(f"\n\n'{char_guess}' was not in the word.")
        LIVES-=1
        
def game_over_state():
    if LIVES == 0:
        print(f"You Lose. The word was {"".join(WORD)}.")
    else:
        print(f"You Win! You guessed the word correctly: {"".join(DISPLAYED_WORD)}")

def main():
    draw_title()
    generate_word()
    while (LIVES > 0) and ("_" in DISPLAYED_WORD):
        guess_char() 
    game_over_state()

if __name__ == "__main__":
    main()