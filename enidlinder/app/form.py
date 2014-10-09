from enidlinder.app import MessageFactory as _
from five import grok
from plone.supermodel import model
from zope import schema

# importing class to customising add view
from plone.dexterity.browser.add import DefaultAddForm, DefaultAddView
from interfaces import IExcludeFromNavigationForm

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
