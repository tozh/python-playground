class Person():
    def __init__(self, _id, _name, _gender, _follower_count, _answer_count, _articles_count):
        self.id = _id
        self.name = _name
        self.gender = _gender
        self.follower_count = _follower_count
        self.answer_count = _answer_count
        self.articles_count = _articles_count
        self.count = _follower_count + _answer_count*2 + _articles_count*5
        # self.str = str({'id':self.id, 'name':self.name, 'gender':self.gender, 'count':self.count})

    def __hash__(self):
        return self.id.__hash__()

    def __eq__(self, other):
        return self.id.__eq__(other.id)

    def __gt__(self, other):
        return self.count.__gt__(other.count)

    def __ge__(self, other):
        return self.count.__ge__(other.count)

    def __lt__(self, other):
        return self.count.__lt__(other.count)

    def __le__(self, other):
        return self.count.__le__(other.count)

    # def __str__(self):
    #     return self.str


