# DRF - Custom User Model, Login, Registration, Forget Password, Reset Password

## 🎯 Objectives

1. ☑️ Custom user model

2. ☑️ Implement custom user interface in admin panel

3. ☑️ Registration API

4. ☑️ Login API
   - ☑️ Token refresh API

5. ☑️ Password change API

6. ☑️ Forget password API
   - Send reset password link to user via email

7. Reset password API
   - Verify reset password link through `GET` request (_When the user clicks the link from his/her mailbox_). Use a separate serializer.
   - Verify password & confirm password through `POST` request. Use a separate serializer.

8. Email Service:
   - Welcome email

   - Password reset link email

9. Throttling:
   - Anonymous User: 20 requests/minute
   - Authenticated User: 50 requests/minute
   - Login API: 20 requests/hour
   - Registration API: 5 requests/day
