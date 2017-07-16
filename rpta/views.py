# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
import time 
from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth import *
from django.contrib.auth.models import User
from preguntatet.models import Pregunta, Respuesta
from django.shortcuts import get_object_or_404, render_to_response
import json

# Create your views here.
def Respondation(request):
	template = loader.get_template('responder.html')
	respuesta = request.POST.get('Respuesta_Usuario','')
	pregunta = request.POST.get('pregunta_id')
	answer = Respuesta(question = pregunta, usuario = User.objects.get(pk=request.session['idUser']),respuesta=respuesta)
	answer.save()
	#ans = pregunta.respuesta_set.all()
	#for abc in preg:
		#preg_question_text=abc.question_text
		#preg_descripcion=abc.descripcion
	context = {}
	#"preg":preg,
	#"preg_question_text":preg_question_text,
	#"preg_descripcion":preg_descripcion
	return RequestContext(template.render(context,request))