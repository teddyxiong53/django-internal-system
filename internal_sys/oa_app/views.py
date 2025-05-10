from django.shortcuts import render

from django.shortcuts import render
from .models import Announcement

def oa_dashboard(request):
    announcements = Announcement.objects.all().order_by('-publish_date')[:5]
    return render(request, 'oa_app/dashboard.html', {
        'announcements': announcements
    })

def announcement_list(request):
    announcements = Announcement.objects.all().order_by('-publish_date')
    return render(request, 'oa_app/announcement_list.html', {'announcements': announcements})
