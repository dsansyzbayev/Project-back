from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from .views import *

urlpatterns = [
    path('register/', register),
    path('login/', obtain_jwt_token),
    path('categories/', category_list, name='all recipes'),
    path('categories/<int:category_id>/', category_detail, name='get one recipe'),
    path('categories/<int:category_id>/recipes/', RecipeByCategoryAPIView.as_view(), name='recipes by categories'),
    path('recipes/', RecipeListAPIView.as_view(), name='all recipes'),
    path('recipes/<int:recipe_id>/', RecipeDetailAPIView.as_view(), name='one recipe'),
    path('recipes/<int:recipe_id>/comments/', CommentsByRecipeAPIView.as_view(), name='comments by recipe'),
    path('recipes/<int:recipe_id>/follow/', FollowRecipeAPIView.as_view(), name='follow recipe'),
    path('recipes/<int:recipe_id>/like/', LikeRecipeAPIView.as_view(), name='like recipe'),
    path('recipes/top_ten/', TopTenRecipesAPIView.as_view(), name='top ten'),
    path('recipes/search/', RecipeSearchAPIView.as_view(), name="search_results") #to make search in postman write following query '/?search=food'
]
