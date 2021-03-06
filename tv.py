from resources import keys, config
import samsungctl
import time

char_list = [["a", "b", "c", "d", "e", "f"], ["g", "h", "i", "j", "k", "l"], ["m", "n", "o", "p", "q", "r"],
             ["s", "t", "u", "v", "w", "x"], ["y", "z", "1", "2", "3", "4"], ["5", "6", "7", "8", "9", "0"]]
film_name = "friends"


def get_char_map(film_name, char_list):
    char_map = []
    for letter in film_name:
        for row in char_list:
            for item in row:
                if item == letter:
                    n_row = char_list.index(row)
                    n_col = row.index(letter)
                    char_map.append((n_row, n_col))
                    print(f"letra {letter}, coordenadas row {n_row} e col {n_col}")
    return char_map


def move(*args):
    with samsungctl.Remote(config) as remote:
        c_row = 0
        c_col = 0
        print(f"começando na linha {c_row}, e na coluna  {c_col} ")
        for tuples in args:
            for item in tuples:
                t_row = item[0]
                t_col = item[1]
                print(f"e tenho que ir para a linha  {t_row}, e  coluna  {t_col} ")
                coordinate_row = c_row - t_row
                coordinate_col = c_col - t_col
                print(f" para isso tenho que andar  {coordinate_row} linhas e {coordinate_col}  colunas")
                i = 0
                print(f" descobrindo se vou para cima, para baixo ou se fico...")
                while i < abs(coordinate_row):
                    if coordinate_row < 0:
                        print(f" andando uma casa  para baixo...")
                        remote.control((keys['down key']))
                        time.sleep(0.5)
                        i += 1
                    elif coordinate_row > 0:
                        remote.control((keys['up key']))
                        print(f" andando uma casa para cima...")
                        time.sleep(0.5)
                        i += 1
                    else:
                        print("ja estou na linha certa vamos para a coluna certa agora...")
                        i += 1
                i = 0
                print(f" descobrindo se vou para direita ou para esquerda...")
                while i < abs(coordinate_col):
                    if coordinate_col < 0:
                        print(f" andando uma casa para direita...")
                        remote.control((keys['right key']))
                        time.sleep(0.5)
                        i += 1
                    elif coordinate_col > 0:
                        print(f" andando uma casa para esquerda...")
                        remote.control((keys['left key']))
                        time.sleep(0.5)
                        i += 1
                print ("não preciso mais mudar de coluna, apertando enter...")
                c_row = t_row
                c_col = t_col
                print(f"agora estou na linha {c_row} e coluna {c_col} ")
                i += 1
                remote.control((keys['enter key']))



def netflix_on():
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


def forward_medium_on():
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


# for play, pause and enter
def play():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['enter key']))


def play_from_beginning():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['down key']))
        time.sleep(1)
        remote.control((keys['enter key']))


def get_out():
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


def turn_off():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['poweroff key']))


move(get_char_map(film_name, char_list))
