# Boutique Ado

Boutique Ado is a Django web application for an online clothing store. Users can browse through available products, add items to their shopping bag, and proceed to checkout to complete their orders.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run the Boutique Ado application locally, follow these steps:

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your_username/boutique_ado.git
    ```

2. Navigate to the project directory:

    ```bash
    cd boutique_ado
    ```

3. Install the project dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the project root directory and set the environment variables:

    ```plaintext
    STRIPE_PUBLIC_KEY=your_stripe_public_key
    STRIPE_SECRET_KEY=your_stripe_secret_key
    ```

5. Apply migrations to create the database schema:

    ```bash
    python manage.py migrate
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

The application should now be accessible at `http://localhost:8000`.

## Usage

Once the application is running, you can access it using a web browser. Users can navigate through the product listings, add items to their shopping bag, and proceed to checkout to complete their orders.

## Configuration

### Settings

- `BASE_DIR`: Base directory of the Django project.
- `SECRET_KEY`: Secret key used for cryptographic signing.
- `DEBUG`: Boolean flag indicating whether debug mode is enabled.
- `ALLOWED_HOSTS`: List of allowed host/domain names for the application.
- `INSTALLED_APPS`: List of installed Django applications.
- `MIDDLEWARE`: List of middleware classes used by the application.
- `CRISPY_TEMPLATE_PACK`: Name of the template pack for crispy forms.
- `TEMPLATES`: Configuration for Django templates.
- `MESSAGE_STORAGE`: Storage backend for messages framework.
- `AUTHENTICATION_BACKENDS`: Authentication backends for user authentication.
- `SITE_ID`: ID of the current site in the Django Sites framework.
- `EMAIL_BACKEND`: Email backend for sending emails.
- `DATABASES`: Configuration for database connections.
- `LANGUAGE_CODE`: Default language code for the application.
- `TIME_ZONE`: Default time zone for the application.
- `USE_I18N`: Boolean flag indicating whether to enable translation.
- `USE_L10N`: Boolean flag indicating whether to enable localization.
- `USE_TZ`: Boolean flag indicating whether to enable timezone support.
- `STATIC_URL`: URL prefix for static files.
- `STATICFILES_DIRS`: List of directories to search for static files.
- `MEDIA_URL`: URL prefix for media files.
- `MEDIA_ROOT`: Directory where uploaded media files are stored.
- `FREE_DELIVERY_THRESHOLD`: Threshold amount for free delivery.
- `STANDARD_DELIVERY_PERCENTAGE`: Percentage of the order total for standard delivery.
- `STRIPE_CURRENCY`: Currency used for Stripe payments.
- `STRIPE_PUBLIC_KEY`: Public key for Stripe integration.
- `STRIPE_SECRET_KEY`: Secret key for Stripe integration.

## Dependencies

- Django 3.2.25
- Python 3.x
- Stripe API

## Contributing

Contributions to Boutique Ado are welcome! To contribute, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch with a descriptive name.
3. Make your changes and commit them to your branch.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

## Acknowledgments

I would like to acknowledge the following resources and individuals who have contributed to the development of this project:

- [Niel McEwen](https://github.com/NielMc)
- [Matt Rudge](https://github.com/lechien73)
