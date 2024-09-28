from config import db

class Challenge(db.Model):
    __tablename__ = 'challenges'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    steps = db.relationship('Step', backref='challenge', lazy=True)

class Step(db.Model):
    __tablename__ = 'steps'
    
    id = db.Column(db.Integer, primary_key=True)
    challenge_id = db.Column(db.Integer, db.ForeignKey('challenges.id'), nullable=False)
    order = db.Column(db.Integer, nullable=False)  # Ordem da etapa no desafio
    content = db.Column(db.Text, nullable=False)  # Conteúdo da etapa (ex: perguntas, instruções)
    is_completed = db.Column(db.Boolean, default=False)  # Status de conclusão da etapa
    
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    repeat_password = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(100), nullable=False)
    short_biography = db.Column(db.Text, nullable=False)
    
