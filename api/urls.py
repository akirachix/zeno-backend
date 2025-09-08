from django.urls import path, include
from .views import AgentListCreateView, AgentRetrieveUpdateDestroyView
from rest_framework.routers import DefaultRouter
from .views import ToolViewSet
router = DefaultRouter()
router.register(r'tools', ToolViewSet)
urlpatterns = [
    path('agents/', AgentListCreateView.as_view(), name='agent-list-create'),
    path('agents/<int:agent_id>/', AgentRetrieveUpdateDestroyView.as_view(), name='agent-detail'),
    path('', include(router.urls))
]
