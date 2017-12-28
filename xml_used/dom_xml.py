from xml.dom.minidom import parse
import xml.dom.minidom

# 使用 minidom 解析器打開 xml 文檔
DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
    print("Root element : {0}".format(collection.getAttribute("shelf")))

# 在集合中获取所有电影
movies = collection.getElementsByTagName("movie")

# 打印每部电影的详细信息
for movie in movies:
    print("******** Movie *******")
    if movie.hasAttribute("title"):
        print("Title : {0}".format(movie.getAttribute("title")))
    type = movie.getElementsByTagName('type')[0]
    print("Type : %s" % type.childNodes[0].data)
    format = movie.getElementsByTagName('format')[0]
    print("Format : %s" % format.childNodes[0].data)

