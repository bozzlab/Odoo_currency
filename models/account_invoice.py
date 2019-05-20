# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    currency_rate = fields.Float(
        string='Exchange Rate (THB)',
        default=1.0,
    )
    currency_related = fields.Float(
        string='Exchange Rate Related',
        related='currency_rate',
    )
    currency_name = fields.Char(
        string='Currency Name',
        related='currency_id.name',
    )

    @api.onchange('currency_id')
    def _onchange_currency(self):
        if self.currency_id and self.currency_id.name == 'THB':
            self.update({
                'currency_rate': 1.0,
                'currency_related': 1.0,
            })

    def _prepare_invoice_line_from_po_line(self,line):
        res = super(AccountInvoice, self)._prepare_invoice_line_from_po_line\
        (line)
        res['price_unit'] = line.price_unit * self.currency_rate
        res['po_price_unit'] = line.price_unit * self.currency_rate
        return res

    @api.onchange('currency_rate')
    def _onchange_rate(self):
        for line in self.invoice_line_ids:
            line._set_currency()


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    po_price_unit = fields.Float(
        string="PO Price Unit"
    )


    @api.depends('invoice_id.currency_rate')
    def _set_currency(self):
        res = super(AccountInvoiceLine, self)._set_currency()
        if self.po_price_unit == 0:
            self.po_price_unit = self.price_unit
        self.price_unit =  self.po_price_unit * self.invoice_id.currency_rate
        return res

