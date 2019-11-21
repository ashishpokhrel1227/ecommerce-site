from django.urls import path
from .views import HomePageView, ChartData, ChartData2, ChartData3, ChartData4, ChartData5, ChartData6

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('charts/api/chart/data/', ChartData.as_view()),
    path('charts/api/chart/data2/', ChartData2.as_view()),
    path('charts/api/chart/data3/', ChartData3.as_view()),
    path('charts/api/chart/data4/', ChartData4.as_view()),
    path('charts/api/chart/data5/', ChartData5.as_view()),
    path('charts/api/chart/data6/', ChartData6.as_view()),
    
    
]
