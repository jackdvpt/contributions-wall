import requests
from bs4 import BeautifulSoup
# Insert your username in the below request
page = requests.get("https://github.com/")
soup = BeautifulSoup(page.text, 'html.parser')
# gets the contributions table
contirbutions = soup.find("div", {"class": "js-yearly-contributions"})
columns = []
# Converts the colour of the rectangle to a numeric value
rock = {"#ebedf0": 0, "#9be9a8": 1, "#40c463": 2, "#30a14e": 3, "#216e39": 4, }
ret = contirbutions.findAll("g")
for r in ret:
    print(r.get("transform"))
    rectangles = r.findAll("rect")
    current = []
    # The first g is techncially every rectangle so just skip that
    if r.get("transform") != "translate(10, 20)":
        for square in rectangles:
            current.append(rock[square.get("fill")])
        columns.append(current)
        print(current)
# columns now contains each column, however i want to now print it to look like the actual grid
output = []
for i in range(6):
    current_column = []
    for row in columns:
        try:
            current_column.append(row[i])
        except IndexError:
            # the last row will only have up to today (so if its tuesday it will only have 2 rects) fill in the future with 0's
            current_column.append(0)
    output.append(current_column)

#prints the output in the nice format
for child in output:
    print(child)
