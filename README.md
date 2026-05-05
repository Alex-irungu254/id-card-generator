# ID Card Generator

A Django-based web application for generating realistic ID cards that resemble US driver's licenses. Users can create, edit, and download custom ID cards with photos and personal details.

## Features

- **Create ID Cards**: Fill out a form with name, date of birth, ID number, and photo to generate a custom ID card.
- **Edit Cards**: Modify existing card details and regenerate the image.
- **Download Cards**: Download the generated ID card as an image file.
- **Realistic Design**: Cards are designed to look like Florida driver's licenses with proper layout, colors, and elements like seals and barcodes.
- **Responsive UI**: Styled with Tailwind CSS for a clean, modern interface.
- **Verification**: Each card includes a unique verification code for authenticity checks.

## Technologies Used

- **Backend**: Django 6.0.4
- **Image Processing**: Pillow (PIL)
- **QR Codes**: qrcode library
- **Frontend**: HTML, Tailwind CSS
- **Database**: SQLite (default Django database)
- **Deployment**: Ready for deployment on platforms like Heroku, AWS, etc.

## Installation

### Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

### Steps

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-username/id-card-generator.git
   cd id-card-generator
   ```

2. **Create and activate a virtual environment**:

   ```bash
   python -m venv dlvenv
   dlvenv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a template image** (if not present):
   - Ensure `media/template.jpeg` exists. You can create a blank image or use the provided script.

6. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

7. **Access the application**:
   - Open your browser and go to `http://127.0.0.1:8000/`

## Usage

1. **Create a Card**:
   - Navigate to the home page.
   - Fill in the form: Name, Date of Birth, ID Number, and upload a photo.
   - Click "Submit" to generate the card.

2. **View and Download**:
   - After creation, view the generated card.
   - Download the image using the provided link.

3. **Edit a Card**:
   - From the card detail page, click "Edit details".
   - Modify the information and resubmit to regenerate.

4. **Verify a Card**:
   - Use the verification code to check card authenticity.

## Project Structure

```
id_generator/
├── cards/
│   ├── models.py          # IDCard model
│   ├── forms.py           # IDCardForm with Tailwind styling
│   ├── views.py           # Views for create, edit, detail
│   ├── urls.py            # URL patterns
│   ├── utils.py           # Card generation logic
│   ├── templates/
│   │   ├── base.html      # Base template with Tailwind
│   │   ├── form.html      # Form template
│   │   ├── card_detail.html # Card display template
│   │   └── verify.html    # Verification template
│   └── migrations/        # Database migrations
├── id_generator/
│   ├── settings.py        # Django settings
│   ├── urls.py            # Root URL configuration
│   ├── wsgi.py            # WSGI configuration
│   └── asgi.py            # ASGI configuration
├── media/                 # Uploaded files and generated cards
├── db.sqlite3             # SQLite database
├── manage.py              # Django management script
└── requirements.txt       # Python dependencies
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by real US driver's license designs.
- Uses Tailwind CSS for styling.
- Image generation powered by Pillow.

## Contact

For questions or support, please open an issue on GitHub.
