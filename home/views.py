from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Profile, Contact, Post, Donation
#Category
from django.views.generic import (DetailView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (ListView, DetailView, CreateView,UpdateView, DeleteView)
from .forms import Form, UserRegisterForm, UserUpdateForm, ProfileUpdateForm
#PostForm
from django.conf import settings

# Create your views here.
def home(request):
    return render(request, 'home.html')

def donate(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'donate.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'donate.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

def dashboard(request):
    donations = Donation.objects.filter(donor=request.user)
    recieved = Donation.objects.filter(receiver=request.user)
    context = {
        'donations': donations,
        'recieved': recieved
    }
    return render(request, 'dashboard.html')

class ProfileView(DetailView):
    model = Profile
    template_name = 'profile_view.html'
    
# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'newpost.html'

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)
    
def PostDetailView(request,pk):
    form = ""
    if request.method== 'POST':
        form=Form(request.POST)
        if form.is_valid():
            print(type(request.user))
            form.save()
            donation =Donation()
            post = get_object_or_404(Post, pk=pk)
            qty=form.cleaned_data.get('quantity')
            donation.quantity=qty
            donation.receiver= post.author
            donation.donor= request.user
            donation.category= post.category
            donation.save()
            send_mail('Corona Rangers has some great news for you',f' {donation.donor} ({request.user.email}) wants to donate  {qty} { donation.category}',settings.EMAIL_HOST_USER,[f'{post.author.email}'],fail_silently=False)
            messages.success(request, 'We have notified the NGO, thankyou for the donation.The NGO will contact you')
            return redirect('dashboard')
        else:
            pass
    else:
        form=Form()
        context = {
            "form": form,
            "post": get_object_or_404(Post, pk=pk),
        }
        return render(request,'post_detail.html',{
                "form": form,
                "post": get_object_or_404(Post, pk=pk),
            })

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content','category']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = 'donate'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile()
            # profile = Profile.objects.get(email = form.cleaned_data.get("email"))
            profile.ngo = form.cleaned_data.get("ngo")
            messages.success(request, 'Your account has been created! Please log in')
            return redirect('http://127.0.0.1:8000/login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES, 
                                   instance = request.user.profile
                                  )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('http://127.0.0.1:8000/profile')
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile.html', context)


def contact(request):
    if request.method=="POST":
        print(request)
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('phone', '')
        desc=request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, 'contact.html')

# def CategoryView(request, cats):
#     category_posts = Post.objects.filter(category=cats)
#     return render(request, 'categories.html', {'cats': cats, 'category_posts': category_posts})



