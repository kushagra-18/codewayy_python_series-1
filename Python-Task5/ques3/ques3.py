# QUESTION3
# READING FROM A FILE AND PRINTING ITS CONTENT

try:
    # opening text.txt file
    with open("text.txt", 'r') as file1:
        # Iterating to print the content of the file
        for fileLine in file1:
            print(fileLine, end = "")
except:
    print("File not found")
