def print_vector_as_pic(vector,cols):
    i = 0
    while i< len(vector):
        if i%cols==0:
            print("")
        print("█" if vector[i] else " ",end="")
        i+=1
    print("")

def choose(text_file,cols,rows,min_dots):
    file = open(text_file,"w")
    import itertools as it
    for x in it.product([0,1],repeat=cols*rows):
        if x.count(1)>min_dots:
            print_vector_as_pic(x,cols)
            print("Category:")
            key = input()
            if key.isdigit() and int(key) > 0:
                s = "{"+" ".join((str(element) for element in x))+"}"
                file.write("{0}={1}".format(s,key))
                print("Accepted")
            elif key.isdigit() and int(key) == -2:
                print("Exiting")
                break
            else:
                pass
    file.close()

if __name__ == '__main__':
    choose("test.txt",5,5,5)



