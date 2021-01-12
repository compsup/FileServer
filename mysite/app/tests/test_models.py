from django.test import TestCase
from app.models import Files


class ModelsTestCase(TestCase):
    def test_file_uploading(self):
        file = Files.objects.create(
            file_name="yolo", file='awesome_file.txt')
        file.save()

        File = Files.objects.get(file_name="yolo")

        self.assertEqual(File.file_name, 'yolo')
        self.assertEqual(File.file, 'awesome_file.txt')
