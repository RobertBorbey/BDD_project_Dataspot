# Proiect BDD (Behavior-Driven Development) - Borbey Robert - Dataspot.ro
In acest proiect voi implementa teste atât pozitive, cât și negative, pentru următoarele :
- Funcționalitatea de autentificare
- Funcționalitatea de înregistrare
- Casuța de căutare (search box)
- Opțiunea de filtrare și de sortare a rezultatelor

# Cum se folosește și clonează proiectul? Cum se rulează testele și cum se accesează rapoartele?
1. _Utilizarea proiectului_ presupune deschiderea acestuia în PyCharm și instalarea tuturor dependențelor
(se poate rula în terminal comanda: _pip install -r requirements.txt). Trebuie creat un mediu virtual
(venv) pentru proiect și să se instaleze pachetele necesare din Selenium.

2. _Clonarea proiectului_ se realizează prin urmarea pașilor următori:
- Se deschide PyCharm și se selectează optiunea “Check out from Version Control” din meniul VCS
- Se alege opțiunea “GitHub” și se introduce URL-ul către depozitul GitHub care conține pachetul
- Se selectează directorul local în care se dorește clonarea proiectului și se apasă butonul “Clone”

3. _Instalarea formatter-ului HTML_ pentru BEHAVE se face prin rularea urmatoarei comenzi in terminal :
##### _pip install behave-html-formatter_

4. _Crearea fișierului behave.ini_ se realizează prin deschiderea unui editor de text și adăugarea următorului conținut :
##### _[behave.formatters]_
##### _html=behave_html_formatter:HTMLFormatter_

5. _Pentru a rula testele_ și _genera rapoartele_ se folosește comanda care va rula testele automate și va genera un raport HTML sub numele de "behave-report.html" :	
##### _behave -f html-o behave-report.html_

_________________________________________________
_________________________________________________

# BDD Project (Behavior-Driven Development) - Borbey Robert - Dataspot.ro
In this project I will be implementing positive and negative tests for the following :
- Authentication functionality
- Registration functionality
- Search box feature
- Filter and sort features

# How to use and clone the project? How to run the tests and how to access the reports?
1. _To use the project_, it's required to open it in PyCharm and to install all the dependencies (you can run
the following command in the terminal : _pip install -r requirements.txt_). It is also required to create a
virtual environment (venv) for the project and to install all the required packages from Selenium.

2. _Cloning the project_ involves following these steps:
- Open PyCharm and select the option "Check out from Version Control", from the VCS menu
- Choose the option "GitHub" and insert the URL of the GitHub repository that contains the package
- Select the local directory in which you want to clone the project and press the "Clone" button

3. _The installation of the HTMLFormatter_ for BEHAVE is done by running the following command in the terminal:
##### _pip install behave-html-formatter_

4. _To create the behave.ini file_ it is required to open a text editor and to add the following content:
##### _[behave.formatters]_
##### _html=behave_html_formatter:HTMLFormatter_

5. _To run the tests_ and _generate the reports_, the following command has to be used in order to run the automation tests
and generate a HTML report under the name of "behave-report.html":
##### _behave -f html-o behave-report.html_