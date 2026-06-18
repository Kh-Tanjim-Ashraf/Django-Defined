class PrimaryReplicaRouter:
    def db_for_read(self, model, **hints):
        """
        Reads go to a randomly-chosen replica.
        """
        return "slave"

    def db_for_write(self, model, **hints):
        """
        Writes always go to default.
        """
        return "default"