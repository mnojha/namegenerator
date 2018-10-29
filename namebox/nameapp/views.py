from django.shortcuts import render, HttpResponse
from .models import Namelist
import random
from django.core.mail import BadHeaderError, send_mail, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def indexView(request):
	name = Namelist.objects.all()
	return render(request, 'nameapp/index.html', context={'mylist': name})

def search(request):
	# import pdb;pdb.set_trace()
	human_name = request.POST.get('human_name', 'this is default')
	email = request.POST.get('email', 'this is default')	
#	subject = 'Thank you'
#	message = ' it means a world to us '
	pool = list(Namelist.objects.all())
	random.shuffle(pool)
	object_list = pool[:5]
	try:
		x = []
		for ran in object_list:
			x.append(str(ran.human_name))
		print(x)

		send_mail('Amazing Names', human_name + '  ' + str(x), 'mansiojha7@gmail.com', [email])
	except Exception as e:
		print("error", e)
#	return render(request, 'nameapp/search.html', context={'human_name' : human_name, 'object_list':object_list, 'email': email})
	return render(request, 'nameapp/result.html', context={'human_name' : human_name, 'email': email})


#def email(request):
#	import pdb;pdb.set_trace()
#	subject = 'Thank you'
#	message = ' it means a world to us '
#	email_from = 'mansi@webllisto.com'
#	recipient_list = ['mansiojha7@gmail.com',]

#	send_mail(subject, message, email, recipient_list)

#	return HttpResponse('email sent')

