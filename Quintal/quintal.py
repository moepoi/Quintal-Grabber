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
        self.id = str(id)
        self.endpoint = "/id/api/initial_data/{}/?format=json".format(self.id)
        try:
            self.req = requests.get(self.host + self.endpoint)
            self.data = json.loads(self.req.text)
        except:
            print ("Invalid ID")
            sys.exit()

    def get_identity(self):
        res = self.data["student_class_semester"]
        return res
    
    def get_event(self):
        res = self.data["event_users"]
        return res
    
    def get_payment(self):
        res = self.data["payments"]
        return res
    
    def get_assignment(self):
        res = self.data["assignment_class_semester_subject_submissions"]
        return res
    
    def get_test(self):
        res = self.data["test_class_semester_subject_submissions"]
        return res
        
    def get_settings(self):
        res = self.data["section_settings"]
        return res
    
    def get_subjects(self):
        res = self.data["student_class_semester_subjects"]
        return res
    
    def get_materials(self):
        res = self.data["materials"]
        return res
    
    def get_announcements(self):
        res = self.data["announcement_users"]
        return res
    
    def get_schedule(self):
        res = self.data["class_timetable_periods"]
        return res