from pyramid.view import view_config


@view_config(route_name='addevent', renderer='json')
def addevent(request):
#	cshUserName = request.headers["X-Webauth-User"]
	name = request.params['name']
	starttime = request.params['starttime']
	endtime = request.params['endtime']
	date = request.params['date']
	return {'username' : 123, 'userNumber' : 0}

@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'pdpreg'}
