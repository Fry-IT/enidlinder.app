from Acquisition import aq_inner, aq_parent
from AccessControl.SecurityManagement import getSecurityManager
from enidlinder.app import MessageFactory as _
from five import grok
from plone.supermodel import model
from zope import schema
from Products.statusmessages.interfaces import IStatusMessage
from plone.dexterity.events import AddCancelledEvent
from zope.event import notify
# importing class to customising add view
from plone.dexterity.browser.add import DefaultAddForm, DefaultAddView
from interfaces import IExcludeFromNavigationForm
from z3c.form import button
from plone.dexterity.utils import addContentToContainer
from plone.dexterity.interfaces import IDexterityFTI
from zope.component import getUtility

# import for edit form
from plone.directives import dexterity, form

from plone.namedfile.field import NamedBlobFile


class IForm(model.Schema):
    """An application form for foundation.
    """

    title = schema.TextLine(
        title=_(u"Name of Charity"),
        )

    charity_number = schema.Int(
        title=_(u"Registered Charity Number"),
        required=False,
        )

    aim_of_charity = schema.Text(
        title=_(u"Aim of charity"),
        description=_(u"(Maximum 50 words)"),
        required=False,
        )

    name_of_correspondent = schema.TextLine(
        title=_(u"Name of Correspondent"),
        required=False,
        )

    position = schema.TextLine(
        title=_(u"Position"),
        required=False,
        )

    address = schema.Text(
        title=_(u"Name and Address for Correspondence"),
        required=False,
        )

    telephone = schema.TextLine(
        title=_(u"Telephone number"),
        required=False,
        )

    email = schema.TextLine(
        title=_(u"Email address"),
        required=False,
        )

    project = schema.Text(
        title=_(u"Title of Project"),
        required=False,
        )

    aim_of_project = schema.Text(
        title=_(u"Aim of Project"),
        description=_(u"(Maximum 200 words)"),
        required=False,
        )

    length_of_project = schema.TextLine(
        title=_(u"Length of Project"),
        required=False,
        )

    project_benefit = schema.Text(
        title=_(u"Who will benefit from the project?"),
        required=False,
        )

    money_applying = schema.TextLine(
        title=_(u"How much are you applying for?"),
        required=False,
        )

    money_raised = schema.TextLine(
        title=_(u"How much have you raised towards the project?"),
        required=False,
    )

    previous_grant = schema.TextLine(
        title=_(u"Have you received a grant from the Foundation before? Please specify any dates"),
        required=False,
    )

    supporting_docs = NamedBlobFile(
        title=_(u"Supporting document"),
        description=_(u"No more than 2 sides of A4 paper"),
        required=False,
    )


@form.default_value(field=IExcludeFromNavigationForm['exclude_from_nav'])
def excludeFromNavDefaultValue(data):
    return True


class AddForm(DefaultAddForm):
    immediate_view = '/apply'
    enable_form_tabbing = True

    def updateWidgets(self):
        super(AddForm, self).updateWidgets()

        field_list = {
                'aim_of_charity': 4,
                'aim_of_project': 10,
                'project_benefit': 4,
                }

        for key, value in field_list.iteritems():
            self.widgets[key].rows = value

    @button.buttonAndHandler(_('Save'), name='save')
    def handleAdd(self, action):
        data, errors = self.extractData()
        if errors:
            self.status = self.formErrorsMessage
            return
        obj = self.createAndAdd(data)
        if obj is not None:
            # mark only as finished if we get the new object
            self._finishedAdd = True
            IStatusMessage(self.request).addStatusMessage(_(u"Please review your application and submit when ready"), "info")
            self.request.response.redirect(self.nextURL())

    @button.buttonAndHandler(_(u'Cancel'), name='cancel')
    def handleCancel(self, action):
        container = aq_parent(aq_inner(self.context))
        IStatusMessage(self.request).addStatusMessage(_(u"Add New Item operation cancelled"), "info")
        notify(AddCancelledEvent(self.context))
        self.request.response.redirect(container.absolute_url())


class AddView(DefaultAddView):
    form = AddForm


class EditForm(dexterity.EditForm):

    grok.context(IForm)
    enable_form_tabbing = True

    def updateWidgets(self):
        dexterity.EditForm.updateWidgets(self)

        field_list = {
                'aim_of_charity': 4,
                'aim_of_project': 10,
                'project_benefit': 4,
                }

        for key, value in field_list.iteritems():
            self.widgets[key].rows = value


class AuthenticatedUser:
    def __init__(self):
        self.user = getSecurityManager().getUser()
        if self.user:
            self.user_type = self.user.getProperty('user_type')

    def isIndividual(self):
        if self.user_type == 'Individual':
            return True
        return False

    def isMedicalSchool(self):
        if self.user_type == 'Medical School':
            return True
        return False


class View(grok.View):
    grok.context(IForm)
    grok.require('zope2.View')
    grok.name('view')

    def userIndividual(self):
        auth_user = AuthenticatedUser()
        if auth_user.isIndividual():
            return True
        return False

    def userMedicalSchool(self):
        auth_user = AuthenticatedUser()
        if auth_user.isMedicalSchool():
            return True
        return False

    def update(self):
        self.review_state = self.context.portal_workflow.getInfoFor(self.context, 'review_state')

    def canEdit(self):
        return self.review_state == 'private'

    def canSubmit(self):
        return self.review_state == 'private'
