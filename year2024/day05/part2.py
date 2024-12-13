import re

class Rule:
    x:int; y:int
    def __init__(self,x,y):
        self.x=x; self.y=y
    def __str__(self):
        return str(self.x)+'|'+str(self.y)
    
def retrieveRulesWhereSecondIs(page, rules):
    about = [r for r in rules if r.y == page]
    return about

def checkUpdate(update, rules, correct):
    current_rules = [] # rules that apply to this update
    for i in range(0, len(update)):
        page = update[i]
        for rule in current_rules:
            if rule.x == page: 
                for j in range(0,i):
                    if update[j] == rule.y: # rule violation :(
                        update[i], update[j] = update[j], update[i]
                        if correct: return checkUpdate(update, rules, correct)
                        else: return False
                        
        current_rules += retrieveRulesWhereSecondIs(page, rules) # rules where this page is in 2nd position now apply to this update
    
    if correct: return update
    else: return True
    
def main():
    with open('input') as f:
        input = f.readlines()

    # parse
    parsing_rules=True
    rules = []
    updates = []
    for l in input:
        if l=="\n": parsing_rules = False; continue
        else: 
            if parsing_rules: n = re.findall(r'\d+', l); rules.append(Rule(int(n[0]),int(n[1])))
            else: n = re.findall(r'\d+', l); updates.append([int(x) for x in n])
            
    # compute
    ko_updates = [update for update in updates if not checkUpdate(update, rules, False)]
    corrected_updates = [checkUpdate(update, rules, True) for update in ko_updates]
    corrected_middle_pages = [update[int((len(update)-1)/2)] for update in corrected_updates]
    
    print(sum(corrected_middle_pages))
        
if __name__ == '__main__':
    main()