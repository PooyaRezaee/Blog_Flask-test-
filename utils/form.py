from wtforms import SelectMultipleField
from wtforms.widgets import CheckboxInput,ListWidget

class SelectCheckBoxField(SelectMultipleField):
    widget = ListWidget(prefix_label=False)
    option_widget = CheckboxInput()