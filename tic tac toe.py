board=[" " for x in range(9)]
row1="|{}|{}|{}|".format(board[0],board[1],board[2])
row2="|{}|{}|{}|".format(board[3],board[4],board[5])
row3="|{}|{}|{}|".format(board[6],board[7],board[8])

print(row1)
print(row2)
print(row3)
current_player="X"
n=int(input("enter:"))
board[n]=current_player
if current_player=="X":
    current_player="o"
else:
    current_player="X"
print(row1)
print(row2)
print(row3)