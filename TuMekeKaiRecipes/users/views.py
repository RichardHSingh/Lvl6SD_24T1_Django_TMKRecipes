from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
# from .models import UserProfile
from . import forms
from .forms import UserProfileForm


# Create your views here.
def register(request):  
    if request.method == "POST":
        form = forms.UserCreationForm(request.POST) #calling on the def userRegistrationForm created in forms.py
        if form.is_valid(): # validating user into            
            form.save() # should save the details into the server   
            username = form.cleaned_data.get('username') # states which data to get and put into django server
            messages.success(request, f" Congratulations {username}. Your account has been created. Please login") # successful message prompt
            return redirect('user-login') # takes them back to index page
    else:
        form = forms.UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form})



# adds functionallity to functions
@login_required()
def profile(request):
    return render(request, 'users/profile.html')



def update_profile(request):
    user_profile = request.user.userprofile
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page after updating
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'update_profile.html', {'form': form})

# @receiver(post_save, sender = User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# @receiver(post_save, sender = User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.userprofile.save()