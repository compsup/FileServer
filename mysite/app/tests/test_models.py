from django.test import TestCase
from app.models import Files


class ModelsTestCase(TestCase):
    def test_file_uploading(self):
        file = Files.objects.create(
            file_name="yolo", pub_date="2020-2-28 2:30", uploaded_by='John', file='awesome_file.txt')
        file.save()

        File = Files.objects.get(file_name="yolo")

        self.assertEqual(File.file_name, 'yolo')
        self.assertEqual(File.uploaded_by, 'John')
        self.assertEqual(File.file, 'awesome_file.txt')
