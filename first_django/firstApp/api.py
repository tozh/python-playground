from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.template import loader, Context
from firstApp.query import Query
from pymongo import MongoClient
import json


def myself(request):
    request.encoding = 'utf-8'
    t = loader.get_template("index.html")
    context = {}
    if 'id' in request.GET:
        # client = MongoClient('127.0.0.1', 27017)
        id = request.GET['id']
        # p = Query(id, client)
        context['id'] = id
        # context['myself'] = p.person.__dict__
        # context['followers'] = list(p.followers)
        # context['followees'] = list(p.followees)
        # context['r_friend'] = list(p.r_friend)
        # context['relations'] = p.relations()
        # context['inner_relations'] = p.inner_relations()
        return HttpResponse(t.render(context))
    else:
        context['error'] = 'The API format is wrong. Maybe you need add the <id> parameter.'
        return HttpResponseNotFound(str(context))


def other(request):
    request.encoding = 'utf-8'
    context = {}
    if 'myself' in request.GET and 'other' in request.GET:
        client = MongoClient('127.0.0.1', 27017)
        myself_id = request.GET['myself']
        other_id = request.GET['other']
        myself = Query(myself_id, client)
        other = Query(myself_id, client)
        





