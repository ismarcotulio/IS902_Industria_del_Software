# -*- coding: utf-8 -*-

from odoo import models, fields

class Country(models.Model):
    _name = "airline.country.model"
    _description = "Modelo que hace referencia a una tabla paises"

    name = fields.Char(string="Nombre del pais", required=True)
    code = fields.Integer(string="Codigo", required=True)