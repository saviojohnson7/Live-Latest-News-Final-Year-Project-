from django.shortcuts import render
import requests

def home(request):
	src = "google-news"
	try:
		a1 = "https://newsapi.org/v2/top-headlines"
		a2 = "?sources=" + "google-news"
		a3 = "&apiKey=" + "41a051464f6944478ff59b949559bcb8"
		
		wa = a1 + a2 + a3
		res = requests.get(wa)
		data = res.json()
		info = data['articles']
		return render(request, "home.html", {"msg":info})		
	
	except Exception as e:
		return render(request, "home.html")				

	return render(request, "home.html")

def news(request):
	if request.POST.get("src") and request.POST.get("btn"):	
		src = request.POST.get("src")
		try:
			a1 = "https://newsapi.org/v2/top-headlines"
			a2 = "?sources=" + src
			a3 = "&apiKey=" + "41a051464f6944478ff59b949559bcb8"
			
			wa = a1 + a2 + a3
			res = requests.get(wa)	
			data = res.json()
			info = data['articles']
			
			return render(request, "news.html", {"msg":info, "src":src})
		
		except Exception as e:
			return render(request, "news.html", {"msg": Issue + str(e)})

	else:
		return render(request, "news.html")

def argentina(request):

	if request.GET.get("src") and request.GET.get("btn"):
		try:
			src= request.GET.get("src")
			a1 = "https://newsapi.org/v2/top-headlines"
			a2 = "?sources=" + src
			a3 = "&apiKey=" + "41a051464f6944478ff59b949559bcb8"
			wa = a1 + a2 + a3 
			res= requests.get(wa)
			data = res.json()
			info = data['articles']
			
			return render(request, "argentina.html", {"msg":info, "src":src})
		except Exception as e:
			return render(request, "argentina.html", {"msg": "issue" + str(e)})

	else:
		return render(request, "argentina.html")