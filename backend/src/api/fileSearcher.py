from .jsonSearcher import searchJSON

def search(city):
	possible_cities = []
	lst = searchJSON()

	possible_cities = [x for x in lst if city == x[0].lower()]
	return possible_cities