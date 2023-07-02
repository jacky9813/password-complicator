====================
Password Complicator
====================

A Python-based CLI tool for generating a rather complicated password from 
some easy to remember text.

For example, passing ``myBestPasswordForGithub`` into the program with 
default configuration will retrieve ``DHrEJih+Vg1/``. (Don't worry I'm 
not actually using this password.)

Due to hashing, you can just remember ``myBestPasswordFor`` and append 
service name in the password, limiting the scale of compromise when 
``DHrEJih+Vg1/`` is leaked by somebody.

.. warning::

    This CLI tool will not talk to your system clipboard. It'll show 
    the result directly on stdout.

System Requirements
===================

* Python 3.8 or later


Install
=======

Method 1: Directly from GitHub
------------------------------

.. code-block:: shell

    pip3 install git+https://github.com/jacky9813/password-complicator@1.0.0

Method 2: From wheel file
-------------------------

.. _release page: https://github.com/jacky9813/password-complicator/releases/latest

1. Navigate to `release page`_ and download the wheel (.whl) file
2. Install the package with pip. (For example: 
   ``pip3 install ./password_complicator-1.0.0-py3-none-any.whl``)


Usage
=====

.. code-block:: shell

    pc --help
    pc --version
    pc -d sha3_512 -e ascii85
