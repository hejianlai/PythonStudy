import urllib
def getHtml(url):
    page = urllib.urlopen("http://www.pythontab.com/html/pythonhexinbiancheng/")
    html = page.read()
    page.close()
    return html
