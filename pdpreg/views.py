from pyramid.view import view_config
import arrow
from dateutil.tz import gettz
from gcal import GoogleCalendar

class Arrow(arrow.Arrow):
    def convertGoogleCalendar(self):
        """
            Converts Arrow object into a string that can be sent to Google Calendar.
            Google Calendar expects datetimes in this format, 2011-06-03T10:00:00.000-07:00
        """
        return(self.format('YYYY-MM-DDTHH:mm:ssZZ'))

def convertFullTime(datettimeString):
	"""
		Converts times from POST from FullCalendar in this format Mon Aug 05 2013 15:30:00 GMT-0400 (EDT)
		into an Arrow object that can be used to convert to a Google Calendar time string.
	"""
	datetime = datettimeString[:24]
	timezone = datettimeString[35:38]
	return Arrow.strptime(datetime, "%a %b %d %Y %H:%M:%S", gettz(timezone))

@view_config(route_name='addevent', renderer='json')
def addevent(request):
#	cshUserName = request.headers["X-Webauth-User"]
	title = request.params['title']
	start = request.params['start']
	end = request.params['end']
	allDay = request.params['allDay']
	#closeddate = request.params['closeddate']
	print (title + start + end + allDay)
	start = convertFullTime(start)
	end = convertFullTime(end)
	gcal = GoogleCalendar()
	gcal.addEvent(start, end, title)
	return {'username' : 123, 'userNumber' : 0}

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'pdpreg'}
