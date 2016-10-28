from django.shortcuts import render, reverse


ninja_turtles_list = {'red':"raphael.jpg", 'blue':"leonardo.jpg", 'purple':"donatello.jpg", 'orange':"Michelangelo.jpeg"}
april = 'april.jpg'
all_turtles = "tmnt.png"
# Create your views here.
def index(request):
    return render(request,
    'disappearing_ninja/index.html')

def show_turtles(request, color):
    if len(color) < 1:
        image=all_turtles
    else:
        if color in ninja_turtles_list.keys():
            image = ninja_turtles_list[color]
        else:
            image = april
    data = {"turtle":image}
    return render(request,
    'disappearing_ninja/display_turtles.html', data)
