import requests
import random


class APIComunicator(object):
    DEFAULT_URL = 'https://hackbulgaria.com/api/students'

    def __init__(self):
        self.connection_state = False
        self.response = None

    def connect(self, url='None'):
        if url == 'None':
            request = requests.get(APIComunicator.DEFAULT_URL, verify=False)
        else:
            request = requests.get(url, verify=False)

        if request.status_code == 200:
            self.response = request.json()
            self.connection_state = True
        else:
            self.connection_state = False
            print('Somthig went wrong')

    def list_courses(self):

        self.courses_list = []
        for course in self.response:
            for i in range(len(course['courses'])):
                if course['courses'][i]['name'] not in self.courses_list:
                    self.courses_list.append(course['courses'][i]['name'])
                else:
                    continue
        self.courses_list = sorted(self.courses_list)
        print('Here are the courses:')
        for index, course in enumerate((self.courses_list)):
            print("[" + str(index+1) + "] " + course)

    def match_teams(self, course_id, team_size, group_time):
        courses = self.courses_list
        peoples = self.response
        course_id = course_id-1
        team = 0
        print('=========================')
        for people in peoples:
            if not people['available']:
                continue
            else:
                for pepole_courses in people['courses']:
                    if pepole_courses['name'] != courses[course_id]:
                        continue
                    else:
                        print(people['name'])
                        team += 1
                        if team == team_size:
                            print('=========================')
                            team = 0

    def help(self):
        print("\tYou can use one the the following commands:\n"
              "\tlist_courses - this lists all the courses" +
              "that are available now.\n"
              "\tmatch_teams <course_id>, <team_size>, <group_time>\n"
              "\tquit - to exit")


def main():
    a = APIComunicator()
    a.help()
    while True:
        decision = input('Enter a command# ')
        params = decision.split()
        if len(params) == 1 and params[0].startswith('list'):
            if not a.connection_state:
                a.connect()
            a.list_courses()
        elif len(params) == 4 and params[0] == 'match_teams':
            if not a.connection_state:
                print("First is suposed to load lis")
                a.help()
            a.match_teams(int(params[1]), int(params[2]), int(params[3]))
        elif params[0].lower() == 'quit':
            exit()
        else:
            a.help()

if __name__ == '__main__':
    main()
