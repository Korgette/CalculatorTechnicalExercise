'''
This is a calculator program, including Addition, Subtraction, Multiplication, Division and Conversion
The user is given descriptions of the calculators functionality as they
'''

#Flag for main function
run = True

#a dictionary for selecting operations, including their title,description and symbol
opp_dict = {"1":["addition","Please insert a second number to be added to the initial number","+"],
            "2":["subtraction", "Please enter a second number to be subtracted from the initial number","-"],
            "3":["multiplication","Please enter a second number to be multiplied by the initial number","*"],
            "4":["division", "please enter a second number to be divided by the initial number","/"],
            "5":["conversion", "please designate which conversion you would like to take place", "->"],
            "q":["quit"]}

#A list of all selected numbers for non-conversion operation (used to exclude conversion operation)
non_conv_opps = ["1","2","3","4"]

#a dictionary for selecting conversion operations, including title, units, description and ratio
conv_dict = {"1":["stone","kg","st","Kilos -> Stone",(1/6.35)],
             "2":["bytes","GB","bytes", "Gigabytes -> bytes",(10**9)],
             "3":["inches","inches","cm", "Inches -> Centimetres",(2.54)],
             "4":["days","days","s", "Days -> seconds",(86400)]}
#Options for answer editing/removal
edit_ans_options = ["1: reuse an answer", "2: delete an answer","3: abort"]

#Basic function for multiplying two numbers
def multi(n1, n2):
    return (n1 * n2)

#Basic function for addition of two numbers
def addition(n1,n2):
   return (n1 + n2)

#Basic function for subtracting a number from another
def subtraction(n1,n2):
    return (n1 - n2)

#Basic function for dividing a number by another
def division(n1, n2):
    return (n1 / n2)

#Function for displaying previous answers with their index+1
def displayAns(prev_ans):
    print('')
    print("previous answers:")
    for i in range(len(prev_ans)):
        print(f"{i+1}: {(' '.join(prev_ans[i]))}")
    print('')


#Main function for operation of calculator
def calculate():
    #Initialisation values for first function call - on first loop, there is no previous answer
    ans = 0
    prev_ans = []
    use_prev_ans = False
    #previous answer index - abbreviated due to line length
    pa_ind = 0
    print("Welcome to the calculator application" + "\n")
    #Main loop within the function
    while run == True:
        #Set flags to True - opening up answer select and edit operations upon each loop
        edit_ans = True
        ans_select = True
        print('')
        print("What operation would you like to carry out? Please press the corresponding number:")
        #Looping through opp_dict for description of each operation and how to carry out, asking user input
        for i in opp_dict:
            print(f"{i}: {opp_dict[i][0]}")
        op_choice = input()
        if op_choice == 'q':
            break
        #If there is a previous answer, use that as n1 - else, ask for user input, then display function descrip
        try:
            if use_prev_ans == False:
                num1 = float(input("Please enter the initial number you would like to be operated upon"))

            print(f"Your initial number is: {num1}")
            print(f"{opp_dict[op_choice][1]}")
            #Behaviour if conversion chosen as above - adding units to answer from conv_choice index
            if op_choice == "5":
                try:
                    for i in conv_dict:
                        print(f"{i}: {conv_dict[i][3]}")
                    conv_choice = input()
                    if conv_choice in conv_dict:
                        conv_ans = (num1 *conv_dict[conv_choice][4])
                        print(f"{num1}{conv_dict[conv_choice][1]} -> {conv_ans}{conv_dict[conv_choice][2]}")
                except:
                    print("incorrect input - please try again.")

            #If no conversion, a second input is required:
            else:
                num2 = float(input())
        except:
            print("Incorrect input - please try again.")
            continue
        #Conditionals for the other operations, assigning return of corresponding functions to ans
        try:
            if op_choice == '1':
                ans = addition(num1,num2)
            elif op_choice == '2':
                ans = subtraction(num1,num2)
            elif op_choice == '3':
                ans = multi(num1,num2)
            elif op_choice == '4':
                ans = division(num1,num2)


        except:
            print("the input was invalid: please try again")
            continue
        else:
            #If the operation is not conversion, show the user their answers with operators added in
            if op_choice in non_conv_opps:
                final_ans = (f"{num1} {opp_dict[op_choice][2]} {num2} = {ans}")
                print(final_ans)
            #If is conversion, set final_ans to the operation with units added
            else:
                final_ans = (f"{num1}{conv_dict[conv_choice][1]} -> {conv_ans}{conv_dict[conv_choice][2]}")

            #Append the answer to prev_ans list, split into nested lists
            prev_ans.append((final_ans.split()))

            #Loop for dealing with previous answers, giving the user the option to see them and edit them
            #Breaking out of the loop if 'n' is inputted, repeating this loop on incorrect input
            while ans_select == True:
                ans_choice = input("Would you like to see your previous answers? y/n")
                if ans_choice.upper() == 'Y':
                    displayAns(prev_ans)
                    ans_select = False
                elif ans_choice.upper() == 'N':
                    ans_select = False
                    use_prev_ans = False
                    break
                else:
                    "input was not correct: please try again"
                    continue

                #Loop allowing the user to edit the answers they have just accessed, asking them to choose it's index
                while edit_ans == True:
                    edit_y_n = input("Would you like to reuse/remove any of these answers? y/n")
                    if edit_y_n.upper() == 'Y':
                        ans_to_edit = int(input("Please select which answer you would like to reuse/remove"))
                        print("Please select from the below:")
                        #Loop through options for editing and their descriptions
                        for i in range(len(edit_ans_options)):
                            print(f"{edit_ans_options[i]}")
                        edit_choice = input()
                        #If the user would like to reuse, grab the index of its list and then assign it as num1
                        #num1 is stripped of its units, and then used on next loop of calculate
                        if edit_choice == "1":
                            pa_ind = ans_to_edit -1
                            num1 = prev_ans[pa_ind][-1].replace("st","").replace("bytes","").replace("cm","").replace("s","")
                            num1 = float(num1)
                            use_prev_ans = True
                            edit_ans = False
                        #If user wishes to remove, pop the chosen index
                        elif edit_choice == "2":
                            print(f"The answer at {ans_to_edit} has been deleted")
                            prev_ans.pop(ans_to_edit -1)
                            break
                        #Give the user the option to abort this operation
                        elif edit_choice == "3":
                            ans_select = False
                            break
                        else:
                            print("incorrect input: please try again")
                    #If 'n' selected, escape the edit loop so function returns to start
                    elif edit_y_n.upper() == "N":
                        ans_select = False
                        break
                    else:
                        print("incorrect input - please try again")




calculate()
