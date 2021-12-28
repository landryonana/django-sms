from django.urls import path
from django.contrib.auth import views as auth_views

from evangelisation import views



app_name="notification"


urlpatterns = [
    path('messages/', 
        views.notification_app_index, 
        name="notification_app_index"
    ),

    path('messages/<int:pk>/detail', 
        views.notification_app_index, 
        name="notification_app_index"
    ),

    path('messages/<int:pk>/supprimer', 
        views.notification_app_delete, 
        name="notification_app_delete"
    ),

    path('messages/recherche', 
        views.notification_app_recherche, 
        name="notification_app_recherche"
    ),

    path('personnes/ajouter', 
        views.notification_app_ajouter_personne, 
        name="notification_app_ajouter_personne"
    ),

    path('personnes/<int:pk>/modifier', 
        views.notification_app_detail_personne, 
        name="notification_app_detail_personne"
    ),
    

    path('personnes/<int:pk>/supprimer', 
        views.notification_app_supprimer_personne, 
        name="notification_app_supprimer_personne"
    ),
            
]
