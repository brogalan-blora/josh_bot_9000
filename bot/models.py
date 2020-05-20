from os import environ, getenv
import sqlite3
from flask import Flask, g
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
# ----------------------------------- Flask ---------------------------------- #
app = Flask(__name__)
host = getenv('HOST')
port = environ.get('PORT')
# --------------------------------- DB Config -------------------------------- #
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = getenv('SQLALCHEMY_TRACK_MODIFICATIONS')
db = SQLAlchemy(app)
# ---------------------------------------------------------------------------- #


class Tweets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer)
    created_at = db.Column(db.String)
    full_text = db.Column(db.String)
    retweeted_status = db.Column(db.Integer)
    quoted_status = db.Column(db.Integer)
    place = db.Column(db.String)
    source = db.Column(db.String)
    truncated = db.Column(db.Integer)
    display_text_range = db.Column(db.String)
    in_reply_to_status_id = db.Column(db.String)
    in_reply_to_user_id = db.Column(db.String)
    in_reply_to_screen_name = db.Column(db.String)
    geo = db.Column(db.String)
    coordinates = db.Column(db.String)
    contributors = db.Column(db.String)
    is_quote_status = db.Column(db.Integer)
    retweet_count = db.Column(db.Integer)
    favorite_count = db.Column(db.Integer)
    favorited = db.Column(db.Integer)
    retweeted = db.Column(db.Integer)
    possibly_sensitive = db.Column(db.Integer)
    lang = db.Column(db.String)


class MentionsTweets(db.Model):
    user = db.Column(db.Integer, primary_key=True)
    tweet = db.Column(db.Integer, primary_key=True)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    screen_name = db.Column(db.String)
    name = db.Column(db.String)
    description = db.Column(db.String)
    location = db.Column(db.String)
    url = db.Column(db.String)
    protected = db.Column(db.Integer)
    followers_count = db.Column(db.Integer)
    friends_count = db.Column(db.Integer)
    listed_count = db.Column(db.Integer)
    created_at = db.Column(db.String)
    favourites_count = db.Column(db.Integer)
    utc_offset = db.Column(db.String)
    time_zone = db.Column(db.String)
    geo_enabled = db.Column(db.Integer)
    verified = db.Column(db.Integer)
    statuses_count = db.Column(db.Integer)
    lang = db.Column(db.String)
    contributors_enabled = db.Column(db.Integer)
    is_translator = db.Column(db.Integer)
    is_translation_enabled = db.Column(db.Integer)
    profile_background_color = db.Column(db.String)
    profile_background_image_url = db.Column(db.String)
    profile_background_image_url_https = db.Column(db.String)
    profile_background_tile = db.Column(db.Integer)
    profile_image_url = db.Column(db.String)
    profile_image_url_https = db.Column(db.String)
    profile_banner_url = db.Column(db.String)
    profile_link_color = db.Column(db.String)
    profile_sidebar_border_color = db.Column(db.String)
    profile_sidebar_fill_color = db.Column(db.String)
    profile_text_color = db.Column(db.String)
    profile_use_background_image = db.Column(db.Integer)
    has_extended_profile = db.Column(db.Integer)
    default_profile = db.Column(db.Integer)
    default_profile_image = db.Column(db.Integer)
    following = db.Column(db.Integer)
    follow_request_sent = db.Column(db.Integer)
    notifications = db.Column(db.Integer)
    translator_type = db.Column(db.String)
    suspended = db.Column(db.Integer)
    needs_phone_verification = db.Column(db.Integer)
    profile_location = db.Column(db.String)
    live_following = db.Column(db.Integer)
    muting = db.Column(db.Integer)
    blocking = db.Column(db.Integer)
    blocked_by = db.Column(db.Integer)
