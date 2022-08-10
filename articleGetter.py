from newspaper import Article

# Testing the fine tuning
# pulling an article from our github repo
# and parsing all the data to train the model


# TO-DO
# get all 5 articles
# https://incentivized.substack.com/p/how-dopex-might-change-the-curve

f = open('/Users/baldwin/GitProjects/squareLabs/DeFi-Bots/data/article_2.txt', 'w')

url1 = 'https://incentivized.substack.com/p/this-is-why-the-curve-wars-are-being'
url2 = 'https://incentivized.substack.com/p/how-convex-stacked-as-much-crv-as'
url3 = 'https://incentivized.substack.com/p/how-bribes-drive-the-curve-wars'
url4 = 'https://incentivized.substack.com/p/what-the-is-redacted'
url5 = 'https://incentivized.substack.com/p/how-dopex-might-change-the-curve'


article = Article(url4)

article.download()


# TO-DO
# convert output to JSON
article.parse()
with open('/Users/baldwin/GitProjects/squareLabs/DeFi-Bots/data/testArticle4.txt', 'w') as f:
    f.write(article.text)

print(article.text)
