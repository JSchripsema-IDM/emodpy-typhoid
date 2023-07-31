from emod_api import schema_to_class as s2c
from emod_api.interventions import utils
from emod_api.interventions import common
import json

def new_intervention( camp, rate ):
    """
    TyphoidCarrierClear intervention wrapper.
    """
    intervention = s2c.get_class_with_defaults( "TyphoidCarrierClear", camp.schema_path )
    intervention.Clearance_Rate = rate
    return intervention

def new_triggered_intervention( 
        camp, 
        rate,
        start_day=1, 
        triggers=[ "Births" ],
        coverage=1.0, 
        node_ids=None,
        property_restrictions_list=[],
        co_event=None # expansion slot
    ):
    """
    Distribute TyphoidCarrierClear when something happens as determined by a signal published from the
    model or another campaign event.
    """
    iv = new_intervention( camp, rate )

    #event = common.ScheduledCampaignEvent( camp, Start_Day=start_day, Demographic_Coverage=coverage, Intervention_List=[ act_intervention, bcast_intervention ], Node_Ids=nodeIDs, Property_Restrictions=property_restrictions_list )
    event = common.TriggeredCampaignEvent( camp, Start_Day=start_day, Triggers=triggers, Demographic_Coverage=coverage, Intervention_List=[ iv ], Node_Ids=node_ids, Property_Restrictions=property_restrictions_list, Event_Name="Triggered Typhoid Vax" )

    return event

def new_scheduled_intervention( 
        camp, 
        start_day=1, 
        coverage=1.0, 
        node_ids=None,
        property_restrictions_list=[],
        co_event=None # expansion slot
    ):
    """
    Distribute TyphoidCarrierClear when something happens as determined by a signal published from the
    model or another campaign event.
    """
    iv = new_intervention( camp )

    #event = common.ScheduledCampaignEvent( camp, Start_Day=start_day, Demographic_Coverage=coverage, Intervention_List=[ act_intervention, bcast_intervention ], Node_Ids=nodeIDs, Property_Restrictions=property_restrictions_list )
    event = common.ScheduledCampaignEvent( camp, Start_Day=start_day, Demographic_Coverage=coverage, Intervention_List=[ iv ], Node_Ids=node_ids, Property_Restrictions=property_restrictions_list )

    return event

def new_intervention_as_file( camp, start_day, filename=None ):
    import emod_api.campaign as camp
    camp.add( new_triggered_intervention( camp, start_day=start_day, rate=0.567 ), first=True )
    if filename is None:
        filename = "TyphoidCarrierClear.json"
    camp.save( filename )
    return filename
