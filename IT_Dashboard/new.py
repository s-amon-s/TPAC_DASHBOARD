from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import URLValidator
from django.contrib.auth.models import User
from django.forms import SelectDateWidget,DateField
from simple_history.models import HistoricalRecords
from .choices import LEVEL_CHOICES,Is_Important_CHOICES,OCCURRENCE_CHOICES,IS_Under_CHOICES,DEPARTMENT_CHOICES,User_Choices,google_api
import reversion
from Auditable.models import Auditable_Category,Auditable_Introduction,Auditable_Subintroduction,Auditable_Task,Auditable_Subtask,Auditable_Troubleshoot,Auditable_Subtroubleshoot,Auditable_Fpe
# from apiclient.discovery import build
# Create your models here.

def category_file_upload(instance, filename):
    return "%s/%s" % (instance.name, filename)

def introduction_file_upload(instance, filename):
    return "%s/%s/%s" % (instance.category.name,instance.name,filename)
def sub_introduction_file_upload(instance, filename):
    return "%s/%s/%s" % (instance.introduction.category.name.strip(),instance.introduction.name.strip(),instance.name.strip(),filename)

def task_file_upload(instance, filename):
    return "%s/%s/%s" % (instance.category.name.strip(),instance.name.strip(),filename)
def sub_task_file_upload(instance, filename):
    return "%s/%s/%s" % (instance.task.category.name.strip(),instance.task.name.strip(),instance.name.strip(),filename)

def troubleshoot_file_upload(instance, filename):
    return "%s/%s/%s" % (instance.category.name.strip(),instance.name.strip(),filename)
def sub_troubleshoot_file_upload(instance, filename):
    return "%s/%s/%s" % (instance.troubleshoot.category.name.strip(),instance.troubleshoot.name.strip(),instance.name.strip(),filename)

def user_image_upload(instance, filename):
    return "Userimages/%s_(%s)/%s" % (instance.fullname.strip(),instance.user,filename)


class Category(Auditable_Category):
	"""docstring for Product"""
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	name = models.CharField(max_length=250,default='topic name goes here')
	image_url = models.TextField(validators=[URLValidator()],null=True, blank=True)
	background_url = models.TextField(validators=[URLValidator()],null=True, blank=True)
	video_url = models.TextField(validators=[URLValidator()],null=True, blank=True)
	image = models.ImageField(upload_to=category_file_upload,null=True, blank=True)
	background = models.ImageField(upload_to=category_file_upload,null=True, blank=True)
	description = models.TextField(max_length=40000,default='topic Description goes here')

	name_th = models.CharField(max_length=255,null=True, blank=True)
	description_th = models.TextField(max_length=40000,null=True, blank=True)

	history = HistoricalRecords()


	def get_absolute_url(self):
		return reverse('it:index')
	
	def __str__(self):
		return self.name

		
reversion.register(Category)

class Introduction(Auditable_Introduction):
	
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	start_date = models.DateField(null=True, blank=True)
	end_date = models.DateField(null=True, blank=True)

	name = models.CharField(max_length=255,default='introduction heading goes here')
	description = models.TextField(max_length=40000,default='introduction Description goes here')

	is_expert_and_incharge =  models.ManyToManyField(User,null=True)
	is_important = models.BooleanField(default=False,choices=Is_Important_CHOICES)

	name_th = models.CharField(max_length=255,null=True, blank=True)
	description_th = models.TextField(max_length=40000,null=True, blank=True)
	
	image = models.ImageField(upload_to=introduction_file_upload,null=True, blank=True)
	file = models.FileField(upload_to=introduction_file_upload,null=True, blank=True)
	file_url = models.TextField(validators=[URLValidator()],null=True, blank=True)
	image_url = models.TextField(validators=[URLValidator()],null=True, blank=True)
	video_url = models.TextField(validators=[URLValidator()],null=True, blank=True)

	history = HistoricalRecords()
	# service = build('translate', 'v2')
	# google_api[2][1]
	# def save(self):
	# 	"Get last value of Code and Number from database, and increment before save"
	# 	if self.name == 'introduction heading goes here' 
 #      	top = Product.objects.order_by('-code','-number')[0]
 #      	self.code = top.code + 1
 #      	self.number = top.number + 1
 #      	super(Introduction, self).save()

	def get_absolute_url(self):
		return reverse('it:intro',args=[str(self.category.id)])
	
	def __str__(self):
		return self.name
reversion.register(Introduction)

class Subintroduction(Auditable_Subintroduction):
	
	introduction = models.ForeignKey(Introduction, on_delete=models.CASCADE)

	name = models.CharField(max_length=255,default='introduction heading goes here')
	description = models.TextField(max_length=40000,default='introduction Description goes here')

	name_th = models.CharField(max_length=255,null=True, blank=True)
	description_th = models.TextField(max_length=40000,null=True, blank=True)

	image = models.ImageField(upload_to=sub_introduction_file_upload,null=True, blank=True)
	file = models.FileField(upload_to=sub_introduction_file_upload,null=True, blank=True)
	file_url = models.TextField(validators=[URLValidator()],null=True, blank=True)
	image_url = models.TextField(validators=[URLValidator()],null=True, blank=True)
	video_url = models.TextField(validators=[URLValidator()],null=True, blank=True)

	history = HistoricalRecords()

	def get_absolute_url(self):
		return reverse('it:intro-detail',args=[str(self.introduction.id)])
	
	def __str__(self):
		return self.name

reversion.register(Subintroduction)

class Task(Auditable_Task):

	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	start_date = models.DateField(null=True, blank=True)
	end_date = models.DateField(null=True, blank=True)

	name = models.CharField(max_length=255,default='introduction heading goes here')
	description = models.TextField(max_length=40000,default='introduction Description goes here')

	is_expert_and_incharge =  models.ManyToManyField(User,null=True)
	is_important = models.BooleanField(default=False,choices=Is_Important_CHOICES)

	name_th = models.CharField(max_length=255,null=True, blank=True)
	description_th = models.TextField(max_length=40000,null=True, blank=True)
	
	image = models.ImageField(upload_to=introduction_file_upload,null=True, blank=True)
	file = models.FileField(upload_to=introduction_file_upload,null=True, blank=True)
	file_url = models.TextField(validators=[URLValidator()],null=True, blank=True)
	image_url = models.TextField(validators=[URLValidator()],null=True, blank=True)
	video_url = models.TextField(validators=[URLValidator()],null=True, blank=True)

	history = HistoricalRecords()

	def get_absolute_url(self):
		return reverse('it:task',args=[str(self.category.id)])
	
	def __str__(self):
		return self.name


reversion.register(Task)

class Subtask(Auditable_Subtask):
	
	task = models.ForeignKey(Task, on_delete=models.CASCADE)

	name = models.CharField(max_length=255,default='introduction heading goes here')
	description = models.TextField(max_length=40000,default='introduction Description goes here')

	name_th = models.CharField(max_length=255,null=True, blank=True)
	description_th = models.TextField(max_length=40000,null=True, blank=True)

	image = models.ImageField(upload_to=sub_task_file_upload,null=True, blank=True)
	file = models.FileField(upload_to=sub_task_file_upload,null=True, blank=True)
	file_url = models.TextField(validators=[URLValidator()],null=True, blank=True)
	image_url = models.TextField(validators=[URLValidator()],null=True, blank=True)
	video_url = models.TextField(validators=[URLValidator()],null=True, blank=True)

	history = HistoricalRecords()

	def get_absolute_url(self):
		return reverse('it:task-detail',args=[str(self.task.id)])
	
	def __str__(self):
		return self.name


reversion.register(Subtask)

class Troubleshoot(Auditable_Troubleshoot):
	
	
	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	start_date = models.DateField(null=True, blank=True)
	end_date = models.DateField(null=True, blank=True)

	name = models.CharField(max_length=255,default='introduction heading goes here')
	cause = models.TextField(max_length=40000,default='Cause of the issue',blank=True,null=True)
	description = models.TextField(max_length=40000,default='introduction Description goes here')
	
	
	occurrence = models.CharField(max_length=250,choices=OCCURRENCE_CHOICES,default={'occurrence': 'Once so far'})
	has_been_solved = models.BooleanField(default=False,choices=Is_Important_CHOICES)
	is_expert_and_incharge =  models.ManyToManyField(User,null=True)
	is_important = models.BooleanField(default=False,choices=Is_Important_CHOICES)

	name_th = models.CharField(max_length=255,null=True, blank=True)
	cause_th = models.TextField(max_length=40000,default='Cause of the issue',blank=True,null=True)
	description_th = models.TextField(max_length=40000,null=True, blank=True)
	
	image = models.ImageField(upload_to=introduction_file_upload,null=True, blank=True)
	file = models.FileField(upload_to=introduction_file_upload,null=True, blank=True)
	file_url = models.TextField(validators=[URLValidator()],null=True, blank=True)
	image_url = models.TextField(validators=[URLValidator()],null=True, blank=True)
	video_url = models.TextField(validators=[URLValidator()],null=True, blank=True)

	history = HistoricalRecords()

	def get_absolute_url(self):
		return reverse('it:trouble',args=[str(self.category.id)])
	
	def __str__(self):
		return self.name

reversion.register(Troubleshoot)

class Subtroubleshoot(Auditable_Subtroubleshoot):
	
	troubleshoot = models.ForeignKey(Troubleshoot, on_delete=models.CASCADE)

	name = models.CharField(max_length=255,default='troubleshoot heading goes here')
	description = models.TextField(max_length=40000,default='troubleshoot Description goes here')

	name_th = models.CharField(max_length=255,null=True, blank=True)
	description_th = models.TextField(max_length=40000,null=True, blank=True)

	image = models.ImageField(upload_to=sub_troubleshoot_file_upload,null=True, blank=True)
	file = models.FileField(upload_to=sub_troubleshoot_file_upload,null=True, blank=True)
	file_url = models.TextField(validators=[URLValidator()],null=True, blank=True)
	image_url = models.TextField(validators=[URLValidator()],null=True, blank=True)
	video_url = models.TextField(validators=[URLValidator()],null=True, blank=True)

	history = HistoricalRecords()

	def get_absolute_url(self):
		return reverse('it:trouble-detail',args=[str(self.troubleshoot.id)])
	
	def __str__(self):
		return self.name

reversion.register(Subtroubleshoot)

class Userdetail(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
	id = models.IntegerField(default=7726)
	fullname_english = models.CharField(max_length=250,)
	fullname_thai = models.CharField(max_length=250,default=fullname_english)
	ip = models.GenericIPAddressField(null=True, blank=True,default="192.168.12.")
	selfie = models.ImageField(upload_to=user_image_upload,null=True, blank=True)
	selfie_url = models.TextField(validators=[URLValidator()],null=True, blank=True)
	table = models.IntegerField()
	department = models.CharField(max_length=250,choices=DEPARTMENT_CHOICES,null=True, blank=True)
	is_head_of_department = models.BooleanField(blank=True,default=False)
	designation = models.CharField(max_length=250,null=True, blank=True)
	level = models.IntegerField(choices=LEVEL_CHOICES,null=True)
	permission = models.IntegerField()
	is_under = models.CharField(max_length=250,null=True, blank=True)
	joined_tpac = models.DateField(null=True, blank=True)
	birthday = models.DateField(null=True, blank=True)
	house_location = models.CharField(max_length=250,null=True, blank=True)
	personal_contact = models.CharField(max_length=250,null=True, blank=True,default="0")
	is_incharge_of = models.CharField(max_length=250,null=True, blank=True)
	is_responsible_to = models.CharField(max_length=250,null=True, blank=True)
	nickname = models.CharField(max_length=250,null=True, blank=True)
	work_at = models.CharField(max_length=250,null=True, blank=True,default="TPAC")
	credit = models.IntegerField(default=0)
	daily_task_timeline = models.TextField(validators=[URLValidator()],null=True, blank=True)
	groupflow = models.TextField(max_length=400000,null=True, blank=True)
	history = HistoricalRecords()
	
	def get_absolute_url(self):
		return reverse('it:index')
	
	def __str__(self):
		return self.fullname_english + ' - ' + str(self.id)

reversion.register(Userdetail)
# amom


class Fpe(Auditable_Fpe):
	issue_itd_econs = models.IntegerField(default=170023)
	issue_itd_others = models.IntegerField(default=170217) 
	issue_date = models.DateField(null=True,blank=False)
	issue_subejct = models.CharField(max_length=255)
	thai_name = models.CharField(max_length=255)
	english_name = models.CharField(max_length=255)
	tpac_id = models.IntegerField(default=7726)
	department = models.CharField(max_length=250,choices=DEPARTMENT_CHOICES,null=True, blank=True)
	position = models.CharField(max_length=255)
	personal_contact = models.CharField(max_length=250,null=True, blank=True,default="0")
	
	check_repair = models.BooleanField(blank= True)
	check_problem = models.BooleanField(blank= True)
	check_add = models.BooleanField(blank= True)
	check_replace = models.BooleanField(blank= True)
	check_request_or_cancle_service = models.BooleanField(blank= True)
	check_change_or_edit = models.BooleanField(blank= True)
	check_miscellaneous = models.BooleanField(blank= True)
	miscellaneous_text1 = models.TextField(max_length=255,blank= True)

	check_os = models.BooleanField(blank= True)
	check_os_windows7 = models.BooleanField(blank= True)
	check_os_windows10 = models.BooleanField(blank= True)

	check_application_msoffice10 = models.BooleanField(blank= True)
	check_application_msoffice13 = models.BooleanField(blank= True)
	check_application_econs = models.BooleanField(blank= True)
	check_application_hmi = models.BooleanField(blank= True)
	check_application_adobeandmore = models.BooleanField(blank= True)
	check_application_miscellaneous = models.BooleanField(blank= True)
	miscellaneous_text2 = models.TextField(max_length=255,blank= True)

	check_mail_or_internet = models.BooleanField(blank= True)
	check_mail_internal = models.BooleanField(blank= True)
	check_mail_external = models.BooleanField(blank= True)
	check_internet = models.BooleanField(blank= True)

	check_ad = models.BooleanField(blank= True)
	check_ad_user_join = models.BooleanField(blank= True)
	check_ad_file_sharing = models.BooleanField(blank= True)
	check_ad_map_drive = models.BooleanField(blank= True)

	check_hardware = models.BooleanField(blank= True)
	check_hardware_pc = models.BooleanField(blank= True)
	check_hardware_nb = models.BooleanField(blank= True)
	check_hardware_monitor = models.BooleanField(blank= True)
	check_hardware_network = models.BooleanField(blank= True)
	check_hardware_printer = models.BooleanField(blank= True)
	check_hardware_miscellaneous = models.BooleanField(blank= True)

	detail_description = models.TextField(max_length=40000,null=True, blank=True)
	issue_objective = models.TextField(max_length=40000,null=True, blank=True)

	history = HistoricalRecords()

	def get_absolute_url(self):
		return reverse('it:index')
	
	def __str__(self):
		return self.issue_subejct

reversion.register(Fpe)

IS_Under_CHOICES = (
	('Khun Kevin','Khun Kevin'),
	('Khun Theerawit','Khun Theerawit'),
	('Khun Phairot','Khun Phairot'),
	('Khun Kohli','Khun Kohli'),
	('Khun Kothari','Khun Kothari'),
	('Khun Anong','Khun Anong'),
	('Khun Chakraphan','Khun Chakraphan'),
	('Khun Phairot','Khun Phairot'),
	('Khun Pricha','Khun Pricha'),
	('Khun Somchai','Khun Somchai'),
	)

class Message(models.Model):
    user = models.ForeignKey(User, related_name='sender')
    recipient = models.ForeignKey(User, related_name='recipient')
    subject = models.CharField(max_length=100)
    body = models.CharField(max_length=1000,null=True, blank=True)
    read = models.BooleanField(default=False)
    trash = models.BooleanField(default=False)
    sentmessage = models.BooleanField(default=False)
    in_response_to = models.ForeignKey('self', null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add = True, null = True)

    def get_all_in_reponse_to(self):
        response_objects = self.in_response_to.message_set.order_by('-created_on')
        for obj in response_object:
            response += obj.body
        return response

    def __str__(self):
    	return self.subject

reversion.register(Message)