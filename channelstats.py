import vidstats
import json
import statplotting
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pandas as pd


CLIENT_SECRETS_FILE = "client_secret.json"

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
df = pd.DataFrame()

forjson = []
def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def channels_list_by_username(service, df, **kwargs):
      plotstats = []
      single = []
      views = []
      singlejson = []
      results = service.channels().list(**kwargs).execute()
      print('Channel Title: ', results['items'][0]['snippet']['title'])
      single.append([results['items'][0]['id'], results['items'][0]['snippet']['title'], results['items'][0]['statistics']])
      gen = []
      for i in results['items'][0]['topicDetails']['topicCategories']:
        gen.append(str(i.split('/')[-1]))

      single.append(gen)

      vid_id = results['items'][0]['contentDetails']['relatedPlaylists']['uploads']
      vids = service.playlistItems().list(part = 'snippet', playlistId = vid_id, maxResults = 10).execute()
      for i in range(10):
        try:
            x = vids['items'][i]['snippet']['resourceId']['videoId']
            stats = vidstats.videos_list_by_id(service, part='snippet,contentDetails,statistics', id=x)
            plotstats.append(stats)
            views.append(int(stats['viewCount']))
        except:
            continue

      singlejson.append([single[0][1], single[0][2]['subscriberCount'], single[0][2]['viewCount'], single[1],'https://www.youtube.com/channel/' + str(single[0][0])])

      return singlejson, views


def main(channelnames, channelids):
  totaljson = []
  service = get_authenticated_service()

  channelnames = ['allindiabakchod','TheViralFeverVideos','KSIOlajidebt','teamcoco','DjWalkzz']

  # df = pd.DataFrame(columns = ['Name', 'Subs', 'TotalViews', 'Genres', 'Link'])
  for channel in channelnames:
    views = []
    singlejson, views = channels_list_by_username(service, df, part='snippet,contentDetails,statistics,status,topicDetails',
      forUsername=channel)
    for i in singlejson:
        totaljson.append(i)
    #statplotting.plottingViews(views)


  channelids = ['UCG8rbF3g2AMX70yOd8vqIZg','UCqwUrj10mAEsqezcItqvwEw','UCDySHzpIIlgxeexkVuFCiJg']


  for channel in channelids:
      singlejson, views = channels_list_by_username(service, df, part='snippet,contentDetails,statistics,status,topicDetails',
     id=channel)
      for i in singlejson:
          totaljson.append(i)
    #statplotting.plottingViews(views)

  print(totaljson)
  jlist = []
  for i in totaljson:
      jdict = {}

      jdict['Channel Name'] = i[0]
      jdict['Subscribers'] = i[1]
      jdict['Total Views'] = i[2]
      jdict['Genres'] = i[3]
      jdict['Channel Link'] = i[4]

      jlist.append(jdict)

  json.dump(jlist , open('dets.json','w'))

  return jlist
