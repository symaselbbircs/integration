from django.shortcuts import render, redirect, reverse
from django.utils.safestring import mark_safe
from random import randrange
from datetime import datetime

def fetch_money(smallest,largest):
    return randrange(smallest,largest)

def build_activity(building,money):
    date = datetime.now().strftime("%Y/%m/%d %I:%M %p")
    response = "<p"
    if money > 0:
        response += " class='gained_money'>Earned {} golds from the {}! ({})</p>".format(money,building,date)
    elif money < 0:
        response += " class='lost_money'>Entered a {} and lost {} golds...Yikes.. ({})</p>".format(building,money,date)
    else:
        response += ">Entered a {} and broke even! Be careful, you may not be so lucky next time... ({})</p>".format(building,date)
    return response


def get_money(building):
    if building == "farm":
        money = fetch_money(10,21)
    elif building == "cave":
        money = fetch_money(5,11)
    elif building == "house":
        money = fetch_money(2,6)
    elif building == "casino":
        money = fetch_money(-50,51)
    return money
# Create your views here.
def index(request):
    if 'my_gold' not in request.session:
        request.session['my_gold'] = 0
    if 'log' not in request.session:
        request.session['log'] = []
    return render(request,
    'ninjagold/index.html')

def process_money(request, building):
    if building == "":
        print "Building field is empty!"
    if request.method == "POST":
        money = get_money(building)
        request.session['my_gold'] += money
        request.session['log'].append(build_activity(building,money))
        request.session['display_log'] = mark_safe("\n".join(request.session["log"]))
    return redirect(reverse("main_gold"))
