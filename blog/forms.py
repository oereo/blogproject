from django import forms
from .models import Photo

# class UploadDocumentForm(forms.Form):
#     file = forms.FileField()
#     image = forms.ImageField()

class UploadForm(forms.ModelForm):
    comment = forms.CharField(max_length=255)
    class Meta:
        model = Photo                         # 어떤 모델과 연결할지
        exclude = ('thumnail_image', 'owner') # 입력받지 않을 필드를 표시가능, 이 부분은 코드로 처리해주기 위해