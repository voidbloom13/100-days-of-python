def main():
    i = 0
    while i <= 100:
        i+=1
        if i%3==0 and i%5==0:
            print(f"{i} fizz buzz")
        elif i%3==0:
            print(f"{i} fizz")
        elif i%5==0:
            print(f"{i} buzz")
        else:
            print(i)
    else:
        print("finished")

if __name__ == "__main__":
    main()
