# -*- coding: utf-8 -*-

from odoo import models, fields


class clase1(models.Model):
     _name = 'Clase.clase1'
     _description = 'Esta clase ayuda al aprendizaje'

     nombre = fields.Char()
     Jugador = fields.Integer()
     Valoración  = fields.Float(compute="_value_pc", store=True)
     descripción = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
