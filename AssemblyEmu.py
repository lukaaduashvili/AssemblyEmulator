def calcNum():
    return 5

R = [0]*1064 ##registers
M = [0]*10640 ##memory

def runFile(): ##
    f = open("Assemb.s", "r")
    if f.mode == "r" : 
        AssemblyCode = f.read()
    ch = '/'
    if ch in AssemblyCode:
        AssemblyCode = AssemblyCode.replace(ch, "/"+ch)
    linebyline = AssemblyCode.splitlines()
    print(linebyline[6])
    exec(AssemblyCode)
    

def main():
    runFile()

if __name__ == "__main__" :
    main()

    
