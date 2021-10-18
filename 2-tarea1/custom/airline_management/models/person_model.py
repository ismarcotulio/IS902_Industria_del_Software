# -*- coding: utf-8 -*-

from odoo import models, fields

class Person(models.Model):
    _name = "airline.person.model"
    _description = "Modelo que hace referencia a cualquier persona registrada"

    secretId = fields.Char(string="Secret Id", required=True)
    passportNumber = fields.Char(string="Passport Number", required=True)
    firstName = fields.Char(string="First Name", required=True)
    middleName = fields.Char(string="Middle Name")
    firstSurname = fields.Char(string="First Surname", required=True)
    secondSurname = fields.Char(string="Second Surname")
    country_id = fields.Many2one(string="Country Id", comodel_name='airline.country.model', help="Pais en el que nacio la persona")
    role_id = fields.Many2one(string="Role Id", comodel_name='airline.role.model', help="Rol de sistema de la persona")
