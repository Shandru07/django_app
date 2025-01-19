from typing import Any
from blog.models import Post,Category
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = "This commands insert category data"

    def handle(self, *args: Any, **options: Any):
        Category.objects.all()

        Categories= ['Sports','Technology','Science','Art','Food']


        for category_name in Categories:
            Category.objects.create(name = category_name)

        self.stdout.write(self.style.SUCCESS("Completed inserting data "))



