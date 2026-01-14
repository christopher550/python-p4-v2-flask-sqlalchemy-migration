from app import app
from models import db, Department

with app.app_context():
    db.session.add(Department(name="Payroll", address="Building A, 4th Floor"))
    db.session.add(Department(name="Human Resources", address="Building C, 1st Floor"))
    db.session.commit()
    print(Department.query.all())
