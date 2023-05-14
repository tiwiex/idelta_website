import frappe


from frappe import render_template

def get_project_portfolio():
    return frappe.get_all("Project Portfolio", fields=["name", "project_description"])

def my_pages():
    data = {
        "project_portfolio": get_project_portfolio(),
        # Add more data from other doctypes here
    }
    return render_template("index.html", data=data)


