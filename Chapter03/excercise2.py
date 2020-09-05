# This program groups tuples

url_tup = ('www', 'thapar', 'edu','index', 'php','about-us','mission') # Tuple

url1 = ".".join(url_tup[:3]) # Groups the first 3 tuples and adds a period between them

url2 = "/".join(url_tup[3:]) # After the third tuple the remaining tuples are paired and /'s are added starting from the 4th tuple

print (url1+"/"+url2) # Groups the formatted tuples and adds a / between "edu" and "index"
