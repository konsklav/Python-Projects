import random
lids = [i for i in range(1,4)]
squares = [i for i in range(9)]
win = 0 
steps = 0
for j in range(100):
    stages = 0
    logic_variable = False
    board = [0,0,0,0,0,0,0,0,0]
    for k in range(9): 
        stages+=1
        random_lid = random.choice(lids)
        while logic_variable == False:
            random_square = random.choice(squares)
            if board[random_square] < random_lid: 
                board[random_square] = random_lid 
                logic_variable = True
            else:
                random_lid = random.choice(lids)
        logic_variable = False
        if stages>=3:
            for i in range(3):
                if board[i]==board[i+3]==board[i+6] or (board[i]==1 and board[i+3]==2 and board[i+6]==3) or (board[i]==3 and board[i+3]==2 and board[i+6]==1):
                    steps=steps+k
                    win+=1
                    logic_variable = True 
                if board[i]==board[i+1]==board[i+2] or (board[i]==1 and board[i+1]==2 and board[i+2]==3) or (board[i]==3 and board[i+1]==2 and board[i+2]==1):
                    steps=steps+k
                    win+=1
                    logic_variable = True
                if board[0]==board[4]==board[8] or (board[0]==1 and board[4]==2 and board[8]==3) or (board[0]==3 and board[4]==2 and board[8]==1):
                    steps=steps+k
                    win+=1
                    logic_variable = True 
                if board[2]==board[4]==board[6] or (board[2]==1 and board[4]==2 and board[6]==3) or (board[2]==3 and board[4]==2 and board[6]==1):
                    steps=steps+k
                    win+=1
                    logic_variable = True
        if logic_variable == True:
            break
average=steps/100
print("The average number of steps the game needs to finish is: ", average)