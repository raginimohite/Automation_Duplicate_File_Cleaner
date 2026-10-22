import sys

def main():

    if len(sys.argv)==2:
        if(sys.argv[1] =="--h"):
         print("Help")
        elif(sys.argv[1] =="--h"):
         print("Usage")
        else:
        
         DirectoryName = sys.argv[1]
         print("directory name is:",DirectoryName)
    else:
        print("invalid number of arguments")
        print("Please use--h or--h more information")

    
        
    
if __name__ == "__main__":
    main()