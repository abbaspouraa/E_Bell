from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime

from patient_app.models import Bell


# Create your views here.

def request_delete_view(request, rq_id):
    obj = get_object_or_404(Bell, id=rq_id)
    if request.method == "POST":
        obj.delete()
        return redirect('../')


def nurse_view(request):
    queryset = Bell.objects.all()
    this_minute = int(datetime.now().minute)

    for b in queryset:
        passed_minutes = abs(b.time.minute - this_minute)
        if passed_minutes < 2:
            b.danger_mode = "green"
        elif 5 > passed_minutes >= 2:
            b.danger_mode = "yellow"
        else:
            b.danger_mode = "red"

    context = {
        'object_list': queryset
    }
    return render(request, "nurse_app/patient_request.html", context)


