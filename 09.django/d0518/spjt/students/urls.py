from django.urls import include, path
from . import views

app_name='students'   # url이동이 아니라 페이지내에서 이동할 때 사용됨
urlpatterns = [
    path('stuWrite/',views.stuWrite,name='stuWrite'), # 학생등록페이지
    path('stuWriteOk/',views.stuWriteOk,name='stuWriteOk'), # 학생등록저장
    path('stuList/',views.stuList,name='stuList'), # 학생전체리스트
    path('<str:s_no>/stuView/',views.stuView,name='stuView'),  # 학생상세보기
    path('<str:s_no>/stuUpdate/',views.stuUpdate,name='stuUpdate'), # 학생수정
    path('stuUpdateOk/',views.stuUpdateOk,name='stuUpdateOk'), # 학생수정저장
    path('<str:s_no>/stuDelete/',views.stuDelete,name='stuDelete'), # 학생삭제
]
