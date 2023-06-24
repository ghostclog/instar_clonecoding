from django.shortcuts import render,get_object_or_404,redirect
from djagno_instar_clone.users.models import User as user_model
from django.urls import reverse
from . import models, serializers,forms


# Create your views here.
def index(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            comment_form = forms.CommentForm()
            user = get_object_or_404(user_model, pk=request.user.id)
            following = user.following.all()
            posts = models.Post.objects.filter(
                Q(author__in=following) | Q(author=user)
            )

            serializer = serializers.PostSerializer(posts, many = True)

            return render(request,'posts/main.html',{"posts":serializer,"comment_form":comment_form})

def post_create(request):
    if request.method == 'GET':
        form = forms.CreatePostForm()
        return render(request,'posts/post_create.html',{"form":form})
    
    elif request.method == 'POST':
        if request.user.is_authenticated:
            user = get_object_or_404(user_model, pk=request.user.id)

            #image = request.FILES['image']
            #caption = request.POST['cation']
            #new_post = models.Post.objects.create(
            #    author = user,
            #    image = image,
            #    caption = caption
            #)
            #new_post.save()
            
            form = forms.CreatePostForm(request.POST,request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = user
                post.save()
            else:
                print(form.errors)

            return render(request, 'posts/main.html')
        else:
            return render(request, 'users/main.html')
        
    
def comment_create(request,post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(models.Post,pk=post_id)

        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.posts = post
            comment.save()

            return redirect(reverse('posts:index')+"#comment-" + str(comment.id))
        else:
            return render(request,'users/main.html')