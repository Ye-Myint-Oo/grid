from django.urls import path
from . import views

urlpatterns = [
    path('queue/<str:queue_name>/request/message', views.QueryRequestView.as_view(), name='query-request'),
    path('queue/<str:queue_name>/update/message', views.UpdateMessageView.as_view(), name='update-message'),
    path('queue/<str:queue_name>/batch/message', views.BatchDispatchView.as_view(), name='batch-dispatch'),
]