from datetime import datetime

from application import db


class Trial(db.Model):
    """A case for a participant with a particular session.
    There might be cases for a single participant having multiple sessions."""
    participant = db.Column(db.Integer, primary_key=True)
    session = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=datetime.today())
    ratings = db.relationship("Rating", backref='trial', lazy=True)

    def __repr__(self):     # pragma: no cover
        return f"<Trial {self.participant}, {self.session}>"


class Rating(db.Model):
    """A rating for a particular image in a trial."""
    participant_id = db.Column(db.Integer, primary_key=True, nullable=False)
    session_id = db.Column(db.Integer, primary_key=True, nullable=False)
    image = db.Column(db.String(16), primary_key=True, nullable=False)
    rating = db.Column(db.Integer, nullable=False)

    __table_args__ = (db.ForeignKeyConstraint(
        [participant_id, session_id], [Trial.participant, Trial.session]), {})

    def __repr__(self):     # pragma: no cover
        return f'<Rating {self.image}, {self.rating}>'
