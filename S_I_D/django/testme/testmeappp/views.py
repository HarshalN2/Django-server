from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def testfun(request):
    s = '1zz789'
    print(s)
    return JsonResponse({'data':str(s)}, safe=False)
    # 

def homepage(req):
    return render(req,'index.html')