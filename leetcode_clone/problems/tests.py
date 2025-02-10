from django.test import TestCase
from django.contrib.auth.models import User
from .models import Problem, QuestionAttempt

class QuestionAttemptModelTest(TestCase):

    def setUp(self):
        # Create a user and a problem for testing
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.problem = Problem.objects.create(
            title='Test Problem',
            description='This is a test problem.',
            option_a='Option A',
            option_b='Option B',
            option_c='Option C',
            option_d='Option D',
            correct_answer='A'
        )

    def test_create_question_attempt(self):
        # Create a QuestionAttempt
        attempt = QuestionAttempt.objects.create(
            user=self.user,
            problem=self.problem,
            selected_answer='A',
            is_correct=True
        )
        self.assertEqual(attempt.user, self.user)
        self.assertEqual(attempt.problem, self.problem)
        self.assertEqual(attempt.selected_answer, 'A')
        self.assertTrue(attempt.is_correct)

    def test_check_answer_logic(self):
        # Create a QuestionAttempt and check the answer logic
        attempt = QuestionAttempt.objects.create(
            user=self.user,
            problem=self.problem,
            selected_answer='B',  # Incorrect answer
            is_correct=False
        )
        attempt.check_answer()  # This should update is_correct
        self.assertFalse(attempt.is_correct)

    def test_unique_attempt_per_user_problem(self):
        # Create a QuestionAttempt
        QuestionAttempt.objects.create(
            user=self.user,
            problem=self.problem,
            selected_answer='A',
            is_correct=True
        )
        # Attempting to create a second attempt should raise an IntegrityError
        with self.assertRaises(Exception):
            QuestionAttempt.objects.create(
                user=self.user,
                problem=self.problem,
                selected_answer='B',
                is_correct=False
            )
