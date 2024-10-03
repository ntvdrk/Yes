from django.urls import path
from app1.views import view2
from app1.views import view1
from app1.views import view3


urlpatterns = [
    path('view1/', view1),
    path('view2/', view2),
    path('view3/', view3)

]
