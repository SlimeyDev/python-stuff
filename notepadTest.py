def main():
    f= open("test.txt","w+")

    for i in range(10):
        f.write("hey"+"yo"+"\n")

if __name__=="__main__":
    main()