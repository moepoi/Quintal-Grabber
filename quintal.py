import requests as rq
import json

class Quintal(object):

    def __init__(self, id):
        self.host = "https://quintal.id"
        self.id = id

    def studentinfo(self):
        endpoint = "/id/api/initial_data/{}/?format=json".format(str(self.id))
        req = rq.get(self.host + endpoint)
        data = json.loads(req.text)
        lastlogin = data["student_class_semester"]["profile"]["user"]["last_login"]
        username = data["student_class_semester"]["profile"]["user"]["username"]
        firstname = data["student_class_semester"]["profile"]["user"]["first_name"]
        lastname = data["student_class_semester"]["profile"]["user"]["last_name"]
        email = data["student_class_semester"]["profile"]["user"]["email"]
        gender = data["student_class_semester"]["profile"]["gender"]
        phonenumber = data["student_class_semester"]["profile"]["mobile_no"]
        address = data["student_class_semester"]["profile"]["address"]
        city = data["student_class_semester"]["profile"]["city"]
        province = data["student_class_semester"]["profile"]["province"]
        country = data["student_class_semester"]["profile"]["country"]
        profilephoto = self.host + data["student_class_semester"]["profile"]["profile_photo"]
        birthdate = data["student_class_semester"]["profile"]["birth_date"]
        sectionname = data["student_class_semester"]["section_name"]
        gradename = data["student_class_semester"]["grade_name"]
        classname = data["student_class_semester"]["class_name"]
        i_fullname = data["student_class_semester"]["profile"]["institution"]["full_name"]
        i_shortname = data["student_class_semester"]["profile"]["institution"]["short_name"]
        i_address = data["student_class_semester"]["profile"]["institution"]["address"]
        i_city = data["student_class_semester"]["profile"]["institution"]["city"]
        i_province = data["student_class_semester"]["profile"]["institution"]["province"]
        i_country = data["student_class_semester"]["profile"]["institution"]["country"]
        i_logo = self.host + data["student_class_semester"]["profile"]["institution"]["logo"]
        i_domain = data["student_class_semester"]["profile"]["institution"]["sch_domain"]
        return (lastlogin, username, firstname, lastname, email, gender, phonenumber, address, city, province, country, profilephoto, birthdate, sectionname, gradename, classname, i_fullname, i_shortname, i_address, i_city, i_province, i_country, i_logo, i_domain)
