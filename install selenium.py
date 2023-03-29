def run(self, cmd):
    completed = subprocess.run(["powershell", "-Command"], capture_output=True)
    
    driver = cmd (exectutable_path="pip install selenium")
    
    return completed

    
