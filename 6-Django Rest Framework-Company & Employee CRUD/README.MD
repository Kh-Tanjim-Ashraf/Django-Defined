# Django Rest Framework (Company-Employee)

## Summary

This is a basic project to practise how Django REST Framework operates. This project consists of backend APIs only & contains 2 models: **Company** & **Employee**.

💡**Note:**

- **API View:** Implemented **APIView** class provided by Django REST Framework. It provides a granular level of controls over _GET, POST, PUT, PATCH & DELETE_ APIs.

- **Serializer:** Implemented **ModelSerializer** to serialize the HTTP Requests & Responses.

## How to Setup

1. Create a Python virtual environment.

   > python -m venv env

2. Activate the virtual environment.

   > Bash: source env/bin/activate

3. Install all the dependencies.

   > pip install -r requirements.txt

4. Run the server using a shell script.

   > bash server.sh

<small>💡 Note: The shell script includes the `migration` commands along with the `runserver` command.</small>

## High Level Design

A conceptual data model is demonstrated below
![Company-Employee Data Model](./doc-resources/Company-Employee-Data-Modelling-2026-06-19-2104.png)
