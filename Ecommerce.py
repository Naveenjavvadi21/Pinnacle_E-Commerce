from flask import Flask, render_template_string, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = "ecommerce_secret_key"

# Product Data
products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 55000
    },
    {
        "id": 2,
        "name": "Smartphone",
        "price": 25000
    },
    {
        "id": 3,
        "name": "Headphones",
        "price": 3000
    },
    {
        "id": 4,
        "name": "Smart Watch",
        "price": 5000
    }
]

# Home Page - Product Listings
@app.route('/')
def home():

    html = """
    <html>
    <head>
        <title>E-Commerce Website</title>

        <style>

            body{
                font-family:Arial;
                background:#f4f4f4;
                padding:20px;
            }

            h1{
                color:#333;
            }

            .product{
                background:white;
                padding:15px;
                margin:15px;
                border-radius:10px;
                width:250px;
            }

            .btn{
                padding:10px;
                background:green;
                color:white;
                border:none;
                cursor:pointer;
            }

        </style>
    </head>

    <body>

        <h1>Python E-Commerce Store</h1>

        <a href="/cart">View Cart</a>

        <div style="display:flex;">

        {% for product in products %}

            <div class="product">

                <h2>{{ product.name }}</h2>

                <p>Price : ₹{{ product.price }}</p>

                <form action="/add_to_cart" method="post">

                    <input type="hidden"
                           name="product_id"
                           value="{{ product.id }}">

                    <button class="btn">
                        Add to Cart
                    </button>

                </form>

            </div>

        {% endfor %}

        </div>

    </body>
    </html>
    """

    return render_template_string(html, products=products)

# Add to Cart
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():

    product_id = int(request.form['product_id'])

    if 'cart' not in session:
        session['cart'] = []

    session['cart'].append(product_id)

    session.modified = True

    return redirect(url_for('home'))

# Cart Page
@app.route('/cart')
def cart():

    cart_items = []

    total = 0

    if 'cart' in session:

        for item_id in session['cart']:

            for product in products:

                if product['id'] == item_id:

                    cart_items.append(product)

                    total += product['price']

    html = """
    <html>

    <head>

        <title>Shopping Cart</title>

        <style>

            body{
                font-family:Arial;
                padding:20px;
            }

            .item{
                background:#f4f4f4;
                padding:10px;
                margin:10px;
                border-radius:10px;
            }

            .btn{
                padding:10px;
                background:blue;
                color:white;
                border:none;
            }

        </style>

    </head>

    <body>

        <h1>Your Shopping Cart</h1>

        {% for item in cart_items %}

            <div class="item">

                <h3>{{ item.name }}</h3>

                <p>₹{{ item.price }}</p>

            </div>

        {% endfor %}

        <h2>Total : ₹{{ total }}</h2>

        <form action="/payment" method="post">

            <button class="btn">
                Proceed to Payment
            </button>

        </form>

        <br>

        <a href="/">Continue Shopping</a>

    </body>

    </html>
    """

    return render_template_string(
        html,
        cart_items=cart_items,
        total=total
    )

# Payment Page
@app.route('/payment', methods=['POST'])
def payment():

    html = """
    <html>

    <head>

        <title>Payment</title>

        <style>

            body{
                font-family:Arial;
                padding:20px;
            }

            input{
                padding:10px;
                margin:10px;
                width:250px;
            }

            .btn{
                padding:10px;
                background:green;
                color:white;
                border:none;
            }

        </style>

    </head>

    <body>

        <h1>Secure Payment Processing</h1>

        <form action="/success" method="post">

            <input type="text"
                   placeholder="Card Holder Name"
                   required><br>

            <input type="text"
                   placeholder="Card Number"
                   required><br>

            <input type="password"
                   placeholder="CVV"
                   required><br>

            <button class="btn">
                Pay Now
            </button>

        </form>

    </body>

    </html>
    """

    return render_template_string(html)

# Payment Success
@app.route('/success', methods=['POST'])
def success():

    session.pop('cart', None)

    return """
    <html>

    <body style="font-family:Arial;padding:20px;">

        <h1>Payment Successful!</h1>

        <h2>Order Placed Successfully</h2>

        <a href="/">Go Back to Home</a>

    </body>

    </html>
    """

# Run Application
if __name__ == '__main__':

    app.run(debug=True)