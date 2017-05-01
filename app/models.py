from app import db


class User(db.Model):
    # 对于一个一对多的关系，db.relationship 字段通常是定义在“一”这一边
    # 在这种关系下，得到一个 user.posts 成员，它给出一个用户所有的 blog
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    post = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.nickname


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % self.body