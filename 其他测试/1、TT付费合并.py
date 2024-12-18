import wordcloud
c = wordcloud.WordCloud(stopwords=set())
c.generate('wordcloud by python')
c.to_file('pywordcloud.png')
