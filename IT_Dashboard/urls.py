from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'it'

urlpatterns = [
# ######################################### Basic  ################################################## #

	url(r'^$',views.index, name='index'),
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^dashboard/',views.index, name='dash'),

# ################################# Registration and Login  ########################################## #
    url(r'^useregister/$',views.register_view.as_view(), name='register'),
    url(r'^userlogin/$',views.LoginFormView.as_view(), name='login'),
    url(r'^logout/$',views.user_logout, name='logout'),
    url(r'^change_password/$',views.change_password, name='change_password'),

# ################################# User Profile Related  ########################################## #

    url(r'^profile/add/$',views.ProfileCreate.as_view(), name='profile-add'),    
    url(r'^profile/(?P<pk>[0-9]+)/update/$',views.ProfileUpdate.as_view(), name='profile-update'),    
    url(r'^profile/(?P<pk>[0-9]+)/delete/$',views.ProfileDelete.as_view(), name='profile-delete'),
    url(r'^groupflow/$',views.group_flow, name='group-flow'),
# ################################# Introduction  ########################################## #

    url(r'^category/type/(?P<cid>[0-9]+)/$',views.CategoryLanding, name='category-type'),
    url(r'^category/add/$',views.CategoryCreate.as_view(), name='category-add'),    
    url(r'^category/(?P<pk>[0-9]+)/update/$',views.CategoryUpdate.as_view(), name='category-update'),    
    url(r'^category/(?P<pk>[0-9]+)/delete/$',views.CategoryDelete.as_view(), name='category-delete'),

# ################################# Timeline Get Contents  ########################################## #

    url(r'^get/allUserListForTimeline/$', views.getUserContent),
    url(r'^get/(?P<cid>[0-9]+)/introduction/$', views.getIntroductionContent),
    url(r'^get/(?P<cid>[0-9]+)/troubleshoot/$', views.getTroubleshootContent),
    url(r'^get/(?P<cid>[0-9]+)/task/$', views.getTaskContent),
    url(r'^get/UserById/(?P<uid>[0-9]+)/$', views.getUserById),

# ################################# Introduction  ########################################## #
    url(r'^category/(?P<cid>[0-9]+)/introduction/$',views.IntroductionLanding, name='intro'),    
    url(r'^category/introduction/add/$',views.IntroductionCreate.as_view(), name='intro-add'),    
    url(r'^category/(?P<cid>[0-9]+)/introduction/(?P<pk>[0-9]+)/update/$',views.IntroductionUpdate.as_view(), name='intro-update'),    
    url(r'^category/(?P<cid>[0-9]+)/introduction/(?P<pk>[0-9]+)/delete/$',views.IntroductionDelete.as_view(), name='intro-delete'),
    url(r'^category/introduction/(?P<iid>[0-9]+)/detail/$', views.IntroDetail, name='intro-detail'),

    url(r'^category/(?P<cid>[0-9]+)/introduction/(?P<iid>[0-9]+)/subintroduction/add/$',views.SubIntroductionCreate.as_view(), name='sub-intro-add'),    
    url(r'^category/(?P<cid>[0-9]+)/introduction/(?P<iid>[0-9]+)/subintroduction/(?P<pk>[0-9]+)/update/$',views.SubIntroductionUpdate.as_view(), name='sub-intro-update'),    
    url(r'^category/(?P<cid>[0-9]+)/introduction/(?P<iid>[0-9]+)/subintroduction/(?P<pk>[0-9]+)/delete/$',views.SubIntroductionDelete.as_view(), name='sub-intro-delete'),

# ################################# Tasks ########################################## #

    url(r'^category/(?P<cid>[0-9]+)/task/$',views.TaskLanding, name='task'),    
    url(r'^category/task/add/$',views.TaskCreate.as_view(), name='task-add'),    
    url(r'^category/(?P<cid>[0-9]+)/task/(?P<pk>[0-9]+)/update/$',views.TaskUpdate.as_view(), name='task-update'),    
    url(r'^category/(?P<cid>[0-9]+)/task/(?P<pk>[0-9]+)/delete/$',views.TaskDelete.as_view(), name='task-delete'),
    url(r'^category/task/(?P<tsid>[0-9]+)/detail/$', views.TaskDetail, name='task-detail'),

    url(r'^category/(?P<cid>[0-9]+)/task/(?P<tsid>[0-9]+)/subtask/add/$',views.SubTaskCreate.as_view(), name='sub-intro-add'),    
    url(r'^category/(?P<cid>[0-9]+)/task/(?P<tsid>[0-9]+)/subtask/(?P<pk>[0-9]+)/update/$',views.SubTaskUpdate.as_view(), name='sub-task-update'),    
    url(r'^category/(?P<cid>[0-9]+)/task/(?P<tsid>[0-9]+)/subtask/(?P<pk>[0-9]+)/delete/$',views.SubTaskDelete.as_view(), name='sub-task-delete'),


# ################################# Troubleshoots ########################################## #

    url(r'^category/(?P<cid>[0-9]+)/troubleshoot/$',views.TroubleshootLanding, name='trouble'),    
    url(r'^category/troubleshoot/add/$',views.TroubleshootCreate.as_view(), name='trouble-add'),    
    url(r'^category/(?P<cid>[0-9]+)/troubleshoot/(?P<pk>[0-9]+)/update/$',views.TroubleshootUpdate.as_view(), name='trouble-update'),    
    url(r'^category/(?P<cid>[0-9]+)/troubleshoot/(?P<pk>[0-9]+)/delete/$',views.TroubleshootDelete.as_view(), name='trouble-delete'),
    url(r'^category/troubleshoot/(?P<trid>[0-9]+)/detail/$', views.TroubleDetail, name='trouble-detail'),

    url(r'^category/(?P<cid>[0-9]+)/troubleshoot/(?P<trid>[0-9]+)/subtroubleshoot/add/$',views.SubTroubleshootCreate.as_view(), name='sub-trouble-add'),    
    url(r'^category/(?P<cid>[0-9]+)/troubleshoot/(?P<trid>[0-9]+)/subtroubleshoot/(?P<pk>[0-9]+)/update/$',views.SubTroubleshootUpdate.as_view(), name='sub-trouble-update'),    
    url(r'^category/(?P<cid>[0-9]+)/troubleshoot/(?P<trid>[0-9]+)/subtroubleshoot/(?P<pk>[0-9]+)/delete/$',views.SubTroubleshootDelete.as_view(), name='sub-trouble-delete'),

# ################################# NOT Verified Yet ########################################## #

    url(r'^users/$',views.ContactListView.as_view(), name='users-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.ContactDetailView.as_view(), name='userdetails'),

    url(r'^Map/$',views.aidedMaps, name='map'),
    url(r'^timeline/$',views.aidedTimeline, name='timeline'),
    url(r'^timeline2/$',views.aidedTimeline2, name='timeline2'),
# ################################# NOT Verified Yet ########################################## #

    url(r'^graphChart/$',views.aidedGraphChart, name='graph-chart'),
    url(r'^graphFlot/$',views.aidedGraphFlot, name='flot-chart'),
    url(r'^graphMorris/$',views.aidedGraphMorris, name='morris-chart'),
    url(r'^graphPeity/$',views.aidedGraphPeity, name='peity-chart'),
    url(r'^graphRickshaw/$',views.aidedGraphRickshaw, name='rickshaw-chart'),
    url(r'^graphSparkline/$',views.aidedGraphSparkline, name='sprakline-chart'),


    
    # url(r'^Product/add/$',views.ProductCreate.as_view(), name='product-add'),
    # url(r'^Product/(?P<pk>[0-9]+)/update/$',views.ProductUpdate.as_view(), name='product-update'),    
    # url(r'^Product/(?P<pk>[0-9]+)/delete/$',views.ProductDelete.as_view(), name='product-delete'),

]
