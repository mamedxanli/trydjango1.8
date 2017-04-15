from django.shortcuts import render

def home(request):
    title = 'My Title {}'.format(request.user)
    context = {
        "title": title

    }
    return render(request, "home.html", context)
