import random
wrong = 0 
def check (wrong):
    if wrong ==3:
        fail = True
    else:
        fail = False 
    print ("you have", 3-wrong, "attempts left before getting locked out of the system")
    return fail
        
#CARDS--------------------------------------------------------------------------------------------------------------------------------
def cards(wrong):
    print ("---------------------------------------------------------------------------------------------------------------------------------------")
    print ("Code: 1375")
    print ("Before you is a box you need to open. Find the correct password to get the box to unlock.")
    print (" ")
    combinations = [["♠♦♣♣", 1], ["♠♦♣♦", 5], ["♥♦♥♦", 7], ["♥♦♣♦", 3]]
    choice = random.choice(combinations)
    answer = choice[1]
    
    print(f"Combination: {choice[0]}")
    
    # --- Dummy Proof Input Logic ---
    while True:
        try:
            guess = int(input("Enter the combinations value: "))
            break
        except ValueError:
    
            print("Invalid entry! Please enter a whole number (e.g., 5).")
    
    if guess == answer:
        print("Correct!")
    else:
        print(f"Incorrect. The answer was {answer}.")
        wrong = wrong +1
    print (" ")
    print (" ")
    return wrong 


#BLOCKS------------------------------------------------------------------------------------------------------------------------------
def blocks(wrong):
    print ("---------------------------------------------------------------------------------------------------------------------------------------")
    
    print ("Code: 1029")
    print ("Quick! You need to disable the cameras so that the execs can't catch you in the act.")
    print (" ")
    given = [56124, 73293, 75414, 40275, 13874, 36298, 20187, 34425, 12126]
    box = ["    🟥🟥 \n  🟥🟥🟥🟥 \n🟥🟥 \n  🟥🟥🟥", 
           "  🟥 \n🟥🟥🟥  🟥🟥 \n  🟥🟥🟥🟥 \n🟥🟥🟥 \n    🟥🟥",
           "🟥🟥  🟥🟥🟥 \n🟥🟥🟥🟥🟥 \n  🟥🟥🟥🟥 \n  🟥🟥  🟥"]
    answer = [[11, 5, 2, 3, 2, 1, 1, 1, 2],
              [15, 6, 3, 5, 2, 2, 1, 2, 2],
              [17, 7, 4, 5, 2, 2, 3, 2, 2]]
    givenN = random.randrange(0, 9)
    boxN = random.randrange(0, 3)
    dummy = True
    
    print("The given number is", given[givenN])
    print()
    print("Box:")
    print(box[boxN])
    
    while dummy: 
        print()
        try: 
            response = int(input("Answer: "))
        except ValueError: 
            print("The answer must be an integer")
            continue
               
        if response == answer[boxN][givenN]:
            dummy = False
        else:
            wrong += 1
            print("Incorrect!")
            
    return wrong 

#MESS------------------------------------------------------------------------------------------------------------------------------


def dummyProof (answer, wrong):
    dummy = True
    while dummy == True:
        inputed = input("Answer: ")
        if len(inputed) != 2:
            print("Error, the answer must be two digits")
            continue
        try:
            temp = int(inputed[0])
        except ValueError:
            print("Error, the first character must be an integer")
            continue
        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n"]
        if inputed[1] not in letters:
            print("Error, the second character must be an a letter a through n")
            continue

        if inputed == answer:
            dummy = False
        else:
            wrong = wrong + 1
            print("Incorect answer! Try again")
            print ("u stupid:", wrong)
    return wrong



def bMess1 (wrong):
    print ("⥳, ↔, †, ✫")
    wrong = dummyProof("4k", wrong)
    return wrong

def bMess2 (wrong):
    print ("⦅, ⥕, ✗, ⦡")
    wrong = dummyProof("9f", wrong)
    return wrong
    print ("")

def bMess3 (wrong):
    print ("⥭, ⥎, ⦓, ⇋")
    wrong = dummyProof("6c", wrong)
    return wrong
    print ("")

def bMess4 (wrong):
    print ("⚜, ✫, ⦓, ⦞")
    wrong = dummyProof("8d", wrong)
    return wrong
    print ("")

def bMess5 (wrong):
    print ("₿, ⥊, ⥞ , ↔")
    wrong = dummyProof("4i", wrong)
    return wrong
    print ("")

def bMess6 (wrong):
    print ("♠, ≡, ⦉ , ⥘")
    wrong = dummyProof("9k", wrong)
    return wrong
    print ("")

def bMess7 (wrong):
    print ("₤, ₩, ⥳ , ⦸")
    wrong = dummyProof("4m", wrong)
    return wrong
    print ("")

def bMess8 (wrong):
    print ("✘, ≠, ⦓ , ⥎")
    wrong = dummyProof("7b", wrong)
    return wrong
    print ("")

def bMess9 (wrong):
    print ("‡, ⦴, ♢ , †")
    wrong = dummyProof("4e", wrong)
    return wrong
    print ("")

def bMess10 (wrong):
    print ("⚛, ₕ, ₓ , ⥭")
    wrong = dummyProof("9j", wrong)
    return wrong
    print ("")
    
def bigMess(wrong):
    print ("---------------------------------------------------------------------------------------------------------------------------------------")
    print ("Code: 3186")
    print ("In front of you is a door. You need to unlock it fast.")
    print (" ")
    num =random.randint(1, 10)
    if num == 1:
        wrong = bMess1 (wrong)
    elif num == 2:
        wrong = bMess2 (wrong)
    elif num == 3:
        wrong = bMess3 (wrong)
    elif num == 4:
        wrong = bMess4 (wrong)
    elif num == 5:
        wrong = bMess5 (wrong)
    elif num == 6:
        wrong = bMess6 (wrong)
    elif num == 7:
        wrong = bMess7 (wrong)
    elif num == 8:
        wrong = bMess8 (wrong)
    elif num == 9:
        wrong = bMess9 (wrong)
    elif num == 10:
        wrong = bMess10 (wrong)
    return wrong
        
        

 #SPECAIL SYMBOLS------------------------------------------------------------------------------------------------------------------------------   
def specialSymbol(wrong):
    print ("---------------------------------------------------------------------------------------------------------------------------------------")
    
    print ("Code: 7250")
    print ("You discover a secret door. In order to get through to the other side you have to crack code.")
    print (" ")
    lists = [["₯","₰","≭","∲","⭄","⥘","⥢"], ["₯","დ","ও","유","ˠ","ˁ","≴"],
        ["₯","≎","∰","⊚","⟡","◇","⧖"], ["₰","დ","≎","ˠ","⊚","✦","✧"],
        ["₰","ও","∰","ˁ","⟡","✦","✩"], ["≭","დ","∰","ˁ","◇","✧","✩"],
        ["∲","ও","≎","ˠ","◇","✦","✩"], ["⭄","⥘","⥢","≴","⊚","⟡","✧"]]
    
    list = []
    listy = []
    index = random.randint(0,7)
    for i in range(4):
        index2 = random.randint(0,6)
        symbol = lists[index][index2]
        while symbol in list:
            index2 = random.randint(0,6)
            symbol = lists[index][index2]
        list.append(symbol)
        listy.append(index2)
        
    listy.sort()
    listy[0], listy[1], listy[2], listy[3] = lists[index][listy[0]], lists[index][listy[1]], lists[index][listy[2]], lists[index][listy[3]]
        
    print("     ")
    print("     ", list[0], list[1])
    print("     ",list[2], list[3])
    print("     ")
        
    answer = []
    for i in range(4):
        guess = input(f"Symbol #{i+1}: ")
        while guess not in list:
            print("Enter one of the four symbols")
            guess = input(f"Symbol #{i+1}: ")
        answer.append(guess)
    return listy, answer
    
    listy,answer = specialSymbol()
    if answer == listy:
        print("You Win")
    else: 
        wrong += 1
        print("Try Again")
    return wrong
#MATH------------------------------------------------------------------------------------------------------------------------------
def math(wrong):
    print ("---------------------------------------------------------------------------------------------------------------------------------------")
    print ("Code: 8439")
    print ("In order to get past the next obstacle you need to discover the truth behind this mystery calculator. ")
    print (" ")
    numbers = [random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9)]
    symbolsList = ["⚛", "✧", "✭", "⟁", "✦", "⊗", "✫", "§", "₾"]
    symbols = [symbolsList[random.randint(0,8)], symbolsList[random.randint(0, 8)], symbolsList[random.randint(0, 8)], symbolsList[random.randint(0, 8)]]
    
    even_count = sum(n % 2 == 0 for n in numbers)
    odd_count = 5 - even_count
    has_duplicate = len(set(numbers)) < 5
    sum_all = sum(numbers)
    two_under_5 = sum(n < 5 for n in numbers) == 2
    first = numbers[0]
    last = numbers[-1]
        
    resolved = []
    has_star = "✭" in symbols
    has_diamond = "✧" in symbols
    
    dummy = True 
    
    for s in symbols:
        if s == "⚛":
            if (first % 2) == (last % 2):
                resolved.append("-")
            else:
                resolved.append("+")
        
        elif s == "✧":
            if has_star:
                # rule 2 disregarded → treat later
                resolved.append(None)
            else:
                if first % 2 == 1:
                    resolved.append("-")
                else:
                    resolved.append(None)
        
        elif s == "⟁":
            if has_duplicate:
                resolved.append("+")
            else:
                resolved.append(None)
        
        elif s == "⊗":
            if even_count > odd_count:
                resolved.append("*")
            else:
                resolved.append(None)
        
        elif s == "✫":
            if two_under_5:
                resolved.append("+")
            else:
                resolved.append(None)
        
        else:
            resolved.append(None)
            
    for i in range(len(resolved)):
        if resolved[i] is None:
            if sum_all % 2 == 0:
                resolved[i] = "+"
            else:
                resolved[i] = "-"
    
    if "✦" in symbols:
        numbers[0], numbers[-1] = numbers[-1], numbers[0]
        first, last = numbers[0], numbers[-1]
                
    expr = str(numbers[0])
    for i in range(4):
        expr += resolved[i] + str(numbers[i+1])
        
    answer = eval(expr)
    
    print("Evaluate:", numbers[0], symbols[0], numbers[1], symbols[1], numbers[2], symbols[2], numbers[3], symbols[3], numbers[4])
    
    while dummy: 
        print()
        try: 
            response = int(input("Answer: "))
        except ValueError: 
            print("The answer must be an integer")
            continue
               
        if response == answer:
            dummy = False
        else:
            wrong += 1
            print("Incorrect! You have", 3 - wrong, "attempts left")
            return wrong
    return wrong
            
#FILE ----------------------------------------------------------------------------------------------------------------------------------

def printFolder(list, index):
    print("\tFolder #",index+1)
    print("1.", list[0])
    print("2.", list[1])
    print("3.", list[2])

def newTarget (moves, column, row):
    countL= moves.count("L")
    countR = moves.count("R")
    if len(moves) == 0:
        column = 0
        row = 2
    elif countL-1 == countR:
        column = 0
        row = 1
    elif moves[0] != moves[-1]:
        column = 1
        row = 1
    elif  countL == countR-2:
        column = 1
        row = 2
    elif countL == len(moves) or countR == len(moves):
        column = 3
        row = 3
    elif countL%2 == 0 and countR%2 == 0:
        column = 3
        row = 2
    elif countL%2 != 0 and countR%2 != 0:
        column = 3
        row = 2
    elif countR%2 == 0:
        column = 3
        row = 3
    elif len(moves) >= 3 and moves[0] == moves[1] and moves[1] == moves[2]:
        for i in range (len(moves)):
            if moves[0] == "L":
                if moves[i] == "R":
                    column = 3
                    row = 1
            else:
                if moves[i] == "L":
                    column = 3
                    row = 1
    elif len(moves) > 0 and moves[0] != moves[-1]:
        column = 4
        row = 3
    elif len(moves) <5:
        column = 0
        row = 3
    elif countL == countR:
        column = 1
        row = 3
    else:
        column = 2
        row = 2
    moves = []
    return moves, column, row




def bGroceryStore(wrong):
    print ("---------------------------------------------------------------------------------------------------------------------------------------")
    
    print ("Code: 2043")
    print ("Finally, one last task until you discover the truth. You open the computer before you to find what you need.")
    print (" ")
    masterList = [["chicken.mp3", "MagicWand.pdf", "bolbfish.heic"],["Apple.docx", "stickykeys.jpeg", "broccolini.jpeg" ], ["pizza.pdf","Dentures.mp4","coolGuy67.jpg" ],
                  ["AngryPenguins.pdf", "smthFunny.jpg", "ketchup.mp4"], ["EverythingBagel.png","Laptop.xlsx ", "baldCaps.mp3"]]

    indexing = 2
    print ("")
    print ("Find the everythingBagel.png file ")
    row = 1 #input (starts at 1)
    column = 4 #index (starts at 0)
    printFolder(masterList[2], 2)
    counter = 0

    moves = []
    while counter<3:
        inputed = input()

        if inputed == "a" or inputed == "A":
            if indexing>0:
                indexing = indexing - 1
                moves.append("L")
            else:
                print ("you are already at the msot left folder")
                print("")
        elif inputed == "d" or inputed == "D":
            if indexing < 4:
                indexing = indexing + 1
                moves.append("R")
            else:
                print("you are already at the most right folder")
                print("")
        elif inputed == "1" or inputed == "2" or inputed == "3":
            counter = counter + 1
            if int(inputed) == row and column == indexing:
                print ("correct!")
                print ("")
                # print ("og")
                # print (moves)
                # print (column)
                # print (row)
                moves, column, row = newTarget(moves, column, row)
                # print("new")
                # print(moves)
                # print(column)
                # print(row)
            else:
                print ("Incorrect file!!")
                print("")
                wrong = wrong + 1

        else:
            print ("Invalid input")



        printFolder(masterList[indexing],indexing)

    print (f"You recovered{3-wrong}/3")
    return wrong


#MEMORY ------------------------------------------------------------------------------------------------------------------------------------------------------------

def memoryGame(wrong):
    print ("---------------------------------------------------------------------------------------------------------------------------------------")

    print ("Code: 5263")
    print ("The filing cabinet in front of you is locked by a keypad. You need to act fast to get through this obstacle. ")
    print (" ")
    score = 0

    stage1Ans = None
    stage2Ans = None
    stage3Ans = None
    stage4Ans = None

    colours = ["Red", "Green", "Yellow", "Blue"]
    colourNum = ['31', '32', '33', '34']

    topColours = []
    keypads = []
    colourNums = []

    for i in range(5):
        keypad = []
        nums = []
        topColour = random.choice(colours)
        topColours.append(topColour)

        for j in range(4):
            colour = random.choice(colours)
            num = random.choice(colourNum)

            while colour in keypad:
                colour = random.choice(colours)

            while num in nums:
                num = random.choice(colourNum)

            keypad.append(colour)
            nums.append(num)

        keypads.append(keypad)
        colourNums.append(nums)

    buttonMaps = []

    for i in range(5):
        stageButtons = []
        for j in range(4):
            stageButtons.append({
                "label": keypads[i][j],
                "ansi": colourNums[i][j],
                "index": j
            })
        buttonMaps.append(stageButtons)

    def getButton(stage, index):
        return buttonMaps[stage][index]

    def userError():
        position = ['1', '2', '3', '4']
        answer = input("\nSelect button position (1-4): ")
        while answer not in position:
            answer = input("Select button position (1-4): ")
        return int(answer)

    def printBoard(stage):
        print("Stage:", stage + 1)
        print("      ", topColours[stage])
        print("")
        for i in range(4):
            print(
                f"\033[{colourNums[stage][i]}m{keypads[stage][i]}\033[0m",
                end=" "
            )
        print()

    # stage 1
    printBoard(0)
    answer1 = userError()
    i = answer1 - 1
    btn = getButton(0, i)

    if topColours[0] == 'Red':
        target = "34"
    elif topColours[0] == 'Green':
        target = "31"
    elif topColours[0] == 'Yellow':
        target = "32"
    elif topColours[0] == 'Blue':
        target = "33"

    if btn["ansi"] == target:
        score += 1
        stage1Ans = btn
    else:
        print("You Failed! Try Again!")
        wrong += 1
        return wrong

    # stage 2
    printBoard(1)
    answer2 = userError()
    i = answer2 - 1
    btn = getButton(1, i)

    if topColours[1] == 'Red':
        correct = "Yellow"

    elif topColours[1] in ['Green', 'Yellow']:
        correct = stage1Ans["ansi"]

    elif topColours[1] == 'Blue':
        correct = "31"

    if btn["label"] == correct or btn["ansi"] == correct:
        score += 1
        stage2Ans = btn
    else:
        print("You Failed! Try Again!")
        wrong += 1
        return wrong

    # stage 3
    printBoard(2)
    answer3 = userError()
    i = answer3 - 1
    btn = getButton(2, i)

    if topColours[2] == 'Red':
        correct = stage2Ans["ansi"]

    elif topColours[2] == 'Green':
        correct = "31"

    elif topColours[2] == 'Yellow':
        correct = stage1Ans["label"]

    elif topColours[2] == 'Blue':
        correct = "Green"

    if btn["label"] == correct or btn["ansi"] == correct:
        score += 1
        stage3Ans = btn
    else:
        print("You Failed! Try Again!")
        wrong += 1
        return wrong

    # stage 4
    printBoard(3)
    answer4 = userError()
    i = answer4 - 1
    btn = getButton(3, i)

    if topColours[3] == 'Red':
        correct = stage1Ans["ansi"]

    elif topColours[3] == 'Green':
        correct = "33"

    elif topColours[3] in ['Yellow', 'Blue']:
        correct = stage2Ans["ansi"]

    if btn["label"] == correct or btn["ansi"] == correct:
        score += 1
        stage4Ans = btn
    else:
        print("You Failed! Try Again!")
        wrong += 1
        return wrong

    # stage 5
    printBoard(4)
    answer5 = userError()
    i = answer5 - 1
    btn = getButton(4, i)

    if topColours[4] == 'Red':
        correct = stage1Ans["label"]

    elif topColours[4] == 'Green':
        correct = stage2Ans["label"]

    elif topColours[4] == 'Yellow':
        correct = stage3Ans["label"]

    elif topColours[4] == 'Blue':
        correct = stage4Ans["label"]

    if btn["label"] == correct:
        score += 1
    else:
        print("You Failed! Try Again!")
        wrong += 1
        return wrong

    return True



#RUN CODE

puzzles = ["cards","blocks","mess", "specialSymbol", "math", "memory"]
random.shuffle(puzzles)
for i in range (len(puzzles)):
    fail = check(wrong)
    if fail == True:
        print("Too late! A eureka hacks exec walks into the room and catches you in the act. Game over, I guess you will never know the truth about eureka hacks.")
        break 
    if puzzles[i] == "cards":
        wrong = cards(wrong)
    elif puzzles[i] == "blocks":
        wrong = blocks(wrong)
    elif puzzles[i] == "mess":
        wrong = bigMess(wrong)
    elif puzzles[i] == "specialSymbol":
        wrong = specialSymbol(wrong)
    elif puzzles[i] == "math":
        wrong = math(wrong)
    elif puzzles[i] == "memory":
        wrong = memoryGame(wrong)

wrong = bGroceryStore(wrong)
fail = check(wrong)
if fail == True:
    print("Too late! A eureka hacks exec walks into the room and catches you in the act. Game over, I guess you will never know the truth about eureka hacks.")
else:
    print ("You've finally made it! After all your hard work you have uncovered the truth.  The key to a successful project is yours! \nThe secret to winning eureka hacks is.. vibes?")

    
    
    
    