import copy
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def recipe_list_view(request):
    data = ''
    for recipe in DATA:
        url = reverse(recipe, kwargs={"recipe_name": recipe})
        data += f'<div><a href={url}>{recipe.capitalize()}</a></div>'
    return HttpResponse(data)


def recipe_view(request, recipe_name):
    servings = int(request.GET.get('servings', 1))
    data = copy.deepcopy(DATA)
    recipe = {recipe_name: data[recipe_name]}
    for ingredient, contein in recipe[recipe_name].items():
        recipe[recipe_name][ingredient] = round(servings * contein, 2)
    context = {
        'recipe': recipe[recipe_name]
    }
    return render(request, 'calculator/index.html', context)
