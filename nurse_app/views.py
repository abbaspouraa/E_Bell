from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from patient_app.models import Bell


# Create your views here.

def request_delete_view(request, rq_id):
    obj = get_object_or_404(Bell, id=rq_id)
    if request.method == "POST":
        obj.delete()
        return redirect('../')


def nurse_view(request):
    queryset = Bell.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "nurse_app/patient_request.html", context)
