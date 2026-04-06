# Introduction to Beautiful Soup

Beautiful Soup is a Python library used for web scraping data from HTML and XML files. It provides tools for navigating, searching, and manipulating the parsed data.

```python
pip install beautifulsoup4
```

## GETTING STARTED

### Import and object creation - get element
```python
from bs4 import BeautifulSoup

html_content = "<html><body><h1>Hello, World!</h1></body></html>"
soup = BeautifulSoup(html_content, 'html.parser')

# Get the first 'h1' tag
h1_tag = soup.h1
print(h1_tag.text)  # Output: Hello, World!
```

### Get value of a attribute - for example class
```python
from bs4 import BeautifulSoup

html_content = "<html><body><h1 class='naslov'>Hello, World!</h1></body></html>"
soup = BeautifulSoup(html_content, 'html.parser')

# Get the first 'h1' tag
h1_tag = soup.h1
print(h1_tag.text)  # Output: Hello, World!

# Get the value of the 'class' attribute of an element
class_value = h1_tag['class']
print(class_value)  # Output: ['heading']
```

### Get the parent of an element

```python
# Get the parent of an element
parent_tag = h1_tag.parent
print(parent_tag.name)  # Output: body
```

### Get children

```python
# Get the children of an element
children = list(parent_tag.children)
for child in children:
    print(child.name)  # Output: h1
```


### Find all 'p' tags

```python
paragraphs = soup.find_all('p')
for paragraph in paragraphs:
    print(paragraph.text)
```

### Finding Elements with Specific Attributes
```python
# Find all 'a' tags with a specific class
links = soup.find_all('a', class_='link-class')
for link in links:
    print(link['href'])
```

### Navigating the HTML Tree

```python
# Get the next sibling of an element
next_sibling = h1_tag.next_sibling
print(next_sibling.name)
```


### Getting Previous Sibling
```python
# Get the previous sibling of an element
prev_sibling = h1_tag.previous_sibling
print(prev_sibling.name)
```

### Extracting Text and Attributes
You can extract text content and attributes from HTML elements using Beautiful Soup.

```python
# Extract text from an element
print(h1_tag.text)
```

```python
# Extract the value of an attribute
href_value = link['href']
print(href_value)
```

## Scraping Web Pages

### 

```python
import requests

# Fetch web content
url = 'https://www.example.com'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all headlines (h2 tags)
headlines = soup.find_all('h2')
for headline in headlines:
    print(headline.text)

# Find all 'a' tags and extract their href attribute
links = soup.find_all('a')
for link in links:
    print(link['href'])

# Check if a tag exists before accessing it
if soup.h1:
    print(soup.h1.text)
else:
    print("No 'h1' tag found.")

with open('scraped_data.txt', 'w') as file:
    file.write(soup.prettify())
```