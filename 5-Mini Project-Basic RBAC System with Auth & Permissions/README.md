# Mini Project: Basic RBAC System with Auth & Permissions

### 🎯Objectives

<small>NB: This mini project moderately utilizes Django's default admin panel. Implemented basic approval system on 'Product' create/update workflow based on Admin's review.</small>

1.  Create a basic Role-Based Access Control (RBAC) system.
    - User Roles:
      - Admin
      - Staff
      - User

2.  Implement basic session-based authentication.

3.  **DB Tables:**
    - Product
    - ProductCreateReview
    - ProductUpdateReview
    - Order
    - User
    - UserProfile

    An ER diagram of this project is added <u>[**here**](./resources/ER%20Diagram.md)</u>.

<hr>

#### Implemented <u>Review-Approval Pattern</u> in "Product" Create/Update Operations

A sequence diagram is added <u>[**here**](./resources/Sequence%20Diagram.md)</u>.

4.  Product record <u>**creation workflow:**</u> (_<small>in Django Admin Panel</small>_)

    <u>**Admin:**</u> Create Product record.

    <u>**Staff:**</u> Cannot create a record directly in the `Product` table. First creates a review record (_request_) for product inside the `ProductCreateReview` table. Later if an admin approves that review, system will create a record inside `Product` table.

    <u>**User:**</u> Not allowed.

5.  Product record <u>**update workflow:**</u> (_<small>in Django Admin Panel</small>_)

    <u>**Admin:**</u> Update Product record.

    <u>**Staff:**</u> Cannot update a record directly in the `Product` table. First creates a review record (_request_) for product inside the `ProductUpdateReview` table. Later if an admin approves that review, system will update the record inside `Product` table accordingly.

    <u>**User:**</u> Not allowed.

<hr>

6.  Product record <u>**read workflow:**</u>

        💡 Allowed User Roles: Admin, Staff, User

    **User:** View paginated product list in a separate webpage.

7.  User & UserProfile record <u>**creation workflow:**</u>

        💡When a user account is created utilizing Django's default User model, a user profile gets created by the system associated with that account.

    <u>**Admin:**</u> Create user account for both admin & staff | Django Admin Panel.

    <u>**Staff:**</u> Not allowed.

    <u>**User:**</u> Create account from webpage.

        💡1:1 relationship between User & UserProfile models.

8.  Order record <u>**creation workflow:**</u>

    <u>**Allowed:**</u> User (<small>_Authenticated_</small>)

    <u>**Not Allowed:**</u> Admin, Staff

9.  User create, email-verfication, forget password & soft delete cycle implemented.
