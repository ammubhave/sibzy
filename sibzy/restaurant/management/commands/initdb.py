from django.core.management.base import NoArgsCommand
from restaurant.models import *

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        print '=== Sibzy Basic DB Initialization Script ==='
        print
        print '--- Countries ---'
        country_usa = Country(name='United States')

        if len(Country.objects.filter(name='United States')) == 0:
            print 'Creating United States...'
            country_usa.save()
        else:
            country_usa = Country.objects.get(name='United States')

        states = [
        #('AK', 'Alaska'),
        #('AL', 'Alabama'),
        #('AZ', 'Arizona'),
        #('AR', 'Arkansas'),
        #('CA', 'California'),
        #('CO', 'Colorado'),
        #('CT', 'Connecticut'),
        #('DE', 'Delaware'),
        #('FL', 'Florida'),
        #('GA', 'Georgia'),
        #('HI', 'Hawaii'),
        #('ID', 'Idaho'),
        #('IL', 'Illinois'),
        #('IN', 'Indiana'),
        #('IA', 'Iowa'),
        #('KS', 'Kansas'),
        #('KY', 'Kentucky'),
        #('LA', 'Louisiana'),
        #('ME', 'Maine'),
        #('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        #('MI', 'Michigan'),
        #('MN', 'Minnesota'),
        #('MS', 'Mississippi'),
        #('MO', 'Missouri'),
        #('MT', 'Montana'),
        #('NE', 'Nebraska'),
        #('NV', 'Nevada'),
        #('NH', 'New Hampshire'),
        #('NJ', 'New Jersey'),
        #('NM', 'New Mexico'),
        #('NY', 'New York'),
        #('NC', 'North Carolina'),
        #('ND', 'North Dakota'),
        #('OH', 'Ohio'),
        #('OK', 'Oklahoma'),
        #('OR', 'Oregon'),
        #('PA', 'Pennsylvania'),
        #('RI', 'Rhode Island'),
        #('SC', 'South Carolina'),
        #('SD', 'South Dakota'),
        #('TN', 'Tennessee'),
        #('TX', 'Texas'),
        #('UT', 'Utah'),
        #('VT', 'Vermont'),
        #('VA', 'Virginia'),
        #('WA', 'Washington'),
        #('DC', 'Washington D.C.'),
        #('WV', 'West Virginia'),
        #('WI', 'Wisconsin'),
        #('WY', 'Wyoming')
        ]
    
        print '--- States ---'
        for (state_code, state_name) in states:
    
            state = State(name=state_name, country=country_usa)
            if len(State.objects.filter(name=state_name)) == 0:
                print 'Creating ' + state_name + '...'
                state.save()
            else:
                state = State.objects.get(name=state_name)
    
            if state.name == 'Massachusetts':
                if len(City.objects.filter(name='Cambridge')) == 0:
                    print 'Creating Cambridge...'
                    cambridge = City(name='Cambridge', state=state)
                    cambridge.save()
                if len(City.objects.filter(name='Boston')) == 0:
                    print 'Creating Boston...'
                    boston = City(name='Boston', state=state)
                    boston.save()
                #if len(City.objects.filter(name='Lexington')) == 0:
                #    lexington = City(name='Lexington', state=state)
                #    lexington.save()
                
        print '--- Dish Categories ---'
        if len(DishCategory.objects.filter(name='Vegetarian')) == 0:
            print 'Creating Vegetarian...'
            cat = DishCategory(name='Vegetarian')
            cat.save()
        if len(DishCategory.objects.filter(name='Vegan')) == 0:
            print 'Creating Vegan...'
            cat = DishCategory(name='Vegan')
            cat.save()
        if len(DishCategory.objects.filter(name='Organic')) == 0:
            print 'Creating Organic...'
            cat = DishCategory(name='Organic')
            cat.save()
        if len(DishCategory.objects.filter(name='Nutfree')) == 0:
            print 'Creating Nutfree...'
            cat = DishCategory(name='Nutfree')
            cat.save()
        if len(DishCategory.objects.filter(name='Glutenfree')) == 0:
            print 'Creating Glutenfree...'
            cat = DishCategory(name='Glutenfree')
            cat.save()
