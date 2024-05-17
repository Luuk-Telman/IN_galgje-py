import time

word = ['h', 'u', 'i', 's']
whole_word = 'huis'
word_guessed = ''
guessed_letters = []
attempts = 5

print('galgje!!!!')
print('Aantal letters in woord: ' + str(len(word)))

while attempts > 0:
    guess = input('Raad een letter: ')
    guess.lower()
    
    guessed_letters.append(guess)
    
    for x in guessed_letters:
        if guess == x:
            has_letter = True
    if has_letter == False:    
        for i in word:
            if guess == i:
                print('goed')
                word_guessed += guess
                print(word_guessed)
            else:
                print('fout')
            
            
    if word_guessed == whole_word:
        print('Woord geraden!!!')
        print('Het woord was ' + whole_word)
        time.sleep(0.5)
        exit()
                