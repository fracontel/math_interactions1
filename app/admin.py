

# Register your models here.

from django.contrib import admin

from .models import GptCharacter, GptCharacterAnalyst, GptCharacterStudent, GptCharacterTutor, GptChat, GptChatModel, GptDocumentation, GptDocumentationModel, GptLabel, GptLabelModel, GptLine, GptLineLabel, GptModel, GptModelParameters, GptPremis,GptProblem, GptTask

admin.site.register(GptCharacter)
admin.site.register(GptCharacterAnalyst)
admin.site.register(GptCharacterStudent)
admin.site.register(GptCharacterTutor)
admin.site.register(GptChat)
admin.site.register(GptChatModel)
admin.site.register(GptDocumentation)
admin.site.register(GptDocumentationModel)
admin.site.register(GptLabel)
admin.site.register(GptLabelModel)
admin.site.register(GptLine)
admin.site.register(GptLineLabel)
admin.site.register(GptModel)
admin.site.register(GptModelParameters)
admin.site.register(GptPremis)
admin.site.register(GptProblem)
admin.site.register(GptTask)
