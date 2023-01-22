import json


class Students:
    def __init__(self):
        # self.engine = create_engine(conn_string, convert_unicode=True)
        # self.sessionmaker = sessionmaker(bind=self.engine)
        # initialize json file reading
        # with open(file) as f:
        #     self.data = json.load(f)
        pass


    def get_student_class(self, classnum):
        students = []
        # return json scores data from json file
        with open('app.json', 'r+') as f:
            self.data = json.load(f)
            for student in self.data['students']:
                class_stud = student['classes']
                for clas in class_stud:
                    if clas['classnum'] == classnum:
                        students.append(student)
            if students:
                return students
            return False
            

    def get_student_email(self, student):
        with open('app.json', 'r+') as f:
            data = json.load(f)
            arrayData = data['scores']
            
            for stud in arrayData:
                # identify student match by email, if not found return False
                if stud['email'] == student:
                    return stud
            
            return False

    # write modify student function, that looks up the student with the email as the argument and displays all the information. It then asks the user if the information needs to be changed. If the user says yes, new fields for all data needBuddy.

    # def modify_student(self, student):
    #     with open('app.json', 'r+') as f:
    #         data = json.load(f)
    #         arrayData = data['scores']
            
    #         for stud in arrayData:
    #             # identify student match by email, if not found return False
    #             if stud['email'] == student:
    #                 return stud
            
    #         return False

        
    # def prepare_scores(self, session):
    #     scores = self.get_scores(session)
    #     scores.sort(reverse=True, key=lambda e: e.points)

    #     result = list(map(lambda score, i: {'id': score.id,
    #                                         'ranking': i + 1,
    #                                         'avatar': self.get_avatar_dic()[str(score.avatar)],
    #                                         'playername': score.playername,
    #                                         'points': score.points
    #                                         },
    #                     scores,
    #                     list(range(len(scores)))))
    #     return result

    def get_avatar_dic(self):
        return {
        "0":"not set",
        "1":"👨🏻",
        "2":"👨🏼",
        "3":"👨🏽",
        "4":"👨🏾",
        "5":"👨🏿",
        "6":"👩🏻",
        "7":"👩🏼",
        "8":"👩🏽",
        "9":"👩🏾",
        "10":"👩🏿"
        }
