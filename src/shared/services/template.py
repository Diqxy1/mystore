
from jinja2 import Environment, PackageLoader

class TemplateService():

    SEND_CODE = 'email/send_code.html'

    def __init__(self):
        self.env = Environment(loader=PackageLoader(package_name=self.get_template_base_path(), package_path='templates'))

    def render(self, template: str, data: dict) -> str:
        return self.env.get_template(template).render(**data)

    def get_template_base_path(cls):
        return "src.shared"