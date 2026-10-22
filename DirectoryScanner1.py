import sys
import os


def Directoryscanner(DirectoryPath):
    for FolderName,SubFolder,FileName in os.walk(DirectoryPath):
       for fname in FileName:
          print(fname)

def main():
    Border = "_"*40
    print(Border)
    print("Marvellous Automation script")

    if len(sys.argv)==2:
        if(sys.argv[1] =="--h"or sys.argv[1]=="--H"):
         print("this automation script is used to travel the directory")
         print("for better usage please check--u flag")

         print("Help")
        elif(sys.argv[1] =="--h"or sys.argv[1]=="--U"):
         print("please execute the script as")
         print("python FileName.py DirectoryName")
         print("Directory name should as path")
         
        else:
        
         DirectoryName = sys.argv[1]
         print("directory name is:",DirectoryName)
    else:
        print("invalid number of arguments")
        print("Please use--h or--u for more information")

    print(Border)
    print("thank you for using")
    print(Border)

    
        
    
if __name__ == "__main__":
    main()