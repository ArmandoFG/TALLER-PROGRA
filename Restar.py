class restar_bases (object):
    def __init__(self):
        pass

    def restar (self, num1, num2, base):
        if isinstance (num1, list) and (num2, list):
            return self.restar_aux (num1, num2, base, 0)
        else:
            "Los valores ingresados son incorrectos"

    def restar_aux (self, num1, num2, base, prestado):
        hexa ={ 0: 0,1: 1,2: 2,3: 3,4: 4,5: 5,6: 6,7: 7,8: 8,9: 9,10: "A",11: "B",12: "C",13: "D",14: "E",15: "F",16: "G"}

        if num1 == [] and num2 == []:
            return []
        elif len (num1) >= 1 and num2 == []:
            return self.restar_aux (num1[:-1], num2, base, 0) + [hexa[num1[-1] - prestado]]
        elif (num1[-1] - prestado) > num2[-1]:
            return self.restar_aux(num1[:-1], num2[:-1], base, 0) + [hexa[(num1[-1] - prestado) - num2[-1]]]
        elif (num1[-1] - prestado) == num2[-1]:
            return self.restar_aux(num1[:-1], num2[:-1], base, 0) + [0]
        elif (num1[-1] - prestado) < num2[-1]:
            return self.restar_aux(num1[:-1], num2[:-1], base, 1) + [hexa[((num1[-1] - prestado) + base) - num2[-1]]]
        else :
            return self.restar_aux (num1[-1], num2[-1], base, prestado)



       
