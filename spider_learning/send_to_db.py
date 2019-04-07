import pymysql
from follower import Follower
config = {
          'host':'localhost',
          'port':3306,
          'user':'root',
          'password':'zt',
          'db':'zhihu',
          'charset':'utf8',
          'cursorclass':pymysql.cursors.DictCursor,
          }


def connect_db(conf):
    return pymysql.connect(**conf)


def get_cursor(connection):
    return connection.cursor()


def add_new_slb(cursor, id, name, type):
    query = "SELECT * FROM {type} WHERE id='{id}';".format(type=type, id=id)
    cursor.execute(query)
    query_result = cursor.fetchone()
    if query_result is None:
        insertion_slb = "INSERT INTO {type} (id, name, count) VALUES ('{id}', '{name}', {count});".format(type=type, id=id, name=name, count=1)
        # print(insertion)
        cursor.execute(insertion_slb)
    else:
        update = "UPDATE {type} SET count=count+1 WHERE id={id};".format(type=type, id=id)
        cursor.execute(update)

def send_f(cursor, f):
    try:
        if f.location_id == '':
            f.location_id = '00000000'
            f.location_name = '未知'
        add_new_slb(cursor, f.location_id, f.location, "locations2")

        if f.school_id == '':
            f.school_id = '00000000'
            f.school_name = '未知'
        add_new_slb(cursor, f.school_id, f.school, "schools2")

        if f.business_id == '':
            f.business_id = '00000000'
            f.business_name = '未知'
        add_new_slb(cursor, f.business_id, f.business, "business2")

        insertion = ("INSERT INTO followers2 (id, name, gender, location, location_id, school, "
                     "school_id,business,business_id,answer_count,articles_count,columns_count,"
                     "question_count,following_count,follower_count,logs_count,favorite_count,"
                     "participated_live_count,hosted_live_count,following_question_count,following_topic_count,"
                     "voteup_count,favorited_count,thanked_count,following_favlists_count,is_bind_sina) "
                     "VALUES ('{0}','{1}', {2}, '{3}', '{4}', '{5}',"
                     "'{6}','{7}', '{8}', {9}, {10}, {11},"
                     "{12}, {13}, {14}, {15}, {16}, "
                     "{17}, {18}, {19}, {20},"
                     "{21}, {22}, {23}, {24}, {25});").format(f.id, f.name, f.gender, f.location, f.location_id, f.school,
                     f.school_id,f.business,f.business_id,f.answer_count,f.articles_count,f.columns_count,
                     f.question_count,f.following_count,f.follower_count,f.logs_count,f.favorite_count,
                     f.participated_live_count,f.hosted_live_count,f.following_question_count,f.following_topic_count,
                     f.voteup_count,f.favorited_count,f.thanked_count,f.following_favlists_count,f.is_bind_sina)
        # print(insertion)
        cursor.execute(insertion)
        return True
    except Exception as err:
        print("3--" + repr(err)+": ")
        # print(insertion)
        return False

def correction(connection, cursor, type):
    if type == "location" or type == "school":
        select_from_type = "SELECT id FROM {type};".format(type=type+'s'+'2')
    else:
        select_from_type = "SELECT id FROM {type};".format(type=type+'2')
    cursor.execute(select_from_type)
    result = cursor.fetchall()
    for id_tuple in result:
        id = id_tuple["id"]
        query_in_followers = "SELECT * FROM followers2 WHERE {type}='{target}'".format(type=type+"_id", target = id)
        state = cursor.execute(query_in_followers)
        print(id +"should be: "+ str(state))
        if type == "location" or type == "school":
            update = "UPDATE {type} SET count = {state} WHERE id = '{id}'".format(type=type+'s'+'2', state=state, id=id)
        else:
            update = "UPDATE {type} SET count = {state} WHERE id = '{id}'".format(type=type+'2', state=state, id=id)
        state2 = cursor.execute(update)
        print(id + "updated.")
        connection.commit()


if __name__ == "__main__":
    conn = connect_db(config)
    cursor = get_cursor(conn)
    correction(conn, cursor, "location")
    correction(conn, cursor, "school")
    correction(conn, cursor, "business")
    # conn.commit()

