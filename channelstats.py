import os
from pprint import pprint
import google.oauth2.credentials
import vidstats
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow


CLIENT_SECRETS_FILE = "client_secret.json"

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def channels_list_by_username(service, **kwargs):
  results = {} 
  results = service.channels().list(**kwargs).execute()
  #print('############################################################################')
  print('This channel\'s ID is %s. Its title is %s,\n%s' %
       (results['items'][0]['id'],
        results['items'][0]['snippet']['title'],
        results['items'][0]['statistics']))
  for i in results['items'][0]['topicDetails']['topicCategories']:
    print(str(i.split('/')[-1]))

  vid_id = results['items'][0]['contentDetails']['relatedPlaylists']['uploads']
  vids = {}
  vids = service.playlistItems().list(part = 'snippet', playlistId = vid_id, maxResults = 10).execute()
  for i in range(10):
    print(vids['items'][i]['snippet']['title'])
    x = vids['items'][i]['snippet']['resourceId']['videoId']
    vid_stat = vidstats.videos_list_by_id(service, part='snippet,contentDetails,statistics', id=x)
    print(vid_stat)
  
  #pprint(results)

if __name__ == '__main__':
  #os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
  service = get_authenticated_service()
  channel = 'PewDiePie'
  channelsnames = ['allindiabakchod','TheViralFeverVideos','KSIOlajidebt','teamcoco','DjWalkzz']
  for channel in channelsnames:
    print('\n\n')
    channels_list_by_username(service, part='snippet,contentDetails,statistics,status,topicDetails',
      forUsername=channel)

  channelsid = ['UCG8rbF3g2AMX70yOd8vqIZg','UCqwUrj10mAEsqezcItqvwEw']

  for channel in channelsid:
    print('\n\n')
    channels_list_by_username(service, part='snippet,contentDetails,statistics,status,topicDetails',
     id=channel)

#'All India Bakchod','The Viral Fever','BB Ki Vines',
