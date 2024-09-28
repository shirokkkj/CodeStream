from flask import Flask, render_template, redirect, url_for, make_response
from form_views.submission_forms import Registration_Form, Login_Form
from helpers.data_handler import create_token, check_password
from database_migrations.migrations import Users
import bcrypt
from config import db

def config_routes(app):
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = Registration_Form()
        
        if form.validate_on_submit():
            
            if not check_password(form.password.data):
                return redirect(url_for('register'))  # Senha pra não ficar criando uma toda hora: cOdeStream@@123Admin
            
            cookie = make_response(redirect(url_for('home')))
            token = create_token(form.username.data)
            cookie.set_cookie('register_token', token, httponly=True, secure=True)
            
            password = str(form.password.data).encode('UTF-8')
            salt = bcrypt.gensalt()
            encrypted_password = bcrypt.hashpw(password, salt)

            new_register = Users(username=form.username.data, email=form.email.data, password=encrypted_password, repeat_password=encrypted_password, position=form.position.data, country=form.country.data, short_biography=form.short_biography.data)
            db.session.add(new_register)
            db.session.commit()
            return cookie
        
        return render_template('register.html', form=form)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = Login_Form()
        

        
        if form.validate_on_submit():
            
            if not check_password(form.password.data):
                return redirect(url_for('login'))
            
            provided_password = str(form.password.data).encode('utf-8')
            
            user = Users.query.filter_by(email=form.email.data).first()
            
            if not user:
                return redirect(url_for('login'))
            
            users_stored_password = user.password.encode('utf-8')
            
            if not bcrypt.checkpw(provided_password, users_stored_password):
                return redirect(url_for('login'))

            
            cookie = make_response(redirect(url_for('home')))
            token = create_token(form.email.data)
            cookie.set_cookie('login_token', token, httponly=True, secure=True)
            
            return cookie
        
        return render_template('login.html', form=form)

    @app.route('/home')
    def home():
        return '<h1>oi</h1>'

    @app.route('/challenges')
    def challenges():
        return render_template('challenges.html')