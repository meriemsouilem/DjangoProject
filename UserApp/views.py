from django.shortcuts import render
from .forms import UserRegistrationForm
from django.shortcuts import redirect 
# Create your views here.
def register(req):
  if req.method=="POST":
    form=UserRegistrationForm(req.POST)
    if form.is_valid():
      form.save()
      return redirect()
    
  else :  #kan get
    form=UserRegistrationForm()
  return render(req , "register.html",{"form":form})

def logout_view(req):
  logout(req)
  return redirect("login")