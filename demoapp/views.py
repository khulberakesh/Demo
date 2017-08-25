from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.template import RequestContext, Context
from demoapp.models import Article
from django.contrib.auth.tokens import default_token_generator
import time





def html_login(request):
    if "UID" in request.session:
        return HttpResponseRedirect('/index')
    else:
        if request.method == "POST":
            username = request.POST.get('username','')
            password = request.POST.get('pass','')
            st = Article.login(username, password)
            if len(st) > 0:
                request.session['UID'] = st[0]["UID"]
                request.session['Name'] = st[0]["Name"]
                request.session['IsActive'] =st[0]["IsActive"]
                return HttpResponseRedirect('/index')
            else:
                return render_to_response('login.html', {'invalid': 'Invalid Username or Password'},
                                          RequestContext(request))

        else:
            return render_to_response('login.html',
                                          RequestContext(request))





def html_logout(request):
    try:
        del request.session['UID']
        del request.session['Name']
    except KeyError:
        pass
    return HttpResponseRedirect('/login')



def configureuser(request):
    if "UID" in request.session:
        if request.method == "POST":

            ap = request.POST['apikey']
            screat = request.POST['Secret']
            uid = request.session['UID']
            result = Article.configureuser(ap,screat,uid)
            return render_to_response('configure-user.html',{}, context_instance=RequestContext(request))
        else:
            return render_to_response('configure-user.html',{}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')

def index(request):
    if "UID" in request.session:
        #result = Article.fetch_instancedetail
        return render_to_response('index.html',{}, context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/login')

def register(request):
    if request.method == "POST":
        try:
            Name = request.POST['Name']
            Email = request.POST['Email']
            Phone = request.POST['Phone']
            passw = request.POST['Password']
            result = Article.adduser(Name,Email,Phone,passw)
            return render_to_response("registration.html", {'success': 'Successfully Inserted!'}, context_instance=RequestContext(request))
        except Exception, err:
            return render_to_response("registration.html", {'error': str(err)}, context_instance=RequestContext(request))
    return render_to_response("registration.html", {}, context_instance=RequestContext(request))



def launchinstance(request):
    if "UID" in request.session:
        if request.method == "POST":
            sizeoffleet = request.POST['sizeoffleet']
            tyinstances = request.POST['tyinstances']
            maxprice = request.POST['maxprice']
            exptime = request.POST['exptime']
            uid = request.session['UID']
            result = Article.launchinstance(sizeoffleet,tyinstances,maxprice,exptime,uid)
            return render_to_response('launchinstance.html' ,{}, context_instance=RequestContext(request))
        else:
            return render_to_response('launchinstance.html' ,{}, context_instance=RequestContext(request))

    else:
        return HttpResponseRedirect('/login')
