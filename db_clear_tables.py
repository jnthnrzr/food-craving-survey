from application import db
from application.models import Image, Rating, Trial


def clear_trial_from_db():          # pragma: no cover
    Trial.query.delete()
    db.session.commit()


def clear_rating_from_db():         # pragma: no cover
    Rating.query.delete()
    db.session.commit()


def clear_images_from_db():         # pragma: no cover
    Image.query.delete()
    db.session.commit()


def clear_all_tables_from_db():     # pragma: no cover
    clear_rating_from_db()
    clear_trial_from_db()
    clear_images_from_db()


if __name__ == "__main__":
    clear_all_tables_from_db()