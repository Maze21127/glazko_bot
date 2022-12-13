from app import db


class Message(db.Model):
    __tablename__ = 'message'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    text = db.Column(db.String(4096), nullable=False)

    def __repr__(self):
        return f"{self.id}\n{self.title}\n{self.text}"
