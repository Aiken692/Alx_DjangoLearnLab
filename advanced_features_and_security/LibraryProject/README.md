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



# HTTPS and Security Configuration

## settings.py Changes

- `SECURE_SSL_REDIRECT`: Redirects all non-HTTPS requests to HTTPS.
- `SECURE_HSTS_SECONDS`: Instructs browsers to only access the site via HTTPS for one year.
- `SECURE_HSTS_INCLUDE_SUBDOMAINS`: Includes all subdomains in the HSTS policy.
- `SECURE_HSTS_PRELOAD`: Allows preloading of the HSTS policy.
- `SESSION_COOKIE_SECURE`: Ensures session cookies are only transmitted over HTTPS.
- `CSRF_COOKIE_SECURE`: Ensures CSRF cookies are only transmitted over HTTPS.
- `X_FRAME_OPTIONS`: Prevents the site from being framed to protect against clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF`: Prevents browsers from MIME-sniffing a response away from the declared content-type.
- `SECURE_BROWSER_XSS_FILTER`: Enables the browser’s XSS filtering to help prevent cross-site scripting attacks.

## Nginx Configuration

- Redirects HTTP to HTTPS.
- Configures SSL/TLS certificates for HTTPS.

## Security Review

The implemented security measures ensure that all data transmitted between the client and server is encrypted, cookies are securely transmitted, and additional headers protect against common web vulnerabilities. Future improvements could include implementing Content Security Policy (CSP) headers and monitoring security headers using tools like Mozilla Observatory.
