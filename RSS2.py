
import feedparser

from flask import Flask
app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml','cnn': 'http://rss.cnn.com/rss/edition.rss','fox': 'http://feeds.foxnews.com/foxnews/latest'}


@app.route("/") 
@app.route("/bbc")
def bbc():
    return get_news('bbc')

@app.route("/cnn")
def cnn():
    return get_news('cnn')

@app.route("/fox")
def fox():
    return get_news('fox')

def get_news(pub):   
    feed = feedparser.parse(RSS_FEEDS[pub])
    first_article = feed['entries'][0]
    
    return '''<html><head><title>News</title></head>
<body>
<h1>{0} Headlines </h1>
<b>{1}</b><br>
<i>{2}</i><br>
<p>{3}</p><br>
</body>
<html>'''.format(pub, first_article.get("title"), first_article.get("published"), first_article.get("summary"))
    

if __name__ == '__main__':
    app.run(use_reloader=False, debug=True)
