import sqlite3

# Create the database and products table if it doesn't exist
def create_database():
    conn = sqlite3.connect('shopkeeper_db')
    cursor = conn.cursor()

    # Check if the table exists
    cursor.execute('''SELECT count(name) FROM sqlite_master WHERE type='table' AND name='products' ''')
    if cursor.fetchone()[0] == 1:
        print('Table products already exists. Skipping creation.')
    else:
        cursor.execute('''
        CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
        ''')

        print('Table products created successfully.')

    conn.commit()
    conn.close()

# Add a new product to the database
def add_product(name, quantity, price):
    conn = sqlite3.connect('shopkeeper_db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)', (name, quantity, price))
        conn.commit()
        print(f"Product '{name}' added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding product '{name}': {e}")

    conn.close()

# Retrieve all products from the database
def view_products():
    conn = sqlite3.connect('shopkeeper_db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('SELECT * FROM products')
        products = cursor.fetchall()
        conn.close()
        return products
    except sqlite3.Error as e:
        print(f"Error retrieving products: {e}")
        return []

# Display the command-line menu
def display_menu():
    print("\n--- Shopkeeper Application ---")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Exit")

# Update an existing product in the database
def update_product(product_id, name, quantity, price):
    conn = sqlite3.connect('shopkeeper_db')
    cursor = conn.cursor()
    
    cursor.execute('UPDATE products SET name = ?, quantity = ?, price = ? WHERE id = ?', (name, quantity, price, product_id))
    conn.commit()
    conn.close()

# Delete a product from the database
def delete_product(product_id):
    conn = sqlite3.connect('shopkeeper_db')
    cursor = conn.cursor()
    
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()

# Main function to run the command-line interface
def main():
    create_database()
    
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter product name: ")
            quantity = int(input("Enter product quantity: "))
            price = float(input("Enter product price: "))
            add_product(name, quantity, price)
        
        elif choice == '2':
            products = view_products()
            if products:
                print("\n--- Product List ---")
                for product in products:
                    print(f"ID: {product[0]}, Name: {product[1]}, Quantity: {product[2]}, Price: {product[3]}")
            else:
                print("No products found.")
        
        elif choice == '5':
            print("Exiting the application.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()