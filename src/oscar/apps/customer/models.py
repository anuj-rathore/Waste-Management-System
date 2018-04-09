from oscar.apps.customer import abstract_models
from oscar.core.loading import is_model_registered
from django.conf import settings
settings.EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
settings.EMAIL_USE_TLS = True
settings.EMAIL_HOST = 'smtp.gmail.com'
settings.EMAIL_PORT = 587
settings.OSCAR_FROM_EMAIL = 'dhongibaba1508@gmail.com'
settings.EMAIL_HOST_USER = 'dhongibaba1508@gmail.com'
settings.EMAIL_HOST_PASSWORD = '9052690965'

from django.core.mail import send_mail

__all__ = []

if not is_model_registered('customer', 'Email'):
    print "here"
    class Email(abstract_models.AbstractEmail):
        def save(self, *args, **kwargs):
            super(Email, self).save(*args, **kwargs)

            send_mail(self.subject, 
                self.body_text, 
                settings.OSCAR_FROM_EMAIL, 
                [self.email], 
                fail_silently=False)

    __all__.append('Email')


if not is_model_registered('customer', 'CommunicationEventType'):
    class CommunicationEventType(
            abstract_models.AbstractCommunicationEventType):
        pass

    __all__.append('CommunicationEventType')


if not is_model_registered('customer', 'Notification'):
    class Notification(abstract_models.AbstractNotification):
        pass

    __all__.append('Notification')


if not is_model_registered('customer', 'ProductAlert'):
    class ProductAlert(abstract_models.AbstractProductAlert):
        pass

    __all__.append('ProductAlert')
