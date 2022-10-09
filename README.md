# Skillsroot  
Building a bridge connecting the youth and industry

## Installation Instructions
1. Clone the repository and ``cd`` into ``skillsroot/settings`` sub-directory.
2. Create an environment file ``.env`` and add a SECRET_KEY variable (your django secret key)
3. Return back to the parent ``skillsroot/`` directory.
4. Create a virtual environment  
    i) ``python3 -m venv vir``  
   **For Windows:**    
    ii) ``./vir/Scripts/Activate``  
   **For Linux:**  
    i) ``source vir/bin/activate``  
5. Install the requirements:  
   ```pip install -r requirements.txt```  
5. Migrate before running  
   ```python manage.py migrate``` 
6. Run !  
   ```python manage.py runserver```
