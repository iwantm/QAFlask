import unittest
from flask import url_for
from flask_testing import TestCase

from app import app, db, Register


class TestBase(TestCase):
    def create_app(self):
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                          SECRET_KEY='TEST_SECRET_KEY',
                          DEBUG=True
                          )
        return app

    def setUp(self):
        db.create_all()

        sample1 = Register(name="MissWoman")

        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):

        db.session.remove()
        db.drop_all()


class TestAdd(TestBase):
    def test_add_post(self):
        response = self.client.post(
            url_for('home'),
            data=dict(name="MrMan")
        )
        self.assertIn(b'MrMan', response.data)


class TestUpdate(TestBase):
    def test_update_post(self):
        response = self.client.post(
            url_for('update'),
            data=dict(oldname="MissWoman", newname="MissLady"),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
# Test Deleting


class TestDelete(TestBase):
    def test_delete_post(self):
        response = self.client.post(
            url_for('delete'),
            data=dict(name="MissWoman"),
            follow_redirects=True
        )
        self.assertEqual(response.status_code, 200)
