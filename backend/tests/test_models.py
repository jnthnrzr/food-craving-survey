import unittest
from datetime import datetime
from unittest.mock import MagicMock

from app.models import Trial


class TestMockTrialModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        mock_trial = MagicMock(spec=Trial)
        mock_trial.participant = 99
        mock_trial.session = 99
        mock_trial.date = datetime.today()
        cls.trial = mock_trial

    def test_trial_instance(self):
        trial = self.trial
        self.assertIsInstance(trial, Trial)

    def test_participant_label(self):
        label = 'participant'
        attributes = dir(self.trial)
        self.assertIn(label, attributes)

    def test_participant_data_type(self):
        data_type = type(self.trial.participant)
        self.assertIs(data_type, int)

    def test_session_data_type(self):
        data_type = type(self.trial.session)
        self.assertIs(data_type, int)

    def test_session_label(self):
        label = 'session'
        attributes = dir(self.trial)
        self.assertIn(label, attributes)

    def test_date_label(self):
        label = 'date'
        attributes = dir(self.trial)
        self.assertIn(label, attributes)


if __name__ == "__main__":
    unittest.main()
