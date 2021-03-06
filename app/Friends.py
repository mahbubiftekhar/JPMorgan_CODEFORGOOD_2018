from datetime import datetime
from app import database as db

#This represents the relationship b/w two friends

class Friends(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	friend1UserID = db.Column(db.Integer)
	friend2UserID = db.Column(db.Integer)

	def addFriends(ffriend1UserID, ffriend2UserID):
		friends = Friends(friend1UserID = ffriend1UserID, friend2UserID = ffriend2UserID)
		db.session.add(friends)
		db.session.commit()
		return True
	def getUsersFriends(uid):
		friendsList = []
		friendsList.append(Friends.query.filter_by(friend1UserID = uid).first().friend2UserID)
		friendsList.append(Friends.query.filter_by(friend2UserID = uid).first().friend1UserID)
		return friendsList

	
db.create_all()




