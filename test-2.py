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

    if(user_choice==1):
        my_name=input("Enter Your Name:")
        my_num=int(input("Enter Your 10-digit Phone Number:"))
        if(len(my_num)!= 10):
            print("Error,'The number You've entered is not accurate.'")
            my_num=int(input("Enter Your 10-digit Phone Number:"))
            
        else:
            print()
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
        del_record=input("Enter The Name You Want to Delete:")
        del my_phone_dictionary[my_name]
        print("Your Record has been Deleted.")
        print("The Remaining Record is:",sorted_dict)
    
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
     



