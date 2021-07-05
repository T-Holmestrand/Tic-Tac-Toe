#TICTACTOE GAME
print("""











        // WRITTEN BY TOMAS HOLMESTRAND //












########################################################
# Welcome to my first terminal game of Tic Tac Toe!    #
# To start your turn, type in the coordinates for      #
# your desired space (starting with the number,        #
# followed by the letter). Then hit enter.             #
########################################################





""")

numbered_coordinates = ' '.join(["  ", "1", "2", "3"])

l1 = ["a|", "▢", "▢", "▢"]
l2 = ["b|", "▢", "▢", "▢"]
l3 = ["c|", "▢", "▢", "▢"]


valid_input = ["1a", "2a", "3a", "1b", "2b", "3b", "1c", "2c", "3c"]

player = " "
false_input = 999
win = 111




def interaction(player):
	user_input = input('Coordinates:')

	if user_input in valid_input:
		if user_input == "1a":
			l1[1] = player
			valid_input.remove("1a")

		elif user_input == "2a":
			l1[2] = player
			valid_input.remove("2a")

		elif user_input == "3a":
			l1[3] = player
			valid_input.remove("3a")

		elif user_input == "1b":
			l2[1] = player
			valid_input.remove("1b")

		elif user_input == "2b":
			l2[2] = player
			valid_input.remove("2b")

		elif user_input == "3b":
			l2[3] = player
			valid_input.remove("3b")

		elif user_input == "1c":
			l3[1] = player
			valid_input.remove("1c")

		elif user_input == "2c":
			l3[2] = player
			valid_input.remove("2c")

		elif user_input == "3c":
			l3[3] = player
			valid_input.remove("3c")

	else: 
		return interaction(player)


def gameboard(l1p, l2p, l3p, player):
	print("It's {}'s turn!".format(player))
	print("""
	{nc}
	{l1p}
	{l2p}
	{l3p}






		""".format(nc = numbered_coordinates, l1p = l1p, l2p = l2p, l3p = l3p), end ='\r')

def check_win(l1, l2, l3, player):
	if l1[1] == player and l1[2] == player and l1[3] == player:
		return win
		#"{} WON!".format(player)
	if player in l2[1] and player in l2[2] and player in l2[3]:
		return win
	if player in l3[1] and player in l3[2] and player in l3[3]:
		return win
	if player in l1[1] and player in l2[1] and player in l3[1]:
		return win
	if player in l1[2] and player in l2[2] and player in l3[2]:
		return win
	if player in l1[3] and player in l2[3] and player in l3[3]:
		return win
	if player in l1[1] and player in l2[2] and player in l3[3]:
		return win
	if player in l1[3] and player in l2[2] and player in l3[1]:
		return win
	return

	
def playgame():
	turn_count = 1

	for i in range(1,10):
		
		if i % 2 != 0:
			player = "X"
		else: player = "O"

		l1p = ' '.join(l1)
		l2p = ' '.join(l2)
		l3p = ' '.join(l3)

		gameboard(l1p, l2p, l3p, player)

		
		interaction(player)

		l1p = ' '.join(l1)
		l2p = ' '.join(l2)
		l3p = ' '.join(l3)
		
		if check_win(l1, l2, l3, player) == win:
			print("""
	{nc}
	{l1p}
	{l2p}
	{l3p}
	""".format(nc = numbered_coordinates, l1p = l1p, l2p = l2p, l3p = l3p))
			print("GAME OVER, {player} WON!".format(player = player))
			exit()
		
		turn_count += 1
	print("""
	{nc}
	{l1p}
	{l2p}
	{l3p}
	""".format(nc = numbered_coordinates, l1p = l1p, l2p = l2p, l3p = l3p))
	print("IT'S A TIE!")


playgame()













