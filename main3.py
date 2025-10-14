from js import document

# Tuple Data Type
business_hours = ("9:00 AM", "7:00 PM")
address = ("67 Dun Dun street", "Las Piñas", "Philippines")
numbers = ("Main: (888) 607-4040", "Mobile: (123) 456-7891")
email = ("dimplduns@gmail.com", "support@dundun.com", "careers@dimpleduns.com")

# Fill in the HTML elements
document.getElementById("openingHours").innerText = f"Open: {business_hours[0]} - {business_hours[1]}"
document.getElementById("address").innerHTML = "<br>".join(address)
document.getElementById("numbers").innerHTML = "<br>".join(numbers)
document.getElementById("email").innerHTML = "<br>".join(email)
