
class Student:
    def __init__(self):
        self.score_list = []

    def add_score(self, score):
        self.score_list.append(score)

    def average_score(self):
        if not self.score_list:
            return 0
        return sum(self.score_list) / len(self.score_list)

    def max_min_score(self):
        if not self.score_list:
            return None, None
        return max(self.score_list), min(self.score_list)
