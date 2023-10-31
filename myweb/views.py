from django.shortcuts import render


# @login_required
def index(request):
    # return HttpResponse('ok')
    return render(request, 'index.html', {'rtl': '欢迎欢迎'})
