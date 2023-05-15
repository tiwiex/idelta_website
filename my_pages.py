import frappe


from frappe import render_template

def get_project_portfolio():
    # Fetch the project data from the database using frappe.get_all or any other suitable method
    project_portfolio = frappe.get_all("Project Portfolio", filters={}, fields=["name", "project_image"])

    return project_portfolio

def my_pages():
    context = {
        "project_portfolio": get_project_portfolio(),
        # Add more data from other doctypes here
    }
    return render_template("index.html", context)


def get_doctype_fields(doctype):
    meta = frappe.get_meta(doctype)
    fields = [field.fieldname for field in meta.fields]
    return fields


@frappe.whitelist()
def list_fields(doctype):
    meta = frappe.get_meta(doctype)
    fields = [field.fieldname for field in meta.fields]

    return fields






