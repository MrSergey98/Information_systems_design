from root.settings import jinja_env
from webapp.BasicWebController import BasicController


class DetailsClientController(BasicController):

    def get_web_view(self, **kwargs):
        context = {
            'view': 'client_new',
            'can_edit_fields': False,
            'data': self.repository.get(id=kwargs.get('client_id')),
            'error': None,
        }
        template = jinja_env.get_template('webapp/shablon_form.html')
        return bytes(template.render(context), 'utf-8')

    def get_app_view(self):
        pass
