
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
	return render(request , 'home.html' )

def count(request):
	my_text= request.GET["mytext"]
	text_in_split=my_text.split()
	word= {}
	for x in text_in_split:
		if x in word:
			word[x] += 1
		else:
			word[x] = 1

	return render(request, 'counted.html',{'splitedText':text_in_split,'wordList' : sorted(list(word.items()))})

def about(request):
	return render(request , 'about.html')      