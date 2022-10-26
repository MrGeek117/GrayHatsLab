import os
import random


## Boundaries can change but total lenght stays the same

class file_RB:
    def __init__(self):
        self.token_line = 'Content-Disposition: form-data; name="__elgg_token"'
        self.timeS_line = 'Content-Disposition: form-data; name="__elgg_ts"'

        self.user_line = 'Content-Disposition: form-data; name="username"'
        self.pass_line = 'Content-Disposition: form-data; name="password"'

def randN(N):
	min = pow(10, N-1)
	max = pow(10, N) - 1
	return random.randint(min, max)


def set_boundary():
    s_newB = str(randN(random.randrange(30, 31)))
    global boundary 
    boundary = (59-len(s_newB))*"-" + s_newB
    return boundary

def Get_RB_string(user, passw, token, timestamp):
    default = file_RB()
    RB_string = boundary+"\n"+ default.token_line+"\n\n"+token+"\n"+boundary+"\n"+default.timeS_line+"\n\n"+str(timestamp)+"\n"+boundary+"\n"+default.user_line+"\n\n"+user+"\n"+str(boundary)+"\n"+default.pass_line+"\n\n"+passw+"\n"+boundary+"--"
    return RB_string



def update_RB_file(user, passw, token, timestamp):
    with open("temp_body","w") as f:
        f.truncate(0)
        #try:
        f.writelines(Get_RB_string(user, passw, token, timestamp))
        #except:
            #print("Insert the right types in the right order: User(str), Passw(str), token(str),timestamp(int/str)")
    return "./temp_body"