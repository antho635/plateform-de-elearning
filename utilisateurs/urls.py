from django.urls import path
from utilisateurs.views import acceuil, user_login, user_logout, register, curriculum, contact, cv_design, \
    eco_demenagement, eco_demenagement_details, la_corddee_numerique, pizzeria

urlpatterns = [
    path('', acceuil, name="acceuil"),
    path('register/', register, name="register"),
    path('login/', user_login, name="login"),
    path('logout/', user_logout, name="logout"),
    path('curriculum/', curriculum, name='curriculum'),
    path('contact/', contact, name='contactForm'),
    path('projet/cv_design/', cv_design, name='cv_design'),
    path('portfolio/eco_demenagement', eco_demenagement, name='eco_demenagement'),
    path('details/eco-demenagement-details', eco_demenagement_details, name='eco_demenagement_details'),
    path('portfolio/la_corddee_numerique', la_corddee_numerique, name='la_corddee_numerique'),
    path('portfolio/pizzeria', pizzeria, name='pizzeria'),
]