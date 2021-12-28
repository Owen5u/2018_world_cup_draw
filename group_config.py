
class dfw_group:
    def __init__(self,n):
        self.id = chr(n + 65)     
        self.nations = []
        self.BEG = 0
        self.MID = 0
        self.UPP = 0
        self.GA = 0
        self.GB = 0
        self.GC = 0
        self.GD = 0
        self.totalrank = 0

            
    def member_update(self,m,flag):
        
        if m[1] == 'C':
            self.BEG += 1
        elif m[1] == 'B':
            self.MID += 1
        elif m[1] == 'A':
            self.UPP += 1
        elif flag:
            print ('Wrong data in ' + m[0])
        if len(m) == 3:
            if m[2] == 0:
                self.GA +=1
            elif m[2] == 1:
                self.GB +=1
            elif m[2] == 2:
                self.GC +=1
            elif m[2] == 3:
                self.GC += 1
    
    def valid_check(self,k):
        if k[1] == 'B' and ( ( self.MID == 1 and (self.UPP ==2 or self.BEG == 2) ) or self.MID == 2):
            return False
        elif k[1] == 'C' and self.BEG == 1:
            return False
        elif k[1] == 'A' and ( ( self.UPP == 1 and (self.BEG ==2 or self.MID == 2) ) or self.UPP == 2):
            return False
        else:
            return True

    def valid_check_ver_2(self,k):
        if k[1] == 'B' and  self.MID == 2:
            return False
        elif k[1] == 'C' and self.BEG == 2:
            return False
        elif k[1] == 'A' and self.UPP == 2:
            return False
        if k[2] == 0 and self.GA == 2:
            return False
        elif k[2] == 1 and self.GB == 2:
            return False
        elif k[2] == 2 and self.GC == 2:
            return False
        elif k[2] == 3 and self.GD == 2:
            return False
        return True

 

   

class group:

    
    def __init__(self,n):
        self.id = chr(n + 65)     
        self.nations = []
        self.EU = 0
        self.AS = 0
        self.SA = 0
        self.AF = 0
        self.CN = 0
        self.totalrank = 0

            
    def member_update(self,m):
        if m[1] == 0:
            self.EU += 1
        elif m[1] == 1:
            self.AS += 1
        elif m[1] == 2:
            self.SA += 1
        elif m[1] == 3:
            self.AF += 1
        elif m[1] == 4:
            self.CN += 1
        else:
            print ('Wrong data in ' + m[0])
    
    def valid_check(self,k):
        if k[1] == 0 and self.EU == 2:
            return False
        elif k[1] == 1 and self.AS == 1:
            return False
        elif k[1] == 2 and self.SA == 1:
            return False
        elif k[1] == 3 and self.AF == 1:
            return False
        elif k[1] == 4 and self.CN == 1:
            return False
        else:
            return True
    
    def cont_rollback(self,m):
        if m == 0:
            self.EU -= 1
        elif m == 1:
            self.AS -= 1
        elif m == 2:
            self.SA -= 1
        elif m == 3:
            self.AF -= 1
        elif m == 4:
            self.CN -= 1
