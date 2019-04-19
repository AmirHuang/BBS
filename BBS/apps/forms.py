# app/forms.py

from wtforms import Form


class BaseForm(Form):
    def get_error(self):
        print('self.errors', self.errors)
        # print('self.errors.popitem', self.errors.popitem())
        # message = self.errors.popitem()[0][0]
        message = self.errors.popitem()
        return message
