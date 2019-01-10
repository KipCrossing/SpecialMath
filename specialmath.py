# By Kipling Crossing
# kip.crossing@gmail.com



class SpecialMath(object):
    example_data = [-5.389564, -2.889934, 0.0, 2.889933, 5.389565, 7.161306, 7.965873, 7.694605, \
    6.384138, 4.211457, 1.469996, -1.469998, -4.211458, -6.38414, -7.694605, -7.965873, -7.161306]

    def __init__(self):
        print("Message: 'Use special math!'")


    def mean(self,numb):
        return float(sum(numb)) / max(len(numb), 1)

    def gen_sin(self,length,shift, amp):
        time = []
        for x in range(length):
            time.append(x/length)
        y_list = []
        for x in time:
            y_list.append(amp*math.sin(math.pi*2*(x-(shift/length))))
        return(y_list)

    def SSE(self,observe,predict):
        summ = 0
        for i in range(0,len(observe)-1):
            summ += (observe[i]-predict[i])**2
        return(summ)

    def fit_sin(self,data_list,itt):
        data_mean =self.mean(data_list)
        Amp_high =self.mean([data_mean - min(data_list),max(data_list) - data_mean])*1.5
        Amp_low = 0

        shft = 0
        Amp = Amp_high

        for i in range(len(data_list)):



        for i in range(itt):
            sta = self.gen_sin(len(data_list),Nstart,Amp)
            end = self.gen_sin(len(data_list),Nend,Amp)
            for j in range(10):
                if self.SSE(data_list,sta) > self.SSE(data_list,end):
                    Nstart =self.mean([Nstart,Nend])
                    shft = Nend
                elif self.SSE(data_list,sta) < self.SSE(data_list,end):
                    Nend =self.mean([Nstart,Nend])
                    shft = Nstart
                else:
                    shft = Nstart
                    print('Break1')
                    break
            high = self.gen_sin(len(data_list),shft,Amp_high)
            low  = self.gen_sin(len(data_list),shft,Amp_low)
            for k in range(10):
                if self.SSE(data_list,high) > self.SSE(data_list,low):
                    Amp_high =self.mean([Amp_high,Amp_low])
                    Amp = Amp_low
                elif self.SSE(data_list,high) < self.SSE(data_list,low):
                    Amp_low =self.mean([Amp_high,Amp_low])
                    Amp = Amp_high
                else:
                    Amp = Amp_high
                    print('Break2')
                    break

        print(shft)
        print(Amp)
        return((Amp,shft))


sm = SpecialMath()
print(sm.fit_sin(sm.example_data,10))
