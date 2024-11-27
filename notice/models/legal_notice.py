# -*- coding: utf-8 -*-
from odoo import models, fields, api
from datetime import timedelta


class LegalNotice(models.Model):
    _name = 'legal.notices'
    _description = 'Legal Notice'
    _order = 'deadline desc'  # Sort by deadline in descending order (latest first)

    name = fields.Char(string='Title', required=True)
    file_no = fields.Char(string='File Number')
    status = fields.Selection([
        ('pending', 'Pending'),
        ('complete', 'Complete'),
    ], string='Status', default='pending')
    instruction_received = fields.Text(string='Instructions Received')
    instruction_received_form = fields.Many2many(
        'ir.attachment',
        'instruction_received_form_rel',  # Unique table name
        string='Instruction Received Form'
    )
    infringer_name = fields.Char(string='Infringer Name')
    infringers = fields.One2many('notice.infringer', 'legal_notice_id', string='Infringers')
    address = fields.Text(string='Address')
    city = fields.Char(string='City')
    contact_info = fields.Text(string='Contact Info')
    email = fields.Char(string='Email')
    mobile_number = fields.Char(string='Mobile Number')
    notice_date = fields.Date(string='Notice Date')
    delivery = fields.Many2many('ir.attachment', string="Delivery Report")
    delivery_report_remarks = fields.Text(string="Delivery Report Remarks")
    legal_notice = fields.Many2many(
        'ir.attachment',
        'legal_notice_rel',  # Unique table name
        string='Legal Notice'
    )
    remarks = fields.Text(string='Remarks')
    deadline = fields.Date(string="Deadline")
    is_reminder = fields.Boolean(string='Reminder', compute='_compute_is_reminder', store=True)

    @api.depends('deadline')
    def _compute_is_reminder(self):
        today = fields.Date.today()
        for record in self:
            record.is_reminder = bool(record.deadline and record.deadline - timedelta(days=1) == today)

    action_type = fields.Selection([
        ('criminal', 'Criminal'),
        ('civil', 'Civil'),
        ('both', 'Both'),
    ], string='Action Type')

    criminal_action_file = fields.Many2many(
        'ir.attachment',
        'criminal_action_file_rel',  # Unique table name
        string='Criminal Action File'
    )
    criminal_action_remarks = fields.Text(string='Criminal Action Remarks')
    criminal_status = fields.Selection([
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ], string='Criminal Status')

    civil_action_file = fields.Many2many(
        'ir.attachment',
        'civil_action_file_rel',  # Unique table name
        string='Civil Action File'
    )
    civil_action_remarks = fields.Text(string='Civil Action Remarks')
    civil_status = fields.Selection([
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ], string='Civil Status')


class LegalNoticeInfringer(models.Model):
    _name = 'notice.infringer'
    _description = 'Legal Notice Infringer'

    name = fields.Char(string='Infringer Name', required=True)
    address = fields.Text(string='Address')
    as_field = fields.Selection(
        [('to', 'TO'), ('cc', 'CC')],
        string='AS'
    )  # Add this field
    legal_notice_id = fields.Many2one('legal.notices', string='Legal Notice', ondelete='cascade')
