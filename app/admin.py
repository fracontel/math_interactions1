# admin.py
from django.contrib import admin, messages
from django.urls import path
from django.shortcuts import render, redirect
from django.utils.html import format_html
from .forms import StudentForm, TutorForm, AnalystForm, DocumentationForm
from .models import Character, Chat, ChatModel, Documentation, DocumentationModel, Label, LabelModel, Line, LineAttachment, LineLabel, Model, ModelParameters, Premis, Problem, Task

class RoleFilter(admin.SimpleListFilter):
    title = 'role'
    parameter_name = 'role'

    def lookups(self, request, model_admin):
        return (
            (1, 'Student'),
            (2, 'Tutor'),
            (3, 'Analyst'),
        )

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(role=self.value())
        return queryset

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    change_list_template = "character_change_list.html"
    list_display = ('id', 'username', 'role_display')
    list_filter = (RoleFilter,)
    search_fields = ('username',)

    def role_display(self, obj):
        return {
            1: 'Student',
            2: 'Tutor',
            3: 'Analyst'
        }.get(obj.role, 'Unknown')
    role_display.short_description = 'Role'
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('add-character/', self.admin_site.admin_view(self.add_character), name="add_character")
        ]
        return custom_urls + urls
    
    def add_character(self, request):
        if request.method == "POST":
            role = request.POST.get('role')
            if role == '1':
                form = StudentForm(request.POST)
            elif role == '2':
                form = TutorForm(request.POST)
            else:
                form = AnalystForm(request.POST)
            
            if form.is_valid():
                character = form.save(commit=False)
                character.role = role
                character.save()
                self.message_user(request, "Character added successfully.", level=messages.SUCCESS)
                return redirect("..")
        else:
            role = request.GET.get('role')
            if role == '1':
                form = StudentForm()
            elif role == '2':
                form = TutorForm()
            else:
                form = AnalystForm()

        return render(request, "add_character.html", {'form': form})

    def get_form(self, request, obj=None, **kwargs):
        role = None
        if obj:
            role = obj.role
        else:
            role = request.GET.get('role')
        
        if role == '1' or (obj and obj.role == 1):
            self.form = StudentForm
        elif role == '2' or (obj and obj.role == 2):
            self.form = TutorForm
        elif role == '3' or (obj and obj.role == 3):
            self.form = AnalystForm
        else:
            self.form = super().get_form(request, obj, **kwargs)
        
        return super().get_form(request, obj, **kwargs)

    def get_fieldsets(self, request, obj=None):
        role = None
        if obj:
            role = obj.role
        else:
            role = request.GET.get('role')
        
        if role == '1' or (obj and obj.role == 1):
            return (
                (None, {
                    'fields': ('username', 'notes', 'age', 'school_grade')
                }),
            )
        elif role == '2' or (obj and obj.role == 2):
            return (
                (None, {
                    'fields': ('username', 'notes', 'affiliation')
                }),
            )
        elif role == '3' or (obj and obj.role == 3):
            return (
                (None, {
                    'fields': ('username', 'notes', 'affiliation')
                }),
            )
        return super().get_fieldsets(request, obj)
    
@admin.register(Documentation)
class DocumentationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'task_type_display')
    search_fields = ('name', 'notes')

    def task_type_display(self, obj):
        return {
            1: 'Analitycal model',
            2: 'Generative model'
        }.get(obj.task_type, 'Unknown')
    task_type_display.short_description = 'Task_type'

admin.site.register(Chat)
admin.site.register(ChatModel)
admin.site.register(DocumentationModel)
admin.site.register(Label)
admin.site.register(LabelModel)
admin.site.register(Line)
admin.site.register(LineAttachment)
admin.site.register(LineLabel)
admin.site.register(Model)
admin.site.register(ModelParameters)
admin.site.register(Premis)
admin.site.register(Problem)
admin.site.register(Task)
