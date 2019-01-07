import requests
import sys

try:
    import ujson as json
except:
    import json

'''
Author : Moe Poi <moepoi@protonmail.com>
License MIT
'''

class QuintalGrabber:

    def __init__(self, id):
        self.host = "https://quintal.id"
        self.id = id

    def get_data(self, query=None):
        endpoint = "/id/api/initial_data/{}/?format=json".format(str(self.id))
        try:
            req = requests.get(self.host + endpoint)
            data = json.loads(req.text)
        except:
            print ("Invalid ID")
            sys.exit()
        x = {
            "lastlogin": data["student_class_semester"]["profile"]["user"]["last_login"],
            "username": data["student_class_semester"]["profile"]["user"]["username"],
            "firstname": data["student_class_semester"]["profile"]["user"]["first_name"],
            "lastname": data["student_class_semester"]["profile"]["user"]["last_name"],
            "email": data["student_class_semester"]["profile"]["user"]["email"],
            "gender": data["student_class_semester"]["profile"]["gender"],
            "phonenumber": data["student_class_semester"]["profile"]["mobile_no"],
            "address": data["student_class_semester"]["profile"]["address"],
            "city": data["student_class_semester"]["profile"]["city"],
            "province": data["student_class_semester"]["profile"]["province"],
            "country": data["student_class_semester"]["profile"]["country"],
            "profilephoto": self.host + data["student_class_semester"]["profile"]["profile_photo"],
            "birthdate": data["student_class_semester"]["profile"]["birth_date"],
            "sectionname": data["student_class_semester"]["section_name"],
            "gradename": data["student_class_semester"]["grade_name"],
            "classname": data["student_class_semester"]["class_name"],
            "i_fullname": data["student_class_semester"]["profile"]["institution"]["full_name"],
            "i_shortname": data["student_class_semester"]["profile"]["institution"]["short_name"],
            "i_address": data["student_class_semester"]["profile"]["institution"]["address"],
            "i_city": data["student_class_semester"]["profile"]["institution"]["city"],
            "i_province": data["student_class_semester"]["profile"]["institution"]["province"],
            "i_country": data["student_class_semester"]["profile"]["institution"]["country"],
            "i_logo": self.host + data["student_class_semester"]["profile"]["institution"]["logo"],
            "i_domain": data["student_class_semester"]["profile"]["institution"]["sch_domain"]
        }
        if query is None:
            return(x)
        else:
            try:
                xm = x["{}".format(str(query))]
                return (xm)
            except Exception as e:
                xm = "type {} not found".format(str(query))
                return (xm)
