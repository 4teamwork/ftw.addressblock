from plone.dexterity.interfaces import IDexterityFTI
from ftw.addressblock.content.addressblock import IAddressBlockSchema
from ftw.addressblock.interfaces import IAddressBlock
from ftw.addressblock.tests import FunctionalTestCase
from zope.component import createObject
from zope.component import queryUtility


class AddressblockIntegrationTest(FunctionalTestCase):

    def setUp(self):
        super(AddressblockIntegrationTest, self).setUp()
        self.grant('Manager')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='ftw.addressblock.AddressBlock')
        schema = fti.lookupSchema()
        self.assertEqual(IAddressBlockSchema, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='ftw.addressblock.AddressBlock')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='ftw.addressblock.AddressBlock')
        factory = fti.factory
        addressblock = createObject(factory)
        self.assertTrue(IAddressBlock.providedBy(addressblock))
