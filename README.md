Shopkeeper Application
This Python application allows users to manage a list of products using a command-line interface (CLI). Users can add, view, update, and delete products stored in an SQLite database.

Features
Add Product: Add a new product to the database with name, quantity, and price.
View Products: Display a list of all products currently stored in the database.
Update Product: Modify details (name, quantity, price) of an existing product.
Delete Product: Remove a product from the database by its ID.
Requirements
Python 3.x
SQLite3 (comes with Python by default)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/shopkeeper-app.git
cd shopkeeper-app
Install dependencies (none required beyond Python's standard library).

Usage
Run the application:

bash
Copy code
python shop.py
Follow the on-screen prompts to interact with the application:

Choose options from the main menu to add, view, update, or delete products.
Exit the application by choosing the appropriate menu option.
Database Structure
The application uses a SQLite database (shopkeeper_db) with a single table products:

products:
id INTEGER PRIMARY KEY: Unique identifier for each product.
name TEXT NOT NULL: Name of the product.
quantity INTEGER NOT NULL: Quantity of the product available.
price REAL NOT NULL: Price of the product.
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

License
This project is licensed under the MIT License - see the LICENSE file for details.

