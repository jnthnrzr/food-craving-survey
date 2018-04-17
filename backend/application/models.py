from datetime import datetime
from application import db


class Trial(db.Model):
    """A case for a participant with a particular session.
    There might be cases for a single participant having multiple sessions."""
    participant = db.Column(db.Integer, primary_key=True)
    session = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=datetime.today())
    # ratings = db.relationship("Rating", backref="trial", lazy="dynamic")

    def __repr__(self):     # pragma: no cover
        return f"<Trial {self.participant}, {self.session}>"
