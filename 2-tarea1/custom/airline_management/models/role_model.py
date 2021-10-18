# -*- coding: utf-8 -*-

from odoo import models, fields

class Role(models.Model):
    _name = "airline.role.model"
    _description = "Modelo que hace referencia a la tabla rol de persona"

    name = fields.Char(string="Rol de la persona" , required=True)