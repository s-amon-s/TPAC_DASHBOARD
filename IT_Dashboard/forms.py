from django.contrib.auth.models import User
from django import forms
from jsignature.forms import JSignatureField
from jsignature.widgets import JSignatureWidget
from django.forms import SelectDateWidget,DateField
from .models import Category,Introduction,Subintroduction,Task,Subtask,Troubleshoot,Subtroubleshoot,Userdetail,Fpe,Worklocation
from .fields import ListTextWidget
from .choices import LEVEL_CHOICES,Is_Important_CHOICES,OCCURRENCE_CHOICES,OU_CHOICES,DEPARTMENT_CHOICES,IS_Under_CHOICES
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
	
class UserForm(forms.ModelForm):
	password = forms.CharField(max_length=250,widget=forms.PasswordInput)
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['first_name','last_name','username','password','email']

class ProfileForm(forms.ModelForm):
	birthday = forms.DateField(widget=SelectDateWidget(years=range(1945, 2000),empty_label=("Choose Year", "Choose Month", "Choose Day")),required=False)
	joined_tpac = forms.DateField(widget=SelectDateWidget(years=range(1985, 2020),empty_label=("Choose Year", "Choose Month", "Choose Day")),required=False)
	is_under = forms.ChoiceField(choices = [])
	work_at = forms.ChoiceField(choices = [])

	def __init__(self, *args, **kwargs):
		super(ProfileForm, self).__init__(*args, **kwargs)
		self.fields['is_under'].choices = IS_Under_CHOICES
		self.fields['work_at'].choices = [(x.pk, x.location_building+'- ชั้น '+x.location_floor) for x in Worklocation.objects.all()]
	class Meta:
		model = Userdetail
		fields =  ['user','id','fullname','nickname','ip','table','department','designation','level','is_under','work_at','joined_tpac','personal_contact','is_incharge_of','is_responsible_to','birthday','selfie','selfie_url']
		labels = {
        "fullname": "Full Name (ชื่อเต็มภาษาไทย)",
        "id": "รหัสพนักงาน",
    }
class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['name','description','image','image_url','background','background_url','name_th','description_th']
		widgets = {
			'name' : SummernoteWidget(),
			'name_th' :  SummernoteWidget(),
            'description': SummernoteWidget(),
            'description_th': SummernoteWidget(),
        }

class FpeForm(forms.ModelForm):
	pass
	# class Meta:
	# 	model = Fpe
	# 	fields = ['name','description','image','image_url','background','background_url','name_th','description_th']
		# widgets = {
		# 	'name' : SummernoteWidget(),
		# 	'name_th' :  SummernoteWidget(),
  #           'description': SummernoteWidget(),
  #           'description_th': SummernoteWidget(),
  #       }


class IntroductionForm(forms.ModelForm):

	start_date = forms.DateField(widget=SelectDateWidget(years=range(1985, 2020),empty_label=("Choose Year", "Choose Month", "Choose Day")),required=False)
	end_date = forms.DateField(widget=SelectDateWidget(years=range(1985, 2020),empty_label=("Choose Year", "Choose Month", "Choose Day")),required=False)
	is_expert_and_incharge = forms.MultipleChoiceField(choices = [])

	def __init__(self, *args, **kwargs):
		super(IntroductionForm, self).__init__(*args, **kwargs)
		self.fields['is_expert_and_incharge'].choices = [(x.pk, x.fullname+' - '+x.nickname) for x in Userdetail.objects.all()]
	
	class Meta:
		model = Introduction
		fields = ['category','start_date','end_date','name','description','is_important','is_expert_and_incharge','image','image_url','file','file_url','video_url','name_th','description_th']
		widgets = {
			'name' : SummernoteWidget(),
			'name_th' :  SummernoteWidget(),
            'description': SummernoteWidget(),
            'description_th': SummernoteWidget(),
        }

class SubintroductionForm(forms.ModelForm):
	class Meta:
		model = Subintroduction
		fields = ['name','description','image','image_url','file','file_url','video_url','name_th','description_th']
		widgets = {
			'name' : SummernoteWidget(),
			'name_th' :  SummernoteWidget(),
            'description': SummernoteWidget(),
            'description_th': SummernoteWidget(),
        }

class TaskForm(forms.ModelForm):
	start_date = forms.DateField(widget=SelectDateWidget(years=range(1985, 2020),empty_label=("Choose Year", "Choose Month", "Choose Day")),required=False)
	end_date = forms.DateField(widget=SelectDateWidget(years=range(1985, 2020),empty_label=("Choose Year", "Choose Month", "Choose Day")),required=False)
	is_expert_and_incharge = forms.MultipleChoiceField(choices = [])

	def __init__(self, *args, **kwargs):
		super(TaskForm, self).__init__(*args, **kwargs)
		self.fields['is_expert_and_incharge'].choices = [(x.pk, x.fullname+' - '+x.nickname) for x in Userdetail.objects.all()]
	

	class Meta:
		model = Task
		fields = ['category','start_date','end_date','name','description','is_important','is_expert_and_incharge','image','image_url','file','file_url','video_url','name_th','description_th']
		widgets = {
			'name' : SummernoteWidget(),
			'name_th' :  SummernoteWidget(),
            'description': SummernoteWidget(),
            'description_th': SummernoteWidget(),
        }

class SubtaskForm(forms.ModelForm):
	class Meta:
		model = Subtask
		fields = ['name','description','image','image_url','file','file_url','video_url','name_th','description_th']
		widgets = {
			'name' : SummernoteWidget(),
			'name_th' :  SummernoteWidget(),
            'description': SummernoteWidget(),
            'description_th': SummernoteWidget(),
        }

class TroubleshootForm(forms.ModelForm):
	start_date = forms.DateField(widget=SelectDateWidget(years=range(1985, 2020),empty_label=("Choose Year", "Choose Month", "Choose Day")),required=False)
	end_date = forms.DateField(widget=SelectDateWidget(years=range(1985, 2020),empty_label=("Choose Year", "Choose Month", "Choose Day")),required=False)
	is_expert_and_incharge = forms.MultipleChoiceField(choices = [])

	def __init__(self, *args, **kwargs):
		super(TroubleshootForm, self).__init__(*args, **kwargs)
		self.fields['is_expert_and_incharge'].choices = [(x.pk, x.fullname+' - '+x.nickname) for x in Userdetail.objects.all()]
	
        	
	class Meta:
		model = Troubleshoot
		fields = ['category','start_date','end_date','name','cause','occurrence','has_been_solved','description','is_important','is_expert_and_incharge','image','image_url','file','file_url','video_url','name_th','description_th','cause_th']
		widgets = {
			'name' : SummernoteWidget(),
			'name_th' :  SummernoteWidget(),
            'description': SummernoteWidget(),
            'description_th': SummernoteWidget(),
            # 'occurrence': ListTextWidget(data_list=OCCURRENCE_CHOICES, name='occurrence'),
        }

class SubtroubleshootForm(forms.ModelForm):
	class Meta:
		model = Subtroubleshoot
		fields = ['name','description','image','image_url','file','file_url','video_url','name_th','description_th']
		widgets = {
			'name' : SummernoteWidget(),
			'name_th' :  SummernoteWidget(),
            'description': SummernoteWidget(),
            'description_th': SummernoteWidget(),
        }       

# class SignatureForm(forms.Form):
#     signature = JSignatureField()
#     class Meta:
# 		model = UserSignature