from resources import keys, config
import samsungctl
import time

char_list = [["a","b","c","d","e","f"],["g","h","i","j","k","l"],["m","n","o","p","q","r"],["s","t","u","v","w","x"],["y","z","1","2","3","4"],["5","6","7","8","9","0"]]
film_name = "friends"


def get_char_map(film_name, char_list):
    char_map =[]
    for letter in film_name:
        for row in char_list:
            for item in row:
                if item == letter:
                    n_row = char_list.index(row)
                    n_col = row.index(letter)
                    char_map.append((n_row, n_col))
                    #print(f"letra {letter}, coordenadas row {n_row} e col {n_col}")
    return char_map



def move(*args):
    with samsungctl.Remote(config) as remote:
        c_row = 0
        c_col = 0
        for tuples in args:
            for item in tuples:
                t_row = item[0]
                t_col = item[1]
                coordinate_row = c_row-t_row
		coordinate_col = c_col-t_col
                i = 0
                while i <= abs(coordinate_row):
		    if coordinate_row < 0:
		    remote.control((keys['right key']))
	            time.sleep(0.5)
		    i += 1
		    elif coordinate_row > 0:
		    remote.control((keys['left key']))
		    time.sleep(0.5)
		    i += 1
	        while i <= abs(coordinate_row):
		    if coordinate_row < 0:
		    remote.control((keys['right key']))
		    time.sleep(0.5)
		    i += 1
		    elif coordinate_row > 0:
		    remote.control((keys['left key']))
		    time.sleep(0.5)
		    i += 1
		    remote.control((keys['enter key']))


def netflix_on ():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['return key']))
        time.sleep(2)
        remote.control((keys['return key']))
        remote.control((keys['smart hub key']))
        time.sleep(10)
        remote.control((keys['enter key']))


def netflix_off():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['return key']))
        time.sleep(2)
        remote.control((keys['return key']))
        remote.control((keys['smart hub key']))
        time.sleep(5)
        remote.control((keys['enter key']))
        time.sleep(20)
        remote.control((keys['return key']))


def forward_medium_on ():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['enter key']))
        time.sleep(0.5)
        for i in range(12):
            remote.control((keys['right key']))
            time.sleep(0.5)


def forward_plenty_on():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['enter key']))
        time.sleep(0.5)
        for i in range(25):
            remote.control((keys['right key']))
            time.sleep(0.5)


def forward_little_on():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['enter key']))
        time.sleep(0.5)
        for i in range(5):
            remote.control((keys['right key']))
            time.sleep(0.5)


def rewind_medium_on():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['enter key']))
        time.sleep(0.5)
        for i in range(12):
            remote.control((keys['left key']))
            time.sleep(0.5)


def rewind_plenty_on():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['enter key']))
        time.sleep(0.5)
        for i in range(25):
            remote.control((keys['left key']))
            time.sleep(0.5)


def rewind_little_on():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['enter key']))
        time.sleep(0.5)
        for i in range(5):
            remote.control((keys['left key']))
            time.sleep(0.5)


#for play, pause and enter
def play():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['enter key']))


def play_from_beginning ():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['down key']))
        time.sleep(1)
        remote.control((keys['enter key']))


def get_out ():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['return key']))


def zap_right():
    with samsungctl.Remote(config) as remote:
        for i in range(180):
            time.sleep(2)

            remote.control((keys['right key']))


def zap_left():
    with samsungctl.Remote(config) as remote:
        for i in range(180):
            time.sleep(2)
            remote.control((keys['left key']))


def turn_off ():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['poweroff key']))


move(get_char_map(film_name, char_list))
