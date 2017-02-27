from django.contrib import admin
from .models import Category,Introduction,Subintroduction,Task,Subtask,Troubleshoot,Subtroubleshoot,Userdetail,Message,Worklocation
from django_summernote.admin import SummernoteModelAdmin
from reversion.admin import VersionAdmin,Version
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
class CategoryAdmin(VersionAdmin,SummernoteModelAdmin):
	list_display = 	('name','description')
	search_fields = ['name','description']

admin.site.register(Category,CategoryAdmin)


class IntroductionAdmin(VersionAdmin,SummernoteModelAdmin):	
	pass
admin.site.register(Introduction,IntroductionAdmin)

class SubintroductionAdmin(VersionAdmin,SummernoteModelAdmin):
	pass
admin.site.register(Subintroduction,SubintroductionAdmin)

class TaskAdmin(VersionAdmin,SummernoteModelAdmin):
	pass
admin.site.register(Task,TaskAdmin)

class SubtaskAdmin(VersionAdmin,SummernoteModelAdmin):
	pass
admin.site.register(Subtask,SubtaskAdmin)

class TroubleshootAdmin(VersionAdmin,SummernoteModelAdmin):
	pass
admin.site.register(Troubleshoot,TroubleshootAdmin)

class SubtroubleshootAdmin(VersionAdmin,SummernoteModelAdmin):
	pass
admin.site.register(Subtroubleshoot,SubtroubleshootAdmin)

class UserdetailAdmin(VersionAdmin,SummernoteModelAdmin):
	pass
admin.site.register(Userdetail,UserdetailAdmin)  

# class FpeAdmin(VersionAdmin,SummernoteModelAdmin):
# 	pass
# admin.site.register(Fpe,FpeAdmin)  

class WorklocationAdmin(VersionAdmin,SummernoteModelAdmin):	
	pass
admin.site.register(Worklocation,WorklocationAdmin)

class MessageAdmin(VersionAdmin,SummernoteModelAdmin):
	pass
admin.site.register(Message,MessageAdmin)  
