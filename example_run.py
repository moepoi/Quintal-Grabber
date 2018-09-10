from quintal import Quintal

id = input("Quintal ID : ")
data = Quintal(id).studentinfo()
username = data[1]
name = data[2] + data[3]
email = data[4]
print ("Username : {}\nName : {}\nEmail : {}".format(str(username), str(name), str(email)))
