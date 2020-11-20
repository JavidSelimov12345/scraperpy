from pywebcopy import save_website 
  
kwargs = {'project_name': 'site folder'} 
  
save_website( 
    
    # url pf the website 
    url='https://hobbylife.az/', 
      
    # folder where the copy will be saved 
    project_folder='C:\\Users\code\Desktop\pyscrap', 
    **kwargs 
)