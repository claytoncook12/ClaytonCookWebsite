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
    list_display = ("id","current_status","company","job_short_description","job_posting_location")
    list_filter = ("current_status","job_location")
    inlines = [PreInterviewInline, InterviewInline]

    def job_posting_location(self, obj):
        try:
            return obj.job_location.location
        except:
            return ''


@admin.register(PreInterview)
class PreInterviewAdmin(admin.ModelAdmin):
    list_display = ("id", "job_posting", "job_found_date", "apply", "date_applied","follow_up_email")
    list_filter = ("apply","follow_up_email")


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ("id", "date_of_interview","job_posting_company","interviewer")

    def job_posting_company(self, obj):
        return obj.job_posting.company.company_name