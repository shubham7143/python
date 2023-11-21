# wap to generate a strong random password.

import random
import string

if __name__ == "__main__":
    alpha = string.ascii_letters
    num = "1234567890"
    sym = "!@$%^&?"

    passw = alpha+num+sym
    passw = random.sample(passw, 8)

    print(''.join(passw))
