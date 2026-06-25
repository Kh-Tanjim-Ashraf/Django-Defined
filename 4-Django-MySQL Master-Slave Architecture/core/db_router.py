from product.middleware import get_current_request_is_admin

class PrimaryReplicaRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label in ['admin', 'auth', 'contenttypes', 'sessions']:
            return "default"

        # Intercept the admin requests through a custom middleware   
        if get_current_request_is_admin():
            print("Admin request detected! Routing read to: default")
            return "default"

        print("Public request! Redirects to slave DB!")
        return "slave"

    def db_for_write(self, model, **hints):
        print("Hit write db!")
        return "default"