# By Kipling Crossing
# kip.crossing@gmail.com
import math


class SpecialMath(object):
    example_data = [7013, 4020, 3648, 5009, 8975, 14013, 20992, 28005, 35020, 41425, 46042, 49082, 49977, 48239, 44645, 38966, 32582, 25132, 18021, 11989]

    example_data2 = [30206, 37110, 43028, 47243, 49986, 49995, 47950, 43435, 37826, \
     30909, 23363, 16531, 10771, 6034, 3997, 3995, 6000, 10003, 16299, 23232]


    def __init__(self):
        print("Message: 'Use special math!'")


    def mean(self,numb):
        return float(sum(numb)) / max(len(numb), 1)

    def gen_sin(self,length,shift, amp):
        time = []
        for x in range(length):
            time.append(x/float(length))
        y_list = []
        for x in time:
            y_list.append(amp*math.sin(math.pi*2*(x-(shift/float(length)))))
        return(y_list)

    def SSE(self,observe,predict):
        summ = 0
        for i in range(0,len(observe)-1):
            summ += (observe[i]-predict[i])**2
        return(summ)

    def fit_sin(self,data_list,itt):
        data_mean = self.mean(data_list)
        for d in range(0,len(data_list)):
            data_list[d] -= data_mean
        Amp_high = self.mean([data_mean - min(data_list),max(data_list) - data_mean])
        print(data_list)
        print(Amp_high)
        Amp_low = 0

        shft = 0
        Amp = Amp_high
        small_sse = 9999999999
        small_sse_a = 9999999999
        temp_shft = 0
        ALT = 0
        AHT = Amp_high

        for itteration in range(0,itt):

            for i in range(0,len(data_list)):
                if i == len(data_list):
                    t_shift = shft + float(0)/float(len(data_list)**itteration)
                else:
                    t_shift = shft + float(i)/float(len(data_list)**itteration)
                u_shift = t_shift + float(1)/float(len(data_list)**itteration)
                print(t_shift,u_shift)
                t_wave = self.gen_sin(len(data_list),t_shift,Amp)
                u_wave = self.gen_sin(len(data_list),u_shift,Amp)
                t_sse = self.SSE(data_list, t_wave)
                u_sse = self.SSE(data_list, u_wave)
                if self.mean([t_sse,u_sse]) < small_sse:
                    small_sse = self.mean([t_sse,u_sse])
                    temp_shft = t_shift
            shft = temp_shft
            print('SHIFT: %f'%shft)

        for itteration in range(1,itt):
            for step in range(0,9):
                amp_step_l = Amp_low + float(step)*((Amp_high - Amp_low)*2/(10.0))
                print('amp_step_l: %f' % amp_step_l)
                amp_step_h = amp_step_l + ((Amp_high - Amp_low)*2/(10.0))

                l_wave = self.gen_sin(len(data_list),shft,amp_step_l)
                h_wave = self.gen_sin(len(data_list),shft,amp_step_h)
                l_sse = self.SSE(data_list, l_wave)
                h_sse = self.SSE(data_list, h_wave)

                if self.mean([l_sse,h_sse]) < small_sse_a:
                    small_sse_a = self.mean([l_sse,h_sse])
                    ALT = amp_step_l
                    AHT = amp_step_h



            Amp_low  = ALT
            Amp_high = AHT
            print(itteration,Amp_low,Amp_high)
            Amp = self.mean([Amp_low,Amp_high])
            print('AMP %f' % Amp)



        return((Amp,shft))



sm = SpecialMath()
(a,s) = sm.fit_sin(sm.example_data,5)
print(round(a,4),round(s,4))

wavedat = sm.gen_sin(20,s,a)

for h in wavedat:
    print(h)
