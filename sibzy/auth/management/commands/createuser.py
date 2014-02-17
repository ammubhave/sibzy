from django.core.management.base import NoArgsCommand
from auth.models import User, UserProfile

class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        print '=== Sibzy Create User Script ==='
        fbid = ''
        fbusername = ''
        while fbid == '':
            fbid = raw_input('Facebook ID: ')
        while fbusername == '':
            fbusername = raw_input('Facebook username: ')

        is_staff = None
        is_superuser = False

        while (is_staff not in ('yes', 'no')):
            is_staff = raw_input('Is staff? (yes/no): ')
        if is_staff == 'yes':
            is_staff = True
            is_superuser = None
            while (is_superuser not in ('yes', 'no')):
                is_superuser = raw_input('Is superuser? (yes/no): ')
            if is_superuser == 'yes': is_superuser = True
            else: is_superuser = False
        else:
            is_staff = False

        print 'Creating user...'
        user = User.objects.create_user(username=fbid, email=fbid + '@facebook.com', password=fbid + 'sibzypassword')
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()
        print 'Creating user profile...'
        profile = UserProfile(user=user, fbid=fbid, fbusername=fbusername)
        profile.save()

        print 'User created successfully.'
