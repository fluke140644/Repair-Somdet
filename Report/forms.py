from django import forms
from .models import RepairRequest
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class RepairRequestForm(forms.ModelForm):
    class Meta:
        model = RepairRequest
        exclude = ['created_by', 'created_at', 'request_id', 'status', 'completed_at', 'in_progress_at']
        widgets = {
            'category': forms.Select(attrs={'class': 'w-full h-12 border-gray-300 rounded-md shadow-sm'}),
            'sub_item': forms.TextInput(attrs={'class': 'w-full h-12 border-gray-300 rounded-md shadow-sm'}),
            'status_user': forms.Select(attrs={'class': 'w-full h-12 border-gray-300 rounded-md shadow-sm'}),
            'device_code': forms.TextInput(attrs={'class': 'w-full h-12 border-gray-300 rounded-md shadow-sm'}),
            'asset_number': forms.TextInput(attrs={'class': 'w-full h-12 border-gray-300 rounded-md shadow-sm'}),
            'department': forms.TextInput(attrs={'class': 'w-full h-12 border-gray-300 rounded-md shadow-sm'}),
            'detail': forms.Textarea(attrs={'class': 'w-full mt-1 h-12 border-gray-300 rounded-md shadow-sm', 'rows': 4}),
            'remake': forms.Textarea(attrs={'class': 'w-full mt-1 h-12 border-gray-300 rounded-md shadow-sm', 'rows': 4}),
            'status': forms.TextInput(attrs={'class': 'w-full h-12 border-gray-300 rounded-md shadow-sm'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['department'].widget.attrs.update({
            'readonly': 'readonly',
            'class': 'w-full border-gray-300 h-12 rounded-md shadow-sm bg-gray-100 text-gray-500'
        })

        if 'status' in self.fields:
            self.fields['status'].widget.attrs.update({
                'readonly': 'readonly',
                'class': 'w-full h-12 border-gray-300 rounded-md shadow-sm bg-gray-100 text-gray-500'
        })
            
        self.fields['remark'].widget = forms.Textarea(attrs={'class': 'w-full mt-1 h-12 border-gray-300 rounded-md shadow-sm','row': 4,})

        
        self.fields['assigned_to'] = forms.ModelChoiceField(
            queryset=User.objects.filter(is_active=True).filter(is_staff=True) | User.objects.filter(is_superuser=True),
            required=False,
            widget=forms.Select(attrs={
                'class': 'w-full h-12 border-gray-300 rounded-md shadow-sm'
            }),
            label="เจ้าหน้าที่ที่รับผิดชอบ"
        )

        
        self.fields['reported_by'] = forms.ModelChoiceField(
            queryset=User.objects.filter(is_active=True),
            required=True,
            widget=forms.Select(attrs={
                'class': 'w-full h-12 border-gray-300 rounded-md shadow-sm'
            }),
            label="ชื่อผู้แจ้ง"
        )

        
        self.fields['reported_by'].label_from_instance = lambda obj: f"{obj.first_name} {obj.last_name}" if obj.first_name else obj.username


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})