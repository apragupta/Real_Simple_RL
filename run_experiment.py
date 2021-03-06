"""
Run this to conduct an experiment
"""
import os
import time
import matplotlib.pyplot as plt

from Experiment.ExperimentClass import Experiment
from GridWorld.GridWorldMDPClass import GridWorldMDP
from GridWorld.GridWorldStateClass import GridWorldState
from GridWorld.TaxiMDPClass import TaxiMDP
from GridWorld.TwoRoomsMDP import TwoRoomsMDP
from Agent.AgentClass import Agent
from resources.AbstractionTypes import Abstr_type
from resources.AbstractionCorrupters import *

# MDP details
MDP = GridWorldMDP()
mdp_sum = 'FourRooms MDP'
MDP = TwoRoomsMDP(hallway_states=[5], goal_location=[(1,8)])
#MDP = TwoRoomsMDP()
mdp_sum = 'TwoRooms MDP'

# Experiment parameters
NUM_EPISODES = 250
NUM_CORR_MDPS = 5
NUM_AGENTS = 10
EPS = 0.0
#MDP_STR = 'rooms'
EXPLORATION_EPSILON = 0.1
DETACH_INTERVAL = 1000
DETACH_POINTS = [1000]
#DETACH_INTERVAL = None
#DETACH_POINTS = None
PREVENT_CYCLES = True
RESET_Q_VALUE = True
VARIANCE_THRESHOLD = None
EXPLORING_STARTS = False
DECAY_EXPLORATION = False
STEP_LIMIT = 10000
NOTES = 'heck'
AGENT_DETACH_METHOD = 'abstr'
DETACH_REASSIGNMENT = 'group'

# Trying to find 'gadget' instances for divergent pair
CORRUPTION_LIST = None
ABSTR_EPSILON_LIST = [(Abstr_type.Q_STAR, EPS), (Abstr_type.A_STAR, EPS), (Abstr_type.PI_STAR, EPS)]


# This one fucks up pi*
ERROR_DICTS = [{GridWorldState(1,2): GridWorldState(2,8)}, # State to the right of the starting state mapped with the
                                                            # state to the right of the goal state
               {GridWorldState(2,2): GridWorldState(1,9)},
               {GridWorldState(3,3): GridWorldState(2,8)},
               {GridWorldState(6,5): GridWorldState(1,9)}]



# No errors
'''
ABSTR_EPSILON_LIST = [(Abstr_type.A_STAR, EPS), (Abstr_type.PI_STAR, EPS), (Abstr_type.Q_STAR, EPS)]
ERROR_DICTS = None
CORRUPTION_LIST = None
'''

# Q* specific
'''
# Only need first and third 
ABSTR_EPSILON_LIST = [(Abstr_type.Q_STAR, EPS)]
ERROR_DICTS = [{GridWorldState(6,3): GridWorldState(10,9),
                GridWorldState(9,10): GridWorldState(9,3)},
               #{GridWorldState(1,5): GridWorldState(1,2),
               # GridWorldState(3,6): GridWorldState(3,9)},
               {GridWorldState(9,8): GridWorldState(2,1),
                GridWorldState(9,11): GridWorldState(2,4)}]
CORRUPTION_LIST = None
NUM_CORR_MDPS = 1
'''

# A* specific
# Only need first and fourth
# OR third and fourth
'''
ABSTR_EPSILON_LIST = [(Abstr_type.A_STAR, EPS)]
ERROR_DICTS = [#{GridWorldState(4,2): GridWorldState(9,9),
               # GridWorldState(7,4): GridWorldState(7,3),
               # GridWorldState(7,11): GridWorldState(7,10)},
               #{GridWorldState(2,4): GridWorldState(8,10),
               # GridWorldState(2,9): GridWorldState(9,10)},
               {GridWorldState(4,9): GridWorldState(9,10),
                GridWorldState(10,11): GridWorldState(2,4)},
               {GridWorldState(2,11): GridWorldState(7,10)}]#,
               #{GridWorldState(5,1): GridWorldState(7,9),
               # GridWorldState(7,8): GridWorldState(11,10)}]
CORRUPTION_LIST = None
'''


# Pi* specific
'''
ABSTR_EPSILON_LIST = [(Abstr_type.PI_STAR, EPS)]
# From Random
ERROR_DICTS = [{GridWorldState(10,11): GridWorldState(1,2),
                GridWorldState(3,4): GridWorldState(1,8),
                GridWorldState(5,10): GridWorldState(1,2),
                GridWorldState(1,11): GridWorldState(1,2),
                GridWorldState(3,6): GridWorldState(4,11),
                GridWorldState(11,6): GridWorldState(4,11),
                GridWorldState(7,4): GridWorldState(1,2),
                GridWorldState(9,9): GridWorldState(1,8),
                GridWorldState(3,3): GridWorldState(4,11),
                GridWorldState(5,5): GridWorldState(1,2)},
               {GridWorldState(3,5): GridWorldState(1,5),
                GridWorldState(1,3): GridWorldState(4,5),
                GridWorldState(4,9): GridWorldState(4,5),
                GridWorldState(11,3): GridWorldState(1,5),
                GridWorldState(9,3): GridWorldState(1,5),
                GridWorldState(4,8): GridWorldState(4,4),
                GridWorldState(1,1): GridWorldState(1,5),
                GridWorldState(7,1): GridWorldState(4,11),
                GridWorldState(3,8): GridWorldState(4,4),
                GridWorldState(1,9): GridWorldState(4,4)}]
# Guesses
ERROR_DICTS = [{GridWorldState(10,11): GridWorldState(1,2),
                GridWorldState(1,5): GridWorldState(4,5),
                GridWorldState(3,6): GridWorldState(3,11)},
               {GridWorldState(10,11): GridWorldState(1,2),
                GridWorldState(1,5): GridWorldState(4,5)}]

ERROR_DICTS = [{GridWorldState(9,11): GridWorldState(2,3),
                GridWorldState(7,8): GridWorldState(1,8),
                GridWorldState(6,3): GridWorldState(5,2)},
               {GridWorldState(2,11): GridWorldState(5,3),
                GridWorldState(3,8): GridWorldState(2,3),
                GridWorldState(11,7): GridWorldState(4,8),
                GridWorldState(4,7): GridWorldState(1,10)}]
CORRUPTION_LIST = None
'''


'''
ERROR_DICTS = [{GridWorldState(4,2): GridWorldState(1,5),
                GridWorldState(5,5): GridWorldState(1,5),
                GridWorldState(4,3): GridWorldState(1,2),
                GridWorldState(6,3): GridWorldState(1,2),
                GridWorldState(7,4): GridWorldState(1,2),
                GridWorldState(7,11): GridWorldState(1,2),
                GridWorldState(1,11): GridWorldState(4,5),
                GridWorldState(9,10): GridWorldState(11,9)}]#,
               #{GridWorldState(3,5): GridWorldState(1,11),
               # GridWorldState(8,2): GridWorldState(1,11),
               # GridWorldState(2,4): GridWorldState(1,5),
               # GridWorldState(3,2): GridWorldState(1,5),
               # GridWorldState(2,9): GridWorldState(1,2)},
               #{GridWorldState(9,11): GridWorldState(1,2),
               # GridWorldState(9,8): GridWorldState(1,5),
               # GridWorldState(1,11): GridWorldState(1,2),
               # GridWorldState(4,9): GridWorldState(2,1)}]

CORRUPTION_LIST = None
'''



# Uncomment this if applying random corruption of a given proportion
'''
#CORRUPTION_LIST = [(Corr_type.UNI_RAND, 2), (Corr_type.UNI_RAND, 3), (Corr_type.UNI_RAND, 4), (Corr_type.UNI_RAND, 5)]
CORRUPTION_LIST = [(Corr_type.UNI_RAND, 0)]
ERROR_DICTS = None

ABSTR_EPSILON_LIST = [(Abstr_type.A_STAR, EPS), (Abstr_type.PI_STAR, EPS), (Abstr_type.Q_STAR, EPS)]
#ABSTR_EPSILON_LIST = [(Abstr_type.PI_STAR, EPS)]
#CORRUPTION_LIST = [(Corr_type.UNI_RAND, 0.01)]
'''

def run_experiment():
    start_time = time.time()



    exp = Experiment(MDP,
                     num_agents=NUM_AGENTS,
                     abstr_epsilon_list=ABSTR_EPSILON_LIST,
                     corruption_list=CORRUPTION_LIST,
                     error_dicts=ERROR_DICTS,
                     num_corrupted_mdps=NUM_CORR_MDPS,
                     num_episodes=NUM_EPISODES,
                     results_dir='exp_output/hot',
                     agent_type='abstraction',
                     agent_exploration_epsilon=EXPLORATION_EPSILON,
                     decay_exploration=DECAY_EXPLORATION,
                     exploring_starts=EXPLORING_STARTS,
                     step_limit=STEP_LIMIT,
                     detach_interval=DETACH_INTERVAL,
                     prevent_cycles=PREVENT_CYCLES,
                     reset_q_value=RESET_Q_VALUE,
                     agent_detach=AGENT_DETACH_METHOD,
                     detach_reassignment=DETACH_REASSIGNMENT,
                     detach_points=DETACH_POINTS)

    # Run experiment. This will write results to files
    # Commented out for testing visualization
    if DETACH_INTERVAL is not None:
        data, steps, corr_data, corr_steps, corr_detach_data, corr_detach_steps = exp.run_all_ensembles(include_corruption=True)
    else:
        data, steps, corr_data, corr_steps = exp.run_all_ensembles(include_corruption=True)


    # Visualize step counts
    exp_res = open(steps, "r")
    plt.style.use('seaborn-whitegrid')
    ax = plt.subplot(111)

    for mdp in exp_res:
        # splitting on double quotes
        mdp = mdp.split("\"")

        # if ground, first list item will have the word "ground"
        if ("ground" in mdp[0]):
            # and will contain everything we need as a comma seperated string
            mdp = mdp[0].split(",")
        else:
            # if not, the name of the abstraction will be the second list item
            # and everything else we need will be in the 3rd list item
            # which needs to be cleaned of empty strings
            mdp = [mdp[1]] + [m for m in mdp[2].split(",") if m != ""]

        episodes = [i for i in range(1, len(mdp))]
        ax.plot(episodes, [float(i) for i in mdp[1:]], label="%s" % (mdp[0],))

    plt.xlabel('Episode Number')
    plt.ylabel('Average Cumulative Steps Taken')
    plt.suptitle('Cumulative Steps Taken in True Abstractions and Ground MDP')
    leg = ax.legend(bbox_to_anchor=(0.6, 0.25), loc='upper left', ncol=1, mode="expand", shadow=True, fancybox=True)
    leg.get_frame().set_alpha(0.5)

    plt.savefig(os.path.join(exp.results_dir, 'true_step_counts.png'))
    plt.clf()

    # Plot performance for true results
    exp.visualize_results(data, outfilename='true_aggregated_results.png')

    # Plot performance for corrupt results
    if CORRUPTION_LIST is not None or ERROR_DICTS is not None:
        exp.visualize_corrupt_results(corr_data, outfilename='corrupt_aggregated_results.png',
                                      title='Q-Learning Performance in Corrupt MDPs')

        # Visualize step counts
        exp_res = open(corr_steps, "r")
        plt.style.use('seaborn-whitegrid')
        ax = plt.subplot(111)

        for mdp in exp_res:
            # splitting on double quotes
            mdp = mdp.split("\"")

            # if ground, first list item will have the word "ground"
            if ("ground" in mdp[0]):
                # and will contain everything we need as a comma seperated string
                mdp = mdp[0].split(",")
            else:
                # if not, the name of the abstraction will be the second list item
                # and everything else we need will be in the 3rd list item
                # which needs to be cleaned of empty strings
                mdp = [mdp[1]] + [m for m in mdp[2].split(",") if m != ""]

            episodes = [i for i in range(1, len(mdp))]
            ax.plot(episodes, [float(i) for i in mdp[1:]], label="%s" % (mdp[0],))

        plt.xlabel('Episode Number')
        plt.ylabel('Average Cumulative Steps Taken')
        plt.suptitle('Cumulative Steps Taken in Corrupted MDPs')
        leg = ax.legend(bbox_to_anchor=(0.6, 0.25), loc='upper left', ncol=1, mode="expand", shadow=True, fancybox=True)
        leg.get_frame().set_alpha(0.5)
        print('Saving corrupted step counts to', os.path.join(exp.results_dir, 'corrupted_step_counts.png'))
        plt.savefig(os.path.join(exp.results_dir, 'corrupted_step_counts.png'))
        plt.clf()

    # Plot performance for corrupt w/ detach results
    if (CORRUPTION_LIST is not None or ERROR_DICTS is not None) and DETACH_INTERVAL is not None:
        exp.visualize_corrupt_results(corr_detach_data,
                                      outfilename='corrupt_detach_aggregated_results.png',
                                      individual_mdp_dir='corrupted_w_detach',
                                      title='Q-Learning Performance in Corrupt MDPs with Detachment Algorithm')

    # Write a summary of the parameters to this file
    param_file = open(os.path.join(exp.results_dir, 'param_summary.txt'), 'w')
    abs_sum = 'Abstraction types:'.ljust(30) + str(ABSTR_EPSILON_LIST) + '\n'
    corr_sum = 'Corruptions applied:'.ljust(30) + str(CORRUPTION_LIST) + '\n'
    error_sum = ''
    if exp.error_dicts is not None:
        error_sum += 'Error dictionary:'.ljust(30)
        for dic in exp.error_dicts:
            error_sum += '{'
            for key, value in dic.items():
                error_sum += str(key) + ': ' + str(value) + ', '
            # Cut off last comma
            error_sum = error_sum[:-2]
            error_sum += '}\n'
    mdp_num_sum = '# corrupt MDPs:'.ljust(30) + str(NUM_CORR_MDPS) + '\n'
    ep_num_sum = '# episodes trained:'.ljust(30) + str(NUM_EPISODES) + '\n'
    exp_num_sum = 'Starting exploration epsilon:'.ljust(30) + str(exp.agent_exploration_epsilon) + '\n'
    decay_sum = 'Decay exploration?:'.ljust(30) + str(exp.decay_exploration) + '\n'
    exp_sum = 'Exploring starts?:'.ljust(30) + str(exp.exploring_starts) + '\n'
    detach_sum = 'Detach interval:'.ljust(30) + str(exp.detach_interval) + '\n'\
                 + 'Reset Q-value:'.ljust(30) + str(exp.reset_q_value) + '\n'\
                 + 'Prevent cycles?:'.ljust(30) + str(exp.prevent_cycle) + '\n'\
                 + 'Variance threshold:'.ljust(30) + str(exp.variance_threshold) + '\n'
    step_limit = 'Step limit:'.ljust(30) + str(exp.step_limit) + '\n'
    runtime = 'Runtime:'.ljust(30) + str(round(time.time() - start_time)) + '\n'
    detach_sum += 'Detachment method:'.ljust(30) + AGENT_DETACH_METHOD + '\n'\
                 + 'Reassignment method:'.ljust(30) + DETACH_REASSIGNMENT + '\n'

    param_file.write(mdp_sum
                     + abs_sum
                     + corr_sum
                     + mdp_num_sum
                     + error_sum
                     + detach_sum
                     + ep_num_sum
                     + exp_num_sum
                     + decay_sum
                     + exp_sum
                     + detach_sum
                     + step_limit
                     + runtime
                     + NOTES + '\n')
    if isinstance(MDP, TwoRoomsMDP):
        param_file.write(MDP.get_params())

if __name__ == '__main__':
    run_experiment()