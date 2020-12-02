from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from versatileimagefield.fields import VersatileImageField
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):

    def avatar_directory_path(self, instance, filename):
        return 'user-avatars/user_{0}'.format(instance.User.id)

    username = models.CharField(max_length=128, unique=False, blank=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=256, blank=True)
    last_name = models.CharField(max_length=256, blank=True)
    country = models.CharField(max_length=128, blank=True)
    company_name = models.CharField(max_length=256, blank=True)  
    street_address_1 = models.CharField(max_length=256, blank=True)
    street_address_2 = models.CharField(max_length=256, blank=True)
    city = models.CharField(max_length=256, blank=True)
    city_area = models.CharField(max_length=128, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    note = models.TextField(null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    last_visit = models.DateTimeField(auto_now=True, editable=True)
    avatar = VersatileImageField(
        upload_to=avatar_directory_path, blank=True, null=True)

    USERNAME_FIELD = "email"

    objects = UserManager()

    class Meta:
        verbose_name = u'User'
        verbose_name_plural = u'Users'

    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s %s' % (self.username, self.email, self.first_name, self.last_name, self.street_address_1, self.street_address_2, self.city, self.city_area, self.postal_code, self.note)

    @property
    def full_name(self):
        return "%s %s" % (self.first_name, self.last_name)


class CustomerEvents:

    # Account-related events
    ACCOUNT_CREATED = "account_created"
    PASSWORD_RESET_LINK_SENT = "password_reset_link_sent"
    PASSWORD_RESET = "password_reset"
    PASSWORD_CHANGED = "password_changed"
    EMAIL_CHANGE_REQUEST = "email_change_request"
    EMAIL_CHANGED = "email_changed"

    # Order-related events
    PRODUCT_PURCHASED = "product_purchased"
    NOTE_ADDED_TO_ORDER = "note_added_to_order"
    DIGITAL_LINK_DOWNLOADED = "digital_link_downloaded"

    # Staff actions over customers events
    CUSTOMER_DELETED = "customer_deleted"
    EMAIL_ASSIGNED = "email_assigned"
    NAME_ASSIGNED = "name_assigned"
    NOTE_ADDED = "note_added"

    CHOICES = [
        (ACCOUNT_CREATED, "The account was created."),
        (PASSWORD_RESET_LINK_SENT, "Password reset link was sent to the customer."),
        (PASSWORD_RESET, "The account password was reset."),
        (
            EMAIL_CHANGE_REQUEST,
            "The user requested to change the account's email address.",
        ),
        (PASSWORD_CHANGED, "The account password was changed."),
        (EMAIL_CHANGED, "The account email address was changed."),
        (PRODUCT_PURCHASED, "A product was purchased."),
        (NOTE_ADDED_TO_ORDER, "A note was added."),
        (DIGITAL_LINK_DOWNLOADED, "A digital product was downloaded."),
        (CUSTOMER_DELETED, "The customer was deleted."),
        (NAME_ASSIGNED, "The customer's name was edited."),
        (EMAIL_ASSIGNED, "The customer's email address was changed."),
        (NOTE_ADDED, "A note was added to the customer"),
    ]


"""
class CustomerEvent(models.Model):
    datetime = models.DateTimeField(default=timezone.now, editable=False)
    type = models.CharField(
        max_length=255,
        choices=[
            (type_name.upper(), type_name) for type_name, _ in CustomerEvents.CHOICES
        ],
    )
    order = models.ForeignKey(
        "order.Order", on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(
        User, related_name="events", on_delete=models.CASCADE)

    class Meta:
        ordering = ("date",)

    def __repr__(self):
        return f"{self.__class__.__name__}(type={self.type!r}, user={self.user!r})"
"""