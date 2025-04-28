from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Review

def game_list(request):
    games = Game.objects.all()
    return render(request, 'reviews/game_list.html', {'games': games})

def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if request.method == 'POST':
        rating = request.POST.get('rating')
        comment = request.POST.get('comment')
        if rating and comment:
            Review.objects.create(game=game, rating=rating, comment=comment)
            return redirect('game_detail', pk=pk)
    return render(request, 'reviews/game_detail.html', {'game': game})

def review_game(request):
    games = Game.objects.all()
    return render(request, 'reviews/review_game.html',{'games': games})
