def main():
    #write your code below this line

    while True:

        number = int(input("Enter a number: "))

        if number < 0:
            print("Unsuitable number")
        elif number == 0:
            break
        elif number > 0:
            print(str(number ** 2))

if __name__ == '__main__':
    main()
