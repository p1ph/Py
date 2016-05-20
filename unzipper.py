import zipfile
import optparse
import threading


def extractfile(zipfile, password):
    try:
        zipfile.extractall(pwd=password)
        return True
    except:
        return False

def threading(extractfile):
    for line in passFile.readlines():
        s =  Thread(target = extractfile, args=(zipfile, password))
        s.start()

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
        
    zipfile=zipfile.ZipFile(zname)
    passFile = open(dname)

    for line in passFile.readlines():
        threading(extractfile)
        password = line.strip('\n')
        success = extractFile(zipfile, password)
        if success is True:
            print ("\n" + "[+] Password found: " + "\n")
            break
        else:
            print ("\n" + "[-] No Password Found" "\n")

if __name__ == "__main__":
    main()
    


    

