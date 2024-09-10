import random

# word:list = list(open('words.txt').readlines()[random.randrange(0, len(open('words.txt').readlines()) + 1, 1)].rstrip())
# opent het woorden bestand en pakt een random regel eruit
# variable:TYPE maakt het sneller om het soort variable te definieren

file_input = open('words.txt')
content:list = file_input.readlines()
word:list = content[random.randrange(0, len(content) + 1, 1)].rstrip() # rstrip elimineert alle eventuele spaties

word_guessed:list = []
guessed_letters:list = []
guessed_letters_wrong:list = []

visual:list = []
attempts:int = len(word) * 2
numbers:list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
guess = ''
guessed:bool = False

# laad all dingen aan begin en zet alles klaar om te gebruiken
def init(): 
    global visual
    
    print('Galgje!!!!')
    print('Je kunt 1 letter per keer raden!')
    print('Aantal letters in woord: ' + str(len(word)))

    for _ in word: # maakt het aantal puntjes aan dat nodig is in het woord
        visual.append('.')

# vraagt de gebruiker voor input
def askForInput():
    global guess # input vragen
    
    print(''.join(visual)) # Print de visuals voor feedback
    print('')
    
    guess = input('Raad een letter: ')
    guess.lower() # verander naar lowercase

# checkt of de input in het woord zit 
def checkIfInputIsInWord():
    global attempts
    
    str(guess) # convert guess naar naar string
    if guess in word and guess not in guessed_letters: # als de gok in de word list zit en je het niet eerder hebt gegokt doe dit
        
        letter_count = word.count(guess)

        for i in range(letter_count):
            word_guessed.append(guess) #voegt het woord toe aan het tot nu toe gegokte woord
            
        for i in range(len(word)): #veranderd de visuals
            if word[i] == guess:
                visual[i] = guess
            
        guessed_letters.append(guess) # voegt de letter toe aan de gegokte letters
        print('Pogingen over: ' + str(attempts)) # geeft feedback voor het aantal pogingen over

    else: # als de gok niet in het woord zit
        
        guessed_letters.append(guess) # voegt de letter toe aan de verkeerd geraden letters
        attempts -= 1 # verwijderd 1 poging
        
        print('Gegokte letters: ' + ', '.join(guessed_letters)) # laat de al gegokte foute letters zien
        print('Pogingen over: ' + str(attempts)) # geeft feedback voor het aantal pogingen over

# checkt of de gegeven input valide is 
def checkIfInputIsValid():
    if guess == '' or len(guess) > 1 or guess in numbers or guess in guessed_letters_wrong:
        print('Type een letter!')

    else: # als die niet leeg is doe dit
        checkIfInputIsInWord()

# checkt of het spel is afgelopen
def checkIfGameEnded():
    global word_guessed
    global word
    global guessed
    
    if attempts == 0:
        print('Je hebt fout gegokt!')
        print('Het woord was: ' + ''.join(word))

    # als het complete woord geraden is
    if sorted(word_guessed) == sorted(word): # wordt gesorteerd zodat het altijd de zelfde volgorde is als we het checken
        
        print('Woord geraden!!!') 
        print('Het woord was ' + ''.join(word))
        
        guessed = True

init()

while attempts > 0 and not guessed:
    askForInput()
    checkIfInputIsValid()
    checkIfGameEnded()