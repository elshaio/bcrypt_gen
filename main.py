import bcrypt
import sys
import string


def main(argumentos):
    plainpassword = bytes(" ".join(argumentos), "utf8")
    hashed = bcrypt.hashpw(plainpassword, bcrypt.gensalt(rounds=10, prefix=b"2a"))

    if bcrypt.checkpw(plainpassword, hashed):
        print("Al cien")
        print("password: \n{}".format(plainpassword))
        print("hashed: \n{}".format(hashed.decode()))
    else:
        print("oh-oh")

if __name__ == "__main__":
    args = sys.argv[1:]
    main(args)
