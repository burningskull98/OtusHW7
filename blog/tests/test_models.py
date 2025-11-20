import pytest
from blog.models import User, Post, Comment, UserProfile, Tag


@pytest.mark.django_db
def test_user_creation():
    user = User.objects.create(name="Test User")
    assert user.name == "Test User"
    assert str(user) == "Test User"


@pytest.mark.django_db
def test_post_creation():
    user = User.objects.create(name="Test User")
    post = Post.objects.create(title="Test Title", content="Test Content", user=user)
    assert post.title == "Test Title"
    assert post.content == "Test Content"
    assert post.user == user
    assert post.pub_date is not None
    assert str(post) == "Test Title"


@pytest.mark.django_db
def test_comment_creation():
    user = User.objects.create(name="Test User")
    post = Post.objects.create(title="Test Title", content="Test Content", user=user)
    comment = Comment.objects.create(text="Test Comment", user=user, post=post)
    assert comment.text == "Test Comment"
    assert comment.user == user
    assert comment.post == post
    assert comment.pub_date is not None
    assert str(comment) == f"Comment by {user} on {post}"


@pytest.mark.django_db
def test_user_profile_creation():
    user = User.objects.create(name="Test User")
    profile = UserProfile.objects.create(
        user=user, bio="This is a bio", website="http://mysite.com"
    )
    assert profile.user == user
    assert profile.bio == "This is a bio"
    assert profile.website == "http://mysite.com"
    assert str(profile) == f"Profile for {user}"


@pytest.mark.django_db
def test_tag_creation():
    tag = Tag.objects.create(name="Test Tag")
    assert tag.name == "Test Tag"
    assert str(tag) == "Test Tag"
