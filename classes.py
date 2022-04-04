class User():
    first_name = ''
    last_name = ''
    email_address = ''
    phone_number = ''
    allergies = ''
    food_diet = ''
    user_type = ''

    def get_full_name(self):
        return "{}, {}".format(user.first_name, user.last_name)

class MenuItem():
    name = ''
    description = ''
    serving_size = ''
    allergens = ''


class Order():
    pass

class Price():
    pass

user = User()
user.first_name = 'Ini'
user.last_name = 'Arthur'
user.phone_number = '948559393'
user.email_address = 'ini@bamba.com'

print ("My name is {} and we are Fuudia".format(user.get_full_name()))