import sys

def main():

    if len(sys.argv)==2:
        if(sys.argv[1] =="--h"or sys.argv[1]== "--H"):
         print('this automation script is used to travel the directory')
         print('Help:This script is used for automation tasks.Use --u for usage in instructions.')

        elif(sys.argv[1] =="--u" or sys.argv[1]=="--U"):
         print('usage: python automations.py --Directoryname <directory_name> --d <directory_path>')
         print('please exicute the script as ')
         print('python filename.py Directoryname')
         print("Directory name should be absolute path")
        else:
         DirectoryName = sys.argv[1]     #takes first file name as input
         print('directory name is:',DirectoryName)
    else:
        print('invalid number of arguments')
        print(' use--u for usage or--h for help')

    print(len(sys.argv))

    
        
    
if __name__ == "__main__":
    main()