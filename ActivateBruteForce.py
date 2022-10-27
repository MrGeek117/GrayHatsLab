from SendPostForm import Session
from PasswordGen import bruteforce
from time import monotonic

def main():
    SessionData = Session()
    bruteforce(SessionData,5,False)
    





if __name__=="__main__":
    main()





def timer(s):
    passed = 0
    time = monotonic()
    while (s>=0):
        print(int(monotonic()-time))
        #passed += monotonic()


