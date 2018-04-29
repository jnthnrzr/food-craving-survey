import os
from application.config import basedir
from application.models import Image
from application import db


def add_images_to_db():         # pragma: no cover
    """Programmatically add images to database from images directory."""
    path = os.path.join(basedir, "static/images")

    for i, filename in enumerate(os.listdir(path)):
        if filename.endswith(".jpg"):
            img = Image(id=i, filename=filename)
            db.session.add(img)
    db.session.commit()


if __name__ == '__main__':
    add_images_to_db()
