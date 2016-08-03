from ftw.addressblock import _
from plone.app.textfield import RichText
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import provider
from zope.schema.interfaces import IContextAwareDefaultFactory


@provider(IContextAwareDefaultFactory)
def get_default_address_title(context):
    title = context and context.title or u''
    if not isinstance(title, unicode):
        title = title.decode('utf-8')
    return title


@provider(IFormFieldProvider)
class IAddressblockDefault(model.Schema):

    address_title = schema.TextLine(
        title=_(u'label_address_title', default='Address title'),
        required=False,
        defaultFactory=get_default_address_title,
    )

    address = schema.TextLine(
        title=_(u'label_address', default=u'Address'),
        required=False,
        missing_value=u'',
    )

    extra_address_line = schema.TextLine(
        title=_(u'label_extra_address_line', default=u'Extra address line'),
        required=False,
        missing_value=u'',
    )

    zip_code = schema.TextLine(
        title=_(u'label_zip', default=u'ZIP'),
        required=False,
        missing_value=u'',
    )

    city = schema.TextLine(
        title=_(u'label_city', default=u'City'),
        required=False,
        missing_value=u'',
    )

    country = schema.TextLine(
        title=_(u'label_country', default=u'Country'),
        default=u'Schweiz',
        required=False,
    )

    directions = RichText(
        title=_(u'label_directions', default=u'Directions'),
        description=_(
            u'description_directions',
            default=u'Describe how to get to the above address by various means of transport.'
        ),
        required=False,
        default_mime_type='text/html',
        output_mime_type='text/x-html-safe',
        allowed_mime_types=('text/html',),
    )
