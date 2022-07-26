#file = file containing all 50-digit numbers, separated by a line break (\n)
def problem13(file):
    with open(file) as f:    
        numbers = [int(line[:-7]) for line in f.readlines() if line[:-7] != '']
        
    return str(sum(numbers))[:10]
