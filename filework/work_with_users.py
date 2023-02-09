def read_user_data():
    with open("users.txt", "r") as usersFile:
        usersData = usersFile.readlines()

    return usersData


def write_user_data(usersData):
    with open("users.txt", "w") as usersFile:
        usersFile.writelines(usersData)


# def change_user_data(usn, requests):  # USN - User String Number
#     usersData = read_user_data()  # data[0] = "UserNickName;user_id;userFirstName;userLastName;"
#     usn_list = usersData[usn].split(";")
#     usn_list[-1] = requests
#
#     usersData[usn] = ""
#     for i in usn_list:
#         usersData[usn] += i + ";"
#     usersData[usn] += "\n"
#
#     write_user_data(usersData)


def get_users_list():
    usersData = read_user_data()
    users = dict()

    count = 1
    for i in usersData:
        userData = i.split(";")
        users[userData[1]] = count

    return users


def set_new_user(*userData):
    userStr = str()
    for i in userData:
        userStr += i + ";"
    with open("users.txt", "a") as usersFile:
        usersFile.write(userStr)
