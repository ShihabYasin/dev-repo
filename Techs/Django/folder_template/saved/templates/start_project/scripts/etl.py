from app.models import Snippet
from django.contrib.auth.models import User


def run():
    snippet = Snippet(code='foo = "bar"\n',title='Foo Bar Title.', owner = User(username='test'))
    snippet.save()


