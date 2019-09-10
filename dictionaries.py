# Dictionaries
# Key-Value Pairs

months = {
    # "Key" : "Value" 
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(months["Feb"])
print(months.get("Dec"))
print(months.get("Luv","Not a valid key"))