from datetime import datetime

# from sqlalchemy import UniqueConstraint

from application import db


class Trial(db.Model):
    """A case for a participant with a particular session.
    There might be cases for a single participant having multiple sessions."""
    participant = db.Column(db.Integer, primary_key=True)
    session = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=datetime.today())
    ratings = db.relationship("Rating", backref='trial', lazy=True)
    # __table_args__ = (UniqueConstraint('participant', 'session',
    #                                    name='_participant_session_uc'), )

    def __repr__(self):     # pragma: no cover
        return f"<Trial {self.participant}, {self.session}>"


class Rating(db.Model):
    """A rating for a particular image in a trial."""
    participant_id = db.Column(db.Integer, #db.ForeignKey('trial.participant'),
                               primary_key=True, nullable=False)
    session_id = db.Column(db.Integer, #db.ForeignKey('trial.session'),
                           primary_key=True, nullable=False)
    image = db.Column(db.String(16), primary_key=True, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    # participant = db.relationship('Trial', backref='trial_participant',
    #                               foreign_keys=participant_id)
    # session = db.relationship('Trial', backref='trial_session',
    #                           foreign_keys=session_id)
    # __table_args__ = (UniqueConstraint('participant_id', 'session_id', 'image',
    #                                    name='_participant_session_uc'), )
    __table_args__ = (db.ForeignKeyConstraint(
        [participant_id, session_id], [Trial.participant, Trial.session]), {})
    def __repr__(self):     # pragma: no cover
        return f'<Rating {self.image}, {self.rating}>'
