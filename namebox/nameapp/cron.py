"""from django_cron import CronJobBase, Schedule

from django.shortcuts import render, HttpResponse

import random
from django.core.mail import BadHeaderError, send_mail, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
"""
from django.core.mail import send_mail
from django.conf import settings
import smtplib
import kronos
import random

@kronos.register('0 0 * * *')
def email():
	try:
		send_mail('Amazing Names', 'Hello!', 'mansiojha7@gmail.com', ['mansiojha7@gmail.com'])
	except Exception as e:
		print("error", e)

	print('mail sent successfully')
#class MyCronJob(CronJobBase):
#	RUN_EVERY_MINS = 5

#	schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
#	code = 'mjnh6556'

#	def do(self):
#		try:
#			send_mail('Amazing Names', 'Hello!', 'mansiojha7@gmail.com', ['mansiojha7@gmail.com'])
#		except Exception as e:
#			print("error", e)
#		print('ghdvc')

