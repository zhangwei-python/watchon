from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View


class Template(View):

    def get(self, request):
        print("GET 请求返回模板")
        # return HttpResponse()
        # return render(request, "index.html")

        dict = {
            'name': "xiaoming",
            'age': 20
        }

        return render(request, "index.html", dict)
