class PhonesDBRouter:
    route_app_labels = "phones"
    db_name = "mongo_db"

    def db_for_read(self, model, **hints):
        return self.db_name

    def db_for_write(self, model, **hints):
        return self.db_name

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label == self.route_app_labels
            or obj2._meta.app_label == self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return db == self.db_name
