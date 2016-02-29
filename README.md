# hacks_mbof
If you know MBOF, you don't need to know anything else.

# Setup

0. Install Vagrant - https://www.vagrantup.com/
0. Start Vagrant
   - `cd hacks_mbof`
   - `vagrant up`
   - `vagrant ssh`
0. Install Bower packages
   - `cd /vagrant/mbofui`
   - `bower install`

# Development
0. Initialize and start app server
    - `cd /vagrant`
    - `python manage.py migrate`
    - `python manage.py loaddata mbof/fixtures/dev_data.json`
    - `python manage.py runserver`
0. Browse to...
    - Testing UI:
        - Root (AKA BoF list): [http://localhost:18000/](http://localhost:18000/)
        - BoF list: [http://localhost:18000/mbof/](http://localhost:18000/mbof/)
        - BoF detail: [http://localhost:18000/mbof/1/](http://localhost:18000/mbof/1/)
    - REST API
        - Root: [http://localhost:18000/api/](http://localhost:18000/api/)
        - Messages: [http://localhost:18000/api/messages/](http://localhost:18000/api/messages/)
        - Users: [http://localhost:18000/api/users/](http://localhost:18000/api/users/)
    - DB admin: [http://localhost:18000/admin/](http://localhost:18000/admin/)
