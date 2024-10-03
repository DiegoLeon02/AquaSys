from wtforms import Form, StringField, IntegerField, FloatField, validators
from wtforms import Form, StringField, TextAreaField, DateField, FileField, validators


class ProductoForm(Form):
    nombre = StringField('Nombre', [validators.InputRequired()])
    descripcion = StringField('Descripción', [validators.Optional()])
    codigo = StringField('Código del Producto', [validators.InputRequired()])
    cantidad = IntegerField('Cantidad', [validators.InputRequired()])
    precio = FloatField('Precio', [validators.InputRequired()])


class CampaignForm(Form):
    nombre = StringField('Nombre de la Campaña', [validators.InputRequired()])
    objetivo = StringField('Objetivo', [validators.InputRequired()])
    fecha_inicio = DateField('Fecha de Inicio', [validators.InputRequired()], format='%Y-%m-%d')
    fecha_fin = DateField('Fecha de Fin', [validators.InputRequired()], format='%Y-%m-%d')
    texto_principal = TextAreaField('Texto Principal', [validators.InputRequired()])
  