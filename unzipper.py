import zipfile
import optparse
import threading

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def extractfile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        return True
    except:
        return False


def main():
    result = None
    
    parser = optparse.OptionParser("usage %prog "+\
                                   "-f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string',\
                      help = 'specify zip file ')
    parser.add_option('-d', dest="dname", type='string',\
                      help = 'specify dictionary file')
    (options, args) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print (parser.usage)
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
        
    zFile=zipfile.ZipFile(zname)
    passFile = open(dname)

    def threading(extractfile):
        for line in passFile.readlines():
            s =  Thread(target = extractfile, args=(zipfile, password))
            s.start()

    for line in passFile.readlines():
        threading(extractfile)
        password = line.strip('\n')
        success = extractfile(zFile, password)
        if success is True:
            print ("\n" + color.BOLD + "[+] Password found: " + password + color.END + "\n")
            break
        else:
            print (color.BOLD + "[-]" + color.END + "Password Not Found")

if __name__ == "__main__":
    main()
