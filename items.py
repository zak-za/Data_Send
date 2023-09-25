


class Item:
    """Item Model"""

    def __init__(self, IDJOBPLAN,JOBNAME,INSTANCIA,PRIOSALI,DATEPLAN,FMINEJEC,):
        self.IDJOBPLAN = IDJOBPLAN
        self.JOBNAME = JOBNAME
        self.INSTANCIA = INSTANCIA
        self.PRIOSALI = PRIOSALI
        self.DATEPLAN = DATEPLAN
        self.FMINEJEC = FMINEJEC
        

class ItemStore:
     
    def __init__(self):
        self.items = []

    def get_item(self, item_id):
        """Get item"""

        for item in self.items:
            if item.IDJOBPLAN == item_id:
                return item
        return None        
           