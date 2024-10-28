import random

## variable:TYPE maakt het sneller om het soort variable te definieren ##
# script voor het woord kiezen uit de woordenlijst #
file_input = open('words.txt') # opent het woordenlijst bestand
content:list = file_input.readlines() # leest alle regels van het text document en stopts ze in een lijst
word:list = content[random.randrange(0, len(content) + 1, 1)].rstrip() # kiest een willekeurige index van de woordenlijst lijst, rstrip elimineert alle eventuele spaties

word_guessed:list = [] # lijst waar alle goed geraden letters worden opgeslagen
guessed_letters:list = [] # lijst waar alle letters worden opgeslagen
guessed_letters_wrong:list = [] # lijst waar alle fout geraden letters worden opgeslagen

visual:list = [] # een lijst waar alle visuele puntjes worden ogeslagen
attempts:int = len(word) * 2 # het aantal pogingen die de speler krijgt
numbers:list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] # een lijst met alle nummers erin
guess:str = '' # globale variable voor de speler input
guessed:bool = False # of de speler het woord heeft geraden

# de functie waar alle dingen in staan om het spel klaar te zetten
def init(): 
    global visual # pakt de globale variable visual zodat het niet alleen lokaaal word aan gepast
    
    print('Galgje!!!!')
    print('Je kunt 1 letter per keer raden!')
    print('Aantal letters in woord: ' + str(len(word)))

    for _ in word: # maakt het aantal puntjes aan dat nodig is in het woord
        visual.append('.') # voegt het aantal puntjes toe aan de visual lijst

# vraagt de gebruiker voor input
def askForInput():
    global guess # pakt de globale variable guess zodat die niet lokaal wordt aan gepast
    
    print(''.join(visual)) # Print de visuals voor feedback, join voegt het toe aan het einde van de string
    print('')
    
    guess = input('Raad een letter: ') # vraagt de speler voor een input
    guess = guess.lower() # verander naar lowercase

# checkt of de input in het woord zit 
def checkIfInputIsInWord():
    global attempts # pakt de globale variable attempts zodat die niet lokaal wordt aan gepast
    
    str(guess) # convert guess naar naar string
    if guess in word and guess not in guessed_letters: # als de gok in de word list zit en je het niet eerder hebt gegokt doe dit
        
        letter_count = word.count(guess) # zet het aantal letters gelijk het aantal letters in het woord

        for i in range(letter_count): # gaat alle letters van het woord langs
            word_guessed.append(guess) # voegt het woord toe aan het tot nu toe gegokte woord
            
        for i in range(len(word)): # veranderd de visuals
            if word[i] == guess: # als de locatie van de gegokte letter is gevonden
                visual[i] = guess # veranderd de visual op de goed locatie
            
        guessed_letters.append(guess) # voegt de letter toe aan de gegokte letters
        
        print('Je gok was goed!')
        print('Pogingen over: ' + str(attempts)) # geeft feedback voor het aantal pogingen over

    else: # als de gok niet in het woord zit
        
        guessed_letters.append(guess) # voegt de letter toe aan de verkeerd geraden letters
        attempts -= 1 # verwijderd 1 poging
        
        print('Je gok was fout!')
        print('Gegokte letters: ' + ', '.join(guessed_letters)) # laat de al gegokte foute letters zien
        print('Pogingen over: ' + str(attempts)) # geeft feedback voor het aantal pogingen over

# checkt of de gegeven input valide is 
def checkIfInputIsValid():
    if guess == '' or len(guess) > 1 or guess in numbers or guess in guessed_letters_wrong: # alle opties wanneer het NIET valide is 
        print('Type een letter!')

    else: # als de input wel valide is doe dit
        checkIfInputIsInWord()

# checkt of het spel is afgelopen
def checkIfGameEnded():
    global word_guessed # pakt de globale variable word_guessed zodat die niet lokaal wordt aan gepast
    global word # pakt de globale variable word zodat die niet lokaal wordt aan gepast
    global guessed # pakt de globale variable guessed zodat die niet lokaal wordt aan gepast
    
    if attempts == 0: # wanneer de pogingen op zijn
        print('Je hebt fout gegokt!')
        print('Het woord was: ' + ''.join(word))

    if sorted(word_guessed) == sorted(word): # als het complete woord geraden is, sort zorgt er voor dat het gesorteerd is zodat het altijd de zelfde volgorde is als we het checken
        
        print('Woord geraden!!!') 
        print('Het woord was: ' + ''.join(word))
        
        guessed = True # zorgt er voor dat het spel geraden is


init() # voert de inatilizeer functie uit

# de main loop van het spel
while attempts > 0 and not guessed:
    askForInput() # vraagt de speler voor input via de functie
    checkIfInputIsValid() # checkt of de input die de speler heeft gegeven kan
    checkIfGameEnded() # checkt of de speler het woord heeft geraden of geen pogingen meer over heeft
