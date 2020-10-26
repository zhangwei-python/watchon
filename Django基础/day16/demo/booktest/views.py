from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from booktest.models import BookInfo, HeroInfo

class BookView(View):

    def get(self, request):

        b1 = BookInfo.objects.get(id=1)

        dict = {
            "book": b1.btitle
        }

        return render(request, "index.html", dict)

