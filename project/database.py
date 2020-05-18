from project import db


class question_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_name = db.Column(db.String(45), unique=True, nullable=False)
    question_description = db.Column(db.String(45), unique=False, nullable=False)
    CreateUser = db.Column(db.String(45), unique=False, nullable=False)
    game_infos = db.RelationshipProperty('game_info', backref=db.backref('question_info', lazy=True),
                                         cascade='all, delete-orphan')

    def __repr__(self):
        return f"game_info('{self.id}','{self.question_name}','{self.question_description}')"


class game_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_name = db.Column(db.String(45), unique=True, nullable=False)
    game_description = db.Column(db.String(45), unique=False, nullable=False)
    game_belong = db.Column(db.Integer(), db.ForeignKey('question_info.id', ondelete='CASCADE'), nullable=False)
    user = db.Column(db.String(45), unique=False, nullable=False)
    Tickets = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f"game_info('{self.game_name}', '{self.game_description}','{self.game_belong}' ,'{self.user}', '{self.Tickets}')"


class user_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_account = db.Column(db.String(45), unique=True, nullable=False)
    user_password = db.Column(db.String(45), unique=False, nullable=False)
    user_name = db.Column(db.String(45), unique=True, nullable=False)

    def __repr__(self):
        return f"game_info('{self.user_account}', '{self.user_name}')"


class voted_info(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    game_name = db.Column(db.String(45), unique=False, nullable=False)

    def __repr__(self):
        return f"game_info('{self.game_name}')"


class log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_account = db.Column(db.String(45), unique=False, nullable=False)
    game_name = db.Column(db.String(45), unique=False, nullable=False)
    time = db.Column(db.String(45), unique=False, nullable=False)

    def __repr__(self):
        return f"game_info('{self.user_account}', '{self.game_name}', '{self.time}')"
