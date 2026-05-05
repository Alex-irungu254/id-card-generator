import os
import django
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'id_generator.settings')
django.setup()

from cards.utils import generate_id_card
from cards.models import IDCard

from datetime import date

# Create a dummy card for testing
card = IDCard(name='Test User', dob=date(1990, 1, 1), id_number='123456789')
# Assuming a test photo exists, or use a dummy path
card.photo.name = 'photos/IMG_20251004_133639_539.jpg'  # Use existing photo
card.save()

start = time.time()
generate_id_card(card)
end = time.time()
print(f'Time taken: {end - start:.2f} seconds')