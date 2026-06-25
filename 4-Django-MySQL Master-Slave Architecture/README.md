# Django-MySQL Master-Slave Architecture

### 👥Roles & Permissions

- User Roles: Admin, User

- Models: Product

- Admin Perms: CRUD

- User Perms: Read

<hr>

### 🎯Objectives

1. Implements Master-Slave database replication utilizing <u>Docker container & network</u>.

   **Used DB:** MySQL

2. For administrators, make both the read & write (_Create, Update, Delete_) operations all in the <u>**Master DB**</u>.

3. For users, they are going to read from the <u>**Slave DB**</u>.

### 🛠️Implementation

1. Implementation of Master-Slave Replication in MySQL running inside Docker containers | [**Link ➡️**](./resources/MySQL%20Master-Slave%20Architecture%20in%20Docker%20Containers.md)

#### Splitting the READ & WRITE requets

📃 <u>**Note-1:**</u> The public store-front views will be read from the **replica DBs**, on the other hand, the administrators will read & write from the default **master DB**.

📃 <u>**Note-2:**</u> Create a user in the master db server. (<small>_Slave db server will automatically create the db in itself_</small>)

    CREATE USER 'username'@'%' IDENTIFIED BY 'password';

📃 <u>**Note-3:**</u> Create a database in the master db server (<small>_Slave db server will automatically create the db in itself_</small>)

    CREATE DATABASE dbname;

📃 <u>**Note-4:**</u> Grant all privileges to the user of the newly created database.

    GRANT PRIVILEGES ON dbname.* TO 'username'@'%';

1. Define two database configurations inside the `DATABASES` dictionary in 'settings.py' file. One is known as `default` & another is known as `slave`.

2. Create a db-router class `PrimaryReplicaRouter` utilizing Django's automatic database routing scheme in 'core/db_router.py' file.

3. For all the read operations generated inside the app will be routed to the `slave` DB. Inversely, all the write opts (_create, update, delete_) will be routed to the `default` DB.

4. 💥 But to avoid <u>the replication lag</u> (_a common bottleneck in this scenario_) & keep the data consistency in the admin panel operations, we route both the read & write opts in the default master DB.

   To distinguish the operations coming from the admin panel, we wrote a middleware & defined that in the 'settings.py' file. It intercepts those requests which starts with `/admin/` in the `request.path` object. With this, conditionally route the admin requests in db-router class to the `default` DB.

   4.1# Create a `view` to display the products to any public requests into the app server.
