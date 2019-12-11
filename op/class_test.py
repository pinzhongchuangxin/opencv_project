class A(object):
    a1 = 35
    a2 = 90
    def __init__(self,jbk=56,mjo=37):
        self.a1 = jbk
        self.a2 = mjo

class B(A):

    s1 = 3
    s2 = 0
    def __init__(self,src_1=3,src_2=0):
        # super(A,self).__init__()
        s1 = src_1
        self.s3 = src_1
        self.s4 = src_2

    def get_src_notst():
        print(B.s1)
        print(B.s2)

    @staticmethod 
    def get_src():
        print(B.s1) 
        print(B.s2)
        

    @staticmethod
    def set_src(a1,a2):
        B.s1 = a1
        B.s2 = a2
# b = B()
# b.get_src_notst()
# b.get_src()
for i in range(45,-46,-10):
    print(i)
