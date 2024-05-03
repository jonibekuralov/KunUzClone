# from django.urls import path
from django.urls import path
from django.views.generic import TemplateView

from .views import news_list, news_detail, HomePageView, single, SubjectNewsView, WorldNewsView, \
    IqtisodiyotNewsView, SportNewsView, LocalNewsView, ContactPageView, NewsCreateView, NewsDeleteView, NewsUpdtaeView, \
    admin_page, search_view

urlpatterns = [
    path("", HomePageView.as_view(), name="homepage"),
    path('adminpage/', admin_page, name='admin_page'),
    #     path("Uzbekistan", , name="uzbekistan"),
    #     path("Fan_texnika", Fan_texnikaPageview, name="fan_texnika"),
    #     path("iqtisodiyot/", IqtisodiyotPageview, name="iqtisodiyot"),
    #     path("Sport", SportPageview, name="sport"),
    #     path("Jamiyat", JamiyatPageview, name="jamiyat"),
    #     path("Jahon", JahonPageview, name="jahon"),
    #     path("single/", single, name="single"),
    #     path("News", news_list, name='news_all'),
    #     path("news/<int:id>/", news_detail, name='news_detail_page'),
    #     path("news/<int:id>/", news_detail, name='news_detail_page'),
    #     path("contact/", ContactPageView.as_view() , name="contact"),
    path('news/<slug:news>', news_detail, name='news_detail_page'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<slug>/edit/', NewsUpdtaeView.as_view(), name='news_update'),
    path('news/<slug>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('contact/', ContactPageView.as_view(), name='contact-us'),
    path('Uzbekistan/', LocalNewsView.as_view(template_name='news/local.html'), name="Uzbekistan"),
    path('Jahon/', WorldNewsView.as_view(template_name='news/jahon.html'), name="Jahon"),
    path('Fan_texnika/', SubjectNewsView.as_view(template_name='news/fan_texnika.html'), name="Fan_texnika"),
    path('Sport/', SportNewsView.as_view(template_name='news/Sport.html'), name="Sport"),
    path('Iqtisodiyot/', IqtisodiyotNewsView.as_view(template_name='news/Iqtisodiyot.html'), name="Iqtisodiyot"),
    path('searchresult/',search_view, name="search_results"),
]
