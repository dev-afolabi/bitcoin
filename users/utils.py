import logging
from django.template.loader import render_to_string
import traceback
from django.contrib.auth.tokens import default_token_generator as token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.exceptions import ValidationError




logger = logging.getLogger(__name__)

class ActivationMailFormMixin:
    mail_validation_error = ''

    def log_mail_error(self, **kwargs):
        msg_list = [
            'Activation Email did not sent. \n',
            'from_email: {from_email}\n'
            'subject: {subject}\n'
            'message: {message}\n',
        ]
        recipient_list = kwargs.get(
            'recipient_list', []
        )
        for recipient in recipient_list:
            msg_list.insert(
                1,'recipient: {r}\n'.format(r=recipient)
            )
        if 'error' in kwargs:
            level = ERROR

            error_msg = (
                'error: {0.__class__.__name__}\n'
                'args: {0.args}\n'
            )
            error_info = error_msg.format(
                kwargs['error']
            )
            msg_list.insert(1,error_info)
        else:
            level = CRITICAL
        
        msg = ''.join(msg_list).format(**kwargs)
        logger.log(level,msg)

    @property
    def mail_sent(self):
        if hasattr(self, '_mail_sent'):
            return self._mail_sent
        return False

    @mail_sent.setter
    def set_mail_sent(self, value):
        raise TypeError('cannot set mail_sent attribute')

    def get_message(self, **kwargs):
        email_template_name = kwargs.get(
            'email_template_name'
        )
        context = kwargs.get(
            'context'
        )
        return render_to_string(
            email_template_name,context
        )

    def get_subject(self, **kwargs):
        subject_template_name = kwargs.get(
            'subject_template_name'
        )
        context = kwargs.get(
            'context'
        )
        subject = render_to_string(
            subject_template_name, context
        )
        return subject

    def get_context_data(self, request, user, context=None):
        if context is None:
            context = dict()
        current_site = get_current_site(request)
        if request.is_secure():
            protocol = 'https'
        else:
            protocol = 'http'
        token = token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        context.update({
            'domain':current_site.domain,
            'protocol':protocol,
            'site_name':current_site.name,
            'token':token,
            'uid':uid,
            'user':user
        })
        return context


        def _send_email(self, request, user, **kwargs):
            kwargs['context'] = self.get_context_data(request, user)
            mail_kwargs = {
                "subject":self.get_subject(**kwargs),
                "message":self.get_message(**kwargs),
                "from_email":(
                    settings.DEFAULT_FROM_EMAIL
                ),
                "recipient_list":[user.email],
            }
            try:
                number_sent = send_email(**mail_kwargs)
            except Exception as error:
                self.log_mail_error(error = error, **mail_kwargs)
                if isinstance(error, BadHeaderError):
                    err_code = 'badheader'
                elif isinstance(error, SMTPException):
                    err_code = 'smpterror'
                else:
                    err_code = 'unexpectederror'
                return (False, err_code)
            else:
                if number_sent > 0:
                    return (True, None)
            self.log_mail_error(**mail_kwargs)
            return (False, 'unknowneror')

    def send_mail(self, user, **kwargs):
        request = kwargs.pop('request', None)
        if request is None:
            tb = traceback.format.stack()
            tb = [' ' + line for line in tb]
            logger.warning(
                'send mail called without '
                'request. \nTraceback: \n{}'.format(
                    ''.join(tb)
                )
            )
            self.mail_sent = False
            return self.mail_sent
        self._mail_sent, error = (
            self._send_mail(request, user, **kwargs)
        )
        if not self.mail_sent:
            self.add_error(
                None,
                ValidationError(
                    self.mail_validation_error,
                    code = error
                )
            )
        return self.mail_sent

class MailContextMixin:
    email_template_name = 'registration/email_create.txt'
    subject_template_name = ('registration/subject_create.txt')

    def get_save_kwargs(self, request):
        return {
            'email_template_name': self.email_template_name,
            'request': request,
            'subject_template_name':self.subject_template_name,
        }
