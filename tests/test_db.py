import unittest
from peewee import *
from app import TimelinePost

MODELS = [TimelinePost]

# use an in-memory SQLite for tests.
test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        # Bind model classes to test db. Since we have a complete list of
        # all models, we do not need to recursively bind.dependencies.
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        # Not strictly necessary since SQLite in-memory databases only live
        # for the duration of the connection, but it's a good practice...
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        # Create 2 timeline posts.
        first_post = TimelinePost.create(
            name='John Doe',
            email='john@example.com',
            content="Hello world, I'm John!"
        )
        assert first_post.id == 1

        second_post = TimelinePost.create(
            name='Jane Doe',
            email='jane@example.com',
            content="Hello world, I'm Jane!"
        )
        assert second_post.id == 2

        # TODO: Get timeline posts and assert that they are correct

    def test_timeline_get(self): #basically here we do  two tests, 1) check if we have 2 posts and 2) check first post contents
       
        first_post = TimelinePost.create( #just copying over creating posts
            name='John Doe',
            email='john@example.com',
            content="Hello world, I'm John!" )
        assert first_post.id == 1

        second_post = TimelinePost.create(
            name='Jane Doe',
            email='jane@example.com',
            content="Hello world, I'm Jane!")
        posts = TimelinePost.select() #select all basically
        assert len(posts) == 2 #should have 2 posts

        obtained_post = posts[0] #grab first post
        assert first_post.name == 'John Doe'
        assert first_post.email == 'john@example.com'