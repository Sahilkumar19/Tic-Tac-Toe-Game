# print the required board to play the game
def board(matrix):
    for row in matrix:
        print(" | ".join(row))
        print("-" * 9)

matrix = [[' ' for i in range(3)] for i in range(3)]
count = 0
player = 'X'

def have_won(matrix, player):
    for i in range(3):
        # Checking in a row if all elements in the row are equal to the player
        if all([cell == player for cell in matrix[i]]):
            return True

        # Checking in a col if all elements in the row are equal to the player
        if all([matrix[j][i] == player for j in range(3)]):
            return True

    # Check diagonals
    if all([matrix[i][i] == player for i in range(3)]) or all([matrix[i][2 - i] == player for i in range(3)]):
        return True

    return False


while True:
    board(matrix)
    try:
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))

        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Input out of bounds. Please enter two integers between 0 and 2.")
            continue

        if matrix[row][col] == ' ':
            matrix[row][col] = player
            count += 1
            game_over = have_won(matrix, player)  # Assuming you have the have_won function defined
            if count >= 9:
                print("Game over It's a tie!")
                break

            if game_over:
                print(f"Player {player} has won")
                break
            else:
                player = 'O' if player == 'X' else 'X'  # change player
        else:
            print("\nThis position is already taken\n")
            continue

    except ValueError:
        print("Invalid input. Please enter two integers between 0 and 2.")
        continue

board(matrix)
0