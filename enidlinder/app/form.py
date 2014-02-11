from enidlinder.app import MessageFactory as _
from five import grok
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema

# importing class to customising add view 
from plone.dexterity.browser.add import DefaultAddForm, DefaultAddView
from z3c.form import interfaces

# importing for fieldset
from plone.directives import form

#from zope import interface

# import for view class
from plone.dexterity.browser.add import DefaultAddForm, DefaultAddView

#from z3c.form.browser.textlines import TextLinesFieldWidget

from interfaces import IExcludeFromNavigationForm

# import for edit form
from plone.directives import dexterity, form


class IForm(model.Schema):
    """An application form for foundation. 
    """
    
    form.fieldset('Content',
        label=u"",
        fields=['title', 'charity_number', 'address', 'telephone',
            'email', 'website', 'description', 'project', 'project_aim']
    )
    
    
    title = schema.TextLine(
				title=_(u"Name of Charity"),
				)
	
    charity_number = schema.Int(
			title=_(u"Registered Charity Number"),
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

    website = schema.TextLine(
			title=_(u"Website"),
			required=False,
			)

    description = schema.Text(
			title=_(u"Brief statement of main objectives of your charity"),
			required=False,
			)

    project = schema.Text(
			title=_(u"Name of Project"),
			required=False,
			)
	
    project_aim = schema.Text(
			title=_(u"Aim of Project"),
			required=False,
			)
            
    form.fieldset('default',
        label=u"Level of funding sought",
        fields=['c_funding_sought', 'f_funding_sought']
    )        
				
    c_funding_sought = schema.TextLine(
			title=_(u"Current year"),
			required=False,
			)   
	
    f_funding_sought = schema.TextLine(
			title=_(u"Following year"),
			required=False,
			)
	
    form.fieldset('default',
        label=u"Briefly of Project",
        fields=['brief_project']
    )  		
    
    brief_project = schema.Text(
			title=_(u"Briefly describe your project and why it is needed and who will benefit"),
			required=False,
            )

    form.fieldset('default',
        label=u"Total Annual Income",
        fields=['c_income', 'f_income']
    )
    

    c_income = schema.TextLine(
			title=_(u"Current year"),
			required=False,
			)
			
    f_income = schema.TextLine(
			title=_(u"Following year"),
			required=False,
			)

    form.fieldset('default',
        label=u"Statutory Income",
        fields=['c_statutory_income', 'f_statutory_income']
    )
		
    c_statutory_income = schema.TextLine(
			title=_(u"Current year"),
			required=False,
			)
			
    f_statutory_income = schema.TextLine(
			title=_(u"Following year"),
			required=False,
			)

    form.fieldset('non_statutory_income',
        label=u"Non-Statutory Income",
        fields=['c_non_statutory_income', 'f_non_statutory_income']
    )
    
    
    c_non_statutory_income = schema.TextLine(
			title=_(u"Current year"),
			required=False,
			)
			
    f_non_statutory_income = schema.TextLine(
			title=_(u"Following year "),
			required=False,
			)
	
    form.fieldset('non_charitable_activities',
        label=u"Total spent on non-charitable activities",
        fields=['c_non_charitable_activities', 'f_non_charitable_activities']
    )
    
    c_non_charitable_activities = schema.TextLine(
			title=_(u"Current year"),
			required=False,
			)
			
    f_non_charitable_activities = schema.TextLine(
			title=_(u"Following year"),
			required=False,
			)

    form.fieldset('spent_fundraising',
        label=u"How much is spent annually on fundraising",
        fields=['c_spent_fundraising', 'f_spent_fundraising']
    )            
	
    c_spent_fundraising = schema.TextLine(
			title=_(u"Current year"),
			required=False,
			)
			
    f_spent_fundraising = schema.TextLine(
			title=_(u"Following year"),
			required=False,
			)

    form.fieldset('income_expenditure',
        label=u"Income & Expenditure balance - surplus or (deficit)",
        fields=['c_income_expenditure', 'f_income_expenditure']
    ) 
    
    c_income_expenditure = schema.TextLine(
			title=_(u"Current year"),
			required=False,
			)
			
    f_income_expenditure = schema.TextLine(
			title=_(u"Following year "),
			required=False,
			)

    form.fieldset('cash_reserves',
        label=u"Total cash reserves",
        fields=['c_cash_reserves', 'f_cash_reserves']
    )             
			
    c_cash_reserves = schema.TextLine(
			title=_(u"Current year"),
			required=False,
			)
			
    f_cash_reserves = schema.TextLine(
			title=_(u"Following year"),
			required=False,
			)

    form.fieldset('realisable_assets',
        label=u"Any other realisable assets? (e.g. land, property)",
        fields=['c_realisable_assets', 'f_realisable_assets']
    ) 
			
    c_realisable_assets = schema.TextLine(
			title=_(u"Current year "),
			required=False,
			)
			
    f_realisable_assets = schema.TextLine(
			title=_(u"Following year"),
			required=False,
			)
	 
    form.fieldset('',
        label=u"",
        fields=['trustees', 'supporters', 'previous_grant', 'hear']
    ) 
    
    trustees = schema.Text(
			title=_(u"Names of your trustees"),
			required=False,
			)
	
    supporters = schema.Text(
			title=_(u"Names of previous significant supporters"),
			required=False,
			)
			
    previous_grant  = schema.Text(
			title=_(u"Details of any previous significant supporters"),
			description=_(u"please list date(s) and amount(s)"),
			required=False,
			)
	
    hear = schema.Text(
			title=_(u"How did you hear of the foundation?"),
			required=False,
			)

            
@form.default_value(field = IExcludeFromNavigationForm['exclude_from_nav'])
def excludeFromNavDefaultValue(data):
    return True    

    
class AddForm(DefaultAddForm):
    
    enable_form_tabbing = False
    
    def updateWidgets(self):
        super(AddForm, self).updateWidgets()
        
             
class AddView(DefaultAddView):
    form = AddForm

    
class EditForm(dexterity.EditForm):
    
    grok.context(IForm)
    enable_form_tabbing = False
	
    def updateWidgets(self):
        dexterity.EditForm.updateWidgets(self)    