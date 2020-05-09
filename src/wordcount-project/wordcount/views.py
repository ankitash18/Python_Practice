from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']

    wordlist = fulltext.split()
    worddict = {}

    for word in wordlist:
        if word in worddict:
            worddict[word] += 1
        else:
             worddict[word] = 1


    sorted_words = sorted(worddict.items(),reverse=True)                
    
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sorted_words':sorted_words})
    
