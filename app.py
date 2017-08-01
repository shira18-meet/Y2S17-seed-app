# flask imports
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
import sys

# SQLAlchemy
from model import Base, Comp, Options
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# setup
app = Flask(__name__)
engine = create_engine('sqlite:///project.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route ('/',methods=['GET', 'POST'])
def add_poll():
    if request.method == 'GET':
   	 return render_template('addpoll.html')
   	else:
    	new_poll=Post(id=poll_id,category=request.form.get('category'),title=request.form.get('title'),description=request.form.get('description'),votes=request.form.get('votes'))
    	new_options=Options(option=request.form.get('option1'),pic_url=request.form.get('pic_url1'),
    	session.add(new_poll,new_options)
    	session.commit()
    	return redirect(url_for('myfeed'))



@app.route('/')
def vote(poll_id):
	session.query(Post).filter_by(id=poll_id).first()
	session.commit()
	return redirect(url_for('myfeed'))





@app.route('/')
def my_feed():
    
    comps = session.query(Comp).all()
 
    
    return render_template('myfeed.html', comps= comps)

@app.route('/<string:category>')
def my_feed_category():
    polls = session.query(Comp).filter_by(category=category).all()
    return render_template('myfeed.html', polls=polls)
