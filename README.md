This homework assignment helps to demonstrate how to build and run a basic CI/CD pipeline using Jenkins for a simple Python application.
The pipeline automatically performs checkout, build, test, and deploy stages — showing the core concepts of continuous integration and continuous deployment.
The Python application (app.py) defines a function that adds two numbers and returns their sum.
Unit tests (test_app.py) verify that this function works correctly using Python’s built-in unittest framework.
simple-pipeline/
├── app.py              # Simple Python application (adds two numbers)
├── test_app.py         # Unit tests for the application
├── requirements.txt    # Python dependencies
├── Jenkinsfile         # Jenkins pipeline configuration
└── README.md           # Project documentation
Jenkins Pipeline stages include:
1. Checkout (retrieves the latest source code form the git repository and ensures Jenkins uses the most up-to-date version of the project)
2. Build (sets up the python virtual environment, installs all dependencies listes in requirements.txt, prepares project for testing)
3. Test (runs automated tests using pythons framework, verfies that the code funtions correctly)
4. Deploy (simulates a deployment step, prints a success message, and demonstrates the final stage of a CI/CD workflow)