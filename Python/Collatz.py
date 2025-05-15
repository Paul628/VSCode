def collatz(n,i):
    print(int(n))
    if n <= 0:
        print("Not a number >0")
        return 0;
    if n == 1:
        if i == 1:
            print("As you can see, this pattern will now repeat")
            return 1;
        i+=1      
    if n % 2 == 0:
        collatz(n/2,i)
    else:
        collatz(3*n+1,i)


def main():
    while 1:
        collatz(int(input("Enter number > 0 : ")),0)
        if input("Continue? y/n: ") == "n":
            break

if __name__ == "__main__":
    main()