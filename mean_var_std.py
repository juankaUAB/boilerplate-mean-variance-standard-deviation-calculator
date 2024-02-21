import numpy as np

def calculate(lista):

    if len(lista) == 9:
        matrix = np.array(lista).reshape(3,3)
        array = np.array(lista)
        calculations = {}
        
        # means
        means = []
        means.append(list(np.mean(matrix, axis=0)))
        means.append(list(np.mean(matrix, axis=1)))
        means.append(np.mean(array))
        calculations['mean'] = means
        
        #variance
        variance = []
        variance.append(list(np.var(matrix, axis=0)))
        variance.append(list(np.var(matrix, axis=1)))
        variance.append(np.var(array))
        calculations['variance'] = variance
        
        #standard deviation
        std = []
        std.append(list(np.std(matrix, axis=0)))
        std.append(list(np.std(matrix, axis=1)))
        std.append(np.std(array))
        calculations['standard deviation'] = std
        
        #min
        min = []
        min.append(list(np.min(matrix, axis=0)))
        min.append(list(np.min(matrix, axis=1)))
        min.append(np.min(array))
        calculations['min'] = min

        #max
        max = []
        max.append(list(np.max(matrix, axis=0)))
        max.append(list(np.max(matrix, axis=1)))
        max.append(np.max(array))
        calculations['max'] = max
        
        #sum
        sum = []
        sum.append(list(np.sum(matrix, axis=0)))
        sum.append(list(np.sum(matrix, axis=1)))
        sum.append(np.sum(array))
        calculations['sum'] = sum

        return calculations
    else:
        raise ValueError("List must contain nine numbers.")