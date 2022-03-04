from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def get_room_number(request, *args, **kwargs):
    return render(request, "room_number.html", {})


def home_view(request, *args, **kwargs):
    room_number = request.POST.get("input_number")
    print(room_number)
    return render(request, "home.html", {})


def medical_need(request, *args, **kwargs):
    return render(request, "medical_need.html", {})


def non_medical_need(request, *args, **kwargs):
    return render(request, "nonmedicalneed.html", {})


def request_sent(request, *args, **kwargs):
    req = request.POST
    emergency_medical_need_list = ['sos', 'vaginal_bleed', 'baby', 'water-broke', 'pressure', 'pain', 'nausea',
                                   'beeping', 'foley', 'help']
    non_medical_need_list = ['bathroom', 'linens', 'food', 'settle']
    question_list = ['nurse', 'health-care']
    for key in req.keys():
        # if key == 'sos' or key == 'vaginal_bleed' or key == 'baby' or key == 'water-broke' or key == 'pressure':
        if key in emergency_medical_need_list or key in non_medical_need_list or key in question_list:
            print(key)
    return render(request, "request_sent.html", {})


def non_urgent_question(request, *args, **kwargs):
    return render(request, "nonurgentquestion.html", {})
