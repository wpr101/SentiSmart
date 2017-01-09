import pymongo
from pymongo import MongoClient
import nltk
import re

client = MongoClient('localhost', 27017)

db = client.stock_exchange_news_feeds
col = db.OilStories.find()

#creation of table
#storyOne = {}
#storyOne['WallStreetJournal'] = 'Oil is up today'
#db.OilStories.insert(storyOne)

#storyTwo = {}
#storyTwo['NewYorkTimes'] = 'OPEC lowered their oil production targets'
#db.OilStories.insert(storyTwo)

#storyThree = {}
#storyThree['MarketWatch'] = 'Why oil could go much lower'
#db.OilStories.insert(storyThree)

#storyFour = {}
#storyFour['MotleyFool'] = 'Oil will rise over 100 again'
#db.OilStories.insert(storyFour)

#storyFive = {}
#storyFive['WashingtonPost'] = 'Oil tanker collides with cruise ship in Carribean'
#db.OilStories.insert(storyFive)

storyEconomist = {}
storyEconomist['Economist'] = 'The oil conundrum. Plunging prices have neither halted oil production nor stimulated a surge in global growth.'

db.OilStories.insert(storyEconomist)



#for key, value in d.iteritems():
    #print key, '\t', value

storyContents = []
for story in col:
    #print(story)
    for source, content in story.items():
        if (source != "_id"):
            storyContents.append(content)

for story in storyContents:
    tokenized = nltk.word_tokenize(story)
    tagged = nltk.pos_tag(tokenized)
    namedEnt = nltk.ne_chunk(tagged, binary=True)
    print(namedEnt)
    entities = re.findall(r'NE\s(.*?)/', str(namedEnt))
    descriptives = re.findall(r'\(\'(\w*)\',\s\'JJ\w?\'', str(tagged))
    print(entities)
    print('-----------')
    #print(descriptives)
