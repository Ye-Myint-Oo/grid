from django.urls import path
from . import views

urlpatterns = [
    path('<str:endpoint>/reply/message', views.QueryResponseView.as_view(), name='query-response'),
    path('<str:endpoint>/update/message', views.UpdateMessageView.as_view(), name='update-message'),
    path('<str:endpoint>/batch/message', views.BatchDispatchView.as_view(), name='batch-dispatch'),
    # Other URL patterns
]