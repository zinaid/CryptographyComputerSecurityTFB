from bs4 import BeautifulSoup

html_content = "<html><body><h1 class='naslov'>Hello, World!</h1></body></html>"
soup = BeautifulSoup(html_content, 'html.parser')

# Get the first 'h1' tag
h1_tag = soup.h1
print(h1_tag.text)  # Output: Hello, World!

# Get the value of the 'class' attribute of an element
class_value = h1_tag['class']
print(class_value)  # Output: ['heading']