# -*- coding: utf-8 -*-
##############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from trytond.model import ModelSQL, ModelView, fields

__all__ = ['Opportunity']

class Opportunity(ModelSQL, ModelView):
    'Opportunity'
    __name__ = 'trainning.opportunity'
    _rec_name = 'description'
    
    description = fields.Char('Description', required=True)
    start_date = fields.Date('Start Date', required=True)
    end_date = fields.Date('End Date')
    party = fields.Many2One('party.party', 'Party', required=True)
    comment = fields.Text('Comment')