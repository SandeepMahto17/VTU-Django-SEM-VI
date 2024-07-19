from django.http import HttpResponse
from datetime import datetime, timedelta

# Create your views here.
def datetime_with_offsets(request):
    now = datetime.now()
    four_hours_ahead = now + timedelta(hours=4)
    four_hours_before = now - timedelta(hours=4)
    html = f"<html><body><h1>Current date and time with offsets:</h1>" \
        f"<p>Current: {now}</p>" \
        f"<p>Four Hours Ahead: {four_hours_ahead}</p>" \
        f"<p>Four Hours Before: {four_hours_before}</p></body></html>"
    return HttpResponse(html)
