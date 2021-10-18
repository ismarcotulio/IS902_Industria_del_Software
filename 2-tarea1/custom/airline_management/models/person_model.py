# -*- coding: utf-8 -*-

from odoo import models, fields

class Person(models.Model):
    _name = "airline.person.model"
    _description = "Modelo que hace referencia a cualquier persona registrada"

    secretId = fields.Char(string="Id Secreto", required=True)
    passportNumber = fields.Char(string="Numero de Pasaporte", required=True)
    firstName = fields.Char(string="Primer Nombre", required=True)
    middleName = fields.Char(string="Segundo Nombre")
    firstSurname = fields.Char(string="Primer Apellido", required=True)
    secondSurname = fields.Char(string="Segundo Apellido")
    country_id = fields.Many2one(string="Id del pais", comodel_name='airline.country.model', help="Pais en el que nacio la persona")
    role_id = fields.Many2one(string="Rol de sistema", comodel_name='airline.role.model', help="Rol de sistema de la persona")
