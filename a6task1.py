import random

class Matrix:
    
    def __init__(self, matrix):
        """initialises matrix object with a matrix input"""
        self.matrix = matrix
        self.matrix_dimensions()
        self.sum_matrix()
        self.sum_columns()
        self.column_means()
        
    def matrix_dimensions(self):
        """Calculates matrix dimensions"""
        self.rows = len(self.matrix)
        self.columns = len(self.matrix[0])
    def swap_rows(self, src, dest):

        """swaps rows from source to destination"""
        M = self.matrix
        temp = M[src]
        M[src] = M[dest]
        M[dest] = temp
        
        self.matrix = M
        
    def __repr__(self):
        """prints matrix"""
        
        s = "["
        M = self.matrix
        
        for i in range(len(M)):

            if i == 0:
                s += "["
            else:
                s += " ["
                
            for j in range(len(M[0])):
                formatted_elem = "{:.2f}".format(M[i][j])
                if j == len(M[0]) - 1:
                    s += formatted_elem
                else:
                    s += formatted_elem + ", "
            # Add a newline character after each row
            if i == len(M) - 1:
                s += "]]"
            else:
                s += "] \n"
        return s
    
    def mult_row_scalar(self, row, scalar):
        
        """scalar multiply for a targeted row"""
        M = self.matrix
        for i in range(len(M[row])):
            M[row][i] *= scalar
            
        return M

    def add_row_into(self, src, dest):
        """ adds row to target location"""
        M = self.matrix
        temp = []
        for i in range(len(M[src])):
            temp.append(M[src][i]+ M[dest][i])
        M[dest] = temp
        
        self.matrix = M
        
    def add_mult_row_into(self, factor, src, dest):
        """ adds row to target location with scalar"""
        M = self.matrix
        temp = []
        for i in range(len(M[src])):
            temp.append(factor*M[src][i]+ M[dest][i])
        M[dest] = temp
        
        self.matrix = M
    
    def transpose(self):
        """transposes matrix"""
        M = self.matrix

        result = isinstance(M[0], list) #1d lists dont compute the same way so in the event that A[0] is not iterable, the function goes to assuming its 1
        if result:
            mat = [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]
        else:
            mat = [[row for col in range(1)] for row in M]
        return mat
    
    def blank(self, n, m = 0):
        """creates matrix[n][m] of zeros """ 
        if m == 0:
            m = n

        mat = [[0 for col in range(m)] for row in range (n)];
        return mat
    
    def __eq__(self, value):
        if type(value) is int:
            A = self.matrix
            
            for i in range(len(A)):
                for j in range(len(A[0])):
                    A[i][j] += value
            return A
        if type(value) is Matrix:
            A = self.matrix
            B = value.matrix
            
            for i in range(len(A)):
                for j in range(len(A[0])):
                    if A[i][j] != B[i][j]:
                        return False
            
            return True
    
    def __add__(self, value):
        if type(value) is int:
            A = self.matrix
            
            for i in range(len(A)):
                for j in range(len(A[0])):
                    A[i][j] += value
            return A
        if type(value) is Matrix:
            A = self.matrix
            B = value.matrix
            
            for i in range(len(A)):
                for j in range(len(A[0])):
                    A[i][j] += B[i][j]
            
            return A
            
    
    def __sub__(self, value):
        if type(value) is int:
            A = self.matrix
            
            for i in range(len(A)):
                for j in range(len(A[0])):
                    A[i][j] -= value
            return A
        if type(value) is Matrix:
            A = self.matrix
            B = value.matrix
            
            for i in range(len(A)):
                for j in range(len(A[0])):
                    A[i][j] -= B[i][j]
            
            return A
        
    def __mul__(self, value):
        if type(value) is int:
            A = self.matrix
            
            for i in range(len(A)):
                for j in range(len(A[0])):
                    A[i][j] *= value
            return A
        
        if type(value) is Matrix:
            A = self.matrix
            B = value.matrix
            assert len(A) == len(B[0]), "incompatible dimensions: cannot dot-product (" + str(len(A)) + "," + str(len(A[0])) + ") with (" + str(len(B)) +  "," + str(len(B[0])) + ")"
            dotMatrix = [[0 for col in range(len(A))] for row in range (len(B[0]))]
            
            for i in range(len(A)):
                 for j in range(len(B[0])):
                    for k in range(len(B)):
                        dotMatrix[i][j] += A[i][k]*B[k][j]
            return dotMatrix
    
    def __truediv__(self, value):
        if type(value) is int:
            A = self.matrix
            
            for i in range(len(A)):
                for j in range(len(A[0])):
                    A[i][j] /= value
            return A
        if type(value) is Matrix:
            A = self.matrix
            B = value.matrix
            
            for i in range(len(A)):
                for j in range(len(A[0])):
                    A[i][j] /= B[i][j]
            
            return A
        
    def sum_matrix(self):
        """ sum of matrix"""
        matrix = self.matrix
        matrix_sum = 0
        for row in matrix:
            for element in row:
                matrix_sum += element
    
        self.matrix_sum = matrix_sum
    
    def sum_columns(self):
        """ sum of matrix columns"""
        matrix = self.matrix
        column_sums = [0] * len(matrix[0])
    
        for j in range(len(matrix[0])):
            for i in range(len(matrix)):
                column_sums[j] += matrix[i][j]
    
        self.column_sums = column_sums
    
    def column_means(self):
        """ sum of columns means"""
        matrix = self.matrix
        column_means = []
    
        for i in range(self.columns):
            column_mean = self.column_sums[i] / len(matrix)
            column_means.append(column_mean)
    
        self.column_means = column_means
    
    def describe(self):
        """describes useful characteristics of matrix"""
        s = "["
        M = self.matrix
        
        for i in range(len(M)):

            if i == 0:
                s += "["
            else:
                s += " ["
                
            for j in range(len(M[0])):
                formatted_elem = "{:.2f}".format(M[i][j])
                if j == len(M[0]) - 1:
                    s += formatted_elem
                else:
                    s += formatted_elem + ", "
            # Add a newline character after each row
            if i == len(M) - 1:
                s += "]]"
            else:
                s += "] \n"
        s += "\n"
        s += f"dimensions: {self.rows} X {self.columns}"
        s += "\n"
        s += f"sum of elements: {self.matrix_sum}"
        s += "\n"
        s += f"mean of elements: {self.matrix_sum/(self.rows*self.columns)}"
        s += "\n"
        s += f"column sums: {self.column_sums}"
        s += "\n"
        s += f"column means: {self.column_means}"
        return s
    
    def mult_scalar(self, s):
        """ Returns matrix times some scalar"""
        M = self.matrix
        for i in range(len(M)):
            for j in range(len(M[0])):
                M[i][j] *= s
        
        return M


    def add_scalar(self, value):
        """ Returns Element wise addition """
        A = self.matrix
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] += value
        return A

    def dot_product(self, other):
        """ Dot product of matrix"""
        assert type(other) == Matrix, "Input has to be a Matrix"
        B  = other.matrix
        A = self.matrix
        m = len(A)  # number of rows in A
        n = len(B[0])  # number of columns in B
    
        assert len(A[0]) == len(B), "Matrices cannot be multiplied"
    
      
        result = [[0 for _ in range(n)] for _ in range(m)]
    
        for i in range(m):
            for j in range(n):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]
    
        return result
            
        
    def element_product(A, B):
        """ Returns Element wise multiplication """
        resultA = isinstance(A[0], list) #1d lists dont compute the same way so in the event that A[0] is not iterable, the function goes to assuming its 1
        resultB = isinstance(B[0], list)
        
        if resultA and resultB:
            assert len(A) == len(B) and len(A[0]) == len(B[0]), "Matrix Dimensions don't match"
            
            for i in range(len(A)):
                for j in range(len(A[0])):
                    A[i][j] *= B[i][j]
        else:
            for i in range(len(A)):
                A[i] *= B[i]
        return A    
    
    @classmethod
    def zeros(cls, n, m = 0):
        """creates matrix[n][m] of zeros """ 
        if m == 0:
            m = n

        mat = [[0 for col in range(m)] for row in range (n)]
        return cls(mat)
    
    @classmethod
    def ones(cls, n, m = 0):
        """creates matrix[n][m] of ones """
        if m == 0:
            m = n
 
        mat = [[1 for col in range(m)] for row in range (n)]
        return cls(mat)
    @classmethod   
    def identity(cls, n):
        """creates the square identity matrix of size n """
        mat = [[0 for col in range(n)] for row in range (n)]
        for i  in range(len(mat[0])):
            mat[i][i] = 1.00
        return mat
    @classmethod    
    def random_int_matrix(cls, n, m = 0, lower = 1, upper = 10):
        """creates matrix of size [n][m] in the range of lower and upper inclusive"""
        if m == 0:
            m = n

        mat = [[0 for col in range(m)] for row in range (n)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = random.randint(lower, upper)
        return cls(mat)
    @classmethod       
    def random_float_matrix(cls, n, m = 0):
        """creates matrix of size [n][m] in the range of lower and upper inclusive"""
        if m == 0:
            m = n
            
        mat = [[random.random() for col in range(m)] for row in range(n)]
        return cls(mat)
    

