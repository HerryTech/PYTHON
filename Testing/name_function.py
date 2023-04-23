def get_formatted_name(firstname, lastname, middlename = ""):
    """Generate a neatly formatted full name."""
    if middlename:
        fullname = f"{firstname} {middlename} {lastname}"
    else:
        fullname = f"{firstname} {lastname}"
    return fullname.title()

