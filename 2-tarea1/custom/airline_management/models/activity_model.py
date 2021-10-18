# -*- coding: utf-8 -*-

from odoo import models, fields

class Activity(models.Model):
    _name = "airline.activity.model"
    _description = "Modelo que hace referencia a la actividad de una persona en la aerolinea"

    name = fields.Char(string="Nombre de la actividad", required=True)