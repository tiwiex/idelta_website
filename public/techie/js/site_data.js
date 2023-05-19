$(document).ready(function() {
    $.ajax({
      url: "/api/method/idelta_website.api.get_active_customers",
      method: "GET",
      success: function(response) {
        var activeCustomers = response.active_customers;
        console.log(activeCustomers); // Log the value to the console
        $("#active-customers").text("Active Customers: " + activeCustomers);
      },
      error: function(xhr, textStatus, errorThrown) {
        console.error("Error:", errorThrown);
      }
    });
  });
  