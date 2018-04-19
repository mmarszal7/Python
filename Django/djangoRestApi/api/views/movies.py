from django.http import JsonResponse
from django.db.models import Avg, Count, Func
from ..models import Movie


def new_movie(request):
    if request.method != 'POST':
        pass

    # get movie id and title
    id = request.POST.get('id', '')
    title = request.POST.get('title', '')

    # save new movie
    m = Movie(source_id = id, title = title)
    try:
        m.save()
    except Exception as e:
        return JsonResponse({
            'status': 'fail',
            'data': {
                'message': str(e) if type(e) == ValueError else 'Error while saving movie'
            }
        }, status=500)

    return JsonResponse({
        'status': 'success',
        'data': {
            'title': m.title
        }
    })


def movie_details(request, movie_id):
    if request.method != 'GET':
        pass

    # get movie
    try:
        m = Movie.objects.get(source_id=movie_id)
    except Movie.DoesNotExist:
        return JsonResponse({
            'status': 'success',
        })

    return JsonResponse({
        'status': 'success',
    })

class Round(Func):
    function = 'ROUND'
    template='%(function)s(%(expressions)s, 1)'

def movies_summary(request):
    if request.method != 'GET':
        pass

    # get all requested movie ids
    movie_ids = request.GET.get('ids', '').split(',')

    m = Movie.objects.filter(source_id__in=movie_ids).values()

    movies = {}
    for movie in list(m):
        movies[movie.get('source_id')] = movie

    return JsonResponse({
        'status': 'success',
        'data': {
            'movies': movies
        }
    })
