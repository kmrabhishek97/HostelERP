# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

from manager.models import EmployeeInfo
from smartadmin.models import AdminInfo
from .models import Room
from student.models import Studentinfo
# Create your views here.


class _room:
    def __init__(self, room_object):
        self.room_number = room_object.room_number
        self.capacity = room_object.capacity
        self.vacancy = room_object.vacancy
        self.roomType = room_object.roomType
        tenants = Studentinfo.objects.filter(room=room_object, active=True)
        self.tenant1 = '-'
        self.tenant2 = '-'
        if len(tenants) > 0:
            self.tenant1 = tenants[0].first_name + " " + tenants[0].last_name
            if len(tenants) == 2:
                self.tenant2 = tenants[1].first_name + " " + tenants[1].last_name
        #self.rent = room_object.rent
        self.additional_charges = room_object.additional_charges
        self.need_maintenance = room_object.need_maintenance
        self.repairs = room_object.repairs


def index(request):
    if checkuser(request):
        if checkusersession(request):
            rooms = []
            all_rooms = Room.objects.all()
            for i in all_rooms:
                rooms.append(_room(i))
            return render(request, 'RoomView.html',{'object_list':rooms})
    elif checkadmin(request):
        if checkadminsession(request):
            rooms = []
            all_rooms = Room.objects.all()
            for i in all_rooms:
                rooms.append(_room(i))
            return render(request, 'RoomView.html', {'object_list': rooms})
    else:
        return render(request, 'error.html')


def checkuser(request):
    if request.session.has_key('userid'):
        return True
    else:
        return False


def checkusersession(request):
    if request.session.session_key == EmployeeInfo.objects.get(empid=request.session['userid']).session_key:
        return True
    else:
        return False


def checkadmin(request):
    if request.session.has_key('adminid'):
        return True
    else:
        return False


def checkadminsession(request):
    if request.session.session_key == AdminInfo.objects.get(adminid=request.session['adminid']).session_key:
        return True
    else:
        return False

