from xml.dom.minidom import parse as minidomm
import xml.dom.minidom

#open xml document using minidom parser
domTree = minidomm("demo/dataone.xml")
collection = domTree.documentElement #movie, type, format

if collection.hasAttribute("shelf"):
    print("Root element : %s"%collection.getAttribute("shelf"))


#get all the movies in the colllection
movies = collection.getElementsByTagName("movie")

print(movies)

#print detail if each movie
for movie in movies:
    print("*********MOVIE************")
    if movie.hasAttribute("title"):
        print("Title : %s"%movie.getAttribute("title"))

    type = movie.getElementsByTagName("type")[0]
    print("Type : %s"%type.childNodes[0].data)
    format = movie.getElementsByTagName("format")[1]
    print(f"Format : %s"%type.childNodes[1].data)
    year = movie.getElementsByTagName("year")[2]
    print(f"year : %s" % type.childNodes[2].data)
    rating = movie.getElementsByTagName("rating")[3]
    print(f"rating : %s" % type.childNodes[3].data)
    stars = movie.getElementsByTagName("stars")[4]
    print(f"stars : %s" % type.childNodes[4].data)
    description= movie.getElementsByTagName("description")[5]
    print(f"description : %s" % type.childNodes[5].data)

