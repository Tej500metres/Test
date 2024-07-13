### Part 2: Test Case Design

#### Functional Test Cases

1. **User Registration:**
   - Test if a new user can register with valid details.
   - Test registration with missing required fields.
   - Test registration with invalid email format.

2. **Product Search:**
   - Test searching for a product by name.
   - Test searching with no matching results.
   - Test searching with special characters.

3. **Adding Items to Cart:**
   - Test adding a single item to the cart.
   - Test adding multiple items to the cart.
   - Test adding an item to the cart and then removing it.

4. **Checkout Process:**
   - Test the checkout process with valid payment details.
   - Test checkout with invalid payment details.
   - Test checkout with empty cart.

5. **Order Management:**
   - Test viewing order history.
   - Test viewing details of a specific order.
   - Test cancelling an order.

#### Edge and Boundary Test Cases

1. **User Registration:**
   - Test registration with minimum and maximum length of username.
   - Test registration with edge cases in password (e.g., just minimum required length).

2. **Product Search:**
   - Test search with the maximum allowed length of the search query.
   - Test search input with edge characters like "", [], {}, etc.

3. **Adding Items to Cart:**
   - Test adding the maximum allowed quantity of an item.
   - Test cart functionality with a large number of different items.
