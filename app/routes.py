from flask import render_template, flash, redirect, url_for
from . import db
from .forms import PaymentForm
from .models import Comprador
from flask import current_app as app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    form = PaymentForm()
    if form.validate_on_submit():
        comprador = Comprador(
            nombre=form.nombre.data,
            email=form.email.data,
            fecha_nacimiento=form.fecha_nacimiento.data,
            dni=form.dni.data,
            tarjeta_credito=form.tarjeta_credito.data,
            fecha_expiracion=form.fecha_expiracion.data,
            codigo_seguridad=form.codigo_seguridad.data
        )
        db.session.add(comprador)
        db.session.commit()
        flash('Pago realizado con éxito!', 'success')
        return redirect(url_for('success'))
    return render_template('payment.html', form=form)

@app.route('/success')
def success():
    return render_template('success.html')

