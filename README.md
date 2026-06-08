# Pinnacle_E-Commerce
Python E-Commerce Store is a Flask-based web application that allows users to browse products, add items to a shopping cart, and complete purchases through a simulated payment process. The project demonstrates product management, session-based cart functionality, web routing, and fundamental e-commerce application development using Python.

# Python E-Commerce Store

## Description

Python E-Commerce Store is a web-based shopping application developed using Flask. The platform allows users to browse product listings, add products to a shopping cart, review selected items, and complete purchases through a simulated secure payment process. The project demonstrates web development concepts, session management, and e-commerce functionality using Python.

## Features

* Product listing page
* Shopping cart functionality
* Add products to cart
* View cart items and total price
* Session-based cart management
* Simulated secure payment page
* Order confirmation system
* User-friendly web interface
* Flask-based web application

## Technologies Used

* Python 3
* Flask
* HTML
* CSS
* Session Management

## Objectives

* Build a basic e-commerce platform using Flask.
* Implement shopping cart functionality.
* Manage user sessions.
* Create a secure-looking payment workflow.
* Learn web application routing and templates.
* Understand full-stack development fundamentals.

## Project Structure

```text
ECommerceStore/
│
├── app.py
├── README.md
```

## Installation

### Step 1: Install Flask

```bash
pip install flask
```

### Step 2: Run the Application

```bash
python app.py
```

### Step 3: Open Browser

```text
http://127.0.0.1:5000
```

## Application Workflow

### Home Page

* Displays available products.
* Shows product name and price.
* Allows users to add products to the cart.

### Shopping Cart

* Displays selected products.
* Calculates total amount.
* Allows users to proceed to payment.

### Payment Page

* Collects payment details.
* Simulates secure payment processing.

### Order Success Page

* Displays payment confirmation.
* Clears shopping cart after successful purchase.

## Sample Products

| Product     | Price   |
| ----------- | ------- |
| Laptop      | ₹55,000 |
| Smartphone  | ₹25,000 |
| Headphones  | ₹3,000  |
| Smart Watch | ₹5,000  |

## Example User Flow

### Add Product

```text
Select Laptop
Click "Add to Cart"
```

Output:

```text
Product Added Successfully
```

### View Cart

```text
Laptop - ₹55,000
Headphones - ₹3,000

Total: ₹58,000
```

### Payment

Input:

```text
Card Holder Name
Card Number
CVV
```

Output:

```text
Payment Successful!
Order Placed Successfully.
```

## Learning Outcomes

* Flask Routing
* Session Handling
* HTML and CSS Integration
* Shopping Cart Logic
* Form Handling
* Web Application Development
* Basic Payment Workflow Design

## Future Enhancements

* User Registration and Login
* Product Search and Filtering
* Product Images
* Database Integration (MySQL/SQLite)
* Real Payment Gateway Integration
* Order History
* Admin Dashboard
* Inventory Management
* Responsive Design
* Email Notifications

## Security Note

This project uses a simulated payment form for educational purposes only. It does not process real payments or securely store card information. For production use, integrate trusted payment gateways such as Stripe, Razorpay, or PayPal.

## Author

Naveen Kumar
