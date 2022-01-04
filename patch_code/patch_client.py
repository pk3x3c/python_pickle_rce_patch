import os
import pickle
import hashlib
import hmac
def fun(name,password):
    s = {"username":name,"password":password}
    file=open("users.json","wb")
    safecode=pickle.dumps(s)
    signature=hmac.new(b'secret',safecode,hashlib.sha256).digest()       # for example only writing the secret here only , developer can import from other file as >
    file.write(signature+b' '+safecode)


if __name__ == '__main__':
    u = input("Username : ")
    p = input("Password : ")
    fun(u,p)




