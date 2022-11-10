from django.shortcuts import render, HttpResponse, redirect
from time import strftime
from datetime import datetime
# Create your views here.


def index(request):
    content = {
        "date": strftime('%B %d, %Y '),
        "time": strftime('%H:%M %p'),
    }
    local_time = datetime.now()
    current_time = local_time.strftime('%H:%M %p')
    print(current_time)
    return render(request, 'time_display/index.html', content)
