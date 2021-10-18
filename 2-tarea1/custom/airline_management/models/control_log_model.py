# -*- coding: utf-8 -*-

from odoo import models, fields

class ControlLog(models.Model):
    _name = "airline.control.log.model"
    _description = "Modelo que hace referencia a la tabla que lleva un control de las actividades de las personas"

    dueDate = fields.Datetime.now()
    person_id = fields.Many2one(string="Id Persona", comodel_name='airline.person.model', help="Persona que realizo la actividad")
    activity_id = fields.Many2one(string="Id Actividad", comodel_name='airline.activity.model', help="Actividad que realizo la persona")
