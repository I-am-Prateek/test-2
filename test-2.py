#Student Name: Pratik Shrestha and Student Id:23026137
#Creating an empty dictionary and printing the menu for Grann's Phopne directory
my_phone_dictionary={}
print ("""
WELCOME TO THE GRANN'S PHONE DIRECTORY
    1.Add a record
    2.Search a record
    3.Update a record
    4.Sort the record alphabetically
    5.Delete a record
    6.Quit
    """)
user_choice=int(input("Enter Your Choice:"))

while(user_choice!=6):
#applyin the necessary conditions according to the question
    if(user_choice==1):
        my_name=input("Enter Your Name:")
        if (my_name.isalpha()):
            print()
        else:
            print("Error, Please enter the string value")
            my_name=input("Enter Your Name:")
        my_num=input("Enter Your 10-digit Phone Number:")    
        if (my_num.isdigit() and len(my_num) == 10):                #if the user add string or more and less number then it will show error else add the record
            print()
            
            if my_name in my_phone_dictionary:
                update_num = input("Same name already exists. Do you want to update the number? (Y/N):").lower()
                if update_num == 'Y':
                    num_new=int(input("Enter Your New Number:"))
                    print(my_name,"'s number has been updated")
                else:
                    print() 


        else:
            print("Error,'The number You've entered is not accurate.'")
            my_num=int(input("Enter Your 10-digit Phone Number:"))
        my_phone_dictionary[my_name] = my_num 
        print("Your Record Has been Added")


    elif(user_choice==2):
        search_name=input("Enter the Name You want to search:")
        if(search_name in my_phone_dictionary):
            print(search_name,"=",my_phone_dictionary[search_name])
        else:
            print("This Name You've Entered is not in the Directory")


    elif(user_choice==3):
        my_name=input("Enter Your Name:")
        new_num=int(input("Enter Your New Number:"))
        my_phone_dictionary[my_name] = new_num


    elif(user_choice==4):
        sorted_dict=dict(sorted(my_phone_dictionary.items()))
        print("The Sorted Record is:",sorted_dict)

    elif(user_choice==5):
        del_record=input("Enter The Name You Want to Delete:")       #this code will delete the data according to the user input and print the remaining dictionary
        del my_phone_dictionary[my_name]
        print("Your Record has been Deleted.")
        print(my_phone_dictionary)
    
    elif(user_choice==5):
        print()

    print ("""
WELCOME TO THE GRANN'S PHONE DIRECTORY
    1.Add a record
    2.Search a record
    3.Update a record
    4.Sort the record alphabetically
    5.Delete a record
    6.Quit
    """)
    user_choice=int(input("Enter Your Choice:"))
     



