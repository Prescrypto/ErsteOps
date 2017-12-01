from django.conf import settings

class OdooDBRouter(object): 
    def db_for_read(self, model, **hints):
        "Point all operations on odoodb models to 'heroku'"
        if model._meta.app_label == 'odoodb':
            return 'odoodb'
        return 'default'

    def db_for_write(self, model, **hints):
        "Point all operations on odoodb models to 'heroku'"
        if model._meta.app_label == 'odoodb':
            return 'odoodb'
        return 'default'
    
    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a both models in odoodb app"
        if obj1._meta.app_label == 'odoodb' and obj2._meta.app_label == 'odoodb':
            return True
        # Allow if neither is chinook app
        elif 'odoodb' not in [obj1._meta.app_label, obj2._meta.app_label]: 
            return Trues
        return False
    
    def allow_syncdb(self, db, model):
        if db == 'odoodb' or model._meta.app_label == "odoodb":
            return False # we're not using syncdb on our legacy database
        else: # but all other models/databases are fine
            return True

    # def allow_migrate(self, db, app_label, model_name=None, **hints):
    #     """
    #     Make sure the auth app only appears in the 'auth_db'
    #     database.
    #     """
    #     #print "check migrations: "+ app_label
    #     if app_label == 'odoodb':
    #         #return db == 'default'
    #         return False
    #     elif app_label != 'odoodb':
    #         #return True  
    #         return db == 'default'
    #     return None           