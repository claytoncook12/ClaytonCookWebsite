from django.contrib import admin
from .models import Company, CurrentStatus, Person
from .models import JobPosting, PreInterview, Interview


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    ordering = ("company_name",)
    list_display = ("company_name","company_website","company_job_postings")


@admin.register(CurrentStatus)
class CurrenStatusAdmin(admin.ModelAdmin):
    ordering = ("current_status",)
    list_display = ("id", "current_status")


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    ordering = ("company", "name")
    list_dispplay = ("company", "name", "email")

class PreInterviewInline(admin.TabularInline):
    model = PreInterview
    extra = 0
    show_change_link = True

class InterviewInline(admin.TabularInline):
    model = Interview
    extra = 0
    show_change_link = True

@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ("id","company","job_short_description")
    inlines = [PreInterviewInline, InterviewInline]

@admin.register(PreInterview)
class PreInterviewAdmin(admin.ModelAdmin):
    list_display = ("id", "job_posting", "job_found_date", "apply", "date_applied")
    list_filter = ("apply",)

