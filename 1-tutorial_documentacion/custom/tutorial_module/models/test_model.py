# -*- coding: utf-8 -*-

from odoo import models, fields

class TestModel(models.Model):
    _name = "test.model"
    _description = "Modelo de prueba"

    var_name = fields.Char(string="Name", required=True)
    var_testField1 = fields.Char(string="Test Field 1")
    int_testField2 = fields.Integer(string="Test Field 2")