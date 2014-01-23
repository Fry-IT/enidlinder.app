from plone.app.dexterity.behaviors.exclfromnav import IExcludeFromNavigation

from z3c.form.interfaces import IEditForm, IAddForm
from zope.interface import alsoProvides
from zope import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.autoform import directives as form
from plone.supermodel import model
from plone.app.dexterity import MessageFactory as _

from z3c.form import interfaces

class IExcludeFromNavigationForm(IExcludeFromNavigation):
    """Behavior interface to exclude items from navigation.
    """
    model.fieldset(
        'new',
        label=_(u"New Setting"),
        fields=['exclude_from_nav']
    )

    exclude_from_nav = schema.Bool(
        title=_(
            u'label_exclude_from_nav',
            default=u'Exclude from TEST navigation'

        ),
        description=_(
            u'help_exclude_from_nav',
            default=u'If selected, this item will not appear in the ' +
                    u'navigation tree'
        ),
        default=True,
        readonly = True,
    )

    form.omitted('exclude_from_nav')
    form.omitted(IEditForm, 'exclude_from_nav')

   
alsoProvides(IExcludeFromNavigationForm, IFormFieldProvider)