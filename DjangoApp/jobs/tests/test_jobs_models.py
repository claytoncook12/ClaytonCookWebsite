# jobs\test\test_jobs_models.py

from jobs.tests import factories

import pytest

@pytest.mark.django_db
class TestCompanyFactory:
    def test_init(self):
        obj = factories.CompanyFactory()
        assert obj.pk == 1, "Should save an instance"


@pytest.mark.django_db
class TestCurrentStatusFactory:
    def test_init(self):
        obj = factories.CurrentStatusFactory()
        assert obj.pk == 1, "Should save an instance"


@pytest.mark.django_db
class TestPersonFactory:
    def test_init(self):
        obj = factories.PersonFactory()
        assert obj.pk == 1, "Should save an instance"

@pytest.mark.django_db
class TestLocationFactory:
    def test_init(self):
        obj = factories.LocationFactory()
        assert obj.pk == 1, "Should save an instance"


@pytest.mark.django_db
class TestJobPostingFactory:
    def test_init(self):
        obj = factories.JobPostingFactory()
        assert obj.pk == 1, "Should save an instance"


@pytest.mark.django_db
class TestPreInterviewFactory:
    def test_init(self):
        obj = factories.PreInterviewFactory()
        assert obj.pk == 1, "Should save an instance"


@pytest.mark.django_db
class TestInterviewFactory:
    def test_init(self):
        obj = factories.InterviewFactory()
        assert obj.pk == 1, "Should save an instance"
