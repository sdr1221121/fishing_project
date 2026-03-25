from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR,"templates")

env= Environment(loader=FileSystemLoader(TEMPLATE_DIR))

def generate_catch_report(catches):
    template = env.get_template("catch_report.html")

    html_content = template.render(catches=catches)

    pdf = HTML(string=html_content).write_pdf()

    return pdf