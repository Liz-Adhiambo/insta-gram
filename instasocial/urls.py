from django.urls import path
from . import views
from.views import AddCommentView

urlpatterns = [
    path('', views.index, name='index'),
    path('settings/', views.settings, name='settings'),
    path('uploads/', views.uploads, name='uploads'),
    path('uploads/upload', views.upload, name='upload'),
    path('like-post', views.like_post, name='like-post'),
    path('profile/<str:pk>', views.profile, name='profile'),
    path('search', views.search, name='search'),
    path('follow', views.follow, name='follow'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('post/<str:pk>/comment/', AddCommentView.as_view(), name='comment'),
    path('post/<str:pk>/',views.view_post, name='viewpost'),
    path('add_comment/<str:post_id>/',views.add_comment, name='add_comment'),

    
]