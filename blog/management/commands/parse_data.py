import requests
from django.core.management import BaseCommand

from blog.models import Post


class Command(BaseCommand):
    help = "Извлекать задачи из API и загружать их в базу данных."

    def handle(self, *args, **options):
        api_url = "https://jsonplaceholder.typicode.com/posts"
        response = requests.get(api_url)

        if response.status_code == 200:
            posts = response.json()
            for post in posts:
                obj, created = Post.objects.get_or_create(
                    id=post['id'],
                    userId=post['userId'],
                    title=post['title'],
                    body=post['body']
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f"Запись с id:{post['id']} добавлена в базу данных."))
                else:
                    self.stdout.write(self.style.WARNING(f"Запись с id:{post['id']} уже существует в базе данных."))
        else:
            self.stdout.write(self.style.ERROR(f'Ошибка получения записей из API: {response.status_code}'))