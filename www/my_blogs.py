import frappe

def get_context(context):
    context.test_var = "Hello World"
    return context

print("tiwie")

#def get():
 #   return frappe.render_template("templates/my_file.html", context=get_context({}))
