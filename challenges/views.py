from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    'january': "This works!",
    'february': "This works - february!",
    'march': 'Learn Django',
    'april': 'Learn Python',
    'may': 'Do aa training',
    'june': 'Ride a bike',
    'july': 'Learn c++',
    'august': 'Learn JAVA',
    'september': 'Go to the gym',
    'october': 'Learn Swift',
    'november': 'Learn Rust',
    'december': None,
}

# Create your views here.


def index(request):
    list_items = []
    months = list(monthly_challenges.keys())

    return render(request, 'challenges/index.html', {
        "months": months,
    })


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('Invalid month')

    redirect_month = months[month - 1]
    redirect_url = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_url)


def monthly_challenge(request, month):
    challenge_text = None
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            'text': challenge_text,
            'month_name': month,
        })
    except:
        raise Http404()
