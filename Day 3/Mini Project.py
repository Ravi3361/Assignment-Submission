# Generate every time a 6 character OTP  and print it

import random
import string
OTP=''
characters_list=string.ascii_letters+string.digits

for i in range(6):
    OTP+=random.choice(characters_list)
print(OTP)