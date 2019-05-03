import git
import urllib, json, string, random

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone

def get_version_checksum():
    repo = git.Repo(search_parent_directories=True)
    return repo.head.object.hexsha[:7]


def get_online_users():
    # Credits to https://stackoverflow.com/questions/2723052/how-to-get-the-list-of-the-authenticated-users
    # Query all non-expired sessions
    # use timezone.now() instead of datetime.now() in latest versions of Django
    sessions = Session.objects.filter(expire_date__gte=timezone.now())
    uid_list = []

    # Build a list of user ids from that query
    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id', None))

    # Query all logged in users based on id list
    return User.objects.filter(id__in=uid_list)


def google_recaptcha(request):
	recaptcha_response = request.POST.get('g-recaptcha-response')
	google_url = 'https://www.google.com/recaptcha/api/siteverify'
	values = {
		'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
		'response': recaptcha_response
	}

	data = urllib.parse.urlencode(values).encode()
	req =  urllib.request.Request(google_url, data=data)
	response = urllib.request.urlopen(req)
	result = json.loads(response.read().decode())

	return result