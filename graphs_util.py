from matplotlib import pyplot as plt

class GraphsUtil:
    def __init__(self, axisX, axisY, axisZ, times, title = ""):
        self.axisX = axisX
        self.axisY = axisY
        self.axisZ = axisZ
        self.times = times
        self.title = title
        
    def plot3AxisData(self):
        fig, axs = plt.subplots(3)

        fig.suptitle(self.title)
    
        axs[0].plot(self.times,self.axisX) #marker = "o"
        axs[0].set_title("Axis X", loc = 'left')

        axs[1].plot(self.times,self.axisY) #marker = "o"
        axs[1].set_title("Axis Y", loc = 'left')

        axs[2].plot(self.times,self.axisZ) #marker = "o"
        axs[2].set_title("Axis Z", loc = 'left')

        plt.show()
