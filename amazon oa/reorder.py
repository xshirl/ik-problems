class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        # Init list to contain letter and digit logs
        letter_logs = []
        digit_logs = []
        
        # For each log separate and put them into separate logs
        for log in logs:
            l = log.split(" ")
            if l[1].isdigit():
                digit_logs.append(l)
            else:
                letter_logs.append(l)
        
        # Sort letter logs as required
        letter_logs = sorted(letter_logs, key=lambda x: (x[1:],x[0])) 
       
        # re-combine and return
        return [" ".join(l) for l in letter_logs] + [" ".join(l) for l in digit_logs]