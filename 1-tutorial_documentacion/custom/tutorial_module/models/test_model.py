# -*- coding: utf-8 -*-

from odoo import models, fields

class TestModel(models.Model):
    _name = "test.model"
    _description = "Modelo de prueba"

    int_id = fields.Integer(required=True)
    var_name = fields.Char("test", required=True)