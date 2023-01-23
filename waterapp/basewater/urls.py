from django.urls import include, path

from . import views
from .views import WorkerSignUpView, CustomLoginView, TaskList
from django.contrib.auth.views import LogoutView

urlpatterns =[
    path('', views.test, name='home'),
    # path('signup/', views.signup, name='singup'),
    # path('', include('classroom.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    path('signup/', WorkerSignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('reports/', TaskList.as_view(), name='report' ),
    # path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
]
