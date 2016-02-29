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
    - Rough UI:
        - BoF list: [http://localhost:18000/mbof/](http://localhost:18000/mbof/)
        - BoF detail: [http://localhost:18000/mbof/1/](http://localhost:18000/mbof/1/)
        - API root (REST web services, req. login): [http://localhost:18000/](http://localhost:18000/)
    - DB admin: [http://localhost:18000/admin/](http://localhost:18000/admin/)
