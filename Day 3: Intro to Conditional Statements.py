
if __name__ == '__main__':
    N = int(input())

    if (N % 2) != 0:
        print("Weird")
    else:
        if (2 <= N) and (N <= 5):
            print("Not Weird")
        elif (6 <= N) and (N <= 20):
            print("Weird")
        else:
            print("Not Weird")
