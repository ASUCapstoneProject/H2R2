from django.urls import include, path

from . import views
from .views import WorkerSignUpView, CustomLoginView

urlpatterns =[
    path('', views.test, name='home'),
    # path('signup/', views.signup, name='singup'),
    # path('', include('classroom.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    path('signup/', WorkerSignUpView.as_view(), name='student_signup'),
    path('login/', CustomLoginView.as_view(), name='login')
    # path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
]
