# I have created this file
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def analyze(request):
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('fullcaps', 'off')
    remline = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    purpose = 'Operations performed'
    if removepunc is not 'off':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
    if uppercase is not 'off':
        analyzed = djtext.upper()
        djtext = analyzed
    if remline is not 'off':
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        djtext = analyzed
    if extraspaceremover is not 'off':
        analyzed = ''
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == ' '):
                analyzed = analyzed + char
        djtext = analyzed
    analyzed = 0
    for e in djtext:
        if e is not " ":
            analyzed = analyzed + 1
    count = analyzed
    params = {'purpose': purpose, 'analyzed_text': djtext, 'count': count}
    return render(request, 'analyze.html', params)
