from django.test import TestCase

from profiles_api.models import UserProfile, UserProfileManager


class UserProfileManagerTests(TestCase):
    """Tests for UserProfileManager."""

    def test_create_user_with_valid_data(self):
        """Creating a user with valid email, name and password succeeds."""
        user = UserProfile.objects.create_user(
            email="test@example.com",
            name="Test User",
            password="testpass123",
        )
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.name, "Test User")
        self.assertTrue(user.check_password("testpass123"))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user_raises_without_email(self):
        """Creating a user without email raises ValueError."""
        with self.assertRaises(ValueError) as ctx:
            UserProfile.objects.create_user(
                email="",
                name="Test User",
                password="testpass123",
            )
        self.assertIn("email", str(ctx.exception).lower())

    def test_create_user_normalizes_email(self):
        """User email is normalized (domain part lowercased)."""
        user = UserProfile.objects.create_user(
            email="Test@EXAMPLE.COM",
            name="Test User",
            password="testpass123",
        )
        # Django's normalize_email lowercases the domain only
        self.assertEqual(user.email, "Test@example.com")

    def test_create_user_without_password(self):
        """Creating a user without password is allowed (e.g. for unusable password)."""
        user = UserProfile.objects.create_user(
            email="test@example.com",
            name="Test User",
        )
        self.assertFalse(user.check_password(""))
        self.assertTrue(user.password)  # hashed unusable or set

    def test_create_superuser_sets_staff_and_superuser(self):
        """create_superuser sets is_staff and is_superuser to True."""
        user = UserProfile.objects.create_superuser(
            email="admin@example.com",
            name="Admin User",
            password="adminpass123",
        )
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
        self.assertEqual(user.email, "admin@example.com")
        self.assertEqual(user.name, "Admin User")


class UserProfileModelTests(TestCase):
    """Tests for UserProfile model."""

    def test_user_profile_str_returns_email(self):
        """String representation of UserProfile is the email."""
        user = UserProfile.objects.create_user(
            email="str@example.com",
            name="Str Test",
            password="pass",
        )
        self.assertEqual(str(user), "str@example.com")

    def test_get_full_name_returns_name(self):
        """get_full_name returns the user's name."""
        user = UserProfile.objects.create_user(
            email="full@example.com",
            name="Full Name",
            password="pass",
        )
        self.assertEqual(user.get_full_name(), "Full Name")

    def test_get_short_name_returns_name(self):
        """get_short_name returns the user's name."""
        user = UserProfile.objects.create_user(
            email="short@example.com",
            name="Short Name",
            password="pass",
        )
        self.assertEqual(user.get_short_name(), "Short Name")

    def test_username_field_is_email(self):
        """USERNAME_FIELD is 'email'."""
        self.assertEqual(UserProfile.USERNAME_FIELD, "email")

    def test_required_fields_include_name(self):
        """REQUIRED_FIELDS includes 'name'."""
        self.assertIn("name", UserProfile.REQUIRED_FIELDS)

    def test_email_unique(self):
        """Duplicate email is not allowed."""
        UserProfile.objects.create_user(
            email="unique@example.com",
            name="First",
            password="pass",
        )
        with self.assertRaises(Exception):  # IntegrityError from DB
            UserProfile.objects.create_user(
                email="unique@example.com",
                name="Second",
                password="pass",
            )
