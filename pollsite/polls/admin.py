from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.forms import BaseInlineFormSet

from .models import Poll, Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    #    formset = ChoiceInlineFormSet
    extra = 0


class QuestionInline(admin.TabularInline):
    model = Question
    fk_name = "poll"
    extra = 1
    show_change_link = True


@admin.register(Question)
class QuestionAdmin(ModelAdmin):
    inlines = ChoiceInline,


# Register your models here.

@admin.register(Poll)
class PollAdmin(ModelAdmin):
    fields = ("title", "date_start", "is_active", "date_end", "description")
    readonly_fields = ("date_start", "is_active")
    inlines = [QuestionInline, ChoiceInline]

    list_display = ("title", "date_start", "date_end", "is_active")
