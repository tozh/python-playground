from pymongo import MongoClient
from firstApp.person import Person
import json

class Query():

    def __init__(self, _id, _client):
        self.id = _id
        self.db = _client.zhihu
        self.user = self.db.users.find({'_id':self.id})
        self.person = Person(self.user['_id'], self.user['name'], self.user['gender'], self.user['follower_count'], self.user['answer_count'], self.user['articles_count'])

        followers_list = []
        for f in self.user['followers']:
            p = Person(f['_id'], f['name'], f['gender'], f['follower_count'], f['answer_count'], f['articles_count'])
            followers_list.append(p)
        self.followers = set(followers_list)

        followees_list = []
        for f in self.user['followees']:
            p = Person(f['_id'], f['name'], f['gender'], f['follower_count'], f['answer_count'], f['articles_count'])
            followees_list.append(p)
        self.followees = set(followees_list)

        self.r_friend = self.followees & self.followers

        self.total = self.followees | self.followers

    def get_person(self):
        return self.person

    def get_user_info(self):
        return self.user

    def get_followers(self):
        return self.followers

    def get_followees(self):
        return self.followees

    def get_r_friend(self):
        return self.r_friend

    def relations(self):
        relation_list = []
        for p in self.total:
            if p in self.r_friend:
                relation_list.append({'self':self.person.__dict__, 'r_friend':p.__dict__})
            elif p in self.followers:
                relation_list.append({'self':self.person.__dict__, 'followed_by':p.__dict__})
            elif p in self.followees:
                relation_list.append({'self':p.__dict__, 'followed_by':self.person.__dict__})
        return relation_list

    '''
        followers -> me, followees -> me
        what relations inner followers and followees 
    '''
    def inner_relations(self):
        inner_relation_list = []
        total_list = list(self.total)

        for i in range(len(total_list)):
            for j in range(i+1, len(total_list)):
                if total_list[j] in total_list[i].r_friend:
                    inner_relation_list.append({'self':total_list[i].__dict__, 'r_friend':total_list[j].__dict__})
                elif total_list[j] in total_list[i].followers:
                    inner_relation_list.append({'self':total_list[i].__dict__, 'followed_by':total_list[j].__dict__})
                elif total_list[j] in total_list[i].followees:
                    inner_relation_list.append({'self':total_list[j].__dict__, 'followed_by':total_list[i].__dict__})
        return inner_relation_list

    '''
        me -> other ?, other -> me?
    '''
    def relation_to_someone(self, other):
        if other in self.r_friend:
            return 3
        elif other in self.followers:
            return 1
        elif other in self.followees:
            return 2
        else:
            return 0

    def common_followers(self, other):
        return self.followers & other.followers

    def common_followees(self, other):
        return self.followees & other.followees

    def common_friends(self, other):
        return self.r_friend & other.r_friend

    '''
        me -> intermedia -> other
    '''
    def intermedia_to_follow(self, other):
        return self.followees & other.followers

    '''
        other -> intermedia -> me
    '''
    def intermedia_to_be_followed_by(self, other):
        return other.followees & self.followers

    def most_followed_by_my_followees(self):

        return set([])

    def most_followed_by_my_followers(self):

        return set([])

    def to_json(self):
        r_friend_list = [p.__dict__ for p in self.r_friend]
        followers_list = [p.__dict__ for p in self.followers]
        followees_list = [p.__dict__ for p in self.followees]
        json_dict = {'self': self.person.__dict__,
                     'r_friend': r_friend_list,
                     'followers': followers_list,
                     'followees': followees_list,
                     'relations': self.relations(),
                     'inner_relations': self.inner_relations()}
        return json.dumps(json_dict, ensure_ascii = False)




