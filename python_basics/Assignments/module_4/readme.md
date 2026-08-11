---
noteId: "e903607095c311f1a113bb931cae363d"
tags: []

---

# Python Product Collections & Data Operations

This project demonstrates basic Python data structures and their operations using a simple **product catalog** example.

The tasks cover:

* Lists
* Tuples
* Sets
* Dictionaries
* Combining multiple data structures
* Basic calculations and iterations

---

## 📌 Task 1: Product Collections (Lists & Tuples)

### Objective

Learn how to create and manipulate **lists and tuples** in Python.

### 1. Create a Product List

A list named `products` is created containing at least 6 product names.

```python
products = ['Chair', 'Mobile', 'Pen', 'Key', 'Mouse', 'Keyboard']
```

### 2. Create a Product Tuple

A tuple named `sample_product` stores:

* Product name
* Price
* Category

```python
sample_product = ('Chair', 1000, 'Furniture')
```

### 3. Access Products from the List

The second and last products are accessed using list indexing.

```python
print(f'2nd product : {products[1]}', ' & ', 
      f'Last product : {products[-1]}')
```

**Output:**

```text
2nd product : Mobile  &  Last product : Keyboard
```

### 4. Add New Products

Two new products are added using the `append()` method.

```python
products.append('Bottle')
products.append('Fan')

print(f'Updated list : {products}')
```

**Output:**

```text
Updated list : ['Chair', 'Mobile', 'Pen', 'Key', 'Mouse', 'Keyboard', 'Bottle', 'Fan']
```

### Optional: Convert Tuple → List → Tuple

The tuple is converted into a list so that its price can be modified.

```python
print(f'Checking type Before converting : {type(sample_product)}')

a = list(sample_product)

print(f'Checking type after converting : {type(a)}')

# Change price
a[1] = 1200

# Convert list back to tuple
b = tuple(a)

print(f'Checking type again after converting into tuple : {type(b)}')
```

**Output:**

```text
Checking type Before converting : <class 'tuple'>
Checking type after converting : <class 'list'>
Checking type again after converting into tuple : <class 'tuple'>
```

---

# 📌 Task 2: Categories (Sets)

### Objective

Learn how to use **sets** to store unique categories and perform membership checks.

### 1. Create a Set of Categories

```python
categories = [
    'Furniture',
    'Electronics',
    'Accessories',
    'Accessories',
    'Electronics',
    'Electronics'
]

categories_set = set(categories)
```

Since sets only store unique values, duplicate categories are automatically removed.

### 2. Add a New Category

```python
categories_set.add('food')
```

The `add()` method adds a new category to the set.

### 3. Check Whether a Category Exists

A function is created to check whether a category exists in the set.

```python
def fun_check(check):
    return check in categories_set
```

Example:

```python
check_Category = 'Logistic'
print(fun_check(check_Category))

check_Category = 'food'
print(fun_check(check_Category))
```

**Output:**

```text
False
True
```

This demonstrates that:

* `Logistic` does not exist.
* `food` exists in the set.

### Optional: Count Unique Categories

```python
print(len(categories_set))
```

**Output:**

```text
4
```

The set contains **4 unique categories**.

---

# 📌 Task 3: Product Pricing (Dictionaries)

### Objective

Learn how to store product names and their prices using a **dictionary**.

### 1. Create a Price Dictionary

```python
price_dict = {
    'Chair': 1000,
    'Mobile': 15000,
    'Pen': 20,
    'Key': 50,
    'Mouse': 500,
    'Keyboard': 1200
}
```

Here:

* Keys = Product names
* Values = Product prices

### 2. Add and Update Products

A new product is added:

```python
price_dict['Bottle'] = 300
```

The price of an existing product is updated:

```python
price_dict['Pen'] = 10
```

### 3. Calculate Average Product Price

The average price is calculated using dictionary values.

```python
print(
    f'Average price of all products : '
    f'{sum(price_dict.values()) / len(price_dict)}'
)
```

**Output:**

```text
Average price of all products : 2580.0
```

### Optional: Find Maximum and Minimum Prices

The most expensive product can be found using `max()`:

```python
print(
    f'Most expensive product : '
    f'{max(price_dict, key=price_dict.get)}'
)
```

The cheapest product can be found using `min()`:

```python
print(
    f'Cheapest product : '
    f'{min(price_dict, key=price_dict.get)} - '
    f'{price_dict[min(price_dict, key=price_dict.get)]}'
)
```

**Output:**

```text
Most expensive product : Mobile
Cheapest product : Pen - 10
```

> **Note:** The original code printed `Mobile - Mobile` for the most expensive product. The corrected version above prints only the product name.

---

# 📌 Task 4: Combined Operations

### Objective

Combine **lists, dictionaries, tuples, and loops** to create and analyze a product catalog.

### 1. Create a Catalog

A `catalog` list is created where every tuple contains:

```text
(product_name, price, category)
```

```python
catalog = list(zip(products, price_dict.values(), categories))

print(catalog)
```

**Output:**

```text
[
    ('Chair', 1000, 'Furniture'),
    ('Mobile', 15000, 'Electronics'),
    ('Pen', 10, 'Accessories'),
    ('Key', 50, 'Accessories'),
    ('Mouse', 500, 'Electronics'),
    ('Keyboard', 1200, 'Electronics')
]
```

### 2. Create Category-to-Products Dictionary

A dictionary named `category_to_products` maps each category to a list of products.

```python
category_to_products = {}

for product, price, category in catalog:
    if category not in category_to_products:
        category_to_products[category] = []

    category_to_products[category].append(product)

print(category_to_products)
```

**Output:**

```text
{
    'Furniture': ['Chair'],
    'Electronics': ['Mobile', 'Mouse', 'Keyboard'],
    'Accessories': ['Pen', 'Key']
}
```

### 3. Find the Category with Maximum Products

The following code finds the category containing the highest number of products.

```python
max_category = None
max_count = 0

for category in category_to_products:
    if len(category_to_products[category]) > max_count:
        max_count = len(category_to_products[category])
        max_category = category

print(f'Category with maximum products : {max_category}')
print(f'Products : {category_to_products[max_category]}')
```

**Output:**

```text
Category with maximum products : Electronics
Products : ['Mobile', 'Mouse', 'Keyboard']
```

Therefore, **Electronics** is the category with the maximum number of products.

---

# 🧠 Concepts Learned

Through these tasks, the following Python concepts were practiced:

| Concept                | Usage                           |
| ---------------------- | ------------------------------- |
| List                   | Store multiple product names    |
| Tuple                  | Store fixed product information |
| Indexing               | Access specific list elements   |
| `append()`             | Add products to a list          |
| Type Conversion        | Convert tuple to list and back  |
| Set                    | Store unique categories         |
| `add()`                | Add items to a set              |
| Membership Operator    | Check whether an item exists    |
| Dictionary             | Store product prices            |
| Dictionary Methods     | Work with keys and values       |
| `sum()`                | Calculate total prices          |
| `len()`                | Count items                     |
| `max()` / `min()`      | Find highest/lowest values      |
| `zip()`                | Combine multiple collections    |
| `for` Loop             | Iterate through catalog data    |
| Conditional Statements | Group and compare products      |

---

# 📊 Final Result

The project successfully demonstrates how different Python data structures can work together to manage product information.

### Product Categories

* **Furniture:** Chair
* **Electronics:** Mobile, Mouse, Keyboard
* **Accessories:** Pen, Key

### Category with Maximum Products

**Electronics**

### Products in the Maximum Category

```text
Mobile
Mouse
Keyboard
```

---

## 🚀 Conclusion

This assignment provides practical experience with Python's fundamental data structures. Lists, tuples, sets, and dictionaries each serve different purposes, and combining them allows us to build a simple but useful product catalog system.

The project is a good foundation for learning more advanced Python concepts such as functions, comprehensions, classes, file handling, and database operations.
