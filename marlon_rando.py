# Privacy is not something that I'm merely entitled to, it's an absolute prerequisite. -MB

import random
import string
from time import sleep


def id_generator(size=6, chars=string.letters + string.punctuation + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


if __name__ == '__main__':
    x = 0
    while x < 180:
        print id_generator(134)
        x += 1
        sleep(1)
    else:
        print 'The Cuttlefish has cuttled you!'
