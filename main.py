# ---Global Variables---

# game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If game is still going
game_still_going = True

# Who won? Or tie?
winner = None

# Whose turn is it?
current_player = "X"


# ---Functions---



# Play game of Tic Tac Toe 
def play_game():
  #display initial board
  display_board()

  # While the game is still going
  while game_still_going:
    #Handle a single turn of an arbitrary player
    handle_turn(current_player)
    
    # Check if the game is over
    check_if_game_over()

    # Flip to the other player
    flip_player()


  # Since the game is over, print the winner or tie
  if winner == "X" or winner == "O":
    print(winner + " won.")
  elif winner == None:
    print ("It is tie.")


# Display board
def display_board():
  print("\n")
  print(" | " + board[0] + " | " + board[1] + " | " + board[2] + " | " + "   | 1 | 2 | 3 |")
  print(" | " + board[3] + " | " + board[4] + " | " + board[5] + " | " + "   | 4 | 5 | 6 |")
  print(" | " + board[6] + " | " + board[7] + " | " + board[8] + " | " + "   | 7 | 8 | 9 |")
  print("\n")

# Handle a single turm of an arbitrary player
def handle_turn(player):
  
  # Get position from player
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  valid = False
  while not valid:

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")
  
    position = int(position) - 1

    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")

  board[position] = player
  display_board()


def check_if_game_over():
  check_for_winner()
  check_for_tie()

def check_for_winner():

  global winner

  # Check if there was a winner anywhere
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()

  # Return the winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None


def check_rows():
  global game_still_going
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"

  if row_1 or row_2 or row_3:
    game_still_going = False

  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  # Return None if there is no winner
  else: 
    return None


def check_columns():
  global game_still_going
  colomn_1 = board[0] == board[3] == board[6] != "-"
  colomn_2 = board[1] == board[4] == board[7] != "-"
  colomn_3 = board[2] == board[5] == board[8] != "-"

  if colomn_1 or colomn_2 or colomn_3:
    game_still_going = False

  if colomn_1:
    return board[0]
  elif colomn_2:
    return board[1]
  elif colomn_3:
    return board[2]
  # Return None if there is no winner
  else: 
    return None


def check_diagonals():
  global game_still_going
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"

  if diagonal_1 or diagonal_2:
    game_still_going = False

  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]
  # Return None if there is no winner
  else: 
    return None


def check_for_tie():
  # Set global variable
  global game_still_going

  if "-" not in board:
    game_still_going = False
  return


def flip_player():
  global current_player
  if current_player == "X":
    current_player = "O"
  elif current_player == "O":
    current_player = "X"
  return


play_game()




#board
#display board
#play game
#handle turn
#check for win
  #check rows
  #check columns
  #check diagonals
#check for tie
#flip player
