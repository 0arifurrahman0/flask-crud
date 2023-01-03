from flask import Blueprint, render_template, request, flash, url_for, redirect, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/home')
@login_required
def home():
    return render_template('home.html')


@views.route('/note-create', methods=['GET', 'POST'])
@login_required
def note_create():
    try:
        if request.method == 'POST':
            note = request.form.get('note')
            if len(note) < 1:
                flash('Note required', category='error')
            else:
                new_note = Note(data=note, user_id=current_user.id)
                db.session.add(new_note)
                db.session.commit()

                flash('Note created successfully!', category='success')
                return redirect(url_for('views.home'))

        return render_template('note/create.html')
    except Exception as e:
        flash(e, category='error')


@views.route('/note-delete', methods=['POST'])
@login_required
def note_delete():
    try:
        if request.method == 'POST':
            note = json.loads(request.data)
            note_id = note['note_id']
            note = Note.query.get(note_id)
            if note:
                if note.user_id == current_user.id:
                    db.session.delete(note)
                    db.session.commit()
        return jsonify({})

    except Exception as e:
        flash(e, category='error')
