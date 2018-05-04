from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        print(link)
        make_new_url = 'http://player.trunguit.net/play?url=' + link
        return redirect(make_new_url)
    return render(request, 'phim/index.html')

def video(request):
    if request.method == 'POST':
        link = request.POST.get('link')
        return render(request, 'phim/video.html', {"link":link})
    return render(request, 'phim/video.html')