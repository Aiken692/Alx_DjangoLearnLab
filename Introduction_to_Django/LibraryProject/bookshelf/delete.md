# Delete Book

To delete a book by its ID:

```python
from bookshelf.models import Book
retrieved_book = Book.objects.get(id=1)  # Replace '1' with the book's ID
retrieved_book.delete()
