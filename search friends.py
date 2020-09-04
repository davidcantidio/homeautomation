from resources import keys, config
import samsungctl
import time


char_list = [["a","b","c","d","e","f"],["g","h","i","j","k","l"],["m","n","o","p","q","r"],["s","t","u","v","w","x"],["y","z","1","2","3","4"],["5","6","7","8","9","0"]]


film_name = "friends"
current_row_i = 0
curent_col_i = 0
char_position = char_list[current_row_i][curent_col_i]
turn = 0


def get_movie_letter(film_name, turn):
  letter = film_name[turn]
  print(letter)
  return letter



def find_position_of_character(char_list, letter):
    for row in char_list:
        for item in row:
          target_row_i = char_list.index(row)
          target_col_i = row.index(letter)
          return target_row_i, target_col_i


def get_movement_instructions(current_row_i, current_col_i, target_row_i, target_col_i):
  coordinate_row = (current_row_i - target_row_i)
  coordinate_col = (current_col_i - target_col_i)
  print(coordinate_row, coordinate_col)
  return coordinate_row, coordinate_col


def move_row(coordinate_row):
  while i <= abs(coordinate_row):
    if coordinate_row < 0:
      remote.control((keys['right key']))
      time.sleep(0.5)
      i += 1
    else:
      remote.control((keys['left key']))
      time.sleep(0.5)
      i += 1


def move_col(coordinate_col):
  while i <= abs(coordinate_col):
    if coordinate_col < 0:
      remote.control((keys['up key']))
      time.sleep(0.5)
      i += 1
    else:
      remote.control((keys['down key']))
      time.sleep(0.5)
      i += 1
    

def get_turn(film_name, turn):    
    while turn <= len(film_name):
      get_movie_letter(film_name, turn)
      find_position_of_character (char_list, letter)
      get_movement_instructions(current_row_i, current_col_i, target_row_i, target_col_i)
      move_row(coordinate_row)
      move_col(coordinate_col)
      remote.control((keys['enter key']))
      turn+=1
      return turn

get_turn(film_name, turn)
#get_movie_letter(film_name, turn)


