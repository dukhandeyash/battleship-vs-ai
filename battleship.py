import random
 import time
 BOARD_SIZE = 5
 SHIP_SYMBOL = "S"
 HIT_SYMBOL = "X"
 MISS_SYMBOL = "O"
 EMPTY_SYMBOL = "~"
 player_board = [[EMPTY_SYMBOL] * BOARD_SIZE for _ in range(BOARD_SIZE)]
 ai_board = [[EMPTY_SYMBOL] * BOARD_SIZE for _ in range(BOARD_SIZE)]
 player_guesses = [[EMPTY_SYMBOL] * BOARD_SIZE for _ in range(BOARD_SIZE)]
ai_attacks_on_player = [[EMPTY_SYMBOL] * BOARD_SIZE for _ in
 range(BOARD_SIZE)]
 ships = [(1, 2), (2, 1), (3, 1)]
 def print_board(board, reveal=False):
 print(" " + " ".join(str(i) for i in range(BOARD_SIZE)))
 for idx, row in enumerate(board):
 print(f"{idx} " + " ".join(cell if reveal else (cell if cell !=
 SHIP_SYMBOL else EMPTY_SYMBOL) for cell in row))
 def place_ships(board):
 for size, quantity in ships:
 for _ in range(quantity):
 while True:
 print("\nCurrent Board (Your Ships):")
 print_board(board, reveal=True)
 x, y = map(int, input(f"Enter the starting coordinates for
 your {size}-cell ship (x y): ").split())
 orientation = input("Enter orientation (H for horizontal,
 V for vertical): ").upper()
 if is_valid_placement(board, x, y, size, orientation):
 place_ship(board, x, y, size, orientation)
 break
 print("Invalid placement. Try again.")
 def is_valid_placement(board, x, y, size, orientation):
 if orientation == "H" and y + size <= BOARD_SIZE:
 return all(board[x][y + i] == EMPTY_SYMBOL for i in range(size))
 elif orientation == "V" and x + size <= BOARD_SIZE:
 return all(board[x + i][y] == EMPTY_SYMBOL for i in range(size))
 return False
 def place_ship(board, x, y, size, orientation):
 for i in range(size):
 if orientation == "H":
 board[x][y + i] = SHIP_SYMBOL
 elif orientation == "V":
 board[x + i][y] = SHIP_SYMBOL
def ai_place_ships(board):
 for size, quantity in ships:
 for _ in range(quantity):
 while True:
 x, y = random.randint(0, BOARD_SIZE-1),
 random.randint(0, BOARD_SIZE-1)
 orientation = random.choice(["H", "V"])
 if is_valid_placement(board, x, y, size, orientation):
 place_ship(board, x, y, size, orientation)
 break
 def ai_attack(last_hit=None, target_mode=False, tried_positions=None):
 if target_mode and last_hit:
 x, y = last_hit
 possible_targets = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
 random.shuffle(possible_targets)
 for tx, ty in possible_targets:
 if (0 <= tx < BOARD_SIZE and 0 <= ty < BOARD_SIZE and
 ai_attacks_on_player[tx][ty] == EMPTY_SYMBOL and (tx, ty)
 not in tried_positions):
 tried_positions.add((tx, ty))
 return tx, ty
 while True:
 x, y = random.randint(0, BOARD_SIZE-1), random.randint(0,
 BOARD_SIZE-1)
 if ai_attacks_on_player[x][y] == EMPTY_SYMBOL:
 tried_positions.add((x, y))
 return x, y
 def player_attack():
 while True:
 print("\nYour View of AI's Board (Hits and Misses):")
 print_board(player_guesses)
 x, y = map(int, input("Enter attack coordinates (x y): ").split())
 if 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE and
 player_guesses[x][y] == EMPTY_SYMBOL:
 break
 print("Invalid attack or already targeted cell. Try again.")
 if ai_board[x][y] == SHIP_SYMBOL:
 ai_board[x][y] = HIT_SYMBOL
player_guesses[x][y] = HIT_SYMBOL
 print("Hit!")
 else:
 player_guesses[x][y] = MISS_SYMBOL
 print("Miss.")
 def is_game_over(board):
 return all(cell != SHIP_SYMBOL for row in board for cell in row)
 def play_game():
 place_ships(player_board)
 ai_place_ships(ai_board)
 print("\nGame Start!\n")
 target_mode = False
 last_hit = None
 tried_positions = set()
 while True:
 print("\nPlayer's Board (Your Ships with AI's Hits and Misses):")
 print_board(ai_attacks_on_player)
 print("\nPlayer's Turn")
 player_attack()
 if is_game_over(ai_board):
 print("Player wins!")
 break
 print("\nAI's Turn")
 x, y = ai_attack(last_hit, target_mode, tried_positions)
 print(f"AI attacks at ({x}, {y})")
 if player_board[x][y] == SHIP_SYMBOL:
 player_board[x][y] = HIT_SYMBOL
 ai_attacks_on_player[x][y] = HIT_SYMBOL
 print("AI hit!")
 last_hit = (x, y)
 target_mode = True
 else:
 ai_attacks_on_player[x][y] = MISS_SYMBOL
print("AI missed.")
 time.sleep(1)
 if is_game_over(player_board):
 print("AI wins!")
 break
 play_game()