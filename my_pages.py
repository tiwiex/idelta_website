import frappe


from frappe import render_template

def get_project_data():
    # Fetch the project data from the database using frappe.get_all or any other suitable method
    project_data = frappe.get_all("Project Portfolio", filters={}, fields=["name", "project_image"])

    return project_data

def my_pages():
    context = {
        "project_portfolio": get_project_data(),
        # Add more data from other doctypes here
    }
    return render_template("index.html", context)


