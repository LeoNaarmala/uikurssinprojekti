from ._anvil_designer import FebTemplate
from anvil import *
import anvil.server


class Feb(FebTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def outlined_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('march')
    pass

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('January')
    pass

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1', 'feb')
    pass

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1', 'feb')
    pass

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1', 'feb')
    pass

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form1', 'feb')
    pass
