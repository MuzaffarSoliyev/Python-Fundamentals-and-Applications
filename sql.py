# Parameterized Query for get data with pagination from database
def get_all_data(db, table, limit, offset):
    """
    Get all data from database
    :param db: Database connection
    :param table: Table name
    :param limit: Number of data to be retrieved
    :param offset: Number of data to be skipped
    :return: Data from database
    """
    query = "SELECT * FROM {} LIMIT {} OFFSET {}".format(table, limit, offset)
    return db.query(query)


# triangle area
def area(base, height):
    """
    Calculate area of triangle
    :param base: Base of triangle
    :param height: Height of triangle
    :return: Area of triangle
    """
    return 0.5 * base * height


# surface area of pyramid
def pyramidArea(base, height):
    """
    Calculate surface area of pyramid
    :param base: Base of pyramid
    :param height: Height of pyramid
    :return: Surface area of pyramid
    """
    return area(base, height) + base * height

# volume of pyramid
def pyramidVolume(base, height):
    """
    Calculate volume of pyramid
    :param base: Base of pyramid
    :param height: Height of pyramid
    :return: Volume of pyramid
    """
    return area(base, height) * height

# generate html element in BEM format of driving license
def generate_license(name, address, dob):
    """
    Generate driving license in BEM format
    :param name: Name of person
    :param address: Address of person
    :param dob: Date of birth of person
    :return: Driving license in BEM format
    """
    return """
    <div class="license">
        <div class="name">{}</div>
        <div class="address">{}</div>
        <div class="dob">{}</div>
    </div>
    """.format(name, address, dob)


# generate VUE component of driving license
def genvue(name, address, dob):
    """
    Generate driving license in VUE format
    :param name: Name of person
    :param address: Address of person
    :param dob: Date of birth of person
    :return: Driving license in VUE format
    """
    return """
    <div class="license">
        <div class="name">{}</div>
        <div class="address">{}</div>
        <div class="dob">{}</div>
    </div>
    """.format(name, address, dob)
