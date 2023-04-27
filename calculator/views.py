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


def omlet(request):
    data = DATA.copy()
    servings = int(request.GET.get('servings', 1))
    omlet_recipe = {'omlet': data['omlet']}
    for ingredient, contein in omlet_recipe['omlet'].items():
        omlet_recipe['omlet'][ingredient] = round(servings * contein, 2)
    context = {
        'recipe': omlet_recipe['omlet'],
    }
    return render(request, 'calculator/index.html', context)


def pasta(request):
    context = {
        'recipe': DATA['pasta']
    }
    return render(request, 'calculator/index.html', context)


def buter(request):
    context = {
        'recipe': DATA['buter']
    }
    return render(request, 'calculator/index.html', context)
