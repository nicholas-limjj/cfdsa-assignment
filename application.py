import random

from flask import Flask, Response, url_for
import jinja2

jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader('workshop01'))

application = Flask(__name__)

text_dict = [
    "Logic will get you from A to B. Imagination will take you everywhere.",
    "There are 10 kinds of people. Those who know binary and those who don't.",
    "There are two ways of constructing a software design. One way is to make it so simple that there are obviously "
    "no deficiencies and the other is to make it so complicated that there are no obvious deficiencies.",
    "It's not that I'm so smart. It's just that I stay with problems longer.",
    "It is pitch dark. You are likely to be eaten by a grue."
]


@application.route('/', methods=['GET'])
def main():
    template = jinja_env.get_template('index.html')
    template_var = {
        'title': 'Assignment Page',
        'dynamic_text': random.choice(text_dict),
        'github_url': 'https://github.com/nicholas-limjj/cfdsa-assignment',
        'image_src': 'balloon.jpg'
    }
    return Response(template.render(template_var), mimetype='text/html'), 200


if __name__ == "__main__":
    application.run()
