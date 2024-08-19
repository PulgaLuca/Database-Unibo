# Database-Unibo

<p align="center">
  <img src="app/static/img/logo0.JPG" alt="Descrizione dell'immagine" width="150">
</p>

<p align="center">
  <a href="https://www.aurorarocketry.eu/">
  https://www.aurorarocketry.eu/
  </a>
</p>

## Abstract

The aim of the project is to create a website with a related database that will enable the University of Bologna's ‘Aurora Rocketry Team’ to save space missions in view of the ‘Euroc’, European Rocketry Competition.
The site will provide the team's students with a centralised interface for planning, monitoring and analysing space missions, including rocket launches, scientific experiments and data collection.
A user registration page will be available, where each team member can create an account by entering their personal and contact information.
Operations such as mission entry will be implemented, where users can enter the details of a new mission, including objectives, expected launch date, necessary equipment and technical requirements. Editing and deleting existing missions, where authorised users can make changes to the details of existing missions or delete them if necessary. It will be possible for each mission to plan and visualise rocket launches with associated sensors, payloads and sponsors to help plan the various technical and non-technical aspects. In addition, the visualisation of complex statistical information will be possible, as users will have access to detailed statistical data on the performance of past missions, including graphs on launch efficiency, target success, and other metrics relevant to improving future performance. User and permission management will be implemented.

## Scope

Project realised for the ‘Database’ university course

## Installation

>  1. Prepare the environment
Make sure you have Python installed. You can check this with:
 
      python --version
      or
      python3 --version 
>  2. Create a virtual environment (optional but recommended)
      
      python3 -m venv venv

>  3. Activate the virtual environment:

      On Windows: venv\Scripts\activate
      On macOS and Linux: source venv/bin/activate

> 3. Install dependencies

      pip install -r requirements.txt

> 4. Start the application
Run the 'run.py' file with:

      python run.py 
      or 
      python3 run.py

> 5. Access the application
Once started, the application should be accessible at:

      http://127.0.0.1:5000. 

You will need to open a web browser and navigate to this URL to view the web-app's homepage.

> You can log in with a temporary user account:
      
      email: tmpuser@gmail.com
      password: tmpuser
