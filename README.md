# RoboCup@Home Generator Collection
 From 2017 to 2019, all the generator for GSPR and EEGPSR are collected

gpsr_command_generator
======================

''gpsr_command_generator'' is the official command generator used in
the the `RoboCup@Home <http://www.robocupathome.org>`_ competitions
for the "General Purpose Service Robot (GPSR)" test.

## Introduction: What is GPSR?

 
The series of GPSR tests evaluate all abilities of the robots that are
requrired throughout the set of tests in stages I and II. The robot
has to solve multiple tasks upon request. That is, the test is not
incporporated into a predefined story and there is neither a
predefined order of tasks nor a predefined set of actions.  The
actions that are to be carried out by the robot are chosen
(pseudo-)randomly by the referees. In the competitions from 2010 to
2019 variants of this command generator has been used to generate the
commands given to the robot. The actions are organized in categories with 
different complexity. Scoring depends on the complexity class. 


## Installing and running

The latest version of the (publicly available) stripped down variant
of the GPSR command generator can be directly obtained from github::

   git clone https://github.com/RoboCupAtHome/gpsr_command_generator.git

The command generator is a simple python script and be run using::

   python command_generator.py

It will then prompt for entering the desired command category and generate a random command once you hit enter:: 
    
   $ python command_generator.py 
   Which category do you want to do?   1, 2, 3 or q(uit)


## Examples

The following are example commands generated when running the script as above.

* Category I (action sequence)::

   Move to the dinner table, grasp the Energy drink and put it in the trash bin.

* Category II (underspecied command, missing information)::

   Bring me some Drink from a shelf.   ( Drink = Fanta )   ( shelf = bookshelf )

* Category III (erroneous information)::

   Bring me the Milk from the dresser. (But there is NO object!)


Originated from https://github.com/RoboCupAtHome/gpsr_command_generator
