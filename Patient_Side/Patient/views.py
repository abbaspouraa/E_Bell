from django.shortcuts import render
from django.http import HttpResponse
from .models import PatientRequest
from Patient import forms

emergency_medical_need_list = ['sos', 'vaginal_bleed', 'baby', 'water-broke', 'pressure', 'pain', 'nausea',
                               'beeping', 'foley', 'help']
non_medical_need_list = ['bathroom', 'linens', 'food', 'settle']
question_list = ['nurse', 'health-care']
room_number = 0

messages=["STAT call"]
priorities=[1 ]
staff_types=["RN"]
is_emergency=['Y']

def domain(request, *args, **kwargs):
    return render(request, "domain.html", {})


def get_room_number(request, *args, **kwargs):
    return render(request, "room_number.html", {})


def home_view(request, *args, **kwargs):
    room_number = request.POST.get("input_number")
    print(room_number)
    return render(request, "home.html", {"room_number": room_number})


def medical_need(request, *args, **kwargs):
    return render(request, "medical_need.html", {})


def non_medical_need(request, *args, **kwargs):
    return render(request, "nonmedicalneed.html", {})


def request_sent(request, *args, **kwargs):
    room_number = 0
    req = request.POST

    for key in req.keys():
        if key in emergency_medical_need_list or key in non_medical_need_list or key in question_list:
            print(key)
            idx = 0
            if key == "sos":
                idx = 0
            else:
                #TODO add other button types
                idx = -1

            try:
                patient_request = forms.PatientRequest(message=messages[idx],
                                                       priority=priorities[idx],
                                                       staff=staff_types[idx] ,
                                                       emergency=is_emergency[idx],
                                                       room_number=room_number)
                patient_request.save()
            except:
                print("Could not find request type")
                #Do nothing

    return render(request, "request_sent.html", {})


def non_urgent_question(request, *args, **kwargs):
    return render(request, "nonurgentquestion.html", {})
