from django.urls import path
from . import views



urlpatterns = [
# Main page URLs
    path('',views.home_page,name='home_page'),
    path('shortcut',views.shortcut,name='shortcut'),
    path('shortcut_select',views.shortcut_select),
    path('shortcut_insert',views.shortcut_insert),
    path('shortcut_load_for_update/<int:shortcut_id>',views.shortcut_load_for_update),
    path('shortcut_update',views.shortcut_update),
    path('shortcut_disable',views.shortcut_disable),
    path('shortcut_search',views.shortcut_search),
# search Shortut
    path('search_shortcut',views.search_shortcut),
    # path('load_all_accounts',views.load_all_accounts),
    
    path('sell_item_load',views.sell_item_load),
    
]