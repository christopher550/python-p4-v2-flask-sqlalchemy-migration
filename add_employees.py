import sys
sys.path.insert(0, '.')

from server.app import app
from server.models import db, Employee

with app.app_context():
    db.session.add(Employee(name='Kai Uri', salary=89000))
    db.session.add(Employee(name='Alena Lee', salary=125000))
    db.session.commit()
    print(Employee.query.all())
