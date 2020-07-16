from bs4 import BeautifulSoup


soup = BeautifulSoup(open("meme.html"),'html.parser')

marks = open("marks_list.txt","w+")

arr = []

for item in soup.findAll("span"):
    arr.append(item.string)
    if len(arr) == 2:
        marks.write("{} {}\n".format(arr[0],arr[1]))
        arr.clear()

marks.close()