from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return  render(request, 'home.html')

def analyze(request):
    djtext = request.POST.get('text','default')
    cr = request.POST.get('removepunc','off')
    uc = request.POST.get('uppercase','off')
    rnl = request.POST.get('removenl','off')
    esr = request.POST.get('extraspacer','off')
    cc = request.POST.get('charcount','off')
    
    if cr == 'on' :
        analyzed = ""
        panctuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in panctuation:
                analyzed = analyzed + char
        params = {'purpose':'removed puctuation','analyzed_text': analyzed}
        djtext = analyzed
        
    if uc == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'removed puctuation','analyzed_text': analyzed} 
        djtext = analyzed
        
    elif rnl == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n':
                analyzed = analyzed + char
        params = {'purpose':'removed puctuation','analyzed_text': analyzed}
        djtext = analyzed
        
    elif esr == 'on':
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char 
        params = {'purpose':'removed puctuation','analyzed_text': analyzed}
        djtext = analyzed
        
    elif cc == 'on':
        analyzed = 0
        for char in djtext:
            analyzed += 1 
        
    params = {'purpose':'removed puctuation','analyzed_text': analyzed}
    return render(request,'result.html',params)

