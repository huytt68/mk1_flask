from .databaseConfig import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, nullable=False, default=0)
    description = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f'<Product {self.name}>'

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
