import gflags
import httplib2

from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials
import pprint

FLAGS = gflags.FLAGS
# To disable the local server feature, uncomment the following line:
# FLAGS.auth_local_webserver = False

with open('privatekey.p12', 'rb') as f:
    key = f.read()

service_account_name = '107723137689-kdtp1ragrspt1bjk368nfl2iol3p07ga@developer.gserviceaccount.com'
calendarId = '...@group.calendar.google.com'

credentials = SignedJwtAssertionCredentials(
    service_account_name, key,
    scope=['https://www.googleapis.com/auth/calendar',
           'https://www.googleapis.com/auth/calendar.readonly'])

# Create an httplib2.Http object to handle our HTTP requests and authorize it
# with our good Credentials.
http = httplib2.Http()
http = credentials.authorize(http)

# Build a service object for interacting with the API. Visit
# the Google APIs Console
# to get a developerKey for your own application.
service = build(serviceName='calendar', version='v3', http=http)

lists = service.calendarList().list().execute()
pprint.pprint(lists)
print

event = {
  "start": {
      "dateTime": '2011-06-03T10:00:00.000-07:00',
  },
  "end": {
      "dateTime": '2011-06-03T10:25:00.000-07:00',
  },
  "attendees": [
    {
      "email": "jeid64@gmail.com",
    }
  ],
}

recurring_event = service.events().insert(calendarId='primary', body=event).execute()

print (recurring_event['id'])
