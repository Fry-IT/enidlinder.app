from enidlinder.app import MessageFactory as _
from five import grok
from plone.app.textfield import RichText
from plone.supermodel import model
from zope import schema

# fieldset
from plone.directives import form

#datagrid for table inside form
from collective.z3cform.datagridfield import DataGridFieldFactory, DictRow
from zope import interface

from plone.dexterity.browser.add import DefaultAddForm, DefaultAddView


# class ITableRowSchema(interface.Interface):
    # current_year = schema.TextLine(title=u"Current year")
    # following_year = schema.TextLine(title=u"Following year")
    
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
	# form.widget(table=DataGridFieldFactory)  
	# table = schema.List(title=u"Level of funding sought",
				# value_type=DictRow(title=u"", 
								   # schema=ITableRowSchema,
								   # required=False))
				
	c_funding_sought = schema.TextLine(
			title=_(u"Level of funding sought"),
			description=_("current year"),
			required=False,
			)
			
	f_funding_sought = schema.TextLine(
			title=_(u"Level of funding sought"),
			description=_("next year"),
			required=False,
			)
			
			
	brief_project = schema.Text(
			title=_(u"Briefly of Project"),
			description=_("Briefly describe your project and why it is needed and who will benefit"),
			required=False,
			)

	c_income = schema.TextLine(
			title=_(u"Current year total annual income"),
			required=False,
			)
			
	f_income = schema.TextLine(
			title=_(u"Following year total annual income"),
			required=False,
			)
		
	c_statutory_income = schema.TextLine(
			title=_(u"Current year statutory income"),
			required=False,
			)
			
	f_statutory_income = schema.TextLine(
			title=_(u"Following year statutory income"),
			required=False,
			)
			
	c_non_statutory_income = schema.TextLine(
			title=_(u"Current year non-statutory income"),
			required=False,
			)
			
	f_non_statutory_income = schema.TextLine(
			title=_(u"Following year non-statutory income"),
			required=False,
			)
	
	c_non_charitable_activities = schema.TextLine(
			title=_(u"Total spent on current year on non-charitable activities"),
			required=False,
			)
			
	f_non_charitable_activities = schema.TextLine(
			title=_(u"Total spent on following year on non-charitable activities"),
			required=False,
			)
	c_spent_fundraising = schema.TextLine(
			title=_(u"How much is spent current year on annually on fundraising"),
			required=False,
			)
			
	f_spent_fundraising = schema.TextLine(
			title=_(u"How much is spent following year on annually on fundraising"),
			required=False,
			)
	
	c_income_expenditure = schema.TextLine(
			title=_(u"Current year - Income & Expenditure balance - surplus or (deficit)"),
			required=False,
			)
			
	f_income_expenditure = schema.TextLine(
			title=_(u"Following year - Income & Expenditure balance - surplus or (deficit)"),
			required=False,
			)
			
	c_cash_reserves = schema.TextLine(
			title=_(u"Current year - Total cash reserves"),
			required=False,
			)
			
	f_cash_reserves = schema.TextLine(
			title=_(u"Following year - Total cash reserves"),
			required=False,
			)
			
	c_realisable_assets = schema.TextLine(
			title=_(u"Current year - Any other realisable assets? (e.g. land, property)"),
			required=False,
			)
			
	f_realisable_assets = schema.TextLine(
			title=_(u"Following year - Any other realisable assets? (e.g. land, property)"),
			required=False,
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
	
	
# class AddForm(DefaultAddForm):
	# def updateWidgets(self):
		# super(AddForm, self).updateWidgets()
		# self.widgets['table'].allow_insert = False # Enable/Disable the insert button on the right
		# self.widgets['table'].allow_delete = False # Enable/Disable the delete button on the right
		# self.widgets['table'].auto_append = False  # Enable/Disable the auto-append feature
		# self.widgets['table'].allow_reorder = False  # Enable/Disable the re-order rows feature
# #		self.widgets['table'].main_table_css_class = 'my_custom_class'  # Change the class applied on the main table when the field is displayed
		
	
	
# class AddView(DefaultAddView):
	# form = AddForm
		