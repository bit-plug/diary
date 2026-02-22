from django.shortcuts import render, redirect
from django.contrib.auth import logout, login , authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def logout_view(request):
    '''log out user'''
    logout(request)
    return redirect('learning_logs:index')

def register(request):
    if request.method != 'POST':
        '''no post data submitted: create an empty form'''
        form = UserCreationForm()
    else:
        '''post data submitted , process the data'''
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            '''log in the user and redirect user to home page'''
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return redirect('learning_logs:index')
        
    context = {'form':form}
    return render(request, 'registration/register.html', context)
