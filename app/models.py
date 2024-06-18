from . import db

class Comprador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    fecha_nacimiento = db.Column(db.String(8), nullable=False)
    dni = db.Column(db.String(20), nullable=False)
    tarjeta_credito = db.Column(db.String(20), nullable=False)
    fecha_expiracion = db.Column(db.String(5), nullable=False)
    codigo_seguridad = db.Column(db.String(4), nullable=False)

