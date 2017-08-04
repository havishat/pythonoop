class Call(object):
    def __init__(self,unique_id,class_name,caller_phone_num,timeofcall,reason_for_call):
        self.unique_id = unique_id
        self.class_name = class_name
        self.caller_phone_num = caller_phone_num
        self.timeofcall = timeofcall
        self.reason_for_call = reason_for_call
        self.display_all()

    def display_all(self):
        print self.unique_id
        print self.class_name 
        print self.caller_phone_num
        print self.timeofcall 
        print self.reason_for_call
    
    def __str__(self):
        return "unique_id ( {} ) class_name ( {} ) caller_phone_num ( {} ) timeofcall ( {} ) reason_for_call ( {} ) ".format(' '.join(self.unique_id), self.class_name, self.caller_phone_num, self.timeofcall, self.reason_for_call)  

call1 = Call("12","mat","408-245-1345","3:45","lsfksfal")
call2 = Call("53","ho","408-255-13345","6:45","Jav")
call3 = Call("64","ajot","408-255-1245","1:15","lav")
call4 = Call("42","matt","508-456-1345","10:45","lsfksfal")
call5 = Call("54","hoht","708-3434-1745","6:45","Jasafv")
call6 = Call("84","ahho","408-255-7435","8:45","ladv")

class CallCenter(object):
    def __init__(self):
        self.calls = []
        self.queue_size = 0

    def add(self, newcall):
        self.calls.append(newcall)
      #  print self.calls
        return self
    
    def remove(self):
        if len(self.calls) > 0: 
            self.calls.pop(0)
        return self
    
    def ninjalevel(self, phonenum):
        for idx, call in enumerate(self.calls):
             if call.caller_phone_num == phonenum:
                 self.calls.pop(idx)
                 return self
    def hackerlever(self):
        def keyfuc(call):
            return call.timeofcall
        self.calls = sorted(self.calls , key=keyfuc)

    def __str__(self):
            callstring = ''
            for c in self.calls:
                callstring += str(c) + "\n"
            return "calls ( {} ) queue_size ( {} )".format(callstring, self.queue_size)  

callcenter = CallCenter()
callcenter.add(call1)
callcenter.add(call2)
callcenter.add(call3)
callcenter.add(call4)
callcenter.add(call5)
callcenter.add(call6)
callcenter.remove()
callcenter.ninjalevel("408-255-13345")
callcenter.hackerlever()
print callcenter



