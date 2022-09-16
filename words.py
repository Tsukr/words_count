import classes as c
import os 

def main():
    a = c.Words(menu())
    print(a.bild_dict())
    input('Press Enter to exit')

def open_file():
    while True:
        print('Input "exit" for close')
        NameFile = input('Name file: ')
        if NameFile == 'exit':
            exit()
        if os.path.exists(NameFile):
            file = open(NameFile, 'r', encoding='utf-8')
            break    
        else:
            print('File don\'t exsists')    
    return file.read()

def menu():
    print("Hello! This program counts word:\nPress 1 to open file in directory\nPress 2 to write string\nPress 3 to exit ")
    while True:
        q = input()
        if q == '1':
            some_text = open_file()
            break
        elif q == '2':
            some_text = input('Your string: ')
            break
        elif q == '3':
            input('Bue!')
            exit()
        else:
            print('Wrong enter')
    return some_text


    
if __name__ == "__main__":
    main()