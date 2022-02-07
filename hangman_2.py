def hangman():
    word_list = ["starbuck", "Excelsior", "Hoshino", "mac"]
    random_number = random.randint(0, 4)
    word = word_list[random_number]
    wrong_guesses = 0
    wrong=0
    stages=["",
            "_______       ",
            "|             ",
            "|      |      ",
            "|      0      ",
            "|     /|/     ",
            "|     / /     ",
            "|             "
            ]
    rletters=list(word)
    board=["_"]*len(word)
    win=False
    print("ハングマンへようこそ")
    while wrong<len(stages)-1:
       print("\n")
       msg="一文字予想してね"
       char=input(msg)
       if char in rletters:
           cind=rletters.index(char)
           board[cind]=char
           rletters[cind]="$"
       else:
           wrong+=1
       print(" ".join(board))
       e=wrong+1
       print(" ".join(stages[0:e]))
       if "_"not in board:
           print("あなたの勝ち")
           print(" ".join(borad))
           win=True
           break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print(" あなたの負け！正解は{}.".format(word))


hangman(word)



import random


