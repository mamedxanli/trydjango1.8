from django.shortcuts import render
from .forms import SignUpForm
def home(request):
    title = 'Welcome'
    form = SignUpForm(request.POST or None)
    context = {
         "title": title,
         'form': form
     }

    if form.is_valid():
        #form.save()
        #print request.POST['email']
        instance = form.save(commit=False)

        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        # if not instance.full_name == None:
        #     instance.full_name = 'Justin'
        # instance.save()
        context = {
            "title": "Thank you"
        }

    return render(request, "home.html", context)
