from plone import api
from plone.app.uuid.utils import uuidToObject
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.content import Item
from plone.directives import form
from ftw.addressblock import _
from ftw.addressblock.interfaces import IAddressBlock
from zope.i18n import translate
from zope.interface import implements
from zope.interface import provider
from Products.CMFPlone.utils import safe_unicode


@provider(IFormFieldProvider)
class IAddressBlockSchema(form.Schema):
    pass


class AddressBlock(Item):
    implements(IAddressBlock)

    def Title(self):
        return self.title

    @property
    def title(self):
        parent_title = u''
        fallback_title = api.portal.get().Title()

        uuid = getattr(self, '_plone.uuid', None)
        if uuid:
            parent_title = uuidToObject(uuid).aq_parent.Title()

        return u'{0} - {1}'.format(
            safe_unicode(self.block_title),
            safe_unicode(parent_title or fallback_title),
        )

    @property
    def block_title(self):
        return translate(
            _(u'addressblock_title', default=u'Contact'),
            context=api.portal.get().REQUEST,
        )
