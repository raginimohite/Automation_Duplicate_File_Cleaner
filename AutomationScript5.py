import sys

def main():
    print("-----------------------------------")
    print("Marvellous Automation script")
    print("-----------------------------------")

    if(len(sys.argv) ==2):
        if(sys.argv[1 ]=="--h"or sys.argv[1 ]=="--H" ):
            print("This automation script is used to travel directory")
            print("for better usage please check --u flag")
            print("help")
        elif(sys.argv[1]=="--u" or sys.argv[1 ]=="--U"):
            print("please execute the scropt as")
            print("python FileName.py DirectoryName")
            print("DirectoryName should be absolute path")
        else:

          DirectoryName = sys.argv[1]
        print("Directory name is:",DirectoryName)
    
    else:
        print("Invalid number of arguments")
        print("please use --h or --u for more information")

    print("-----------------------------------")
    print("Thank you for using marvellous Automation script")
    print("-----------------------------------")    
    
    
    
if __name__=="main_":
    main()