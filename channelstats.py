import os
from pprint import pprint
import google.oauth2.credentials
import vidstats
import statplotting
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
import pandas as pd


CLIENT_SECRETS_FILE = "client_secret.json"

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
df = pd.DataFrame()


def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def channels_list_by_username(service, df, **kwargs):
  results = {}
  plotstats = []
  single = []
  results = service.channels().list(**kwargs).execute()
  #print(results)
  #print('############################################################################')
  print('This channel\'s ID is %s. Its title is %s,\n%s' %
       (results['items'][0]['id'],
        results['items'][0]['snippet']['title'],
        results['items'][0]['statistics']))
  single.append([results['items'][0]['id'], results['items'][0]['snippet']['title'], results['items'][0]['statistics']])
  gen = []
  for i in results['items'][0]['topicDetails']['topicCategories']:
    print(str(i.split('/')[-1]))
    gen.append(str(i.split('/')[-1]))
    
  single.append(gen)

  vid_id = results['items'][0]['contentDetails']['relatedPlaylists']['uploads']
  vids = {}
  vids = service.playlistItems().list(part = 'snippet', playlistId = vid_id, maxResults = 10).execute()
  for i in range(10):
    print(vids['items'][i]['snippet']['title'])
    x = vids['items'][i]['snippet']['resourceId']['videoId']
    stats = vidstats.videos_list_by_id(service, part='snippet,contentDetails,statistics', id=x)
    plotstats.append(stats)
    views.append(int(stats['viewCount']))

  print(single)
  df = pd.DataFrame([[single[0][1], single[0][2]['subscriberCount'], single[0][2]['viewCount'], single[1], 'https://www.youtube.com/channel/'+str(single[0][0])]], columns = ['Name', 'Subs', 'TotalViews', 'Genres', 'Link'])
  #df = df.append(df2)
  #print(df)
  return(df)
  #pprint(results)

if __name__ == '__main__':
  #os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  service = get_authenticated_service()
  #df = pd.DataFrame(columns = ['Name', 'Subs', 'TotalViews', 'Genres', 'Link'])
  channelsnames = ['allindiabakchod','TheViralFeverVideos','KSIOlajidebt','teamcoco','DjWalkzz']
  df = pd.DataFrame(columns = ['Name', 'Subs', 'TotalViews', 'Genres', 'Link'])
  df2 = pd.DataFrame(columns = ['Name', 'Subs', 'TotalViews', 'Genres', 'Link'])
  for channel in channelsnames:
    views = []
    print('\n\n')
    df = channels_list_by_username(service, df, part='snippet,contentDetails,statistics,status,topicDetails',
      forUsername=channel)
    df2 = df2.append(df)
    print(df2)
    statplotting.plottingViews(views)

  channelsid = ['UCG8rbF3g2AMX70yOd8vqIZg','UCqwUrj10mAEsqezcItqvwEw','UCDySHzpIIlgxeexkVuFCiJg']

  for channel in channelsid:
    print('\n\n')
    df = channels_list_by_username(service, df, part='snippet,contentDetails,statistics,status,topicDetails',
     id=channel)
    df2 = df2.append(df)
    print(df2)
    statplotting.plottingViews(views)

  df2.to_csv('info.csv')
#'All India Bakchod','The Viral Fever','BB Ki Vines',
