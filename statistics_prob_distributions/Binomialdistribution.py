import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
                
    """

    def __init__(self, p = 0, n = 0):
        self.p = p
        self.n = n
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
        super().__init__(self.mean, self.stdev)
 
    def calculate_mean(self):
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
        return self.p * self.n

    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        
        return math.sqrt(self.n * self.p * (1 - self.p))

    def replace_stats_with_data(self):
        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """
        total_trials = len(self.data)
        pos_trails = len([x for x in self.data if x > 0])

        self.n = total_trials
        self.p = pos_trails / total_trials
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()

        return self.p , self.n

    def plot_bar(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """

        plt.hist(self.data)
        plt.title('Histogram of Data')
        plt.xlabel('Data')
        plt.ylabel('Count')
    
    def pdf(self, k):
        """Probability density function calculator for the binomial distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        n = self.n
        p = self.p

        part1 = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
        part2 = (p ** k) * ((1 - p) ** (n - k))
        return part1 * part2

    def plot_bar_pdf(self):
        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        x = []
        y = []

        
        for i in range(self.n):
            pdf = self.pdf(i)
            y.append(pdf)
            x.append(i)
        
        # make the plots
        plt.bar(x, y)
        plt.title('Probability Density Chart')
        plt.ylabel('Probability')
        plt.xlabel('Value')

        plt.show()

        return x, y

    def __add__(self, other):
        
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise

        self.n = self.n + other.n
        return self

    def __repr__(self):
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Binomial object
        
        """
        return f'mean {self.n}, standard deviation {self.stdev}, p {self.p}, n {self.n}'
