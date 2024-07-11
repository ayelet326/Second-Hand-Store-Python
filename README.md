# SecondHandStore

## Overview

SecondHandStore is a Python-based terminal application designed to manage a retail store that sells both new and second-hand items. The application provides a simple interface for users to view a product catalog, add second-hand items, purchase products, and exit the system. All data is stored in and retrieved from a file, ensuring persistence between sessions.

## Features

- **View Catalog**: Display all available products in the store.
- **Add Second-Hand Item**: Add a new second-hand item to the store's inventory.
- **Purchase Product**: Buy a product from the store, updating the inventory accordingly.
- **Exit**: Exit the application gracefully.

## Project Structure

The project is organized into the following classes:

- **Store**: Manages the store's inventory and handles operations such as adding, viewing, and purchasing products.
- **Product**: Represents a general product in the store, including attributes such as name, price, and category.
- **SecondHandProduct**: Inherits from `Product` and includes additional attributes specific to second-hand items, such as condition and previous ownership details.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/ayelet326/Second-Hand-Store-Python.git
    ```

2. Navigate to the project directory:
    ```sh
    cd Second-Hand-Store-Python
    ```

### Usage

Run the application by executing the main Python file:
```sh
python main.py
