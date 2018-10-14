def city_country(city,country,pop=''):
	if pop:
		string=city.title()+', '+country.title()+' - population='+str(pop)
	else:
		string=city.title()+', '+country.title()
	return string
