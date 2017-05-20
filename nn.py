"""Neural Networks implementation 
    (c) R.Pavlov (M.Rashidov)
    20 May 2017
"""
class VectorSizeError(Exception):
    pass
class Neuron:
    """Binary neuron implementation
    _weights - list of weight coefficients
    _function - activatiation function of this neuron
    _inputs - size of X vector which is input vector"""
    def __init__(self, input_vector_size,activation_func):
        """Initializes work of neuron with size of input vector equal to value of input_vector_size
        """
        if input_vector_size < 1:
            raise VectorSizeError("Error 1 in Neuron. Input vector size is less then 1")
        else:
            self._weights = [0]*(input_vector_size+1) #Creating the weights vector sizes
            self._activation_func = activation_func
            self._inputs = input_vector_size #Number of input "dendrits"
    def performance(self,input_vector):
        """Returns the output of initialized neuron
        input_vector - list of numbers which are used as input for neuron"""
        if len(input_vector)==self._inputs:
            input_vector = [1] + list(input_vector)
            S=sum((self._weights[i]*input_vector[i] for i in range(0,self._inputs+1))) #S=summ of w_i*x_i (i=0.._inputs)
            return self._activation_func(S)
        else:
            raise VectorSizeError("Error 2 in Neuron. Input vector size must be equal to number of inputs of neuron")
    def learning(self, learning_base):
        """Learning process
        learning_base - dictionary of (X):t where X is input vector, t - result for X"""
        M = list(learning_base.items())
        y = [0] * len(learning_base.keys())
        t = [x[1] for x in M]
        cycle_count = 0 #Stops learning process if its not able to finish it
        while y != t and cycle_count<20:
            for i in range(len(M)):
                X = M[i][0]
                for j in range(self._inputs):
                    self._weights[j]+=X[j]*t[i]
            for i in range(len(M)):
                X = M[i][0]
                y[i] = self.performance(X)
            cycle_count += 1
        return (self._weights,cycle_count)

def learning_base(learning_file):
    """Learning of the neuron
    learning_file - path to the file which contains the data base for learning"""
    import re
    file = open(learning_file,"r")
    data_base = dict()
    for line in file:
        substring = re.match(r"{[^}]*}=-?[0-9]+",line) #find a valid test case
        if substring is not None:
            substring=substring.group()
            vector = re.match(r"{[^}]*}",substring).group() #extract vector from substring
            vector = vector[1:-1] #delete [ and ] signs
            result = re.findall(r"\=-?[0-9]+",substring)
            result = result[0]
            result = result[1:] #delete = sign
            vector = tuple(int(x) for x in vector.split())
            result = int(result)
            data_base[vector] = result
    file.close()
    return data_base

def binfunc(s):
    return int(s>0)
def bipfunc(s):
    return 1 if s>0 else -1
if __name__ == '__main__':
    t = Neuron(25,bipfunc)
    print(t.learning(learning_base("test.txt")))
    print(t.performance([0,0,0,0,0,0,1,1,1,1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0]))





