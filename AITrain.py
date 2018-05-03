from ReversiAI import ReversiController

TOTAL_EPISODES = 10000000

#path = "/Users/student36/reinforcement-learning-othello/"
path = "/home/oliver/git/othello/reinforcement-learning-othello/Weights_Folder1/"

controller = ReversiController(path, False, False, population_size = 1,
                               learning_rate = 0.001, epsilon = 2,
                               epsilon_increment = 0.01)
#controller.load([0])
controller.main(TOTAL_EPISODES)
