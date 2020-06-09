#! /usr/bin/env python3
# UTF-8
# handler.py

from random import randrange

def main():
    number = randrange(100)
    while True:
        try:
            guess = int(input("? "))
        except:
            continue
        if guess == number:
            print("You win!")
            break

if __name__ == '__main__':
    main()