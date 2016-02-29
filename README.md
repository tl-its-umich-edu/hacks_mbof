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

## Update Data Fixtures ##

This is the procedure to add dummy data to the fixture files.

- Connect to the database in the Vagrant VM. (If MySQL DB is used, this can be done from your host system via the port defined in the Vagrant file.)
- Delete all tables.
- Run the migrations to recreate the tables: `python manage.py migrate`
- Run the loaddata command to load existing fixtures: `python manage.py loaddata mbof/fixtures/dev_data.json`
- Make changes to the database needed to exercise application features.
- Save the changes to a fixture file: `python manage.py dumpdata --indent 4 mbof > mbof/fixtures/dev_data.json`
- Commit the changes to the updated fixture file.