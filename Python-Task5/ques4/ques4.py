# QUESTION4
# Python program to demonstrate writing to file

try:
    # opening the file in writing mode
    with open("text1.txt", 'w') as file1:

        string1 = "Hello\n"
        string2 = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
  
        # Writing a string to file 
        file1.write(string1) 
  
        # Writing multiple strings at a time 
        file1.writelines(string2)

    # opening the file in reading mode
    with open("text1.txt", 'r') as file2:
        #Printing the content that was added to the file
        for fileLine in file2:
            print(fileLine,end = "")

except:
    print("File not found")

 
  
