def queryUser(board, username):
    client = MongoClient('localhost', 27017)
    collection = client['Ptt'][board]

    user_record = collection.find({
        '$or'frown表情符號
            {'author.account': username},
            {'messages':{
                    '$elemMatch':{'push_userid': username}
            }}
        ]https://github.com/behappycc/ptt-clustering.git
    }).sort('date', pymongo.DESCENDING)

    for record in user_record:
        print record['article_title'], record['date']