import time

word = ['h', 'u', 'i', 's']
whole_word = 'huis'
word_guessed = ''

print('galgje!!!!')
print('Aantal letters in woord: ' + str(len(word)))

while 1+1==2:
    guess = input('Raad een letter: ')
    guess.lower()

    for i in word:
        if guess == i:
            print('goed')
            word_guessed += guess
            print(word_guessed)
    if word_guessed == whole_word:
        print('Woord geraden!!!')
        print('Het woord was ' + whole_word)
        time.sleep(0.5)
        exit()
                