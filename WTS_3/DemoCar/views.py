from django.shortcuts import render, render_to_response

# Create your views here.
def index(request):
    return render_to_response('index.html')

def movie(request):
    return render_to_response("movie.html")

def racing(request):
    return render_to_response("racing.html")

def contact(request):
    message = ""
    if request.method == "POST":
        username = request.POST.get("username", None)
        comment = request.POST.get("comment", None)
        if comment =="":
            message = username +" 您好!!" + " 我們期待你的留言，請勿空白留言。"
        else:
            message = username +" 您好!!" + "  感謝留言，我們會盡快回復，"
    return render(request,"contact.html",{'message': message })

def show(request):
    return render_to_response("show.html")

def header(request):
    return render_to_response("header.html")

def footer(request):
    return render_to_response("footer.html")

