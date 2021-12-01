# jobs\tests\factories.py

import factory
import datetime

from jobs import models

class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Company
    
    company_name = "Test Company"
    company_website = "testcompany.com"
    company_job_postings = "testcompany.com\jobs"


class CurrentStatusFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.CurrentStatus
    
    current_status = "need to apply"


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Person

    name = "Andrew Davis"
    company = factory.SubFactory(CompanyFactory)
    email = "andrew.davis@gamil.com"
    additional_informaiton = "Some additona information about the person"


class JobPostingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.JobPosting
    
    company = factory.SubFactory(CompanyFactory)
    job_posting_url = "examplejoburl.com/job/posting12345"
    job_short_description = "Programer I"
    job_description = "This position in open for developer with 2 yrs experience"
    current_status = factory.SubFactory(CurrentStatusFactory)


class PreInterviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.PreInterview
    
    job_posting = factory.SubFactory(JobPostingFactory)
    job_found_date = datetime.date(2021, 11, 15)
    apply = True
    date_applied = datetime.date(2021, 12, 1)
    follow_up_email = True
    follow_up_email_date = datetime.date(2021, 12, 5)

class InterviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Interview
    
    job_posting = factory.SubFactory(JobPostingFactory)
    interviewer = factory.SubFactory(PersonFactory)
    date_of_interview = datetime.date(2021, 12, 1)
    send_thank_you = True
    date_thank_you_sent = datetime.date(2021, 12, 5)
    follow_up_email = True
    follow_up_email_date = datetime.date(2021, 12, 10)
