


from django.urls import path,include



from .views import MonitorView
from .api.monitor_create_view import MonitorCreateView

urlpatterns = [
    path('', MonitorView.as_view(), name="monitor-view"),
    path('create/', MonitorCreateView.as_view(), name="monitor-create-view"),


]




