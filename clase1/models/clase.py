# -*- coding: utf-8 -*-

from odoo import models, fields

class clase1(models.Model):
    _name = 'clase1.alumnos'
    _description = 'Esta clase ayuda al aprendizaje'

    name= fields.Char()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    active = fields.Boolean(string='Active', default=True)
    jugador = fields.Integer()
    valoracion  = fields.Float(compute="_value_pc", store=True)
    descripcion = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
