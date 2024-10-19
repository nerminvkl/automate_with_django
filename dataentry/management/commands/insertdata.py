from django.core.management.base import BaseCommand
from dataentry.models import Student

class Command(BaseCommand):
    help = 'It will insert data to database'
    
    def handle(self, *args, **kwargs):
        dataset = [
            {'roll_no': 1002, 'name': 'Mihriba', 'age':27},
            {'roll_no': 1003, 'name': 'Suada', 'age':57},
            {'roll_no': 1004, 'name': 'Zumret', 'age':57},
            {'roll_no': 1005, 'name': 'Damir', 'age':40},
        ]
        
        for data in dataset:
            roll_no = data['roll_no']
            existing_record = Student.objects.filter(roll_no=roll_no).exists()
            
            if not existing_record:
                Student.objects.create(roll_no=data['roll_no'], name=data['name'], age=data['age'])
            else:
                self.stdout.write(self.style.WARNING(f'Student with roll no {roll_no} already exists!'))
        self.stdout.write(self.style.SUCCESS('Data inserted successfully'))