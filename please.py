import os, sys 

print ("\033[1;32mMasukan UserName&Password:)")
print ("\033[1;31;1mMauTauPasswordnyaContactWaDuluDong085779515200")
print ("\033[1;31;1mScript Ini Hanya Untuk Umur 18 Keatas!!!")
username = 'MRTAMFANX'
password = 'ADMINTAMFAN'

def restart():
        ngulang = sys.executable
        os.execl(ngulang, ngulang, *sys.argv)

def main():
        uname = raw_input("username : ")
        if uname == username:
                pwd = raw_input("password : ")

                if pwd == password:
                        print "\n\033[1;34mSelamat Datang Di MrTamfanX Cyber Team",
                        sys.exit()

                else:
                        print "\n\033[1;36mSorry Invalid Password !!!\033[00m"
                        print "Back Login\n"
                        restart()

        else:
                print "\n\033[1;36mSorry Invalid Username !!!\033[00m"
                print "Back Login\n"
                restart()

try:
        main()
except KeyboardInterrupt:
        os.system('clear')
        restart()