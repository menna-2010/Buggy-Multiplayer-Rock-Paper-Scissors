Problems & Fixes:
1. Syntax Error in get_player_choice Function
Problem:
choice = input(f"Player {player_num}, enter your choice (rock, paper, scissors): ".lower()  #
Issue 1: .lower() is incorrectly applied to the string instead of the input.
Issue 2: Missing closing parenthesis ) at the end.
solve:
choice = input(f"Player {player_num}, enter your choice (rock, paper, scissors): ").lower()
Fix 1: Moved .lower() to apply to input().
Fix 2: Closed the missing parenthesis.
2. Syntax Error in determine_winner Function

problem:
if player1_choice == player2_choice  #
Issue: Missing colon : at the end of the if statement.
solve:
if player1_choice == player2_choice:  # Added missing colon
3. Syntax Error in Multi-Line Condition (determine_winner)
Problem:
elif (player1_choice == "rock" and player2_choice == "scissors") or \  # 
Issue: The comment # is placed incorrectly at the end of the line. Python treats it as an unterminated line break.
solve:
elif (player1_choice == "rock" and player2_choice == "scissors") or \
     (player1_choice == "paper" and player2_choice == "rock") or \
     (player1_choice == "scissors" and player2_choice == "paper"):
solve: 
Removed the misplaced comment.
4. Logical Error in else Statement (determine_winner)
Problem:
else:
    return "Player 1 wins!"  #
Issue: The else block always returns "Player 1 wins!", even when Player 2 should win.
solve:
else:
    return "Player 2 wins!"  # Fixed incorrect return statement
Fix: Changed return statement to "Player 2 wins!" so that Player 2 wins when the first condition is false.
5. Syntax Error in play_game Function Definition
Problem:
def play_game  # 
Issue: Missing parentheses () after the function name.
save:
def play_game():  # Added missing parentheses
