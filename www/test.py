from __future__ import unicode_literals
import frappe


def get_context(context):
        context['body'] = "tiwiex"
        #context.news = frappe.db.sql("select name from `tabNews` where name= ")
