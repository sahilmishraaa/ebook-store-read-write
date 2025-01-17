# E-book Store (on.book)

An online E-book platform where users can read, write, buy, and sell books. Users can explore free and paid books, leave reviews, and manage their reading history. Authors can publish their own books and earn from sales (future payment system).

**Deployed Link**: Coming soon 😊 <!-- [https://your-deployed-link.com](https://your-deployed-link.com) -->

## Features

- **User Registration**: Users can sign up to access the platform.
- **Author Registration**: Authors can register to write and sell books.
- **Browse and Purchase Books**: Users can view, buy, and explore books (both free and paid).
- **Read Books**: Purchased books are available for reading.
- **Wish List**: Users can add books to their wish list.
- **Reading History**: Users can see their recently read books.
- **Ratings & Reviews**: Users can rate and review books.
- **Book Writing**: Authors can write and upload books to the platform.
- **Order History**: Users can track their past book purchases.

**Note**: The payment system for authors is currently off, but it’s under development for future updates.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/OfficialKovid/ebook-store-read-write.git
   cd ebook-store
   ```

2. Set up a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the database:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser to manage the site:

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:

   ```bash
   python manage.py runserver
   ```

Your site will be available at `http://127.0.0.1:8000/`.

## Technologies Used

- **Django**: Web framework used to build the application.
- **Pillow**: Image processing library used for book covers.
- **Python**: Programming language used to develop the platform.

## Future Scope

- Implementing the payment system for authors.
- Enhanced user interface and experience improvements.
- Expanding features for authors, such as analytics and marketing tools.

## License

This project is licensed under the MIT License.

## Contact

For inquiries or contributions, feel free to contact us at [officialkovid@gmail.com](mailto:officialkovid@gmail.com).

