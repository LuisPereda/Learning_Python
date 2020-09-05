# This program parses a url

url = "http://www.flyingbear.co/our-story.html#:~:text=Flying%20Bear%20is%20a%20NYC,best%20rate%20in%20the%20city."

url_list = url.split("/") # Parsing begins at character (/)

domain_name = url_list[2] # Dictates at which character number parsing begins

print (domain_name.replace("www.","")) # Deletes a specific character or string of characters and replaces them with desired input



