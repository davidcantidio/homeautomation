from resources import keys, config
import samsungctl
import time


def turn_off ():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['power off key']))


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


def forward_plenty_on ():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['enter key']))
        time.sleep(0.5)
        for i in range(25):
            remote.control((keys['right key']))
            time.sleep(0.5)


def forward_little_on ():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['enter key']))
        time.sleep(0.5)
        for i in range(5):
            remote.control((keys['right key']))
            time.sleep(0.5)


def rewind_medium_on ():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['enter key']))
        time.sleep(0.5)
        for i in range(12):
            remote.control((keys['left key']))
            time.sleep(0.5)


def rewind_plenty_on ():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['enter key']))
        time.sleep(0.5)
        for i in range(25):
            remote.control((keys['left key']))
            time.sleep(0.5)


def rewind_little_on ():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['enter key']))
        time.sleep(0.5)
        for i in range(5):
            remote.control((keys['left key']))
            time.sleep(0.5)

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


#for play, pause and enter
def play ():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['enter key']))


def play_from_beginning ():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['enter key']))
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
            remote.control((keys['left key']))from resources import keys, config
import samsungctl
import time


def turn_off ():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['power off key']))


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


def forward_plenty_on ():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['enter key']))
        time.sleep(0.5)
        for i in range(25):
            remote.control((keys['right key']))
            time.sleep(0.5)


def forward_little_on ():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['enter key']))
        time.sleep(0.5)
        for i in range(5):
            remote.control((keys['right key']))
            time.sleep(0.5)


def rewind_medium_on ():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['enter key']))
        time.sleep(0.5)
        for i in range(12):
            remote.control((keys['left key']))
            time.sleep(0.5)


def rewind_plenty_on ():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['enter key']))
        time.sleep(0.5)
        for i in range(25):
            remote.control((keys['left key']))
            time.sleep(0.5)


def rewind_little_on ():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['enter key']))
        time.sleep(0.5)
        for i in range(5):
            remote.control((keys['left key']))
            time.sleep(0.5)

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


#for play, pause and enter
def play ():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['enter key']))


def play_from_beginning ():
    with samsungctl.Remote(config) as remote:
        remote.control((keys['enter key']))
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