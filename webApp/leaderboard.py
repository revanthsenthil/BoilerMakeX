import json


class Leaderboard:
    def __init__(self):
        # self.engine = create_engine(conn_string, convert_unicode=True)
        # self.sessionmaker = sessionmaker(bind=self.engine)
        # initialize json file reading
        # with open(file) as f:
        #     self.data = json.load(f)
        pass


    def get_scores(self):
        # return json scores data from json file
        with open('data.json', 'r+') as f:
            self.data = json.load(f)
            return self.data['scores']

    def add_score(self, score):
        with open('data.json', 'r+') as f:
            data = json.load(f)
            arrayData = data['scores']
            arrayData.append(score)
            print(arrayData)
        
        with open('data.json', 'w') as f:
            json.dump({"scores":arrayData}, f)

        
    def prepare_scores(self, session):
        scores = self.get_scores(session)
        scores.sort(reverse=True, key=lambda e: e.points)

        result = list(map(lambda score, i: {'id': score.id,
                                            'ranking': i + 1,
                                            'avatar': self.get_avatar_dic()[str(score.avatar)],
                                            'playername': score.playername,
                                            'points': score.points
                                            },
                        scores,
                        list(range(len(scores)))))
        return result

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
