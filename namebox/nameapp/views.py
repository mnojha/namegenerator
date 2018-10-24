from django.shortcuts import render, HttpResponse
from .models import Namelist
import random


# Create your views here.
def indexView(request):
	name = Namelist.objects.all()
	return render(request, 'nameapp/index.html', context={'mylist': name})

def search(request):
#	import pdb;pdb.set_trace()
	human_name = request.GET.get('human_name', 'this is default')
#	name = Namelist.objects.filter(human_name=human_name)

	number_of_records = Namelist.objects.count()
	print(number_of_records)

	random_index = int(random.random()*number_of_records)+1
	print(random_index)
	ran = Namelist.objects.filter(id__gte = random_index)[0]
	print(ran)
#	random_p = Namelist.get(pk = random_index)
	return render(request, 'nameapp/search.html', context={'human_name' : human_name, 'ran':ran})
