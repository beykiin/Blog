from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *
class UserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
    def __init__(self,*args,**kwargs):
        super(UserForm,self).__init__(*args,**kwargs)
        self.fields["username"].widget.attrs.update({"class":"form-control"})
        self.fields["email"].widget.attrs.update({"class":"form-control"})
        self.fields["password1"].widget.attrs.update({"class":"form-control"})
        self.fields["password2"].widget.attrs.update({"class":"form-control"})

class NewPost(ModelForm):
    class Meta:
        model=Posts
        fields=["title","content","image"]
    def __init__(self,*args,**kwargs):
        super(NewPost,self).__init__(*args,**kwargs)
        self.fields["title"].widget.attrs.update({"class":"form-control","placeholder":"Write Title!"})
        self.fields["content"].widget.attrs.update({"class":"form-control","placeholder":"Please write somethings","style":"resize:none"})
        self.fields["image"].widget.attrs.update({"class":"form-control"})

class NewComment(ModelForm):
    class Meta:
        model=Comment
        fields=["content"]
    def __init__(self,*args,**kwargs):
        super(NewComment,self).__init__(*args,**kwargs)
        self.fields["content"].widget.attrs.update({"class":"form-control","style":"resize:none"})