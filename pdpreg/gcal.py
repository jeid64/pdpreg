import gflags
import httplib2

from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials
import pprint

FLAGS = gflags.FLAGS
# To disable the local server feature, uncomment the following line:
# FLAGS.auth_local_webserver = False

class GoogleCalendar:
    def __init__(self):
        with open('privatekey.p12', 'rb') as f:
            key = f.read()

        service_account_name = '107723137689-kdtp1ragrspt1bjk368nfl2iol3p07ga@developer.gserviceaccount.com'
       # calendarId = '...@group.calendar.google.com'

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
        self.service = build(serviceName='calendar', version='v3', http=http)

        lists = self.service.calendarList().list().execute()
        pprint.pprint(lists)

    def addEvent(self, startTime, endTime, title):
        """
            Adds event to Google Calendar. Time parameters are Arrow objects and get converted to GCal datetimes.
        """
        startTime = startTime.convertGoogleCalendar()
        endTime = endTime.convertGoogleCalendar()
        event = {
            "start": {
                "dateTime": startTime,
            },
            "end": {
                "dateTime": endTime,
            },
            "summary": title,
            "attendees": [
                {
                "email": "jeid64@gmail.com",
                }
            ],
        }
        recurring_event = self.service.events().insert(calendarId='primary', body=event).execute()
        print (recurring_event['id'])
