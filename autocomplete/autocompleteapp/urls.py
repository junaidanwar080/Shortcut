from django.urls import path
from . import views
urlpatterns = [
    
# ------------------------------------------------------------------------------------------------
# Admin
# ------------------------------------------------------------------------------------------------
# Admin Dashboard
    path('admin_dashboard',views.Admin_Dashboard,name='Admin_Dashboard'),
# ------------------------------------------------------------------------------------------------
# Globel Shortcuts
# ------------------------------------------------------------------------------------------------
    path('',views.home_page,name='home_page'),
    path('globle_shortcut',views.shortcut,name='shortcut'),
    path('shortcut_select',views.shortcut_select),
    path('shortcut_insert',views.shortcut_insert),
    path('shortcut_load_for_update/<int:shortcut_id>',views.shortcut_load_for_update),
    path('shortcut_update',views.shortcut_update),
    path('shortcut_disable',views.shortcut_disable),
    path('shortcut_search',views.shortcut_search),
# search Shortut
    path('apply_global_shortcut',views.apply_globle_shortcut_page),
    path('apply_globle_shortcut',views.apply_globle_shortcut),
# ------------------------------------------------------------------------------------------------
# Personal Shortcuts
# ------------------------------------------------------------------------------------------------
    path('personal_shortcut',views.personal_shortcut,name='personal_shortcut'),
    path('personal_shortcut_select',views.personal_shortcut_select),
    path('personal_shortcut_insert',views.personal_shortcut_insert),
    path('personal_shortcut_search',views.personal_shortcut_search),

# search Shortut
    path('apply_personal_shortcut',views.apply_personal_shortcut_page),
    path('apply_personal_shortcut_val',views.apply_personal_shortcut_val),

# ------------------------------------------------------------------------------------------------
# User Profile
# ------------------------------------------------------------------------------------------------
# User
    path('users', views.users, name='users' ),
    path('select_all_users', views.select_all_users), 
    
# ------------------------------------------------------------------------------------------------
# Individual
# ------------------------------------------------------------------------------------------------
# Individual Dashboard
    path('individual_dashboard',views.individual_dashboard),
# ------------------------------------------------------------------------------------------------
# Individual Personal Shortcuts
# ------------------------------------------------------------------------------------------------
    path('individual_personal_shortcut',views.individual_personal_shortcut,name='individual_personal_shortcut'),
    # path('personal_shortcut_select',views.personal_shortcut_select),
    # path('personal_shortcut_insert',views.personal_shortcut_insert),

# search Shortut
    path('apply_individual_personal_shortcut',views.apply_individual_personal_shortcut),
    path('apply_individual_personal_shortcut_val',views.apply_individual_personal_shortcut_val),

# ------------------------------------------------------------------------------------------------
# Login , Logout , User Registraion
# ------------------------------------------------------------------------------------------------
    path('login',views.insert_login,name = 'login'),
    path('logout', views.logout_user , name='logout'),
    path('insert_user', views.user_registration),
    path('registration', views.registration),
    path('user_disable/<int:user_id>',views.user_disable),
    
]