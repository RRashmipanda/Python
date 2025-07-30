# w mode - overwrite the file if it exists, create a new file if it does not
# a mode - append to the file if it exists, create a new file if it does not
# r mode - read the file, raises an error if the file does not exist
# w+ mode - read and write, overwriting the file if it exists, creating a new file if it does not
# r+ mode - read and write, raises an error if the file does not exist

f = open("E:/wvdv coding/Python/12_ReadingAndWritingFiles/test.txt", "r")
f_out = open("E:/wvdv coding/Python/12_ReadingAndWritingFiles/test_wc.txt", "w")

# f.write("I Love chilli chicken \n")
# f.close()
# print(f.read())
# f.close()

# count words in file
for line in f:
    tokens=line.split(' ')
    f_out.write("wordcount: " + str(len(tokens)) +'  ,  '+ line)

    # print(str(tokens))
    # print(len(tokens))

f.close()
f_out.close()


# if you dont want to use close() method, you can use with statement
with open("E:/wvdv coding/Python/12_ReadingAndWritingFiles/test.txt", "r") as f, \
     open("E:/wvdv coding/Python/12_ReadingAndWritingFiles/test_wc.txt", "w") as f_out:
    for line in f:
        tokens = line.split(' ')
        f_out.write("wordcount: " + str(len(tokens)) + '  ,  ' + line)
print(f.closed)        