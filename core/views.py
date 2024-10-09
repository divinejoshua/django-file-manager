import os
import random
import string
from django.http import HttpResponse
from django.conf import settings
from django.utils.timezone import now

def generate_random_file(request):
    # Generate random string content
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=100))  # 100 random characters
    
    # Create a timestamped filename to avoid collisions
    file_name = f"random_file_{now().strftime('%Y%m%d%H%M%S')}.txt"
    
    # Define the file path where the file will be saved
    file_path = os.path.join(settings.BASE_DIR, 'generated_files', file_name)
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    # Write the random string to the file
    with open(file_path, 'w') as f:
        f.write(random_string)
    
    # Return an HTTP response indicating file creation success
    return HttpResponse(f"File '{file_name}' has been created at '{file_path}'", content_type="text/plain")

