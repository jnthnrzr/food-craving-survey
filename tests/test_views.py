import unittest

from application import app, db
from application.config import TestingConfig
from application.forms import InputForm
from application.models import Image, Trial


class TestViews(unittest.TestCase):
    def setUp(self):
        """Set testing configuration before each test."""
        app.config.from_object(TestingConfig)
        self.app = app
        self.client = app.test_client()
        db.create_all()

    def tearDown(self):
        """Clear testing configuration after each test."""
        db.session.remove()
        db.drop_all()

    def test_view_participant_page_get_request(self):
        """Check if get request works on participant page."""
        result = self.client.get("/")
        message = b"Enter the participant number:"
        self.assertIn(message, result.data)

    def test_participant_successful_post_request_302(self):
        """Get a 302 status code for post request at participant page."""
        response = self.client.post("/", data=dict(number=99))
        self.assertEqual(response.status_code, 302)

    def test_participant_successful_post_request_redirect_works(self):
        response = self.client.post("/", data=dict(number=99),
                                    follow_redirects=True)
        message = b"Enter the session number:"
        self.assertIn(message, response.data)

    def test_participant_post_request_no_data(self):
        """Bounce back to same page when sending post request without data."""
        response = self.client.post("/")
        message = b"The input was not valid. Please enter a whole number."
        self.assertIn(message, response.data)

    def test_participant_follow_to_instructions_ok_status(self):
        """Check ok status code to reach instructions page."""
        with self.client.session_transaction() as sess:
            sess["p_num"] = 99
            form = InputForm()
            form.number.data = 99
            response = self.client.post("/", data=form.data,
                                        follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_session_follow_to_instructions_header(self):
        """Reach instructions page by submitting inputs correctly."""
        tester = self.client
        with tester.session_transaction() as sess:
            form = InputForm()
            form.number.data = 99
            sess["p_num"] = 99
            sess["s_num"] = 99
        response = tester.post("/session", data=form.data,
                               follow_redirects=True)
        message = b"Welcome to the Food Craving Survey."
        self.assertIn(message, response.data)

    def test_session_duplicate_trial(self):
        """Get an error message when trial exists in database."""
        with self.client.session_transaction() as sess:
            t = Trial(participant=99, session=99)
            db.session.add(t)
            db.session.commit()
            sess["p_num"] = 99
        response = self.client.post("/session", data=dict(number=99),
                                    follow_redirects=True)
        message = b"Participant and session already exist. Try again."
        self.assertIn(message, response.data)

    def test_session_save_trial(self):
        """Save the trial when inputs are correct."""
        with self.client.session_transaction() as sess:
            sess["p_num"] = 99
        response = self.client.post("/session", data=dict(number=99),
                                    follow_redirects=True)
        message = b"Participant and session recorded."
        self.assertIn(message, response.data)

    def test_session_post_request_no_data(self):
        """Bounce back to same page when sending post request without data."""
        response = self.client.post("/session", follow_redirects=True)
        message = b"The input was not valid. Please enter a whole number."
        self.assertIn(message, response.data)

    def test_get_instructions(self):
        """View instructions page."""
        response = self.client.get("/instructions")
        message = b"Welcome to the Food Craving Survey."
        self.assertIn(message, response.data)

    def test_post_instructions_no_images(self):
        """Get thank you when sending post request with no images."""
        response = self.client.post("/instructions", follow_redirects=True)
        message = b"Thank you for participating in this study."
        self.assertIn(message, response.data)


if __name__ == '__main__':
    unittest.main()
