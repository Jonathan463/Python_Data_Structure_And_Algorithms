import random

def welcome_message():
    print('Welcome to the Nim Game 🎉')

# computer player
# num_sticks: sticks in the heap
# return sticks removed
def nim(num_sticks: int) -> int:
   max_moves = min(3, num_sticks)
   move = random.randint(1, max_moves)
   return move

# human player
# receives number of sticks from the heap
# return no of sticks removed
def nim_human(num_sticks: int) -> int:
      while True:
         try:
            move = int(input('Enter the number of sticks to remove between (1-3): '))

            # handle validation checks
            if (move >= 1 and move <= 3) and move <= num_sticks:
               return move
            print('Invalid move!!')
         except ValueError:
            print('Invalid value! Please provide a number!')


# super computer
# determine the most optimal move
def nim_best(num_sticks: int) -> int:
   value = num_sticks % 4
   if value == 0:
      # loosing position, call random computer to make a valid legal move
      move = nim(num_sticks)
      return move
   else:
      # optimal move
      move = value
      return move


def get_player_type(player_num: int) -> str:
   while True:
      try:
         choice = int(input(f'Select player {player_num} type below: \n1. Human. \n2. Computer. \n3. Smart Computer\n**********\n'))
         if choice == 1:
            return "human"
         elif choice == 2:
            return "computer"
         elif choice == 3:
            return "smart"
         else:
            print('Invalid choice! Please select choice between 1 and 3 inclusive')
      except ValueError:
       print('Invalid value! valid choice must be a number')

# game manager
def setup_game():
   welcome_message()
   player_one_type = get_player_type(1)
   player_two_type  = get_player_type(2)

   while True:
      try:
         # handle the number of sticks for the game
         num_sticks = int(input('Please enter number of sticks between 10 and 100 inclusive: \n'))
         # print(f'player one type: {player_one_type}; player two type: {player_two_type}; number of sticks: {num_sticks}')

         # handle validation checks for number of sticks
         if num_sticks >= 10 and num_sticks <= 100:
            break
         else:
            print('Invalid number of sticks! Number of sticks not within range')

      except ValueError:
         print('Please provide a numeric number of sticks')

   return player_one_type, player_two_type, num_sticks

# game controller
def play_game(player_one_type, player_two_type, sticks: int):
   print(f'\nGame starts with {sticks} number of sticks')

   # map player to the specific method reference
   move_function = {
      "human": nim_human,
      "computer": nim,
      "smart": nim_best
   }

   player_names = {
      "human": "Human",
      "computer": "Computer",
      "smart": "Smart"
   }

   players = [move_function[player_one_type], move_function[player_two_type]]
   player_labels = [player_names[player_one_type], player_names[player_two_type]]

   # intial current player
   current_player = 0

   while sticks > 0:
      # call current player choice method
      move  = players[current_player](sticks)
      # reduce num of sticks
      sticks -= move

      print(f'{player_labels[current_player]} player {current_player + 1} removed {move} sticks')
      print(f'Number of sticks left: {sticks}')

      # if no more sticks, declare winner
      if sticks == 0:
         print(f'Game over! The winner is {player_labels[current_player]} player {current_player + 1}')
         break

      # switch current player
      current_player = 1 if current_player == 0 else 0
      # current_player = (current_player + 1) % 2


def main():
  while True:
       player1, player2, sticks = setup_game()
       play_game(player1, player2, sticks)

       response = input('Do you want to play again? Type (yes/no):\n').strip().lower()

       if response != 'yes':
           print('Thanks for playing! See you next time 🚀')
           break


if __name__ == '__main__':
     main()
