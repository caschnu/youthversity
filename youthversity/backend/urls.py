from django.urls import include, path

from . import views
from youthversity import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required
from ckeditor_uploader.views import upload
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('', include('django.contrib.auth.urls')),
    path('feed/', views.feed, name='feed'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:id>/subtopics/', views.subtopics, name='subtopics'),
    path('projects/filter/', views.projects_filter, name='projects_filter'),
    path('projects/all/', views.projects_all, name='projects_all'),
    path('projects/my/', views.projects_my, name='projects_my'),
    path('projects/new/', views.projects_new, name='projects_new'),
    path('projects/<int:id>/', views.projects_id, name='projects_id'),
    path('projects/<int:id>/save/', views.save_project, name='save_post'),
    path('projects/<int:id>/report/', views.report, name='report'),
    path('projects/<int:id>/upvote/', views.upvote_post, name='upvote_post'),
    path('projects/<int:id>/new_comment/',
         views.project_new_comment, name='project_new_comment'),
    path('projects/<int:id>/file/', views.projects_file, name='projects_file'),
    path('projects/saved/', views.projects_saved, name='projects_saved'),
    path('comments/my/', views.comments_my, name='comments_my'),
    # path('help/', views.help, name='help'),
    path('faq/', views.faq, name='faq'),
    path('imprint/', views.imprint, name='imprint'),
    path('privacy/', views.privacy, name='privacy'),
    path('me/', views.me, name='me'),
    path('rules/', views.rules, name='rules'),
    path('project_guidelines/', views.project_guidelines,
         name='project_guidelines'),
    path('about_us/', views.about_us, name='about_us'),
    path('copyright/', views.copyright, name='copyright'),
    path('profile/', views.me, name='profile'),
    path('comment/<int:id>/report', views.report_comment, name='report_comment'),
    path('upvote_comment/<int:id>/', views.upvote_comment, name='upvote_comment'),
    path('projects/popular/', views.projects_popular, name='projects_popular'),
    path('report/all/', views.all_reports, name='all_reports'),
    path('report/pending/', views.pending_reports, name='pending_reports'),
    path('report/<int:id>', views.reports_id, name='reports_id'),
    url(r'^ckeditor/upload/', login_required(upload), name='ckeditor_upload'),
    path('ckeditor/', include('ckeditor_uploader.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
