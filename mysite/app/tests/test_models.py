from django.test import TestCase
from app.models import Files


class ModelsTestCase(TestCase):
    def test_file_uploading(self):
        file = Files.objects.create(
            file_name="yolo", pub_date="2020-2-28 2:30")
        file.save()

        File = Files.objects.get(file_name="yolo")

        self.assertEqual(File.file_name, 'yolo')
