"""views.py - Definitions for the view functions."""
import os
import random
from datetime import datetime

from flask import (flash, make_response, redirect, render_template, request,
                   session, url_for)

from application import app, db
from application.forms import InputForm, PictureForm
from application.models import Image, Rating, Trial


@app.context_processor
def override_url_for():                     # pragma: no cover
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):      # pragma: no cover
    if endpoint == "static":
        filename = values.get("filename", None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            values["q"] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@app.route("/get", methods=["GET", "POST"])
def manage_data():                          # pragma: no cover
    """Show the data collected so far."""
    result = [(k, v) for k, v in session.items()]
    flash(result)
    if request.method == "POST":
        session["rating"] = request.get_json().get("rating", None)
    return render_template("base.html")

@app.route("/index")
def index():
    return render_template("navbar.html")

@app.route("/", methods=["GET", "POST"])
def input_participant():
    """Show the input_participant input page."""
    label = "Enter the participant number:"
    form = InputForm()
    if request.method == "POST":
        if form.validate_on_submit():
            data = form.number.data
            session["p_num"] = f"{data}"
            form.number.data = ""
            return redirect(url_for("input_session"))
        for error in form.number.errors:
            flash(error)
    return render_template("login.html", form=form, label=label)


@app.route("/session", methods=["GET", "POST"])
def input_session():
    """Show the session input page."""
    label = "Enter the session number:"
    form = InputForm()
    if request.method == "POST":
        if form.validate_on_submit():
            p_num = session["p_num"]
            s_num = session["s_num"] = form.number.data
            form.number.data = ""
            duplicate = db.session.query(Trial).filter_by(participant=p_num,
                                                          session=s_num).all()
            if duplicate:
                flash("Participant and session already exist. Try again.")
                return redirect(url_for("input_participant"))
            else:
                t = Trial(participant=p_num, session=s_num,
                          date=datetime.today())
                db.session.add(t)
                db.session.commit()
                flash("Participant and session recorded.")
                return redirect(url_for("instructions"))
        else:
            for error in form.number.errors:
                flash(error)
            return redirect(url_for("input_session"))
    return render_template("login.html", form=form, label=label)


@app.route("/instructions", methods=["GET", "POST"])
def instructions():
    """Show the instructions page."""
    if request.method == "POST":
        images = db.session.query(Image).limit(None).all()
        random.shuffle(images)
        session["images"] = images
        return redirect(url_for("pictures"))
    return render_template("instructions.html")


@app.route("/pictures", methods=["GET", "POST"])
def pictures():
    """Show all the images for the survey one at a time."""
    images = session["images"]
    if not images:
        return redirect(url_for("finish"))
    image = images[-1]
    filename = image.filename
    form = PictureForm()
    if request.method == "POST":
        if form.validate_on_submit():
            images.pop()
            rating = session["rating"]
            r = Rating(participant_id=session["p_num"],
                       session_id=session["s_num"],
                       image=filename,
                       rating=rating)
            db.session.add(r)
            db.session.commit()
            return redirect(url_for("pictures"))
    return render_template("pictures.html", filename=filename, form=form)


@app.route("/finish", methods=["GET", "POST"])
def finish():
    """Show the survey finish page."""
    # if request.method == "POST":
    #     return redirect(url_for("landing"))
    return render_template("finish.html")


@app.route("/save_data/?p=<int:participant_num>&s=<int:session_num>")
def save_data(participant_num, session_num):
    """Save the survey responses as csv file."""
    trial = Trial.query.filter_by(participant=participant_num,
                                  session=session_num).first()

    # Find date of trial needed to save with survey response
    date = trial.date if trial else None

    results = Rating.query.filter_by(participant_id=participant_num,
                                     session_id=session_num).all()
    cols = "participant_id, session_id, date, "
    images = [item.image for item in results]
    lines1 = cols + ", ".join(images) + "\n"

    values = f"{participant_num}, {session_num}, {date}, "
    ratings = [item.rating for item in results]
    lines2 = values + ", ".join([str(r) for r in ratings]) + "\n"

    lines = lines1 + lines2

    name = f"participant-{participant_num}-session-{session_num}"
    response = make_response(lines)
    content_disposition = f"attachment; filename={name}.csv"
    response.headers["Content-Disposition"] = content_disposition
    response.mimetype = "text/csv"
    return response


@app.route("/download", methods=["GET", "POST"])
def download():
    """Show the download page."""
    results = Trial.query.order_by(Trial.participant).all()
    form = InputForm()
    if request.method == "POST":
        p = request.form.get("participant", None)
        s = request.form["session"]
        return redirect(url_for("save_data", participant_num=p, session_num=s))
    return render_template("download.html", results=results, form=form)
