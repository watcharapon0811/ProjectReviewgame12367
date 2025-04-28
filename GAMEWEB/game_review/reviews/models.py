from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=200)
    poster = models.ImageField(upload_to='game_posters/')

    def __str__(self):
        return self.title

class Review(models.Model):
    game = models.ForeignKey(Game, related_name='reviews', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.game.title} - {self.rating} Stars"
