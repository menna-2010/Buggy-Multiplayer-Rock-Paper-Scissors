def get_player_choice(player_num):
    choice = input(f"Player {player_num}, enter your choice (rock, paper, scissors): ".lower()  #
    return choice

def determine_winner(player1_choice, player2_choice):
    if player1_choice == player2_choice  #
        return "It's a tie!"
    elif (player1_choice == "rock" and player2_choice == "scissors") or \  # 
         (player1_choice == "paper" and player2_choice == "rock") or \
         (player1_choice == "scissors" and player2_choice == "paper"):
        return "Player 1 wins!"
    else:
        return "Player 1 wins!"  #

def play_game():  # Fixed missing parentheses
    player1_choice = get_player_choice(1)
    player2_choice = get_player_choice(2)

    winner = determine_winner(player1_choice, player2_choice)
    print(winner)

if __name__ == "__main__":
    play_game()
