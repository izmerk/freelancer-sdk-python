from freelancersdk.session import Session
from freelancersdk.resources.users.users import search_freelancers
from freelancersdk.resources.users.exceptions import \
    UsersNotFoundException
from freelancersdk.resources.users.helpers import (
    create_get_users_details_object
)

import os


def sample_search_freelancers():
    url = os.environ.get('FLN_URL')
    oauth_token = os.environ.get('FLN_OAUTH_TOKEN')
    session = Session(oauth_token=oauth_token, url=url)
    user_details = create_get_users_details_object(
        avatar=True,
        reputation=True,
        reputation_extra=True,
        profile_description=True,
    )
    try:
        result = search_freelancers(
            session,
            username='CodeJunk',
            user_details=user_details,
            compact=False
        )
    except UsersNotFoundException as e:
        print('Error message: {}'.format(e.message))
        print('Server response: {}'.format(e.error_code))
        return None
    else:
        return result

result = sample_search_freelancers()

if result:
    print('Found freelancers: {}'.format(result))