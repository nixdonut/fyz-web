# fyz-web
A progress tracker for people preparing for mathematical olympiads, makes problem sets more fun using gamification and is useful for keeping track of which chapters/handouts you've done.

![image](https://github.com/nixdonut/fyz-web/assets/95039994/56e119dd-0824-4fcd-8d75-b190bc6f57ea)

# Setup
1. First install python, if you don't already have it or if you have an older version.
2. Clone this repository (or just download and extract if you don't have git).
3. `cd` into the directory where you cloned/extracted this repository.
4. Run `python -m pip install -r requirements.txt`.
5. Run `python manage.py makemigrations`, then `python manage.py migrate`.
6. Run `python manage.py createsuperuser` and create a superuser.
7. Finally, run `python manage.py runserver`.
8. Open http://127.0.0.1:8000/admin or whatever in your browser (tested on firefox, chrome, and edge), log in, and add your units. Leave the solutions field blank, you're supposed to upload those later. Everything else is required.
9. That's it, now log in or make a new account or whatever and start the grind.

# Usage
To view the "units", which are basically pdfs of individual chapters of books or handouts, click on the yellow book emoji next to the unit. Once you "finish" a unit, i.e., read it and solve the problems, you are expected to upload them: either typeset with LaTeX or written on paper and scanned or whatever. To do this, click on the plus file emoji sequence. Once you are done with a unit, the play button emoji will turn into a green check mark and if you ever want to refer to your solutions in the future, click the floppy disk emoji next to the unit. As you do more units, you will level up and gain points.

# Choosing the units
Here are my "units", for reference or recommendation:
1. All chapters of EGMO
2. All chapters of MONT
3. Stephan Wagner's Combinatorics Handout
4. All chapters of Pranav Sriram's book
5. All chapters of Secrets in Inequalities by Pham Kim Hung (both volumes)
6. Evan Chen's Handout on Functional Equations

These are pretty standard textbook/handout recommendations, so if you're confused I'd say just go with these. I obviously can't just upload the PDFs because piracy but it shouldn't be too hard to find them and seperate them into chapters.
