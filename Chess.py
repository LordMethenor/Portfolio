import time
import webbrowser
print("\n")
time.sleep(1)
print("\n************************************************->")
print("*  Welcome to Lee's                              *")
print("*         _____  _   _  _____ _____ _____        *")
print("*        /  __ \| | | ||  ___/  ___/  ___|       *")
print("*        | /  \/| |_| || |__ \ `--.\ `--.        *")
print("*        | |    |  _  ||  __| `--. \`--. \       *")
print("*        | \__/\| | | || |___/\__/ /\__/ /       *")
print("*         \____/\_| |_/\____/\____/\____/        *")
print("*                              Tutorial Program  *")
print("**************************************************\n")
time.sleep(1)
continued = "1"
continued2 = "1"
input("Press enter to continue")
print("")
print("Chess is an age old game of strategy. Hopefully, this will teach you how to play for yourself!")
input("Press enter to continue")
print("")
print("This tutorial will use a text based menu system. Don't worry about losing your place! The program is easily navigable! Simply press enter on any menu, and you will be moved from your most recent location in the program to the next page.")
input("Press enter to continue")
print("")
print("It isn't a complete guide to the game because each piece has its own set of rules, easily found online. Teaching the backbone of how the game itself works is more important, and with that knowledge, you can easily go back and learn how to use individual pieces.")
input("Press enter to continue")
print("")
print("Ok. Here's the show!")
#MAIN MENU
main = True
while main == True:
	time.sleep(1)
	print("\n***************************************************************->")
	print("*        ___  ___      _        ___  ___                        *")
	print("*        |  \/  |     (_)       |  \/  |                        *")
	print("*        | .  . | __ _ _ _ __   | .  . | ___ _ __  _   _        *")
	print("*        | |\/| |/ _` | | '_ \  | |\/| |/ _ \ '_ \| | | |       *")
	print("*        | |  | | (_| | | | | | | |  | |  __/ | | | |_| |       *")
	print("*        \_|  |_/\__,_|_|_| |_| \_|  |_/\___|_| |_|\__,_|       *")
	print("*                                                               *")
	print("*****************************************************************\n")
	time.sleep(1)
	#ASCII
	input("Press enter to continue")
	print("")
	print("Contents: ")
	print("")
	print("The History-1")
	print("")
	print("The Rules-2")
	print("")
	doover = True
	menu_choice = input("Press enter to continue, end to end the program, or one of the listed numbers to go to a certain part.")
	while doover == True:
		if menu_choice == "":
			menu_choice = continued
			doover = True
		elif menu_choice == "1":
			doover = False
			print("")
			time.sleep(1)
			print("\n********************************************************************->")
			print("*         _____ _            _   _ _     _                           *")
			print("*        |_   _| |          | | | (_)   | |                          *")
			print("*          | | | |__   ___  | |_| |_ ___| |_ ___  _ __ _   _         *")
			print("*          | | | '_ \ / _ \ |  _  | / __| __/ _ \| '__| | | |        *")
			print("*          | | | | | |  __/ | | | | \__ \ || (_) | |  | |_| |        *")
			print("*          \_/ |_| |_|\___| \_| |_/_|___/\__\___/|_|   \__, |        *")
			print("*                                                       __/ |        *")
			print("*                                                      |___/         *")
			print("**********************************************************************\n")
			time.sleep(1)
			#ASCII
			input("Press enter to continue")
			print("")
			print("The game of chess is over 1000 years old. It is thought to have been developed in India in the 6th century CE, but it's early history is uncertain at best.")
			input("Press enter to continue")
			print("")
			print("The game spread through trade and conquest, first to the Arab world, then to Southern Europe.")
			input("Press enter to continue")
			print("")
			print("In Europe, in the late 15th century, chess took its modern form. This era of play, characterized by tactics and short-term focus, lasted about 400 years.")
			input("Press enter to continue")
			print("")
			print("Then, in the late 19th century, modern chess tournaments developed, and the first World Chess Championship was held in 1886. In the 20th century, chess theory and tactics advanced significantly and FIDE, the World Chess Federation, was founded.")
			input("Press enter to continue")
			print("")
			print("Now, in the 21st century, computers (that's me!) are mastering the game, beating the world's best players and providing detailed analysis of the game.")
			input("Press enter to continue")
			print("Today, over 600 million adults (a lot) play chess regularly! Both casual and competitive players can be found all over the world!")
			continued = "2"
			doover1 = True
			menu_choice = input("Press enter to continue, back to go back, end to end, or main to go to the main menu.")
			print("")
			while doover1 == True:
				if menu_choice == "":
					menu_choice = "2"
					doover = True
					doover1 = False
				elif menu_choice == "back":
					main = True
					doover = False
					doover1 = False
					continued = "2"
				elif menu_choice == "end":
					main = False
					doover = False
					doover1 = False
				elif menu_choice == "main":
					main = True
					doover = False
					doover1 = False
				else:
					doover1 = True
					menu_choice = input("Please try again with a listed value.")
		elif menu_choice == "2":
			continued = "2"
			doover = False
			main2 = True
			while main2 == True:
				time.sleep(1)
				print("\n***********************************************************->")
				print("*         _____ _           ______      _                   *")
				print("*        |_   _| |          | ___ \    | |                  *")
				print("*          | | | |__   ___  | |_/ /   _| | ___  ___         *")
				print("*          | | | '_ \ / _ \ |    / | | | |/ _ \/ __|        *")
				print("*          | | | | | |  __/ | |\ \ |_| | |  __/\__ \        *")
				print("*          \_/ |_| |_|\___| \_| \_\__,_|_|\___||___/        *")
				print("*                                                           *")
				print("*************************************************************\n")
				time.sleep(1)
				#ASCII
				input("Press enter to continue")
				print("")			
				print("Contents: ")
				print("")
				print("Setup-1")
				print("")
				print("Gameplay/Turns-2")
				print("")
				print("Moving-3")
				print("")
				print("Check-4")
				print("")
				print("Checkmate/Victory-5")
				print("")
				print("Draw-6")
				print("")
				print("Tournament Rules/Other versions-7")
				print("")
				doover2 = True
				menu_choice2 = input("Press enter to continue, main to go to the main menu, end to end the program, or one of the listed numbers to go to a certain part.")
				while doover2 == True:
					if menu_choice2 == "":
						menu_choice2 = continued2
						doover2 = True
					elif menu_choice2 == "main":
						continued = "2"
						doover2 = False
						main2 = False
						main = True
						doover = False
						cont = False
					elif menu_choice2 == "1":
						doover2 = False
						print("Setting up the board")
						print("")
            #Bboard setup picture link
						input("Press enter to continue")
						print("")
						print("First you need a chessboard, an 8x8 square checkered grid.")
						input("Press enter to continue")
						print("")
						print("There shoud be 2 sets, one light colored and one dark, of pieces. Each should include 8 pawns, 2 rooks, 2 knights, 2 bishops, a queen, and a king.")
						input("Press enter to continue. WARNING: An image will open in your web browser.")
						webbrowser.open('https://upload.wikimedia.org/wikipedia/commons/d/dd/AAA_SVG_Chessboard_and_chess_pieces_06.svg')
						print("")
						print("Place your pieces in the places shown on the linked images. If you have a numbered/lettered board, place the white pieces in ranks (rows) 1 and 2, and place your black pieces in ranks 7 and 8.")
						input("Press enter to continue")
						print("")
						print("Double check your pieces to make sure they're all in the correct places. Remember, the queens on both sides should be in a square of their color, and the kings should be in a square of the opposite color.")
						continued2 = "2"
						menu_choice2 = input("Press enter to continue, back to go back, end to end, rule to go to the rule menu, or main to go to the main menu.")
						print("")
						doover21 = True
						while doover21 == True:
							if menu_choice2 == "":
								menu_choice2 = continued2
								main2 = True
								doover2 = True
								doover21 = False
							elif menu_choice2 == "back":
								main2 = True
								doover2 = False
								doover21 = False
							elif menu_choice2 == "end":
								exit()
							elif menu_choice2 == "main":
								main = True
								main2 = False
								doover2 = False
								doover21 = False
								continued = "2"
								print(continued2)
							elif menu_choice2 == "rule":
								main = True
								main2 = True
								doover2 = False
								doover21 = False
							else:
								main2 = True
								doover2 = True
								doover21 = True
								menu_choice2 = input("Please try again with a listed value.")
					elif menu_choice2 == "2":
						doover2 = False
						print("The Gameplay")
						print("")
						input("Press enter to continue")
						print("")
						print("Now that you have set up the board and (presumably) found an opponent it is time to play.")
						input("Press enter to continue")
						print("")
						print("Choose a player to play the darker pieces (black) and one to play the lighter pieces (white). There is no specific way that determines who gets what color, just come to an agreement with your opponent.")
						input("Press enter to continue")
						print("")
						print("The player with the white pieces starts first. Each turn consists of the white player moving a piece and the black player moving a piece after the white player. The rules for moves can be found in the next section, movement, and the individual moves of each piece can be found online.")
						input("Press enter to continue")
						print("")
						print("Making a move is required to complete a turn. There is no fixed 'turn limit.' The structure of the game doesn't ever change. Illegal moves, or moves that break the rules, don't have a specific penalty in casual play. Just try to return your board to before the move was made.")
						continued2 = "3"
						menu_choice2 = input("Press enter to continue, back to go back, end to end, rule to go to the rule menu, or main to go to the main menu.")
						print("")
						doover22 = True
						while doover22 == True:
							if menu_choice2 == "":
								menu_choice2 = continued2
								main2 = True
								doover2 = True
								doover22 = False
							elif menu_choice2 == "back":
								menu_choice2 = "1"
								main2 = True
								doover2 = True
								doover22 = False
							elif menu_choice2 == "end":
								exit()
							elif menu_choice2 == "main":
								main = True
								main2 = False
								doover2 = False
								doover22 = False
								continued = "2"
							elif menu_choice2 == "rule":
								main = True
								main2 = True
								doover2 = False
								doover22 = False
							else:
								main2 = True
								doover2 = True
								doover22 = True
								menu_choice2 = input("Please try again with a listed value.")
					elif menu_choice2 == "3":
						doover2 = False
						print("Movement")
						print("")
						input("Press enter to continue")
						print("")
						print("Although each chess piece has certain rules for movement, the action taken during a turn, there are some rules that are almost universal.")
						input("Press enter to continue")
						print("")
						print("On your turn, you can pick up one of your pieces and relocate it to a square on the board. This is either a move or a capture. Moves are when you relocate your piece to an empty square, and captures are when you relocate it to a square occupied by an opponent's piece.")
						input("Press enter to continue")
						print("")
						print("When you 'capture', the enemy piece is removed from the game, permanently. If one of your pieces is in a square, you cannot move another one to that square.")
						input("Press enter to continue")
						print("")
						print("Unless otherwise stated in the piece rules, a piece cannot make multiple moves during a turn. It cannot switch direction, even if multiple directions are within the piece's rule. Each piece (except for the knight) must have an unobstructed path to the square it wants to move into. If a piece can move forward 5 square according to its rules, but there is a piece, enemy or friendly, in its forward path, it can only go as far as that piece or capture it if it is hostile.")
						continued2 = "4"
						menu_choice2 = input("Press enter to continue, back to go back, end to end, rule to go to the rule menu, or main to go to the main menu.")
						print("")
						doover23 = True
						back2="2"
						while doover23 == True:
							if menu_choice2 == "":
								menu_choice2 = continued2
								main2 = True
								doover2 = True
								doover23 = False
							elif menu_choice2 == "back":
								menu_choice2 = back2
								main2 = True
								doover2 = True
								doover23 = False
							elif menu_choice2 == "end":
								exit()
							elif menu_choice2 == "main":
								main = True
								main2 = False
								doover2 = False
								doover23 = False
								continued = "2"
							elif menu_choice2 == "rule":
								main = True
								main2 = True
								doover2 = False
								doover23 = False
							else:
								main2 = True
								doover2 = True
								doover23 = True
								menu_choice2 = input("Please try again with a listed value.")
					elif menu_choice2 == "4":
						doover2 = False
						print("Check")
						print("")
						input("Press enter to continue")
						print("")
						print("Check is a condition that a chess player is put in when their king is being threatened. In chess, a threatened king means that an opponent's piece is in a position where, if nothing is changed before the opponent's turn, it could 'capture' the king.")
            #king diagram/pic/ascii
						input("Press enter to continue")
						print("")
						print("Kings cannot be 'captured' the way other pieces can. They are the most important piece in the game, so they have their own rules, this being one of them.")
						input("Press enter to continue")
						print("")
						print("When one player 'checks' another, that player says 'check' before the other takes their turn. The checked player must use their next move to get out of check. Sidenote: If this is not possible, then the move was a checkmate, not a check, which will be described in the next section.")
						input("Press enter to continue")
						print("")
						print("A checked player has three options, capture, move, and block. Capturing is when the opponent piece threatening the king is taken, either by the king or another piece. Note that if this piece is protected, meaning an opponent piece has the potential to capture the square if the threatening piece is captured, the king cannot capture it because the king cannot move into check.")
						input("Press enter to continue")
						print("")
						print("Moving is pretty simple; a king in check moves to a different square where it is no longer threatened. The new square must be safe because the king cannot move into check. The third option, blocking, is when the checked player moves a piece to obstruct the threatening piece's direct path to the king.")
						input("Press enter to continue")
						print("")
						print("Although there is usually only one threatening piece, there can theoretically be many, such as in a discovery attack, a tactic you can search up online. If a king is checked by multiple pieces, then the player must respond with a move that neutralizes both. This can be simultaneously blocking one piece and capturing another or moving into a square safe from both. The player still only has one turn to get out of check.")
						input("Press enter to continue")
						print("")
						print("Check does not win points or end the game, so don't check for the sake of checking. Checking has uses, however. By forcing a player to make a move to protect their king, they might leave other areas unopened or become unable to counter your attacks. This becomes very useful for tactics.")
						continued2 = "5"
						menu_choice2 = input("Press enter to continue, back to go back, end to end, rule to go to the rule menu, or main to go to the main menu.")
						print("")
						doover24 = True
						back2 = "3"
						while doover24 == True:
							if menu_choice2 == "":
								menu_choice2 = continued2
								main2 = True
								doover2 = True
								doover24 = False
							elif menu_choice2 == "back":
								menu_choice2 = back2
								main2 = True
								doover2 = True
								doover24 = False
							elif menu_choice2 == "end":
								exit()
							elif menu_choice2 == "main":
								main = True
								main2 = False
								doover2 = False
								doover24 = False
								continued = "2"
							elif menu_choice2 == "rule":
								main = True
								main2 = True
								doover2 = False
								doover24 = False
							else:
								main2 = True
								doover2 = True
								doover24 = True
								menu_choice2 = input("Please try again with a listed value.")
					elif menu_choice2 == "5":
						doover2 = False
						print("Checkmate and Victory")
						print("")
						input("Press enter to continue")
						print("")
						print("When a player's king is in check and there is no legal move to escape; none of the three options in the last section, can be executed, checkmate occurs, the game is over, the checkmating player wins, and the checkmated player loses.")
						input("Press enter to continue")
						print("")
						print("Although this is the ultimate goal of a chess game, it is not the only way to win, nor the only way to end a game. Resignation is when a player voluntarily ends the game through accepting a loss and tipping over their king. In some tournament games, time controls are used, and if a player's time runs out, that player loses. ")
						input("Press enter to continue")
						print("")
						print("The next part explains the other game ending, the draw.")
						continued2 = "6"
						menu_choice2 = input("Press enter to continue, back to go back, end to end, rule to go to the rule menu, or main to go to the main menu.")
						print("")
						back2 = "4"
						doover25 = True
						while doover25 == True:
							if menu_choice2 == "":
								menu_choice2 = continued2
								main2 = True
								doover2 = True
								doover25 = False
							elif menu_choice2 == "back":
								menu_choice2 = back2
								main2 = True
								doover2 = True
								doover25 = False
							elif menu_choice2 == "end":
								exit()
							elif menu_choice2 == "main":
								main = True
								main2 = False
								doover2 = False
								doover25 = False
								continued = "2"
							elif menu_choice2 == "rule":
								main = True
								main2 = True
								doover2 = False
								doover25 = False
							else:
								main2 = True
								doover2 = True
								doover25 = True
								menu_choice2 = input("Please try again with a listed value.")
					elif menu_choice2 == "6":
						doover2 = False
						print("Draws")
						print("")
						input("Press enter to continue")
						print("")
						print("Draws are situations in which the game ends, and neither player wins or loses. In touraments, both players usually get half a point for draws.")
						input("Press enter to continue")
						print("")
						print("There are 5 types of draws, stalemates, insufficient material situations, fifty-move rule situations, threefold repetition, and agreement.")
						input("Press enter to continue")
						print("")
						print("Stalemates are situations where a player is unable to take a turn and move (this includes captures) because all pieces cannot make legal moves, either due to being blocked, being captured, or moving into check. Stalemates only occur when a king is not checked, because if a king is checked, and no legal moves are possible, then checkmate occurs.")
						input("Press enter to continue")
						print("")
						print("Insufficient material draws occur when there is no way to checkmate the opponent with the remaining pieces. This happens with the following pair: king vs king, king vs king and bishop, king vs king and knight, and king and bishop vs king and bishop of the same colored square as the first bishop.")
						input("Press enter to continue")
						print("")
						print("Fifty move rule draws happen when there has been no capture or pawn moves for 50 turns (each player made 50 moves).")
						input("Press enter to continue")
						print("")
						print("If the same board position occurs 3 times on the same player's turn and with each piece having the same rights to move (moves like castling, en pessant, see piece section, become permanently unavailable if certain things happen, and if they go from available to unavailable, they are considered differences in position).")
						input("Press enter to continue")
						print("")
						print("Both players can also agree to a draw. One of the players can request a job on their turn, and the other one can either accept or decline.")						
						continued2 = "7"
						menu_choice2 = input("Press enter to continue, back to go back, end to end, rule to go to the rule menu, or main to go to the main menu.")
						print("")
						doover26 = True
						back2 = "5"
						while doover26 == True:
							if menu_choice2 == "":
								menu_choice2 = continued2
								main2 = True
								doover2 = True
								doover26 = False
							elif menu_choice2 == "back":
								menu_choice2 = back2
								main2 = True
								doover2 = True
								doover26 = False
							elif menu_choice2 == "end":
								exit()
							elif menu_choice2 == "main":
								main = True
								main2 = False
								doover2 = False
								doover26 = False
								continued = "2"
							elif menu_choice2 == "rule":
								main = True
								main2 = True
								doover2 = False
								doover26 = False
							else:
								main2 = True
								doover2 = True
								doover26 = True
								menu_choice2 = input("Please try again with a listed value.")
					elif menu_choice2 == "7":
						doover2 = False
						print("Tournament Rules")
						print("")
						input("Press enter to continue")
						print("")
						print("There are certain rules that you might use in organized tournaments. A warning: these aren't universal, so double check the rules of any tournament you attend.")
						input("Press enter to continue")
						print("")
						print("The first commoon rule is touch move. In many tournaments, when you touch a piece, you have to move it if it is yours or capture it if it is your opponent's. If these aren't possible, you can usually just move something else, depending on the specific rules. In addition, when you release your hand from a piece onto its new square, your turn is over.")
						input("Press enter to continue")
						print("")
						print("Often, there are specific rules governing piece movement. Many chess tournaments only allow one hand to move pieces.")
						print("")
            #Chess Clock
						print("Time controls are common in tournaments. Chess clocks have two paddles, one for each players. Always learn the specific time constraints of a tournament. You have to hit the button to end your turn and start your opponent's clock, often with the hand you use to move the piece. The player who runs out of time loses.")
						input("Press enter to continue")
						print("")
						print("In many tournaments, chess rules are recorded through chess notation score sheets. These sheets can essentially record games, allowing documentation and proof of any irregularities and illegal moves. I recommend you learn notation, but I cannot teach it in this tutorial. Search it online if you are interested.")
						input("Press enter to continue")
						print("")
						print("There are certain rules of conduct that should usually be observed. Using notes, computers, or other outside sources of information is usually not permissable. Players are expected to shake hands before and after a game. Unless they are drawing, resigning, or questioning a possible irrregularity, players should not talk. At many casual or beginner tournaments, announcing check is a common practice, but at more advanced tournaments, it should not be used. Repeatedly asking for a draw or attempting to annoy a player is usually frowned upon or even illegal.")
						menu_choice2 = input("Press enter to continue to go to the conclusion, back to go back, end to end, rule to go to the rule menu, or main to go to the main menu.")
						print("")
						back2 = "6"
						doover27 = True
						while doover27 == True:
							if menu_choice2 == "":
								print("That's the show! This should teach you the fundamentals of the game. Admittedly, it isn't enough to get you started right now, but now, you will be able to understand tactics or pieces that you search up or find in a rule book. In other word's you have learned the language of chess. If you have interest in the game, I recommend joining a local club and doing free tutorials and games at sites like chess.com.")					
								input("Press enter")
								print("")
								print("Here are my sources: https://en.wikipedia.org/wiki/History_of_chess, https://en.wikipedia.org/wiki/Rules_of_chess#Initial_setup")
								input("Press enter")
								print("")
								input("Thanks for taking your time! Press enter to end the program.")
								exit()
							elif menu_choice2 == "back":
								menu_choice2 = back2
								main2 = True
								doover2 = True
								doover27 = False
							elif menu_choice2 == "end":
								exit()
							elif menu_choice2 == "main":
								main = True
								main2 = False
								doover2 = False
								doover27 = False
								continued = "2"
							elif menu_choice2 == "rule":
								main = True
								main2 = True
								continued2 = "conclusion"
								doover2 = False
								doover27 = False
							else:
								main2 = True
								doover2 = True
								doover27 = True
								menu_choice2 = input("Please try again with a listed value.")
					elif menu_choice2 == "end":
						exit() 
					elif menu_choice2 == "conclusion":
						print("That's the show! This should teach you the fundamentals of the game. Admittedly, it isn't enough to get you started right now, but now, you will be able to understand tactics or pieces that you search up or find in a rule book. In other word's you have learned the language of chess. If you have interest in the game, I recommend joining a local club and doing free tutorials and games at sites like chess.com.")					
						input("Press enter")
						print("")
						print("Here are my sources: https://en.wikipedia.org/wiki/History_of_chess, https://en.wikipedia.org/wiki/Rules_of_chess#Initial_setup")
						input("Press enter")
						print("")
						input("Thanks for taking your time! Press enter to end the program.")
						exit()           			
					else:
						doover = True
						menu_choice2 = input("Please try again with a listed value.")
		elif menu_choice == "end":
			main = False
			doover = False
			exit()
		else:
			doover = True
			menu_choice = input("Please try again with a listed value.")
