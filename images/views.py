from django.shortcuts import render

from django.views import View
from django.http.response import HttpResponse
from django.middleware.csrf import get_token
from .models import Image

class UploadView(View):
    def get(self, request):
            html = """
                <form method="post" enctype="multipart/form-data">
                <input type='text' style='display:none;' value='%s' name='csrfmiddlewaretoken'/>
                <input type="file" name="image" accept="image/*">
                <button type="submit">Upload Image</button>
                </form>
            """ % (get_token(request))
            return HttpResponse(html)
    def post(self, request):
            image = request.FILES['image']
            image_model = Image.objects.create(
                   pic = image
            ) 

            image_model.save(using = "media")
