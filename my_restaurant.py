from restaurant import Restaurant

my_restaurant=Restaurant('So de ZhongCanTing','Chinese Food')
my_restaurant.open_restaurant()
my_restaurant.guest.set_number_served(23)
my_restaurant.describe_restaurant()
my_restaurant.guest.increment_number_served(5)
my_restaurant.describe_restaurant()