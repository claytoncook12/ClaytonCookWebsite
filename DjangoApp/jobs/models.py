from django.db import models
from django.db.models.deletion import CASCADE

class Company(models.Model):
    company_name = models.CharField('Company Name', max_length=100)
    company_website = models.URLField('Company Website')
    company_job_postings = models.URLField('Company Website Job Posting Site')

    def __str__(self):
        return self.company_name


class CurrentStatus(models.Model):
    current_status = models.CharField('Current Status', max_length=50)

    def __str__(self):
        return self.current_status


class Person(models.Model):
    name = models.CharField('Full Name', max_length=200)
    company = models.ForeignKey(Company, on_delete=CASCADE)
    email = models.EmailField('Email')
    additional_informaiton = models.TextField('Additional Person Information')

    def __str__(self):
        return f'{self.name} ({self.company}) ({self.email})'

class JobPosting(models.Model):
    company = models.ForeignKey(Company, on_delete=CASCADE)
    job_posting_url = models.URLField("Job Posting URL")
    job_short_description = models.CharField("Job Short Description", max_length=50)
    job_description = models.TextField("Job Description")
    current_status = models.ForeignKey(CurrentStatus, on_delete=CASCADE)
    additional_notes = models.TextField("Additional Notes", null=True, blank=True)

    def __str__(self):
        return f'id:{self.id} status:{self.current_status} company:{self.company}'

class PreInterview(models.Model):
    job_posting = models.ForeignKey(JobPosting, on_delete=CASCADE)
    job_found_date = models.DateField('Job Found Date')
    apply = models.BooleanField('Have Applied?')
    date_applied = models.DateField('Applied Date', null=True, blank=True)
    follow_up_email = models.BooleanField('Have Followed Up Email?')
    follow_up_email_date = models.DateField('Follow Up Email Date', null=True, blank=True)

    def __str__(self):
        return f'{self.job_posting} apply:{self.apply}'


class Interview(models.Model):
    job_posting = models.ForeignKey(JobPosting, on_delete=CASCADE)
    interviewer = models.ForeignKey(Person, on_delete=CASCADE)
    date_of_interview = models.DateField('Date of Interview')
    send_thank_you = models.BooleanField('Sent Thank You?')
    date_thank_you_sent = models.DateField('Date Thank You Sent', null=True, blank=True)
    follow_up_email = models.BooleanField('Sent Follow Up Email?')
    follow_up_email_date = models.DateField('Date Follow Up Email Sent', null=True, blank=True)

    def __str__(self):
        return f'{self.job_posting} {self.interviewer} {self.date_of_interview}'
