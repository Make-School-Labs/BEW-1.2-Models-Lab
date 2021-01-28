"""Import packages and modules."""
import os
import requests
from flask import Blueprint, request, render_template, redirect, url_for, flash
from datetime import date, datetime
from pprint import PrettyPrinter
from books_app.models import Book, Author, Genre

# Import app and db from events_app package so that we can run app
from books_app import app, db

main = Blueprint("main", __name__)

##########################################
#           Routes                       #
##########################################

@main.route('/')
def homepage():
    return render_template('home.html')

@main.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username)