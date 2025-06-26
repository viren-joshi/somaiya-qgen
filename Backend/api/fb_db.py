import firebase_admin
from firebase_admin import db

data = {} # Firebase API Key
cred_obj = firebase_admin.credentials.Certificate(data)
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL':'https://sih-sc500-default-rtdb.firebaseio.com/'
	})


ref = db.reference('/Users/1234')
# ref = db.reference('/Users/' + user_id)
print(ref.child('user_type').get())
res = str(ref.child('user_type').get())
print(res)
