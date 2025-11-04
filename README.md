# Books App Exercise

## Why should I do this?

This lab will guide you through the process of writing SQLAlchemy models and making queries to create, read, and update, and delete data in your database. By the end of this lab, you should be ready to independently write and use model classes for your projects. 

## Setup

Clone this repository to your computer. 

**Take a look at the code** - it looks a bit different than what you're used to. Namely, the code is now separated out into several files rather than being written in a single `app.py` file. Since we're now writing model code as well as route code, this will help us to maintain some structure and separation. (Also, it's really handy to be able to look at your models code side-by-side with your routes code!)

**To run the code**, navigate to the project folder and run the following to install the required packages:

```
pip3 install -r requirements.txt
```

Then, rename the `.env.example` file to `.env`:

```
mv .env.example .env
```

Then you can run the following to run the Flask server:

```
python3 app.py
```

# 

**Navigate to `books_app/routes.py` and complete the TODOs for the `homepage()` route.** When you are done, the homepage should display a list of all users, with each user linking to their profile. Make sure you run the Flask application to test it out!

Next, **complete the TODOs for the `profile()` route.** Once this is complete, if you navigate to the page `/profile/user1`, it should show `user1`'s favorite books.

If you have finished all of the steps so far, congratulations - you have mastered the basics of SQLAlchemy!

## Resources

If you'd like more resources on working with SQLAlchemy models, check out the following:

- [SQLAlchemy Relationship Patterns](https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html) - A comprehensive guide on how to construct models with One-to-Many, One-to-One, and Many-to-Many relationships.
- [Declaring Models](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/) - A shorter, but still useful guide.
- [Filter Operations](https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_filter_operators.htm)


