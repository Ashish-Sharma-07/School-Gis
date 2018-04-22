class ER(object):
   
 
    def db_for_read(self, model, **hints):
        """
        Point all operations on myapp2 models to 'my_db_2'
        """
        if model._meta.app_label == 'state_level':            
		return 'datastore'
        return None
 
    def db_for_write(self, model, **hints):
        """
        Point all operations on myapp models to 'other'
        """
        if model._meta.app_label == 'state_level':
            return 'datastore'
        return None
 
    def allow_syncdb(self, db, model):
        """
        Make sure the 'myapp2' app only appears on the 'other' db
        """
        if db == 'datastore':
            return model._meta.app_label == 'state_level'
        elif model._meta.app_label == 'state_level':
            return False
        return None
