from pymongo import MongoClient
import channelstats


port = 27017   #port of localhost
channelnames = ['allindiabakchod', 'TheViralFeverVideos', 'KSIOlajidebt', 'teamcoco', 'DjWalkzz']
channelids = ['UCG8rbF3g2AMX70yOd8vqIZg', 'UCqwUrj10mAEsqezcItqvwEw', 'UCDySHzpIIlgxeexkVuFCiJg']


data = channelstats.main(channelnames, channelids)

client = MongoClient('mongodb://localhost:' + str(port) + '/')

Youtube = client.Youtube
BasicInfo = Youtube.BasicInfo

for i in data:
    BasicInfo.insert(i)

