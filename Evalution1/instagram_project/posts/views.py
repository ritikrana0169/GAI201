from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

import json
from .models import Post

@csrf_exempt
def create_post(request):
    if request.method=='POST':
        data=json.loads(request.body)
        post=Post(username=data['username'],caption=data['caption'])
        post.save()
        return JsonResponse({'message':'Post SuccessFully'})
    

def view_posts(request):
    posts=Post.objects.all()
    data=[{'username':post.username,'caption':post.caption}for post in posts]
    return JsonResponse(data,safe=False)



@method_decorator(csrf_exempt,name='dispatch')
class DeletePost(View):
    def delete(self,request,post_id):
        get_object_or_404=""
        post=get_object_or_404(Post,pk=post_id)
        post.delete()
        return JsonResponse({'message':'Post Deelted'})

