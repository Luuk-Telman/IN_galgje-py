import time
#word = list(open('words.txt').readlines()[random.randrange(0, len(open('words.txt').readlines()) + 1, 1)].rstrip())
# variable:TYPE maakt het sneller om het soort variable te definieren
word:list = ['b', 'o', 'o', 'm']
word_guessed:list = []
guessed_letters:list = []
guessed_letters_wrong:list = []
visual:list = []
attempts:int = 5

print('Galgje!!!!')
print('Je kunt 1 letter per keer raden!')
print('Aantal letters in woord: ' + str(len(word)))


# maakt het aantal puntjes aan dat nodig is in het woord
for i in word:
    visual.append('.')

# Mainloop
while attempts > 0:
    # Print de visuals voor feedback
    print(''.join(visual))
    print('')
    
    # input vragen
    guess:str = str(input('Raad een letter: '))
    guess.lower() # convert naar lowercase
    
    # checkt of de gok leeg is
    if guess == '':
        print('Type een letter!')
        continue
    
    #als die niet leeg is doe dit
    else:
        if guess in word and guess not in guessed_letters: #als de gok in de word list zit en je het niet eerder hebt gegokt doe dit
            
            letter_count = word.count(guess)
            for i in range(letter_count):
                word_guessed.append(guess) #voegt het woord toe aan het tot nu toe gegokte woord
                
                pos:int = word.index(guess) # vind de positie van de gok in het woord
                visual[pos] = guess # veranderd de visual op de goede positie in het woord naar de gok
                
            guessed_letters.append(guess) # voegt de letter toe aan de gegokte letters
            
        else: # als de gok niet in het woord zit
            guessed_letters.append(guess) # voegt de letter toe aan de verkeerd geraden letters
            attempts -= 1 # verwijderd 1 poging
            
            print('Gegokte letters: ' + ', '.join(guessed_letters)) # laat de al gegokte foute letters zien
            print('Pogingen over: ' + str(attempts)) # geeft feedback voor het aantal pogingen over

    # als het complete woord geraden is
    if sorted(word_guessed) == sorted(word): # wordt gesorteerd zodat het altijd de zelfde volgorde is als we het checken
        
        print('Woord geraden!!!') 
        print('Het woord was ' + ''.join(word))
        
        time.sleep(0.5) # wacht 1/2 seconde met het programma
        exit() # verlaat het programma