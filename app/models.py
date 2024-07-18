# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Character(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=True)
    role = models.IntegerField()
    notes = models.CharField(max_length=500, null=True, default="", blank=True)
    affiliation = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(default=0, null=True, blank=True)
    school_grade = models.IntegerField(default=0, null=True, blank=True)
    insert_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'character'

class Chat(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField()
    place = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    insert_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    problem = models.ForeignKey('Problem', models.DO_NOTHING, db_column='problem', blank=True, null=True)
    student = models.ForeignKey('Character', models.DO_NOTHING, db_column='student', blank=True, null=True, related_name='student_chats')
    tutor = models.ForeignKey('Character', models.DO_NOTHING, db_column='tutor', blank=True, null=True, related_name='tutor_chats')

    class Meta:
         db_table = 'chat'


class ChatModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    model_id = models.IntegerField(blank=True, null=True)
    chat = models.ForeignKey('Chat', models.DO_NOTHING, blank=True, null=True)

    class Meta:

        db_table = 'chat_model'


class Documentation(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    notes = models.CharField(max_length=500, blank=True, null=True)
    task_type = models.IntegerField()
    content_text = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to='documents/', blank=True, null=True)
    insert_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:

        db_table = 'documentation'


class DocumentationModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    documentation = models.IntegerField(blank=True, null=True)
    model = models.ForeignKey('Model', models.DO_NOTHING, db_column='model', blank=True, null=True)

    class Meta:

        db_table = 'documentation_model'


class Label(models.Model):
    id = models.BigAutoField(primary_key=True)
    label_type = models.IntegerField()
    label_value1 = models.IntegerField(default=0)
    label_value2 = models.IntegerField(default=0)
    insert_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:

        db_table = 'label'


class LabelModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    model = models.IntegerField(blank=True, null=True)
    label = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'label_model'


class Line(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.CharField(max_length=2)
    content_text = models.TextField(blank=True, null=True)
    insert_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    chat = models.ForeignKey('Chat', models.DO_NOTHING, blank=True, null=True)

    class Meta:
     db_table = 'line'

class LineAttachment(models.Model):
    id = models.BigAutoField(primary_key=True)
    data = models.BinaryField()
    format = models.CharField(max_length = 50)
    line = models.ForeignKey('Line', models.DO_NOTHING, related_name='attachment', blank=True, null=True)
    notes = models.CharField(max_length=500)
    class Meta:
        db_table = 'line_attachment'


class LineLabel(models.Model):
    id = models.BigAutoField(primary_key=True)
    line = models.IntegerField(blank=True, null=True)
    label = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'line_label'


class Model(models.Model):
    id = models.BigAutoField(primary_key=True)
    model_type = models.IntegerField()
    name = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    premis = models.ForeignKey('Premis', models.DO_NOTHING, blank=True, null=True)
    insert_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    parameters = models.ForeignKey('ModelParameters', models.DO_NOTHING, db_column='parameters', blank=True, null=True)
    problem = models.ForeignKey('Problem', models.DO_NOTHING, db_column='problem', blank=True, null=True)
    task = models.ForeignKey('Task', models.DO_NOTHING, db_column='task', blank=True, null=True)
    analyst = models.ForeignKey('Character', models.DO_NOTHING, db_column='analyst', blank=True, null=True)

    class Meta:

        db_table = 'model'


class ModelParameters(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    insert_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    json_data = models.TextField()

    class Meta:

        db_table = 'model_parameters'


class Premis(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    insert_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    content_text = models.TextField(blank=True, null=True)
    file_format = models.CharField(max_length=5, blank=True, null=True)
    file_data = models.BinaryField(blank=True, null=True)

    class Meta:

        db_table = 'premis'


class Problem(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    problem_type = models.CharField(max_length=100)
    problem_text = models.TextField()
    insert_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:

        db_table = 'problem'


class Task(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    task_text = models.TextField()
    task_type = models.IntegerField()
    insert_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:

        db_table = 'task'
