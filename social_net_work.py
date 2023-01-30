class AdminLoing:

    def __init__(self):
        # makes the input into a string
        self.userId: str = input("enter your user id")
        self.passwordId: str = input("enter your password id")
        self.filename: str = input("enter the file name")
        try:
            # makes the list input into a interger
         self.accessADMIN = int(input("{0}yes or {1}no"))
        except ValueError:
            print("only a interger given thank you")

    def admin_fileCheck(self):

            # Check if userId has been inputted
            while len(self.userId) <= 0:  # If userId has not been inputted
                self.userId  # Prompt user to input userId
            # Check if passwordId has been inputted
                if len(self.passwordId) <= 0:  # If passwordId has not been inputted
                 self.passwordId  # Prompt user to input passwordId
            # If userId and passwordId are not equal to "admin" and "password" respectively
            if self.userId != "admin" and self.passwordId != "password":
                self.userId  # Prompt user to input userId
                self.passwordId  # Prompt user to input passwordId

            # If userId and passwordId are equal to "admin" and "password" respectively
            elif self.userId == "admin" and self.passwordId == "password":
                print(
                    "would you like to access the admin file and enter the file name")  # Ask user if they want to access the admin file
                self.filename  # Input filename
                self.accessADMIN  # Input accessADMIN
                # If accessADMIN is equal to 0
                if self.accessADMIN == 0:
                    try:
                        # Open the file with the specified filename and read its contents
                        adminfile = open(self.filename, "r")
                        print(adminfile.read())
                        adminfile.close()

                    except FileNotFoundError:  # If the file does not exist
                        print("file not found")
                        self.accessADMIN  # Prompt user to input accessADMIN
                        # Open the file with the specified filename and read its contents
                        adminfile = open(self.filename, "r")
                        print(adminfile.read())
                        adminfile.close()
                # If accessADMIN is not equal to 0
                else:
                    exit()  # Exit the program.


class UserRecomendation:
             def __init__(self, filename):
                    self.filename = filename

             def user_recommdation(self):
                    # Open the file "1.txt" in read mode
                    my_file = open(self.filename, "r")

                    # Read the contents of the file
                    data = my_file.read()

                    # Split the data into a list using newline as the delimiter
                    data_into_list = data.split("\n")

                    itemselectedlisappend = []
                    for i in data_into_list:
                        itemselectedlisappend.append(i)

                    # Assign the first, second, and third elements of the list to separate variables
                    list1 = data_into_list[0]
                    list2 = data_into_list[1]
                    list3 = data_into_list[2]
                    list4 = data_into_list[3]
                    list5 = data_into_list[4]
                    list6 = data_into_list[5]
                    list7 = data_into_list[6]
                    number_amount = len(data_into_list)
                    reseting_theAccepets = int(number_amount) - 1

                    print(reseting_theAccepets)
                    # Concatenate the three user you want to check list{} lists and assign to a new variable
                    selected_list = list1 + list2 + list3 + list4 + list5 + list6 + list7

                    # Create an empty list to store the recommended users
                    listofsugetedUser = []

                    # Iterate over the selected list
                    for user in data_into_list:
                        # If the user is not already in the list of recommended users, add it
                        if user != listofsugetedUser:
                            listofsugetedUser.append(user)

                    # Print the list of recommended users
                    data_into_list = tuple(listofsugetedUser)

                    # Tuple displays the users in the networks connections

                    result_listofsugetedUser = str(
                        data_into_list)  # cahnges the infromation found from a list to a string
                    result_listofsugetedUser1 = result_listofsugetedUser.split('(')[1].split(')')[
                        0]  # formates the string

                    # gives you the recommed set for the user  given to diffrent users freind list
                    # which user would you like to screach up prompt
                    # this gives you all poissble recomendation a user can get
                    #  make a input to ask the  users  which list they want to use and then  get the information and  replace list5 from below input("")
                    get_user_input = int(input(
                        f"what is the user  you want to look up range 0 to {reseting_theAccepets}"))  # get the input  for the user


                    try:
                        # get the users input and checks if in range
                        users_first_Pick = data_into_list[get_user_input]
                    except IndexError:
                        print("only a interger in the given  range thank you")
                    counter = -1
                    newlist = []

                    for i in data_into_list:

                        newlist.append(i)
                        output_formater = set(users_first_Pick).symmetric_difference(set(newlist[counter]))
                        if output_formater:
                            output_formater = {int(x) for x in output_formater}
                            print(counter + 1, "---->", str(output_formater))
                        else:
                            print(counter + 1, "NONE ")
                        counter += 1
                    loop_over_functionInputs = str(
                        input("would you like to  check a persons recommaned mates yes or no  "))
                    while loop_over_functionInputs == "yes":
                        try:
                            get_user_input = int(
                                input(
                                    f"what is the user  you want to look up range 0:{reseting_theAccepets}"))  # get the input  for the user
                            users_first_Pick = data_into_list[
                                get_user_input]  # uses the input to navigater throug out the list
                            final_output_Reccomation = set(users_first_Pick).symmetric_difference(
                                set(selected_list))  # finds the diffrencresss
                            final_output_str = ", ".join(
                                final_output_Reccomation)  # stripps and formates the whole text given
                            print(
                                f" the user recomation for user {get_user_input}" + "are" + " " + final_output_str)  # output to users after\
                            loop_over_functionInputs = str(
                                input("would you like to  check another person yes or No "))
                        except IndexError:
                            print("not right noww boyyyyy")

             def user_with_least_friends(self):
                 # Open the file "1.txt" in read mode
                 my_file = open(self.filename, "r")

                 # Read the contents of the file
                 data = my_file.read()

                 # Split the data into a list using newline as the delimiter
                 data_into_list = data.split("\n")

                 # Create a dictionary to store the number of friends for each user
                 friends_count = {}

                 # Iterate over the list of users
                 for user in data_into_list:
                     # Split the user's friends list into separate elements
                     friends = user.split(",")

                     # Count the number of friends and store it in the dictionary
                     friends_count[user] = len(friends)

                 # Find the user with the smallest number of friends
                 least_friends = min(friends_count.values())
                 least_friend_user = [k for k, v in friends_count.items() if v == least_friends]

                 # Get the name of the user with the least friends
                 least_friend_name = least_friend_user[0]

                 # Find the index of the user with the least friends
                 index = data_into_list.index(least_friend_name)

                 # Print the result
                 print(f"The user with the least number of friends is: {index} with {least_friends} friends.")
                 print(f"The index of the user with the least number of friends is: {index}")

                 # Close the file
                 my_file.close()

p1 = AdminLoing()
p1.admin_fileCheck()
p2 = UserRecomendation("1.txt")
p2.user_recommdation()
p2.user_with_least_friends()
