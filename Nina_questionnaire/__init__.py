import random
from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'questionnaire'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass

class Player(BasePlayer):


    def make_field(label):
        return models.IntegerField(
        choices=[['6', 'Agree completely (6)'], ['5', '5'], ['4', '4'], 
                 ['3', '3'], ['2', '2'], ['1', 'Completely disagree (1)'] ],                                
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )

    # questionnaire
    conservative_liberal = models.IntegerField( widget=widgets.RadioSelect,  choices=[['1', 'extremely liberal (1)'], ['2', '2'], ['3', '3'],['4', '4'], ['5', '5'], ['6', '6'], ['7', '7'],['8', '8'], ['9', '9'],  ['10', 'extremely conservative (10)'] ] )
    climate_change_concern1 = make_field('I worry about the climate´s state.')
    climate_change_concern2 = make_field('Climate protection is important for our future.')
    climate_change_concern3 = make_field('We must protect the climate´s delicate equilibrium.')
    climate_change_concern4 = make_field('Climate change has severe consequences for humans and nature.')
    
    def make_field(label):
        return models.IntegerField(
        choices=[['1', 'Strongly oppose (1)'],['2', '2'] ,   ['3', '3'], ['4', '4'] ,
                 ['5', '5'], ['6', '6'] , ['7', 'Strongly support (7)'] ],
        label=label,
        widget=widgets.RadioSelectHorizontal,
    )
    policy_item1 = make_field('Expand public transport (buses, trams, trains).')
    policy_item2 = make_field('Ban the sale of diesel and petrol-engine cars.')
    policy_item3 = make_field('Increasing subsidies for alternatives to flying.')
    policy_item4 = make_field('Increase or introduce taxes on air travel.')  
    policy_item5 = make_field('Increase subsidies for renewable energy projects (e.g., wind and solar energy).')
    policy_item6 = make_field('Increasing the price of electricity consumption during peak times.')  
    policy_item7 = make_field('Increase or introduce taxes on red meat (e.g., beef, lamb, veal).')
    policy_item8 = make_field('Increase subsidies for food products with low greenhouse gas emissions (e.g., fruit, vegetables, legumes, cereals).')
    policy_item9 = make_field('Increase or introduce taxes on non-recyclable garbage.')
    policy_item10 = make_field('Expand recycling facilities and infrastructure for recycling.')
    policy_item11 = make_field('Increase subsidies for local and regional foods.')
    policy_item12 = make_field('Increase or introduce taxes on food imported via plane.')


    
# FUNCTIONS
# PAGES

class cc_concern(Page):
    form_model = 'player'
    form_fields = ['climate_change_concern1', 'climate_change_concern2', 'climate_change_concern3', 'climate_change_concern4']
class policy_support(Page):
    form_model = 'player'
    form_fields = []
    
class policy(Page):
    form_model = 'player'
    form_fields = ['policy_item1', 'policy_item2','policy_item3','policy_item4','policy_item5','policy_item6', 'policy_item7', 'policy_item8', 'policy_item9', 'policy_item10', 'policy_item11', 'policy_item12']

class pol_orientation(Page):
    form_model = 'player'
    form_fields = ['conservative_liberal']

class end(Page):
    form_model = 'player'
    form_fields = []


# Page sequence
page_sequence = [
    policy_support, 
    policy,

    cc_concern,
    pol_orientation,

    end
]
