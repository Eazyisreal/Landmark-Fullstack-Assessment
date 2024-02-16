# Point of Sale System (POS)

## Overview

The Point of Sale (POS) system is a web-based application developed using Django. It provides functionality for managing products, filtering by categories and stores, adding items to a shopping cart, and processing orders through a checkout process.

## Features

- Display a list of products with details such as name, price, and quantity.
- Filter products by categories.
- Filter products by store.
- Add products to a shopping cart.
- Update quantities and remove items from the cart.
- Checkout process for reviewing the cart, entering shipping and payment details, and completing the purchase.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/pos-system.git
   cd pos-system
    ```

2. Create a virtual environment and activate it:

   ```bash
    python -m venv venv
    source venv/bin/activate (Linux/Mac)
    venv\Scripts\activate (Windows)
    ```


3. Install the required dependencies:


   ```bash
   pip install -r requirements.txt
    ```


4. Apply database migrations:
    ```bash
       python manage.py makemigrations && python manage.py migrate
    ```


## Usage

1. Run the development server:
   ```bash
       python manage.py runserver
    ```


2. Access the application in your web browser at http://localhost:8000.

3. Explore the different features of the POS system:
- Browse products and filter by categories or stores.
- Add items to the shopping cart.
- Review the cart contents and proceed to checkout.

