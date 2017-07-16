from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db import connection
from preguntatet.models import Pregunta
import json
@login_required
def index(request):
	template = loader.get_template('base.html')
	preg = Pregunta.objects.all()
	for abc in preg:
		preg_question_text=abc.question_text
		preg_descripcion=abc.descripcion

	context = {
	"preg":preg,
	"preg_question_text":preg_question_text,
	"preg_descripcion":preg_descripcion
	}
	return HttpResponse(template.render(context,request))