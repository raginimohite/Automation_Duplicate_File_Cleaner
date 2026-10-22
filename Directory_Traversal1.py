import os

def main():
    for FolderName,subfolder,FileName in os.walk("Marvellous"):
        print("FolderName:",FolderName)

        for subf in subfolder:
            print("subfolder name:",subf)

        for fname in FileName:
            print("File name:",fname)

if __name__ == "__main__":
    main()