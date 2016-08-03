from ftw.addressblock.tests import FunctionalTestCase
from ftw.builder import Builder
from ftw.builder import create
from ftw.testbrowser import browsing
from zope.component import getMultiAdapter


class AddressblockViewFunctionalTest(FunctionalTestCase):

    def setUp(self):
        super(AddressblockViewFunctionalTest, self).setUp()
        self.grant('Manager')
        self.portal.portal_languages.manage_setLanguageSettings(
            'de',
            ['de'],
            setUseCombinedLanguageCodes=False
        )

        self.page = create(Builder('sl content page')
                           .titled(u'Pr\xe4sidialdirektion'))

    @browsing
    def test_render(self, browser):
        create(Builder('sl addressblock')
               .within(self.page))

        browser.login().visit(self.page)

        self.assertEquals(
            u'Kontakt',
            browser.css('.sl-block h2').first.text
        )

    @browsing
    def test_address_title_default_value_is_parents_title(self, browser):

        page = create(Builder('sl content page').titled(u'A p\xe4ge'))
        browser.login().visit(page, view='++add++ftw.addressblock.AddressBlock')

        self.assertEqual(
            u'A p\xe4ge',
            browser.find_field_by_text('Adresstitel').value
        )

    @browsing
    def test_country_default_value_is_static(self, browser):
        browser.login().visit(
            self.page,
            view='++add++ftw.addressblock.AddressBlock'
        )

        self.assertEqual(
            u'Schweiz',
            browser.find_field_by_text('Land').value
        )

    @browsing
    def test_render_detail_view(self, browser):
        addressblock = create(Builder('sl addressblock')
                              .within(self.page))

        browser.login().visit(addressblock, view='addressblock_detail_view')

        self.assertEquals(
            u'Kontakt - Pr\xe4sidialdirektion',
            browser.css('h1.documentFirstHeading').first.text
        )

    def test_has_team(self):
        addressblock = create(Builder('sl addressblock').within(self.page))
        view = getMultiAdapter(
            (addressblock, self.request), 
            name='block_view'
        )

        self.assertFalse(view.has_team())

        create(Builder('sl content page')
               .titled(u'Team')
               .having(id='team')
               .within(self.page))
        self.assertTrue(view.has_team())
