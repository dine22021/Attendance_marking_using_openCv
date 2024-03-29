import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': ""
})

ref = db.reference('Students')

data = {
    "3021": #change this to your image id
        {
            "name": "Dinesh.S",
            "major": "B.TECH IT",
            "starting_year": 2022,
            "total_attendance": 1,
            "grade": "G",
            "year": 4,
            "last_attendance_time": "2024-03-23 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
