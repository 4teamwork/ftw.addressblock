from plone.registry.interfaces import IRegistry
from zope.component import getUtility
import pkg_resources


IS_PLONE_5 = pkg_resources.get_distribution('Products.CMFPlone').version >= '5'


def uninstalled(site):
    if IS_PLONE_5:
        clean_plone5_registry(site)
    else:
        clean_plone4_registry(site)


def clean_plone5_registry(site):
    pass


def clean_plone4_registry(site):
    pass
    #registry = getUtility(IRegistry)

    #map_viewlet_position = registry[
    #        'collective.geo.settings.interfaces.IGeoFeatureStyle.map_viewlet_position']
    #map_viewlet_position = map_viewlet_position.replace(
    #        'plone.belowcontentbody', '')
    #registry['collective.geo.settings.interfaces.IGeoFeatureStyle.map_viewlet_position'] = \
    #    map_viewlet_position
