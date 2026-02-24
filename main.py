import random

hangman = R'''                                             
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
'''
stages = [R'''
   +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', R'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', R'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
+---+
  |   |
      |
      |
      |
      |
=========''']
lives = 6
word_list = ['bear','camel','aardvark','goat','horse','crocodile','lion','tiger','cow','wolf','fox']
chosen_word = random.choice(word_list)
print(hangman)
print('Category is:  Animals')
placeholder = ""
length = len(chosen_word)
print(f'Hint: {length} letters.')
for j in range(0,length):
    placeholder += '-'
print(placeholder)
game_over = False
correct_list = []
while not game_over:
    guess = input("choose a letter: ").lower()
    display = ''
    for i in chosen_word:
        if i == guess:
            #print('---IF LOOP---')
            #print(f"printing value of i {i}")
            display += guess 
            correct_list.append(guess)
            #print(f"IF loop display value {display}")
        elif i in correct_list:
            #print('---ELIF LOOP---')
            #print(f"printing value of i {i}")
            display += i
            #print(f"ELIF loop display value {display}")
        else:
            #print('---ELSE---')
            #print(f"printing value of i {i}")
            display += '-'
            #print(f"ELSE loop display value {display}")
    print(display) 
    #print(f"WHILE loop {display}")
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("you loose.")
            print(f'Animal was {chosen_word}')
    
    if '-' not in display:
            game_over = True
            print('You win') 
    print(stages[lives])
