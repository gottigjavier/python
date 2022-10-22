# Use Python 3.x or higher interpreter for output by terminal. Otherwise rare characters may appear or throw errors of type charset = "UTF-8"

import time
from io import open

time_init = time.time()

iterations = 0
no_repetitions = True
iterations_max_control = 500000
last_position = 2020202020202020
listx3 = [1,2,3]
set_listx3 = str(listx3)

def resetListx3():
    listx3 = [1,2,3]
    set_listx3 = str(listx3)

def addElements (listx3):
    return (listx3[0] + listx3[1] + listx3[2]) % 10000 # Only the last 4 digits are used

def sortElements (listx3):
    listx3[0] = listx3[1]
    listx3[1] = listx3[2]
    listx3[2] = new_element
    return listx3

def saveArchive(set_listx3):
    archive = open("exit_listx3.txt", "w")
    archive.write("Block start repeating 16291951775 times every 124000 iterations \n")
    archive.write(set_listx3)
    archive.write("\n End of repeating block \n \n \n")
    archive.close() 


def aggregteListx3(set_listx3):
    set_listx3 = set_listx3 + str(listx3) # To include the last triad
    archive = open("exit_listx3.txt", "r+")
    archive.seek(len(archive.read()))
    archive.write("Beginning of the remaining list \n")
    archive.write(set_listx3)
    archive.write("\n End of all lists")
    archive.close()

print("This algorithm solves the following problem: \nA computer starts printing the numbers 1, 2 and 3. \nThen it continues printing without stopping the sum of the last 3 numbers it printed: 6, 11, 20, 37, 68, ... \n What are the last 4 digits of the number printed in position 2020202020202020? \nFor example, in position 30, the number 45152016 that ends in 2016 is printed.\n\n")

print("Solution ---> Start \n\n")

print("Due to the large amount of data, with current technology it is impossible to run the entire sequence because it could take thousands of years. \nBut, it is very possible that the sequence repeats. \nDepending on your equipment, this may take a couple of minutes.\n")
print("If no repetitions are found within an acceptable period, the program will stop and you can choose to extend the search range.\n")
print("-- Searching replays -- Wait please -->\n")


while no_repetitions or iterations > iterations_max_control: # The second condition is a protection in case no repetitions are found 
    iterations+=1
    new_element = addElements(listx3)
    listx3 = sortElements(listx3)
    if str(listx3) in set_listx3: # Searching of listx3 in set_listx3
        no_repetitions=False
    else:
        set_listx3= set_listx3+str(listx3) # Update set_listx3


remaining_iterations = last_position % iterations
repetitions_number = (last_position - remaining_iterations)//iterations

# If it finds repetitions before a prudent period it will enter to following "if", but it will enter to "elif" at the end of the code showing a message to extend the repetition search range. 

if not no_repetitions:
    print("\nThe cycle was found to repeat "+ str(repetitions_number)+ " times every "+ str(iterations)+ " iterations\n") 
    print("The repeated block is still too big to present on screen \nso it was saved in the file exit_listx3.txt in this same directory\n")
    print("\nContinuing with the cycle not repeated...")
    
    # Once the repeating block is found, it is saved, the next repeated blocks are discarded, the listx3 is reset to [1,2,3] and it continues until the end of the sequence. 
    
    saveArchive(set_listx3)
    resetListx3()

    for i in range(3,remaining_iterations): # It starts at 3 because the first three positions are occupied by the elements of the listx3 --> [1,2,3]
        iterations+=1
        new_element= addElements(listx3)
        listx3 = sortElements(listx3)
        set_listx3= set_listx3+str(listx3)

    aggregteListx3(set_listx3) # The final block is added that is not repeated

    print("\nThe last four digits of the sum in the position " + str(last_position) + " are: ", new_element)

    print("\nThe final block added to the archive exit_listx3.txt \n")

    time_end = time.time()

    time_elapsed = round(time_end - time_init, 0)

    print("\n The process lasted " + str(time_elapsed), " seconds.")

    print("End of program.")
elif iterations>iterations_max_control:
    print("\nRepeated cycles were not found in " + str(iterations_max_control) + " iterations.\nYou can extend the search by changing the value of the variable <iterations_max_control> in this program source code")