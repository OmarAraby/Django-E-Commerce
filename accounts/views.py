from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate
from django.urls import reverse
from .models import Profile
from order.models import Order
from .forms import UserForm , ProfileForm
from django.contrib.auth.decorators import login_required
# Create your views here.





def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username , password=password)
            login(request, user)
            return redirect('/')
    
    else:
        form = UserCreationForm



    context = {'form':form}

    return render(request,'registration/signup.html',context)
   




@login_required(login_url='/accounts/login/')
def profile(request , slug):
    profile = get_object_or_404(Profile , slug=slug)
    # Get the latest 5 orders for the user
    latest_orders = Order.objects.filter(user=profile.user).order_by('-order_date')[:5]
    context = {'profile':profile,'latest_orders':latest_orders}

    return render(request , 'profiles/profile.html', context)







@login_required(login_url='/accounts/login/')
def profile_edit(request, slug):

    profile = get_object_or_404(Profile , slug=slug)

    if request.method=='POST':
        
        userform=UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST, request.FILES,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()

            return redirect(reverse('accounts:profile'))


    else :
        userform=UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)

    context = {'userform':userform,'profileform':profileform}

    return render(request,'profiles/profile_edit.html',context)
