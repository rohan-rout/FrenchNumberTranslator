import sys
from fst import FST
from fsmutils import composewords

kFRENCH_TRANS = {0: "zero", 1: "un", 2: "deux", 3: "trois", 4:
                 "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit",
                 9: "neuf", 10: "dix", 11: "onze", 12: "douze", 13:
                 "treize", 14: "quatorze", 15: "quinze", 16: "seize",
                 20: "vingt", 30: "trente", 40: "quarante", 50:
                 "cinquante", 60: "soixante", 100: "cent"}

kFRENCH_AND = 'et'

def prepare_input(integer):
    assert isinstance(integer, int) and integer < 1000 and integer >= 0, \
      "Integer out of bounds"
    return list("%03i" % integer)

def french_count():
    f = FST('french')

    f.add_state('start')
    f.add_state('final')
    f.add_state('state1')
    f.add_state('state2')
    f.add_state('state3')
    f.add_state('state4')
    f.add_state('state5')
    f.add_state('state6')
    f.add_state('state7')
    f.add_state('state8')
    f.add_state('state9')        
        
    f.initial_state = 'start'

    f.set_final('final')

    
    for ii in xrange(10):
    
        if(ii==0):
            f.add_arc('start', 'state1', (str(ii)), ())
        elif(ii == 1):
            f.add_arc('start', 'state7', (str(ii)), ())
        else:
            f.add_arc('start', 'state7', (str(ii)), [kFRENCH_TRANS[ii]])
                  
        if(ii==0):    
            f.add_arc('state1', 'state2', (str(ii)), ())
        
        if(ii >= 0):
            f.add_arc('state2', 'final', (str(ii)), [kFRENCH_TRANS[ii]])
            
        if(ii == 1):
            f.add_arc('state1','state3', (str(ii)), ())
        elif((ii>=2) and (ii<=6)):
            f.add_arc('state1','state4', (str(ii)), [kFRENCH_TRANS[10*ii]])
        elif(ii == 7):
            f.add_arc('state1','state5', (str(ii)), [kFRENCH_TRANS[60]])    
        elif(ii == 8):
            f.add_arc('state1','state6', (str(ii)), [kFRENCH_TRANS[4]+" "+kFRENCH_TRANS[20]])
        elif(ii == 9):
            f.add_arc('state1','state3', (str(ii)), [kFRENCH_TRANS[4]+" "+kFRENCH_TRANS[20]])
        
        if((ii>=0) and (ii<=6)):
            f.add_arc('state3','final', (str(ii)), [kFRENCH_TRANS[10+ii]])
        else:
            f.add_arc('state3','final', (str(ii)), ["dix "+kFRENCH_TRANS[ii]])   
            
        if(ii == 0):
            f.add_arc('state4','final', (str(ii)), ())
        elif(ii == 1):               
            f.add_arc('state4','final', (str(ii)),["et un"])
        else:
            f.add_arc('state4','final', (str(ii)),[kFRENCH_TRANS[ii]])        

        if(ii == 1):
            f.add_arc('state5','final', (str(ii)),["et onze"])
        elif((ii>=0) and (ii<=6)):
            f.add_arc('state5','final', (str(ii)), [kFRENCH_TRANS[10+ii]])
        else:
            f.add_arc('state5','final', (str(ii)), ["dix "+kFRENCH_TRANS[ii]])
                        
        if(ii == 0):
            f.add_arc('state6','final', (str(ii)), ())
        else:
            f.add_arc('state6','final', (str(ii)), [kFRENCH_TRANS[ii]])
            
        f.add_arc('state7', 'state8', (), [kFRENCH_TRANS[100]])
        
        if(ii == 0):
            f.add_arc('state8', 'state9', (str(ii)), ())
        elif(ii == 1):
            f.add_arc('state8', 'state3', (str(ii)), ())
        elif(ii == 9):    
            f.add_arc('state8', 'state3', (str(ii)), [kFRENCH_TRANS[4]+" "+kFRENCH_TRANS[20]])
        elif((ii >= 2) and (ii <= 6)):     
            f.add_arc('state8', 'state4', (str(ii)), [kFRENCH_TRANS[10*ii]])
        elif(ii == 7):
            f.add_arc('state8', 'state5', (str(ii)), [kFRENCH_TRANS[60]])
        elif(ii == 8):
            f.add_arc('state8', 'state6', (str(ii)),[kFRENCH_TRANS[4]+" "+kFRENCH_TRANS[20]])
        
        if(ii == 0):   
            f.add_arc('state9', 'final', (str(ii)), ())
        else:
            f.add_arc('state9', 'final', (str(ii)), [kFRENCH_TRANS[ii]])        
        
    f.set_final('start')

    return f


if __name__ == '__main__':
    string_input = raw_input()
    user_input = int(string_input)
    f = french_count()
    if string_input:
        print user_input, '-->',
        print " ".join(f.transduce(prepare_input(user_input)))
        
