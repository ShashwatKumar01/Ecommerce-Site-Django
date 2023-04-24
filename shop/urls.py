from django.urls import path,include
from . import views

urlpatterns = [
    path('index/',views.index,name='index1'),
    path('products/',views.products,name='product'),
    path('',views.index,name='homepage'),
    path('form/',views.form,name='form'),
    path('details/',views.details,name='details')

    # path("",include('views.index'))

]
