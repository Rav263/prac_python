class morse:
    
    def __init__(self, string=""):
        self.dot, self.end_dot, self.end, self.dah, self.space, self.split = "di", "dit", ".", "dah", " ", ","
        self.gen_string = []

        words = string.split(" ")
        if len(words) == 1 and len(words[0]) >= 2:
            if len(words[0]) == 2:
                self.dot = words[0][0]
                self.end_dot = words[0][0]
                self.dah = words[0][1]
            
            if len(words[0]) >= 3:
                self.dot = words[0][0]
                self.end_dot = words[0][1]
                self.dah = words[0][2]
            
            if len(words[0]) == 4:
                self.end = words[0][3]
            else:
                self.end = ""
            self.space = ""
            self.split = " "
        if len(words) == 2:
            self.dot = words[0]
            self.end_dot = words[0]
            self.dah = words[1]

        if len(words) >= 3:
            self.dot = words[0]
            self.end_dot = words[1]
            self.dah = words[2]
        
        if len(words) == 4:
            self.end = words[3]



    def __neg__(self):
        self.gen_string.append(self.dah)
        self.gen_string.append(self.space)

        return self
   
    
    def __pos__(self):
        if len(self.gen_string) >= 2:
            if self.gen_string[-1] == self.split:
                self.gen_string.append(self.end_dot)
            else:
                self.gen_string.append(self.dot)
        else:
            self.gen_string.append(self.end_dot)
        
        self.gen_string.append(self.space)
        
        return self
    

    def __invert__(self):
        self.gen_string.append(self.split)
        
        return self
    

    def __str__(self):
        self.gen_string = self.gen_string[:-1]
        string = "".join(reversed(self.gen_string))
        string += self.end

        return string
