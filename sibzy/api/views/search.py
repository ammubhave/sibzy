import os
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from sibzy.api.models import *
from django.db.models import Q
import json, operator

# Returns list of search result objects
def search(request, q):
    #dbDishQ = Q(name__icontains=q)
    #
    #if request.user.is_authenticated():        
    #    dbDishQDishCategoryStrong = reduce(operator.and_, [Q(category=c.id) for c in request.user_profile.dish_category_strong])
    #    dbDishQ &= dbDishQDishCategoryStrong
    #    
    #dishes = Dish.objects.filter(dbDishQ)
    
    restaurants = Restaurant.objects.filter(name__icontains=q)
    return HttpResponse(json.dumps([json.loads(r.json()) for r in restaurants]))