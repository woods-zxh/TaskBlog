from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.conf import settings
##POST隐性传递通常使用隐藏的form
##文件上传到的url
## MEDIA_URL ='/media/'
## MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')

urlpatterns =[
    ##关于用户
    url(r'^$', views.index, name='index'),#GET网站主界面；可登陆以及查看他人博客
    url(r'^search/$', views.search, name='search'),#搜索查看他人博客,POST筛选文字
    url(r'^regist/$', views.regist, name='regist'),#注册；POST基本注册信息
    url(r'^login/$', views.login, name='login'),#登陆；POST用户名密码
    url(r'^logout/$', views.logout, name='logout'),#登出；退出按钮

    ##关于主页
    url(r'^homepage/$', views.homepage, name='homepage'),#GET已注册用户个人主页
    url(r'^publish/$', views.publish, name='publish'),#发帖:POST标题,文件,描述,归属任务；
    url(r'^card_detail/(.+)/$', views.card_detail, name='views.card_detail'),  # 发帖:get相应的帖子的单独页面；get传入想要帖子id
    # url(r'^sign/$', views.sign, name='sign'),  # 签到；不确定是否要这个功能
    url(r'^comment/$', views.comment, name='comment'),  # 评论帖子；POST的评论内容，POST隐性传入该帖子id

    ##关于任务

    url(r'^teams/$', views.teams, name='teams'),  # GET 得到队伍概览页面；
    url(r'^create_team/$', views.create_team, name='create_team'),  # 创建一个团队
    url(r'^quit_team/$', views.quit_team, name='quit_team'),  # 退出或解散一个团队
    url(r'^team_message/$', views.team_message, name='team_message'),  # 关于团队的消息通知,包括成员邀请
    url(r'^team_detail/(.+)/$', views.detail, name='team_detail')   # GET得到点击的队伍的详细页面；GET传入该队伍id
    url(r'^team_detail/(.+)/1/$', views.information, name='information'),# GET 得到该队伍当前任务                                                                #默认跳转到第一个：任务信息
    url(r'^team_detail/(.+)/2/$', views.current_task, name='current_task'),  # GET 得到该队伍当前任务界面；
    url(r'^publish_task/$', views.publish_task, name='publish_task'),  # 用于发布任务;
    url(r'^change_task/$', views.change_task, name='change_task'),  # 用于修改任务
    url(r'^delete_task/$', views.delete_task, name='delete_task'),  # 用于删除任务；
    url(r'^team_detail/(.+)/3/$', views.history, name='teams'),  # GET 历史任务；
    url(r'^team_detail/(.+)/4/$', views.result, name='result'),  # GET 项目成果，分成员展示；
    url(r'^task_cards/(.+)/$', views.task_cards, name='task_cards'),#GET该用户归属于某个团队的帖子

    ##文件获得url
    ##如果models里面  FileField(upload_to = 'files/')
    ## http://ip:port/task_blog/media/files/XX.zip
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
