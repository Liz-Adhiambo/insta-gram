
from django.test import TestCase

from .models import  FollowersCount, LikePost, Post, Profile
# Create your tests here.

class ProfileTestClass(TestCase):
    #Set up Method
    def setUp(self):
        self.prof = Profile(name="Liz")
        self.prof.save_profile()

    def test_instance(self):
        self.assertTrue(isinstance(self.prof,Profile))

    def test_save_method(self):
        self.prof.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        self.prof.save_profile()
        self.prof.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)

    def test_update(self):
        profile = Profile.get_profile_id(self.prof.id)
        profile.update_profile('liz')
        profile = Profile.get_profile_id(self.prof.id)
        self.assertTrue(profile.username == 'liz')
 
 
 #test for Post Model

class PostTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.post = Post(caption="fashion")
        self.post.save_post()

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_method(self):
        self.post.save_post()
        posts= Post.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_delete_method(self):
        self.post.save_post()
        self.post.delete_post()
        post = Post.objects.all()
        self.assertTrue(len(post) == 0)

    def test_update(self):
        post = Post.get_category_id(self.post.id)
        post.update_post('Travel')
        post = Post.get_post_id(self.post.id)
        self.assertTrue(post.name == 'Travel')

#  #test for Like Model

class LikePostTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.like = LikePost(username="liz")
        self.like.save_like()


    def test_instance(self):
        self.assertTrue(isinstance(self.like, LikePost))

#     

    def test_save_method(self):
        self.like.save_like()
        likes  = LikePost.objects.all()
        self.assertTrue(len(likes)>0)


# # Create your tests here.

class FollowersCountTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.fol = FollowersCount(user="test1")
        self.fol.save_followers()

        
    def test_instance(self):
        self.assertTrue(isinstance(self.user, FollowersCount))


