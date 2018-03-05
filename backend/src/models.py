from datetime import datetime
from . import db


class Trial(db.Model):
    """A case for a participant with a particular session.
    There might be cases for a single participant having multiple sessions."""
    participant = db.Column(db.Integer, primary_key=True)
    session = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=datetime.today())


    def __repr__(self):
        return f'<Participant {self.participant}, Session {self.session}>'

    def get_id(self):
        return self.id
