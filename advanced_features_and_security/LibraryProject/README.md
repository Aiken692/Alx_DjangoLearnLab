LibraryProject

# Permissions and Groups Setup

## Custom Permissions

The `Book` model has the following custom permissions:

- `can_view`: Can view book
- `can_create`: Can create book
- `can_edit`: Can edit book
- `can_delete`: Can delete book

## Groups

The following groups are set up with corresponding permissions:

- `Editors`: `can_create`, `can_edit`
- `Viewers`: `can_view`
- `Admins`: `can_create`, `can_edit`, `can_delete`, `can_view`

## Views

The views are protected with the following permissions:

- `book_list`: `can_view`
- `book_create`: `can_create`
- `book_edit`: `can_edit`
- `book_delete`: `can_delete`

## Testing

Create test users and assign them to different groups. Log in as these users and attempt to access various parts of the application to ensure that permissions are applied correctly.
