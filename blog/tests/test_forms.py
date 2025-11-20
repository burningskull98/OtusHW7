import pytest
from blog.forms import PostForm, PostModelForm
from blog.models import User


@pytest.fixture
def user():
    return User.objects.create(name="Test User")


@pytest.mark.django_db
def test_post_form_valid(user):
    form_data = {
        "title": "Test Title",
        "content": "This is a test post.",
        "user": user.id,
    }
    form = PostForm(data=form_data)
    assert form.is_valid()
    assert form.cleaned_data["title"] == "Test Title"
    assert form.cleaned_data["content"] == "This is a test post."
    assert form.cleaned_data["user"] == user


@pytest.mark.django_db
def test_post_form_invalid_title(user):
    form_data = {
        "title": "Short",
        "content": "This is a test post.",
        "user": user.id,
    }
    form = PostForm(data=form_data)
    assert not form.is_valid()
    assert "title" in form.errors


@pytest.mark.django_db
def test_post_model_form_valid(user):
    form_data = {
        "title": "Valid Title",
        "content": "This is valid content.",
        "user": user.id,
        "tags": [],
    }
    form = PostModelForm(data=form_data)
    assert form.is_valid()
