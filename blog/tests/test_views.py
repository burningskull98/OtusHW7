import pytest
from django.urls import reverse
from blog.models import Post, User


@pytest.fixture
def user(db):
    return User.objects.create(name="Test User")


@pytest.fixture
def post(db, user):
    return Post.objects.create(title="Test Title", content="Test Content", user=user)


@pytest.mark.django_db
def test_index_view(client):
    response = client.get(reverse("base"))
    assert response.status_code == 200
    assert "blog/base.html" in (t.name for t in response.templates)


@pytest.mark.django_db
def test_post_list_view(client):
    response = client.get(reverse("posts"))
    assert response.status_code == 200
    assert "blog/list_for_post.html" in (t.name for t in response.templates)
    assert "posts" in response.context


@pytest.mark.django_db
def test_post_detail_view(client, post):
    response = client.get(reverse("detail_for_post", args=[post.id]))
    assert response.status_code == 200
    assert "blog/detail_for_post.html" in (t.name for t in response.templates)
    assert response.context["post"] == post


@pytest.mark.django_db
def test_post_create_view(client, user):
    response = client.post(
        reverse("add_post"),
        {
            "title": "New Post Title",
            "content": "New Post Content",
            "user": user.id,
        },
    )
    assert response.status_code == 302
    assert Post.objects.count() == 1
    assert Post.objects.first().title == "New Post Title"


@pytest.mark.django_db
def test_post_delete_view(client, post,):
    response = client.post(reverse("delete_post", args=[post.id]))
    assert response.status_code == 302
    assert Post.objects.count() == 0


@pytest.mark.django_db
def test_user_list_view(client):
    response = client.get(reverse("users"))
    assert response.status_code == 200
    assert "users" in response.context


@pytest.mark.django_db
def test_user_posts_view(client, user, post):
    post.user = user
    post.save()
    response = client.get(reverse("user_posts", args=[user.id]))
    assert response.status_code == 200
    assert response.context["user"] == user
    assert post in response.context["posts"]
