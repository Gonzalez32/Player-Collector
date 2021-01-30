from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Player
from .forms import MatchForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def players_index(request):
    players = Player.objects.all()
    return render(request, 'players/index.html', {'players': players} )

# update this view function
def players_detail(request, player_id):
    player = Player.objects.get(id=player_id)
    # instantiate MatchForm to be rendered in the template 
    match_form = MatchForm()
    return render(request, 'players/detail.html', {
        'player': player, 'match_form': match_form
    })

# add this new fucntion below Player_details
def add_match(request, player_id):
    form = MatchForm(request.POST)
    if form.is_valid():
        new_match = form.save(commit=False)
        new_match.player_id = player_id
        new_match.save()
    return redirect('detail', player_id=player_id)

class PlayerCreate(CreateView):
    model = Player
    fields = '__all__'

class PlayerUpdate(UpdateView):
    model = Player
    # Name won't be within the fields NO renaming at this moment
    fields = ['team', 'position', 'description', 'age']

class PlayerDelete(DeleteView):
    model = Player
    success_url = '/players/'