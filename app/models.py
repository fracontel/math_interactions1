# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class GptCharacter(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100)
    role = models.IntegerField()
    notes = models.CharField(max_length=500)
    insert_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:

        db_table = 'gpt_character'


class GptCharacterAnalyst(models.Model):
    id = models.OneToOneField(GptCharacter, models.DO_NOTHING, db_column='id', primary_key=True)
    #username = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    affiliation = models.CharField(max_length=100)
    insert_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:

        db_table = 'gpt_character_analyst'


class GptCharacterStudent(models.Model):
    id = models.OneToOneField(GptCharacter, models.DO_NOTHING, db_column='id', primary_key=True)
    #notes = models.CharField(max_length=500)
    age = models.IntegerField()
    school_grade = models.IntegerField()
    insert_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:

        db_table = 'gpt_character_student'


class GptCharacterTutor(models.Model):
    id = models.OneToOneField(GptCharacter, models.DO_NOTHING, db_column='id', primary_key=True)
   # username = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    affiliation = models.CharField(max_length=100)
    insert_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'gpt_character_tutor'


class GptChat(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField()
    place = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    insert_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    problem = models.ForeignKey('GptProblem', models.DO_NOTHING, db_column='problem', blank=True, null=True)
    student = models.ForeignKey(GptCharacterStudent, models.DO_NOTHING, db_column='student', blank=True, null=True)
    tutor = models.ForeignKey(GptCharacterTutor, models.DO_NOTHING, db_column='tutor', blank=True, null=True)

    class Meta:

        db_table = 'gpt_chat'


class GptChatModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    model_id = models.IntegerField(blank=True, null=True)
    chat = models.ForeignKey(GptChat, models.DO_NOTHING, blank=True, null=True)

    class Meta:

        db_table = 'gpt_chat_model'


class GptDocumentation(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    task_type = models.IntegerField()
    content_text = models.TextField(blank=True, null=True)
    file_format = models.CharField(max_length=5, blank=True, null=True)
    file_data = models.BinaryField(blank=True, null=True)
    insert_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:

        db_table = 'gpt_documentation'


class GptDocumentationModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    documentation = models.IntegerField(blank=True, null=True)
    model = models.ForeignKey('GptModel', models.DO_NOTHING, db_column='model', blank=True, null=True)

    class Meta:

        db_table = 'gpt_documentation_model'


class GptLabel(models.Model):
    id = models.BigAutoField(primary_key=True)
    label_type = models.IntegerField()
    label_value1 = models.IntegerField()
    label_value2 = models.IntegerField()
    insert_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:

        db_table = 'gpt_label'


class GptLabelModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    model = models.IntegerField(blank=True, null=True)
    label = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'gpt_label_model'


class GptLine(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.CharField(max_length=2)
    content_text = models.TextField(blank=True, null=True)
    file_format = models.CharField(max_length=5, blank=True, null=True)
    file_data = models.BinaryField(blank=True, null=True)
    insert_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    chat = models.ForeignKey(GptChat, models.DO_NOTHING, blank=True, null=True)

    class Meta:

        db_table = 'gpt_line'


class GptLineLabel(models.Model):
    id = models.BigAutoField(primary_key=True)
    line = models.IntegerField(blank=True, null=True)
    label = models.IntegerField(blank=True, null=True)

    class Meta:

        db_table = 'gpt_line_label'


class GptModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    model_type = models.IntegerField()
    name = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    premis = models.IntegerField(blank=True, null=True)
    insert_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    parameters = models.ForeignKey('GptModelParameters', models.DO_NOTHING, db_column='parameters', blank=True, null=True)
    problem = models.ForeignKey('GptProblem', models.DO_NOTHING, db_column='problem', blank=True, null=True)
    task = models.ForeignKey('GptTask', models.DO_NOTHING, db_column='task', blank=True, null=True)
    analyst = models.ForeignKey(GptCharacterAnalyst, models.DO_NOTHING, db_column='analyst', blank=True, null=True)

    class Meta:

        db_table = 'gpt_model'


class GptModelParameters(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    insert_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    json_data = models.TextField()

    class Meta:

        db_table = 'gpt_model_parameters'


class GptPremis(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    insert_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    content_text = models.TextField(blank=True, null=True)
    file_format = models.CharField(max_length=5, blank=True, null=True)
    file_data = models.BinaryField(blank=True, null=True)

    class Meta:

        db_table = 'gpt_premis'


class GptProblem(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    problem_type = models.CharField(max_length=100)
    problem_text = models.TextField()
    insert_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:

        db_table = 'gpt_problem'


class GptTask(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    notes = models.CharField(max_length=500)
    task_text = models.TextField()
    task_type = models.IntegerField()
    insert_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)

    class Meta:

        db_table = 'gpt_task'
