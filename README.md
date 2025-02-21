# SlowLoris DOS
This repo contains usage instructions for SlowLoris. This program is writtten in python. SlowLoris is a denial of service (DOS) module that effectively shutters a website by opening new connections and refusing to close old ones until a website is overloaded.
Most modern websites have protection from this kind of attack, but many smaller cloud based shared hosting services are not designed to hold many simultaneous conenctions for extended periods of time.

# Installation:

Download the repository:  

	$ git clone https://github.com/JohnKearney1/SlowLoris.git

Install the dependencies as administrator:

	$ pip install -r requirements.txt


# Usage:

Open the directory:

    $ cd SlowLoris/  

Run SlowLoris1.py:

    $ python3 auth.py

You may login using "root" as username and password or create your own user locally.



# Notes:
This project is for educational purposes ONLY.
This software impliments several penetration testing tools, intended only for legal use.
I do not condone illegal or unlawful usage of this software.


**Current Version:** V2.0  
**Latest Release:** 07/25/2019  
**Latest Commit:** 05/06/2021 
