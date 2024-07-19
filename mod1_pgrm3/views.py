from django.http import HttpResponse
from datetime import datetime 

# Create your views here.
def current_datetime(request):
    now = datetime.now()
    html = f"<html><body><h1>Current date and time:</h1><p>{now}</p></body></html>"
    return HttpResponse(html)
