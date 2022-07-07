from django.urls import path, re_path
from . import views
from django.views.static import serve
from django.conf import settings

app_name = 'learning_logs'
urlpatterns = [
	path('', views.index, name='index'),
	path('topics/', views.topics, name='topics'),
	path('new_topic/', views.new_topic, name='new_topic'),
	path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
	path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
	path('open_topic/<int:topic_id>', views.open_topic, name='open_topic'),
	path('delete_topic/<int:topic_id>', views.delete_topic, name='delete_topic'),
	path('delete_entry/<int:entry_id>', views.delete_entry, name='delete_entry'),
	re_path('^static/(?P<path>.*)/$', serve, {'document_root': settings.STATIC_ROOT})
]
