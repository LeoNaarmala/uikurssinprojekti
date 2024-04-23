from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
from anvil import get_open_form

class Form1(Form1Template):
  month = 'jan'
  def __init__(self, month):
    # Set Form properties and Data Bindings.
    self.month = month
    #self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    if(self.month == 'jan'):
      open_form('January')
    elif(self.month == 'feb'):
      open_form('Feb')
    elif(self.month == 'march'):
      open_form('march')
    pass
