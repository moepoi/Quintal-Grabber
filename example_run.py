from quintal import Quintal

id = input("Quintal ID : ")
data = Quintal(id).studentinfo()
username = data[1]
name = data[2] + data[3]
email = data[4]
address = data[7]
profilephoto = data[11]
grade = data[14]
print ("Username : {}\nName : {}\nEmail : {}\nAddress : {}\nClass : {}\nProfile photo : {}".format(str(username), str(name), str(email), str(address), str(grade), str(profilephoto)))
