from django.shortcuts import render , HttpResponse , redirect
from eventpro.models import postds
from .form import *
# Create your views here.


# def show(request):
#     return render(request, 'eventpro/base.html')

# def getdata(request):
#     data = postdata.objects.all()
#     if request.method == "POST":
#         eventname = request.POST['eventname']
#         desc = request.POST['desc']
#         time = request.POST['time']
#         location = request.POST['location']
        

#         inser = postdata(eventname=eventname, desc=desc, time=time, location= location,)
#         inser.save()        
#     return render(request, 'eventpro/getdata.html')

def posts(request):
  
    if request.method == 'POST':
        form = postForm(request.POST, request.FILES)
  
        if form.is_valid():
            form.save()
            return HttpResponse('success')
    else:
        form = postForm()
    return render(request, 'eventpro/form.html', {'form' : form})
  
def display_images(request):
  
    if request.method == 'GET':
        imagees = postds.objects.all() 
        return render(request, 'eventpro/display.html',
                     {'d_images' : imagees})


