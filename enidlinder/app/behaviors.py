from enidlinder.app.interfaces import IExcludeFromNavigationForm
from zope.interface import implements


class ExcludeFromNavigationForm(object):
    implements(IExcludeFromNavigationForm)
