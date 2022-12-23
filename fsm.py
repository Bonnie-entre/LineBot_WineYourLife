from transitions import Machine
import random
# from transitions.extensions import GraphMachine as Machine
from transitions.extensions import MachineFactory

# create a machine with mixins
diagram_cls = MachineFactory.get_predefined(graph=True)

class NarcolepticSuperhero(object):

    # Define some states. Most of the time, narcoleptic superheroes are just like
    # everyone else. Except for...
    states = ['user', '3 bar within 1.5k', 'print opening hour', 'goto bar website', 'show bar in Googlemap',
                'start record','record date','record score','record comment','record go_next_time_ornot','show record'
            ]

    def __init__(self, name):

        self.name = name

        # Initialize the state machine
        self.machine = diagram_cls(model=self, states=NarcolepticSuperhero.states, initial='user')

        # Add some transitions. We could also define these using a static list of
        # dictionaries, as we did with states above, and then pass the list to
        # the Machine initializer as the transitions= argument.

        # list 3 bar within 1.5k
        self.machine.add_transition(trigger='location(google map)', source='user', dest='3 bar within 1.5k')
        self.machine.add_transition(trigger='btn: Time', source='3 bar within 1.5k', dest='print opening hour')
        self.machine.add_transition(trigger='btn: Website', source='3 bar within 1.5k', dest='goto bar website')
        self.machine.add_transition(trigger='btn: Map', source='3 bar within 1.5k', dest='show bar in Googlemap')
        self.machine.add_transition(trigger='nap', dest='user', source='3 bar within 1.5k')
        self.machine.add_transition(trigger='nap', dest='user', source='print opening hour')
        self.machine.add_transition(trigger='nap', dest='user', source='goto bar website')
        self.machine.add_transition(trigger='nap', dest='user', source='show bar in Googlemap')

        # record Bar Life
        self.machine.add_transition(trigger='type record', source='user', dest='start record')
        self.machine.add_transition(trigger='type Bar Name', source='start record', dest='record date')
        self.machine.add_transition(trigger='type Date', source='record date', dest='record score')
        self.machine.add_transition(trigger='type Score', source='record score', dest='record comment')
        self.machine.add_transition(trigger='type Comment', source='record comment', dest='record go_next_time_ornot')
        self.machine.add_transition(trigger='type Y/N', source='record go_next_time_ornot', dest='user')
        
        # show Bar Life Record
        self.machine.add_transition(trigger='type show', source='user', dest='show record')
        self.machine.add_transition(trigger='nap', source='show record', dest='user')

        # type other text
        self.machine.add_transition(trigger='type other text', source='user', dest='show reply')
        self.machine.add_transition(trigger='nap', source='show reply', dest='user')


if __name__ == "__main__":
    Wine_You_Life = NarcolepticSuperhero("Wine_You_Life")
    print(Wine_You_Life.state)
    Wine_You_Life.get_graph().draw('fsm.png', prog='dot')