import os 

def main(): 
    i = 0 

    path = input("Enter the path of the files you'd like to rename: ")

    for filename in os.listdir(path): 
        dest = "image" + str(i) + "jpg"
        source = path + filename 
        dest = path + dest
        os.rename(source, dest)
        i += 1

if __name__ == '__main__':
    main()